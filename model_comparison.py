#!/usr/bin/env python3
"""
Model Comparison Script for Cheque Fraud Detection

Tests all three models (Siamese, CNN, Classical ML) on all sample images
and generates a comprehensive comparison report.
"""

import os
import sys
import cv2
import numpy as np
import pandas as pd
from pathlib import Path
import json
from datetime import datetime

# Setup paths
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import config
from src.fraud_pipeline import FraudDetector

def load_sample_images():
    """Load all sample images and categorize them."""
    sample_dir = os.path.join(config.BASE_DIR, "data", "samples")
    samples = {}
    
    # Get all sample files
    sample_files = sorted([
        f for f in os.listdir(sample_dir)
        if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tif', '.tiff'))
    ])
    
    for filename in sample_files:
        filepath = os.path.join(sample_dir, filename)
        img = cv2.imread(filepath)
        if img is not None:
            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            samples[filename] = {
                'image': img_rgb,
                'path': filepath,
                'category': categorize_image(filename)
            }
    
    return samples

def categorize_image(filename):
    """Categorize image based on filename."""
    if 'genuine' in filename.lower():
        return 'Genuine'
    elif 'altered' in filename.lower():
        return 'Altered Fraud'
    elif 'crossed' in filename.lower():
        return 'Crossed Fraud'
    elif 'multi_tamper' in filename.lower():
        return 'Multi-Tampered Fraud'
    else:
        return 'Unknown'

def test_model_on_samples(model_type, samples):
    """Test a specific model on all sample images."""
    print(f"\n{'='*60}")
    print(f"Testing {model_type.upper()} Model")
    print(f"{'='*60}")
    
    results = {}
    detector = None
    
    try:
        detector = FraudDetector(model_type=model_type)
        print(f"✅ {model_type.upper()} model loaded successfully")
    except Exception as e:
        print(f"❌ Failed to load {model_type.upper()} model: {e}")
        return results
    
    for filename, sample_data in samples.items():
        print(f"\nProcessing: {filename}")
        
        try:
            result = detector.detect(sample_data['image'])
            
            # Extract key information
            results[filename] = {
                'verdict': result['verdict'],
                'confidence': result['confidence'],
                'num_suspicious_patches': len(result['suspicious_patches']),
                'avg_similarity': np.mean(result['similarity_scores']) if result['similarity_scores'] else 1.0,
                'actual_category': sample_data['category'],
                'note': result.get('note', '')
            }
            
            print(f"  Verdict: {result['verdict']}")
            print(f"  Confidence: {result['confidence']:.2%}")
            print(f"  Suspicious patches: {len(result['suspicious_patches'])}")
            
        except Exception as e:
            print(f"  ❌ Error processing {filename}: {e}")
            results[filename] = {
                'verdict': 'ERROR',
                'confidence': 0.0,
                'num_suspicious_patches': 0,
                'avg_similarity': 0.0,
                'actual_category': sample_data['category'],
                'note': f'Processing error: {str(e)}'
            }
    
    return results

def calculate_accuracy(results):
    """Calculate accuracy metrics for model results."""
    total = len(results)
    correct = 0
    fraud_correct = 0
    genuine_correct = 0
    total_fraud = 0
    total_genuine = 0
    
    for filename, result in results.items():
        actual = result['actual_category']
        predicted = result['verdict']
        
        # Convert actual category to binary (Genuine vs Fraud)
        is_actual_fraud = actual != 'Genuine'
        is_predicted_fraud = predicted == 'FRAUD'
        
        if is_actual_fraud:
            total_fraud += 1
        else:
            total_genuine += 1
        
        if is_actual_fraud == is_predicted_fraud:
            correct += 1
            if is_actual_fraud:
                fraud_correct += 1
            else:
                genuine_correct += 1
    
    accuracy = correct / total if total > 0 else 0
    fraud_accuracy = fraud_correct / total_fraud if total_fraud > 0 else 0
    genuine_accuracy = genuine_correct / total_genuine if total_genuine > 0 else 0
    
    return {
        'total_accuracy': accuracy,
        'fraud_detection_accuracy': fraud_accuracy,
        'genuine_detection_accuracy': genuine_accuracy,
        'total_samples': total,
        'correct_predictions': correct,
        'fraud_samples': total_fraud,
        'genuine_samples': total_genuine
    }

def generate_comparison_report(all_results):
    """Generate a comprehensive comparison report."""
    print(f"\n{'='*80}")
    print("COMPREHENSIVE MODEL COMPARISON REPORT")
    print(f"{'='*80}")
    print(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Total sample images tested: {len(list(all_results.values())[0])}")
    
    # Model performance summary
    print(f"\n{'='*50}")
    print("MODEL PERFORMANCE SUMMARY")
    print(f"{'='*50}")
    
    for model_type, results in all_results.items():
        if results:  # Only if model ran successfully
            metrics = calculate_accuracy(results)
            print(f"\n{model_type.upper()} Model:")
            print(f"  Overall Accuracy: {metrics['total_accuracy']:.1%}")
            print(f"  Fraud Detection Accuracy: {metrics['fraud_detection_accuracy']:.1%}")
            print(f"  Genuine Detection Accuracy: {metrics['genuine_detection_accuracy']:.1%}")
            print(f"  Total Correct: {metrics['correct_predictions']}/{metrics['total_samples']}")
    
    # Detailed results table
    print(f"\n{'='*50}")
    print("DETAILED RESULTS BY IMAGE")
    print(f"{'='*50}")
    
    # Create DataFrame for better visualization
    data = []
    for filename in list(all_results.values())[0].keys():
        row = {'Image': filename.replace('.png', '').replace('_', ' ').title()}
        for model_type, results in all_results.items():
            if filename in results:
                result = results[filename]
                row[f'{model_type.upper()}_Verdict'] = result['verdict']
                row[f'{model_type.upper()}_Confidence'] = f"{result['confidence']:.1%}"
                row[f'{model_type.upper()}_Suspicious'] = result['num_suspicious_patches']
        row['Actual'] = results.get(filename, {}).get('actual_category', 'Unknown')
        data.append(row)
    
    df = pd.DataFrame(data)
    print(df.to_string(index=False))
    
    # Save detailed results
    output_file = os.path.join(config.BASE_DIR, 'model_comparison_results.csv')
    df.to_csv(output_file, index=False)
    print(f"\n📊 Detailed results saved to: {output_file}")
    
    return df

def main():
    """Main function to run model comparison."""
    print("🚀 Starting Model Comparison Analysis")
    print("=" * 60)
    
    # Load sample images
    samples = load_sample_images()
    print(f"✅ Loaded {len(samples)} sample images")
    
    # Test each model
    models = ['siamese', 'cnn', 'classical']
    all_results = {}
    
    for model_type in models:
        results = test_model_on_samples(model_type, samples)
        if results:  # Only store if model ran successfully
            all_results[model_type] = results
    
    # Generate comparison report
    if all_results:
        df = generate_comparison_report(all_results)
        
        # Save results as JSON for further analysis
        json_file = os.path.join(config.BASE_DIR, 'model_comparison_results.json')
        with open(json_file, 'w') as f:
            json.dump(all_results, f, indent=2, default=str)
        print(f"\n💾 Raw results saved to: {json_file}")
        
        print(f"\n{'='*60}")
        print("✅ Model comparison completed successfully!")
        print(f"{'='*60}")
    else:
        print("\n❌ No models ran successfully. Please check model files and dependencies.")

if __name__ == "__main__":
    main()
