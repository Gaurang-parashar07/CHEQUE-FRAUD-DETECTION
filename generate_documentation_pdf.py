"""
Comprehensive Documentation PDF Generator
Cheque Fraud Detection using Ink Variation Analysis
"""

from fpdf import FPDF
import os
import sys

OUTPUT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Cheque_Fraud_Detection_Documentation.pdf")


class DocPDF(FPDF):
    def __init__(self):
        super().__init__()
        self.set_auto_page_break(auto=True, margin=20)
        self.set_margins(20, 20, 20)

    def header(self):
        if self.page_no() == 1:
            return
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(120, 120, 120)
        self.cell(0, 8, "Cheque Fraud Detection — Complete Project Documentation", align="L")
        self.set_text_color(120, 120, 120)
        self.cell(0, 8, f"Page {self.page_no()}", align="R", new_x="LMARGIN", new_y="NEXT")
        self.set_draw_color(200, 200, 200)
        self.line(20, self.get_y(), 190, self.get_y())
        self.ln(3)

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(150, 150, 150)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

    def cover_page(self):
        self.add_page()
        # Dark background rectangle
        self.set_fill_color(15, 23, 42)
        self.rect(0, 0, 210, 297, "F")

        # Accent line
        self.set_fill_color(233, 69, 96)
        self.rect(20, 60, 170, 4, "F")

        # Title
        self.set_y(72)
        self.set_font("Helvetica", "B", 26)
        self.set_text_color(226, 232, 240)
        self.multi_cell(0, 12, "Cheque Fraud Detection\nusing Ink Variation Analysis", align="C")

        # Subtitle
        self.ln(6)
        self.set_font("Helvetica", "", 13)
        self.set_text_color(148, 163, 184)
        self.multi_cell(0, 8, "Complete Project Documentation & Learning Guide", align="C")

        # Tag pills (simulated)
        self.ln(10)
        self.set_font("Helvetica", "B", 10)
        tags = ["Python 3.8+", "PyTorch 2.0+", "Streamlit", "OpenCV", "Scikit-Learn"]
        self.set_x(20)
        x = 30
        for tag in tags:
            self.set_xy(x, self.get_y())
            self.set_fill_color(30, 41, 59)
            self.set_text_color(148, 163, 184)
            w = self.get_string_width(tag) + 10
            self.cell(w, 8, tag, fill=True, align="C")
            x += w + 5
            if x > 170:
                x = 30
                self.ln(10)

        # Models section
        self.ln(20)
        self.set_font("Helvetica", "B", 11)
        self.set_text_color(233, 69, 96)
        self.cell(0, 8, "MODELS IMPLEMENTED", align="C", new_x="LMARGIN", new_y="NEXT")
        self.ln(4)

        models = [
            ("Siamese Network", "~200K params", "Contrastive Loss Metric Learning"),
            ("CNN Baseline",    "~100K params", "Cross-Entropy Classification"),
            ("Classical ML",    "SVM + RF",     "GLCM + LBP + LAB Features"),
        ]
        for name, params, desc in models:
            self.set_x(25)
            self.set_fill_color(30, 41, 59)
            self.set_text_color(226, 232, 240)
            self.set_font("Helvetica", "B", 10)
            self.cell(60, 9, name, fill=True)
            self.set_fill_color(22, 33, 62)
            self.set_font("Helvetica", "", 9)
            self.cell(35, 9, params, fill=True)
            self.cell(75, 9, desc, fill=True, new_x="LMARGIN", new_y="NEXT")
            self.ln(1)

        # Bottom credit
        self.set_y(260)
        self.set_font("Helvetica", "I", 9)
        self.set_text_color(100, 116, 139)
        self.multi_cell(0, 6,
            "Based on: Dansena, Bag & Pal — \"Differentiating Pen Inks in\n"
            "Hand-written Bank Cheques\", ICPRMI 2017", align="C")

        # Reset colors for rest of doc
        self.set_text_color(0, 0, 0)
        self.set_fill_color(255, 255, 255)

    def toc_page(self):
        self.add_page()
        self.chapter_title("Table of Contents")

        toc = [
            ("1", "Project Overview", ""),
            ("1.1", "What the Project Does", ""),
            ("1.2", "Problem It Solves", ""),
            ("1.3", "Real-World Use Cases", ""),
            ("1.4", "High-Level Architecture", ""),
            ("2", "Project Structure", ""),
            ("2.1", "Directory Layout", ""),
            ("2.2", "File Purposes & Interactions", ""),
            ("3", "Detailed File-by-File Breakdown", ""),
            ("3.1", "config.py", ""),
            ("3.2", "app.py — Streamlit Web Application", ""),
            ("3.3", "src/data_loader.py", ""),
            ("3.4", "src/preprocessing.py", ""),
            ("3.5", "src/patch_generator.py", ""),
            ("3.6", "src/models/siamese_model.py", ""),
            ("3.7", "src/models/cnn_model.py", ""),
            ("3.8", "src/models/classical_model.py", ""),
            ("3.9", "src/train.py", ""),
            ("3.10", "src/evaluate.py", ""),
            ("3.11", "src/fraud_pipeline.py", ""),
            ("3.12", "src/gradcam.py", ""),
            ("3.13", "src/utils.py", ""),
            ("3.14", "Utility & Helper Scripts", ""),
            ("4", "Logic & Execution Flow", ""),
            ("4.1", "Step-by-Step Pipeline", ""),
            ("4.2", "Data Flow Diagram", ""),
            ("5", "Models & Algorithms", ""),
            ("5.1", "Siamese Network — Deep Dive", ""),
            ("5.2", "CNN Baseline — Deep Dive", ""),
            ("5.3", "Classical ML — Deep Dive", ""),
            ("5.4", "Model Comparison & Trade-offs", ""),
            ("6", "Feature Engineering & Data Processing", ""),
            ("6.1", "LAB Color Space", ""),
            ("6.2", "GLCM Texture Features", ""),
            ("6.3", "LBP Features", ""),
            ("6.4", "Data Augmentation", ""),
            ("7", "Visual Elements & Outputs", ""),
            ("8", "Mathematical Concepts", ""),
            ("8.1", "Contrastive Loss Formula", ""),
            ("8.2", "Euclidean Distance & Similarity", ""),
            ("8.3", "Grad-CAM Mathematics", ""),
            ("9", "Code Logic & Design Decisions", ""),
            ("10", "Deployment & Execution", ""),
            ("11", "Testing", ""),
            ("12", "Limitations & Improvements", ""),
            ("13", "Glossary & Quick Reference", ""),
        ]

        self.set_font("Helvetica", "", 10)
        for num, title, _ in toc:
            is_main = len(num) == 1
            if is_main:
                self.ln(2)
                self.set_font("Helvetica", "B", 10)
                self.set_text_color(233, 69, 96)
            else:
                self.set_font("Helvetica", "", 9)
                self.set_text_color(50, 50, 50)

            indent = 5 if not is_main else 0
            self.set_x(20 + indent)
            self.cell(0, 6, f"{'  ' if not is_main else ''}{num}  {title}", new_x="LMARGIN", new_y="NEXT")
        self.set_text_color(0, 0, 0)

    # ── Formatting helpers ─────────────────────────────────────────────

    def chapter_title(self, text, color=(233, 69, 96)):
        self.ln(2)
        self.set_font("Helvetica", "B", 16)
        self.set_text_color(*color)
        self.cell(0, 10, text, new_x="LMARGIN", new_y="NEXT")
        self.set_draw_color(*color)
        self.line(20, self.get_y(), 190, self.get_y())
        self.ln(4)
        self.set_text_color(0, 0, 0)
        self.set_draw_color(0, 0, 0)

    def section_title(self, text):
        self.ln(3)
        self.set_font("Helvetica", "B", 12)
        self.set_text_color(15, 52, 96)
        self.cell(0, 8, text, new_x="LMARGIN", new_y="NEXT")
        self.set_text_color(0, 0, 0)
        self.ln(1)

    def subsection_title(self, text):
        self.ln(2)
        self.set_font("Helvetica", "B", 10)
        self.set_text_color(60, 80, 120)
        self.cell(0, 7, text, new_x="LMARGIN", new_y="NEXT")
        self.set_text_color(0, 0, 0)

    def body(self, text):
        self.set_font("Helvetica", "", 10)
        self.set_text_color(30, 30, 30)
        self.multi_cell(0, 6, text)
        self.ln(2)

    def bullet(self, items, indent=5):
        self.set_font("Helvetica", "", 10)
        self.set_text_color(30, 30, 30)
        for item in items:
            self.set_x(20 + indent)
            self.multi_cell(0, 6, f"\u2022  {item}")
        self.ln(2)

    def code_block(self, code, title=""):
        if title:
            self.set_font("Helvetica", "B", 9)
            self.set_text_color(100, 100, 100)
            self.cell(0, 6, title, new_x="LMARGIN", new_y="NEXT")
        self.set_fill_color(245, 245, 250)
        self.set_draw_color(200, 200, 220)
        self.set_text_color(30, 30, 80)
        self.set_font("Courier", "", 8)
        self.multi_cell(0, 5, code, fill=True, border=1)
        self.set_text_color(0, 0, 0)
        self.set_fill_color(255, 255, 255)
        self.set_draw_color(0, 0, 0)
        self.ln(3)

    def info_box(self, text, color=(230, 245, 255)):
        self.set_fill_color(*color)
        self.set_font("Helvetica", "I", 9)
        self.set_text_color(30, 60, 120)
        self.multi_cell(0, 6, f"  {text}", fill=True)
        self.ln(2)
        self.set_text_color(0, 0, 0)
        self.set_fill_color(255, 255, 255)

    def table(self, headers, rows, col_widths=None):
        n = len(headers)
        usable = 170
        if col_widths is None:
            col_widths = [usable // n] * n

        # Header row
        self.set_fill_color(15, 52, 96)
        self.set_text_color(255, 255, 255)
        self.set_font("Helvetica", "B", 9)
        for h, w in zip(headers, col_widths):
            self.cell(w, 8, h, border=1, fill=True, align="C")
        self.ln()

        # Data rows
        self.set_text_color(30, 30, 30)
        for i, row in enumerate(rows):
            fill_color = (245, 248, 255) if i % 2 == 0 else (255, 255, 255)
            self.set_fill_color(*fill_color)
            self.set_font("Helvetica", "", 9)
            for cell, w in zip(row, col_widths):
                self.cell(w, 7, str(cell), border=1, fill=True)
            self.ln()
        self.ln(3)
        self.set_fill_color(255, 255, 255)


# ════════════════════════════════════════════════════════════════════════
# CONTENT SECTIONS
# ════════════════════════════════════════════════════════════════════════

def write_section_1(pdf):
    pdf.add_page()
    pdf.chapter_title("1. Project Overview")

    pdf.section_title("1.1  What the Project Does")
    pdf.body(
        "This project is an AI-powered system that detects fraudulent modifications in bank cheque images "
        "by analysing pen ink variations. When a fraudster tampers with a cheque — for example, changing "
        "the payee name or inflating the amount — they typically use a different pen. Even when the inks "
        "look almost identical to the naked eye, subtle differences in colour and texture can be detected "
        "computationally.\n\n"
        "Think of it like a handwriting expert comparing ink — except the computer does it automatically, "
        "in seconds, using three distinct AI approaches."
    )

    pdf.section_title("1.2  The Problem It Solves")
    pdf.body(
        "Bank cheque fraud is a major global financial crime. Common tampering techniques include:"
    )
    pdf.bullet([
        "Altering the payee name (crossing it out and writing a new name)",
        "Inflating the amount (e.g., changing '5,000' to '55,000')",
        "Adding unauthorised text with a different pen",
        "Forging a second signature",
        "Crossing a cheque to make it bearer-payable",
    ])
    pdf.body(
        "Traditional forensic methods (chemical testing, spectroscopy) are expensive, time-consuming, "
        "and destructive. This system provides a fast, non-destructive, image-based automated alternative."
    )

    pdf.section_title("1.3  Real-World Use Cases")
    pdf.bullet([
        "Bank back-office automation: Screen cheques before processing",
        "Fraud investigation: Flag suspicious cheques for human review",
        "Audit systems: Batch-verify historical cheque images",
        "Insurance claims: Validate financial documents",
        "Legal forensics: Provide digital evidence of tampering",
    ])

    pdf.section_title("1.4  High-Level Architecture Overview")
    pdf.body(
        "The system follows a clear multi-stage pipeline:"
    )
    pdf.code_block(
        "Cheque Image\n"
        "     |\n"
        "     v\n"
        "[1] Preprocessing\n"
        "     Resize to 256x512, normalize [0,1], convert to LAB & Grayscale\n"
        "     |\n"
        "     v\n"
        "[2] Ink Mask Extraction\n"
        "     Adaptive thresholding to isolate ink pixels from background\n"
        "     |\n"
        "     v\n"
        "[3] Patch Extraction\n"
        "     Sliding window (64x64 patches, stride=32) over ink regions\n"
        "     |\n"
        "     v\n"
        "[4] Model Analysis  (choose one)\n"
        "     A. Siamese Network  --> pairwise similarity scores\n"
        "     B. CNN Baseline     --> patch class predictions\n"
        "     C. Classical ML     --> GLCM+LBP+LAB feature classification\n"
        "     |\n"
        "     v\n"
        "[5] Fraud Decision\n"
        "     If >20% of cross-region patch pairs are suspicious -> FRAUD\n"
        "     |\n"
        "     v\n"
        "[6] Output\n"
        "     Verdict (FRAUD / GENUINE) + Confidence Score\n"
        "     + Highlighted Image + Similarity Heatmap + Grad-CAM",
        title="End-to-End Pipeline"
    )

    pdf.info_box(
        "Analogy: Imagine you received a cheque and suspected the amount was altered. "
        "You would shine a UV light on it to check for erased ink or use a magnifier to see if the "
        "ink texture changes between sections. This system does exactly that — digitally and automatically."
    )


def write_section_2(pdf):
    pdf.add_page()
    pdf.chapter_title("2. Project Structure")

    pdf.section_title("2.1  Directory Layout")
    pdf.code_block(
        "d:/Shanky/                          <- Project root\n"
        "|\n"
        "+-- config.py                       <- Central configuration (all settings)\n"
        "+-- app.py                          <- Streamlit web application (main UI)\n"
        "+-- requirements.txt                <- Python package dependencies\n"
        "+-- README.md                       <- Quick-start guide\n"
        "+-- generate_sample_cheques.py      <- Generates realistic cheque images\n"
        "+-- rebuild_samples.py              <- Rebuilds sample set with high-contrast inks\n"
        "+-- regen_failing_cheques.py        <- Regenerates hard-to-detect fraud samples\n"
        "+-- model_comparison.py             <- Batch tests all models on all samples\n"
        "+-- test_detection.py               <- Quick accuracy test on 20 samples\n"
        "|\n"
        "+-- src/                            <- Core source code\n"
        "|   +-- __init__.py\n"
        "|   +-- data_loader.py              <- Dataset loading & synthetic generation\n"
        "|   +-- preprocessing.py            <- Image resize, LAB, augmentation\n"
        "|   +-- patch_generator.py          <- Patch extraction & pair generation\n"
        "|   +-- train.py                    <- Training all three models\n"
        "|   +-- evaluate.py                 <- Metrics, confusion matrix, ROC curves\n"
        "|   +-- fraud_pipeline.py           <- End-to-end fraud detection class\n"
        "|   +-- gradcam.py                  <- Grad-CAM explainability visualization\n"
        "|   +-- utils.py                    <- Shared utility functions\n"
        "|   +-- models/\n"
        "|       +-- __init__.py\n"
        "|       +-- siamese_model.py        <- Siamese CNN + Contrastive Loss\n"
        "|       +-- cnn_model.py            <- CNN baseline classifier\n"
        "|       +-- classical_model.py      <- GLCM + LBP + SVM/Random Forest\n"
        "|\n"
        "+-- data/\n"
        "|   +-- raw/                        <- Real IDRBT dataset goes here\n"
        "|   +-- processed/                  <- Preprocessed data cache\n"
        "|   +-- synthetic/                  <- Auto-generated synthetic cheques\n"
        "|   +-- samples/                    <- 20 curated sample cheques (5 genuine + 15 fraud)\n"
        "|\n"
        "+-- outputs/\n"
        "|   +-- models/                     <- Saved model weights (.pth, .pkl)\n"
        "|   +-- figures/                    <- Training curves, confusion matrices, ROC\n"
        "|   +-- sample_results/             <- Detection output images\n"
        "|\n"
        "+-- report/\n"
        "|   +-- report.md                   <- Project academic report\n"
        "|   +-- generate_pdf.py             <- Report PDF generator\n"
        "|   +-- Cheque_Fraud_Detection_Report.pdf\n"
        "|\n"
        "+-- tests/\n"
        "    +-- test_pipeline.py            <- Pytest unit tests"
    )

    pdf.section_title("2.2  How Files Interact")
    pdf.body(
        "The files are organized in a clean dependency chain. Here is the dependency flow:"
    )
    pdf.code_block(
        "config.py  <-- imported by ALL other files (paths, hyperparameters)\n"
        "    |\n"
        "    +-> data_loader.py   (loads dataset)\n"
        "    +-> preprocessing.py (transforms images)\n"
        "    +-> patch_generator.py (creates training pairs)\n"
        "    +-> models/*.py      (defines neural architectures)\n"
        "    +-> train.py         (orchestrates training)\n"
        "    +-> evaluate.py      (measures performance)\n"
        "    +-> fraud_pipeline.py (runs detection)\n"
        "    +-> gradcam.py       (generates explanations)\n"
        "    +-> utils.py         (shared helpers)\n"
        "\n"
        "app.py imports: config, fraud_pipeline, data_loader, preprocessing\n"
        "train.py imports: data_loader, patch_generator, all models, utils\n"
        "evaluate.py imports: all models, patch_generator, utils",
        title="Dependency Graph"
    )

    pdf.table(
        headers=["File", "Role", "Used By"],
        rows=[
            ["config.py",          "All settings in one place",           "Every file"],
            ["data_loader.py",     "Load real/synthetic cheque images",   "train.py, app.py"],
            ["preprocessing.py",   "Resize, normalize, LAB conversion",   "patch_generator.py, fraud_pipeline.py"],
            ["patch_generator.py", "Extract patches & training pairs",    "train.py, fraud_pipeline.py"],
            ["siamese_model.py",   "Siamese CNN architecture",            "train.py, fraud_pipeline.py"],
            ["cnn_model.py",       "CNN baseline architecture",           "train.py, fraud_pipeline.py"],
            ["classical_model.py", "GLCM+LBP+SVM/RF",                    "train.py, fraud_pipeline.py"],
            ["train.py",           "Train all models",                    "Called directly"],
            ["evaluate.py",        "Metrics & visualizations",            "Called directly"],
            ["fraud_pipeline.py",  "End-to-end detection",               "app.py, test scripts"],
            ["gradcam.py",         "Visual explanations",                 "fraud_pipeline.py, app.py"],
            ["utils.py",           "EarlyStopping, seeds, meters",        "train.py, evaluate.py"],
            ["app.py",             "Streamlit web UI",                    "User-facing"],
        ],
        col_widths=[42, 70, 58]
    )


def write_section_3(pdf):
    pdf.add_page()
    pdf.chapter_title("3. Detailed File-by-File Breakdown")

    # ── config.py ──
    pdf.section_title("3.1  config.py — Central Configuration")
    pdf.body(
        "This is the single most important file for settings. All hyperparameters, file paths, "
        "and default values are defined here. Any other file that needs a setting imports this file. "
        "This 'single source of truth' design means you only need to change a value once to affect "
        "the entire system."
    )
    pdf.subsection_title("Key Settings Explained")
    pdf.table(
        headers=["Setting", "Value", "What It Does"],
        rows=[
            ["IMAGE_SIZE",             "(256, 512)",     "All cheques resized to 256 rows x 512 cols"],
            ["PATCH_SIZE",             "64",             "Each analysis patch is 64x64 pixels"],
            ["PATCH_STRIDE",           "32",             "Window moves 32px at a time (50% overlap)"],
            ["MIN_INK_RATIO",          "0.05",           "Skip patches with < 5% ink pixels"],
            ["EMBEDDING_DIM",          "64",             "Siamese output vector size"],
            ["EPOCHS",                 "30",             "Max training epochs"],
            ["BATCH_SIZE",             "32",             "Samples per gradient update"],
            ["LEARNING_RATE",          "0.001",          "Adam optimizer step size"],
            ["CONTRASTIVE_MARGIN",     "2.0",            "Margin M in contrastive loss formula"],
            ["SIMILARITY_THRESHOLD",   "0.5",            "Below this score -> suspicious patch pair"],
            ["FRAUD_REGION_THRESHOLD", "0.2",            "> 20% suspicious pairs -> FRAUD verdict"],
            ["LBP_RADIUS",             "1",              "LBP neighbourhood radius"],
            ["LBP_N_POINTS",           "8",              "LBP sampling points"],
            ["GLCM_DISTANCES",         "[1, 3]",         "Pixel distances for GLCM computation"],
            ["COLOR_HIST_BINS",        "32",             "Bins per LAB channel histogram"],
            ["SVM_C",                  "1.0",            "SVM regularisation strength"],
            ["RF_N_ESTIMATORS",        "100",            "Number of trees in Random Forest"],
            ["DEVICE",                 "cuda / cpu",     "Auto-detects GPU, falls back to CPU"],
        ],
        col_widths=[52, 30, 88]
    )

    # ── app.py ──
    pdf.add_page()
    pdf.section_title("3.2  app.py — Streamlit Web Application")
    pdf.body(
        "This is the user-facing web interface built with Streamlit. It provides a polished, "
        "interactive dashboard where users can upload cheque images or choose from 20 sample cheques, "
        "select a detection model, and view a detailed analysis."
    )
    pdf.subsection_title("UI Components")
    pdf.bullet([
        "Sidebar: Model selector (Siamese / CNN / Classical), threshold sliders, model status indicators",
        "Upload area: Drag-and-drop or browse for cheque images",
        "Sample picker: Dropdown of 20 pre-made sample cheques",
        "Verdict banner: Large red FRAUD or green GENUINE verdict with glow effect",
        "4-stat row: Confidence %, patch pairs analysed, suspicious regions, avg. similarity",
        "Side-by-side: Original image vs. highlighted suspicious regions",
        "Similarity heatmap: Color-coded 2D map (green=same ink, red=different ink)",
        "Score distribution: Histogram of all pairwise similarity scores",
        "Grad-CAM panel: Neural network attention visualization",
    ])
    pdf.subsection_title("Key Functions in app.py")
    pdf.body("- st.set_page_config(): Configures the browser tab title and layout\n"
             "- CSS injection via st.markdown(): Dark theme, gradient header, result cards\n"
             "- FraudDetector(model_type): Creates detector with chosen model\n"
             "- detector.detect(image): Runs full pipeline, returns result dict\n"
             "- plt.subplots() sections: Draw heatmap and histogram charts\n"
             "- st.session_state: Remembers the loaded sample image across reruns")
    pdf.info_box(
        "Why Streamlit? It allows creating a fully interactive web app with pure Python — "
        "no JavaScript or HTML knowledge needed. Each user interaction triggers a Python rerun."
    )

    # ── data_loader.py ──
    pdf.add_page()
    pdf.section_title("3.3  src/data_loader.py — Dataset Loading")
    pdf.body(
        "This file handles how the system gets its training data. It has two modes: "
        "real data (from the IDRBT Kaggle dataset) and synthetic data (auto-generated when real data is absent)."
    )
    pdf.subsection_title("Class: ChequeDataset")
    pdf.body(
        "Loads real cheque images from data/raw/. It searches recursively for .jpg, .png, .bmp, .tif files. "
        "It also reads metadata from an Excel file that tells which pen was used in which image."
    )
    pdf.bullet([
        "load(): Scans directory for images, finds metadata Excel",
        "_load_metadata(excel): Reads pandas DataFrame from .xlsx file",
        "_parse_pen_columns(): Extracts pen info — looks for columns named 'pen', 'ink', 'instrument'",
        "_assign_pens_from_filenames(): Fallback — assigns pen IDs based on image index using modular arithmetic",
        "get_image(idx): Reads image with OpenCV, converts BGR -> RGB",
        "get_pen_info(idx): Returns [pen_A_id, pen_B_id] for an image",
        "__len__() and __getitem__(): Makes it work like a Python list",
    ])
    pdf.subsection_title("Class: SyntheticChequeGenerator")
    pdf.body(
        "When no real dataset is found, this generator creates synthetic cheque-like images. "
        "Each image has a paper-textured background, printed horizontal lines, and two regions "
        "with different simulated handwriting in different ink colors."
    )
    pdf.bullet([
        "INK_COLORS: 14 carefully chosen BGR colors simulating real pen inks (blues, blacks, grays)",
        "_create_cheque(): Creates background, adds paper noise, draws guidelines, calls _draw_handwriting()",
        "_draw_handwriting(): Simulates cursive strokes using connected line segments with slight color variation",
        "generate(): Creates N synthetic cheques and saves them to data/synthetic/",
    ])
    pdf.subsection_title("Function: load_dataset()")
    pdf.body(
        "The convenience function that tries real data first. If data/raw/ is empty, it automatically "
        "generates synthetic data. This makes the system work out-of-the-box without any dataset setup."
    )

    # ── preprocessing.py ──
    pdf.add_page()
    pdf.section_title("3.4  src/preprocessing.py — Image Preprocessing")
    pdf.body(
        "Before any model sees an image, it must be standardised. This file handles all image transformations."
    )
    pdf.subsection_title("Functions Explained")
    pdf.bullet([
        "resize_and_normalize(img, size): Resizes to 256x512 using INTER_AREA (best for shrinking), "
        "then divides by 255.0 to get float32 values in [0, 1]",
        "to_grayscale(img): Converts RGB to single-channel grayscale. Handles both float and uint8 input",
        "to_lab(img): Converts RGB -> LAB color space using OpenCV. LAB separates brightness (L) "
        "from color (A=green-red axis, B=blue-yellow axis)",
        "apply_augmentation(img, rng): Randomly applies rotation, noise, and brightness changes "
        "to prevent overfitting during training",
        "preprocess_cheque(img_or_path): The master function — loads an image (or accepts array), "
        "applies all transforms, returns dict with 'rgb', 'grayscale', 'lab', 'original' keys",
        "extract_ink_mask(img): Creates a binary True/False mask where True = ink pixel. "
        "Uses adaptive thresholding (accounts for local brightness variation) + morphological "
        "open/close to clean up noise",
    ])
    pdf.info_box(
        "Why LAB Color Space? Human eyes perceive color non-linearly, but LAB is designed to be "
        "perceptually uniform — equal distances in LAB space look equally different to humans. "
        "This makes it ideal for detecting subtle ink color differences."
    )

    # ── patch_generator.py ──
    pdf.add_page()
    pdf.section_title("3.5  src/patch_generator.py — Patch Extraction & Pairs")
    pdf.body(
        "This is the bridge between raw images and the model inputs. It extracts 64x64 pixel "
        "patches and organises them into training pairs."
    )
    pdf.subsection_title("extract_patches_sliding()")
    pdf.body(
        "Implements a sliding window: moves across the image left-to-right, top-to-bottom, "
        "extracting a 64x64 square at each step (stride=32 means 50% overlap between adjacent patches). "
        "Only keeps patches where at least 5% of pixels are ink (filtered by ink mask)."
    )
    pdf.code_block(
        "for y in range(0, H - patch_size + 1, stride):      # rows\n"
        "    for x in range(0, W - patch_size + 1, stride):  # columns\n"
        "        patch = img[y:y+64, x:x+64]                 # extract\n"
        "        ink_ratio = mask[y:y+64, x:x+64].mean()     # check ink\n"
        "        if ink_ratio >= 0.05: keep patch             # filter"
    )
    pdf.subsection_title("extract_patches_contour()")
    pdf.body(
        "Alternative approach: finds ink regions using contour detection (cv2.findContours), "
        "then extracts patches centred on each detected contour. Good for sparse ink areas."
    )
    pdf.subsection_title("assign_patch_regions()")
    pdf.body(
        "Since each cheque is written with two pens (left half = pen A, right half = pen B), "
        "this function sorts patches into two groups based on their x-coordinate relative to "
        "the image midpoint."
    )
    pdf.subsection_title("generate_pairs()")
    pdf.body(
        "Creates training pairs for the Siamese network:\n"
        "- SAME-pen pairs (label=1): Both patches from the same region → should have small distance\n"
        "- DIFFERENT-pen pairs (label=0): One patch from each region → should have large distance\n"
        "- Balanced: 50% same-pen, 50% different-pen pairs"
    )
    pdf.subsection_title("PyTorch Dataset Classes")
    pdf.bullet([
        "PatchPairDataset: Wraps pairs for the Siamese network. Returns (tensor_A, tensor_B, label)",
        "SinglePatchDataset: Wraps single patches for CNN. Returns (patch_tensor, label)",
        "Both transpose (H,W,C) numpy arrays to (C,H,W) tensors as PyTorch expects",
    ])

    # ── siamese_model.py ──
    pdf.add_page()
    pdf.section_title("3.6  src/models/siamese_model.py — Siamese Network")
    pdf.body(
        "This is the primary and most sophisticated model. A Siamese network uses two identical "
        "CNN branches (sharing the exact same weights) to process two image patches simultaneously, "
        "then compares their output vectors."
    )
    pdf.subsection_title("Class: SiameseEmbeddingNetwork")
    pdf.body("The single branch used by both arms of the Siamese network:")
    pdf.code_block(
        "Input: (B, 3, 64, 64)   <- B images, 3 RGB channels, 64x64 pixels\n"
        "\n"
        "Block 1: Conv2d(3->32, 3x3) -> BatchNorm -> ReLU -> MaxPool(2) -> Dropout2d\n"
        "         Output: (B, 32, 32, 32)\n"
        "\n"
        "Block 2: Conv2d(32->64, 3x3) -> BatchNorm -> ReLU -> MaxPool(2) -> Dropout2d\n"
        "         Output: (B, 64, 16, 16)\n"
        "\n"
        "Block 3: Conv2d(64->128, 3x3) -> BatchNorm -> ReLU -> MaxPool(2)\n"
        "         Output: (B, 128, 8, 8)\n"
        "\n"
        "Global Pool: AdaptiveAvgPool2d(1)\n"
        "         Output: (B, 128, 1, 1) -> Flatten -> (B, 128)\n"
        "\n"
        "Embedding: Linear(128->64) -> BatchNorm1d\n"
        "         Output: (B, 64)   <- 64-dimensional embedding vector",
        title="SiameseEmbeddingNetwork Architecture"
    )
    pdf.subsection_title("Class: SiameseCNN (Full Model)")
    pdf.body(
        "Contains ONE branch (self.branch = SiameseEmbeddingNetwork). Both inputs pass through "
        "THE SAME branch — this weight sharing is what makes it a 'Siamese' network."
    )
    pdf.bullet([
        "forward(x1, x2): Passes both patches through the shared branch, returns (emb1, emb2)",
        "get_distance(x1, x2): Euclidean distance between embeddings",
        "get_similarity(x1, x2): Converts distance to similarity score [0,1] using exp(-d/margin)",
    ])
    pdf.subsection_title("Class: ContrastiveLoss")
    pdf.body("The training objective. For same-ink pairs (label=1): minimises distance. "
             "For different-ink pairs (label=0): maximises distance (up to the margin).")
    pdf.code_block(
        "L = label * 0.5 * D^2   +   (1-label) * 0.5 * max(0, margin - D)^2\n"
        "\n"
        "where:\n"
        "  label = 1 (same ink)  --> first term active, pull embeddings together\n"
        "  label = 0 (diff ink)  --> second term active, push apart up to margin\n"
        "  D     = Euclidean distance between embedding vectors\n"
        "  margin = 2.0  (from config.py)",
        title="Contrastive Loss Formula"
    )

    # ── cnn_model.py ──
    pdf.add_page()
    pdf.section_title("3.7  src/models/cnn_model.py — CNN Baseline")
    pdf.body(
        "A simpler model used as a performance baseline. Instead of comparing pairs, it directly "
        "classifies each patch as 'ink type A' or 'ink type B'. This is the standard classification "
        "approach, contrasted against the more sophisticated Siamese metric learning."
    )
    pdf.code_block(
        "Input: (B, 3, 64, 64)\n"
        "\n"
        "Block 1: Conv2d(3->16) -> BN -> ReLU -> MaxPool  -> (B, 16, 32, 32)\n"
        "Block 2: Conv2d(16->32) -> BN -> ReLU -> MaxPool -> (B, 32, 16, 16)\n"
        "Block 3: Conv2d(32->64) -> BN -> ReLU -> AdaptiveAvgPool -> (B, 64, 1, 1)\n"
        "\n"
        "Classifier: Flatten -> Linear(64->32) -> ReLU -> Dropout(0.3) -> Linear(32->2)\n"
        "Output: (B, 2)  <- logits for [class_A, class_B]",
        title="InkClassifierCNN Architecture (~100K parameters)"
    )
    pdf.subsection_title("Key Methods")
    pdf.bullet([
        "forward(x): Returns raw logits (unnormalized scores)",
        "predict_proba(x): Applies softmax → probability distribution over 2 classes",
        "get_feature_maps(x): Returns the last conv layer's output for Grad-CAM",
    ])
    pdf.info_box(
        "Why is CNN a 'baseline'? Because it has an inherent limitation: it needs the same pen "
        "to always appear on the same side of the cheque (left=class 0, right=class 1). "
        "The Siamese network, by contrast, learns ink similarity independently of position."
    )

    # ── classical_model.py ──
    pdf.add_page()
    pdf.section_title("3.8  src/models/classical_model.py — Classical ML")
    pdf.body(
        "Before deep learning, computer vision relied on hand-crafted features — mathematical "
        "descriptions of image properties computed by experts. This file implements three such "
        "feature types combined with traditional ML classifiers."
    )
    pdf.subsection_title("Feature 1: GLCM (Gray-Level Co-occurrence Matrix)")
    pdf.body(
        "GLCM captures the spatial relationship between pixel brightness values. For each pair of "
        "pixel brightness values (i, j) that appear at a specific distance and angle, it counts "
        "how often they occur together.\n\n"
        "From the GLCM, five texture properties are extracted:"
    )
    pdf.bullet([
        "Contrast: How much the pixel pairs differ (high = rough texture)",
        "Dissimilarity: Similar to contrast but linear (not squared)",
        "Homogeneity: How close the distribution is to the diagonal (high = uniform)",
        "Energy: Sum of squared GLCM entries (high = very uniform texture)",
        "Correlation: Linear dependency between brightness pairs",
    ])
    pdf.body("These are computed at 2 distances (1,3) and 4 angles (0°,45°,90°,135°) = 40 features total.")
    pdf.subsection_title("Feature 2: LBP (Local Binary Pattern)")
    pdf.body(
        "LBP looks at each pixel and its 8 neighbours. For each neighbour, it records 1 if "
        "the neighbour is brighter than the centre pixel, else 0. The 8 bits form a binary number "
        "(0-255). A histogram of these patterns across the patch = 10-bin LBP feature vector.\n\n"
        "LBP captures fine-grain texture patterns like ink stroke edges."
    )
    pdf.subsection_title("Feature 3: LAB Color Histogram")
    pdf.body(
        "The patch is converted to LAB color space and a 32-bin histogram is computed for each "
        "of the 3 channels (L, A, B). This gives 96 features capturing the colour distribution "
        "of ink pixels in a perceptually meaningful space."
    )
    pdf.body("Total feature vector: 40 (GLCM) + 10 (LBP) + 96 (color) = ~146 dimensions per patch.")
    pdf.subsection_title("Classifiers")
    pdf.bullet([
        "SVM (RBF kernel): Finds the optimal hyperplane separating ink classes in 146D feature space. "
        "RBF kernel allows non-linear boundaries. C=1.0 controls regularisation.",
        "Random Forest (100 trees): Builds 100 decision trees on random subsets of data and features, "
        "averages their votes. Inherently handles non-linearity and feature importance.",
        "Both use Pipeline(StandardScaler + Classifier) to normalise features before classification",
    ])

    # ── train.py ──
    pdf.add_page()
    pdf.section_title("3.9  src/train.py — Training All Models")
    pdf.body(
        "This is the master training script. Run 'python src/train.py' to train all three model "
        "types sequentially. It takes 2–5 minutes on CPU."
    )
    pdf.subsection_title("train_siamese()")
    pdf.body(
        "Training loop for the Siamese network:"
    )
    pdf.bullet([
        "Generates patch pairs (same-ink and different-ink)",
        "Splits 70% train / 15% val / 15% test",
        "Creates PatchPairDataset and DataLoader objects",
        "Uses Adam optimizer (lr=0.001, weight_decay=1e-4)",
        "ReduceLROnPlateau scheduler: halves learning rate if val_loss stagnates for 3 epochs",
        "Saves best model based on validation loss ('siamese_best.pth')",
        "EarlyStopping stops training if no improvement for 5 epochs",
        "Plots training curves (loss + accuracy vs. epoch)",
    ])
    pdf.subsection_title("train_cnn()")
    pdf.body(
        "Training loop for CNN baseline — identical structure but uses CrossEntropyLoss "
        "instead of ContrastiveLoss, and single patches instead of pairs."
    )
    pdf.subsection_title("train_classical()")
    pdf.body(
        "Training for SVM and Random Forest — no gradient descent. Just feature extraction "
        "and sklearn's fit() method. Trains both classifiers, saves with pickle."
    )
    pdf.subsection_title("Helper Utilities Used")
    pdf.bullet([
        "AverageMeter: Tracks running average of loss over a mini-batch epoch",
        "EarlyStopping: Monitors val_loss with patience=5 and min_delta=0.001",
        "count_parameters(): Reports total trainable parameter count",
        "set_seed(42): Ensures reproducible results",
        "_plot_training_curves(): Saves loss/accuracy plots to outputs/figures/",
    ])

    # ── evaluate.py ──
    pdf.add_page()
    pdf.section_title("3.10  src/evaluate.py — Evaluation & Metrics")
    pdf.body(
        "After training, evaluate.py measures how well each model actually performs. "
        "Run 'python src/evaluate.py' to generate all metrics and visualisations."
    )
    pdf.subsection_title("evaluate_siamese()")
    pdf.bullet([
        "Loads siamese_best.pth and siamese_metadata.pth (contains test pairs)",
        "Runs inference: for each test pair, computes embedding distance",
        "Predicts: same ink if distance < margin/2 (=1.0)",
        "Computes: accuracy, precision, recall, F1-score",
        "Saves: confusion matrix (siamese_confusion.png)",
        "Saves: distance distribution plot showing overlap between same/different ink",
    ])
    pdf.subsection_title("evaluate_cnn()")
    pdf.bullet([
        "Loads cnn_best.pth and cnn_metadata.pth",
        "Runs softmax predictions on test patches",
        "Computes all classification metrics",
        "Saves: CNN confusion matrix",
    ])
    pdf.subsection_title("evaluate_classical()")
    pdf.bullet([
        "Loads classical_svm.pkl, classical_rf.pkl, and classical_test_data.pkl",
        "Evaluates both SVM and RF on test set",
        "Saves confusion matrices for both",
    ])
    pdf.subsection_title("compare_models()")
    pdf.bullet([
        "Prints a formatted comparison table (accuracy, precision, recall, F1)",
        "Generates a grouped bar chart comparing all models (model_comparison.png)",
        "Plots ROC curves with AUC scores for all models on the same axes (roc_curves.png)",
    ])

    # ── fraud_pipeline.py ──
    pdf.add_page()
    pdf.section_title("3.11  src/fraud_pipeline.py — The Detection Engine")
    pdf.body(
        "This is the core of the system — the FraudDetector class ties everything together "
        "into a single detect() call. This is what app.py calls when you click 'Detect Fraud'."
    )
    pdf.subsection_title("FraudDetector.__init__() and _load_model()")
    pdf.body(
        "Loads the chosen model from disk. If the model file doesn't exist (not yet trained), "
        "uses random weights and warns the user. Supports all three model types."
    )
    pdf.subsection_title("FraudDetector.detect(image_input)")
    pdf.body("Master method — returns a rich result dictionary:")
    pdf.bullet([
        "'verdict': 'FRAUD' or 'GENUINE'",
        "'confidence': float [0.0, 1.0]",
        "'highlighted_image': original image with suspicious regions marked in red",
        "'similarity_map': 2D numpy array (H x W) of similarity scores",
        "'similarity_scores': list of all pairwise scores",
        "'suspicious_patches': list of suspicious (pos_A, pos_B, score) tuples",
        "'gradcam_overlay': Grad-CAM heatmap overlaid on a sample patch",
    ])
    pdf.subsection_title("_detect_siamese() — Hybrid 4-Signal Approach")
    pdf.body("The Siamese detection uses FOUR complementary signals to make a robust decision:")
    pdf.table(
        headers=["Signal", "Trigger", "Fraud Score Contribution"],
        rows=[
            ["Absolute threshold",   "> FRAUD_REGION_THRESHOLD patches below sim 0.5", "+0.5 + ratio"],
            ["Distribution spread",  "score_range > 0.15 AND std > 0.05",              "+0.3 + CV"],
            ["Adaptive outliers",    "ratio of scores below (mean - 1.5*std) > 10%",   "+0.2 + ratio"],
            ["LAB color divergence", "AB chromaticity distance > 7.0 between regions", "+0 to +0.6"],
        ],
        col_widths=[45, 70, 55]
    )
    pdf.body(
        "If total fraud_score >= 0.55 → FRAUD verdict. This multi-signal approach prevents "
        "false negatives from models that aren't well-trained while avoiding false positives "
        "on genuine cheques."
    )
    pdf.subsection_title("_compute_color_divergence()")
    pdf.body(
        "Compares the average LAB chromaticity (A and B channels) of ink pixels in the left vs. "
        "right regions. Ink pixels are identified as dark pixels (L < 150) with some chromaticity "
        "(not pure grey/black, which would be the printed text). High divergence = different ink colors."
    )
    pdf.subsection_title("_highlight_regions()")
    pdf.body(
        "Draws red rectangles over suspicious patches and blends a semi-transparent red overlay "
        "(alpha=0.3) to highlight tampered areas without obscuring the original content."
    )

    # ── gradcam.py ──
    pdf.add_page()
    pdf.section_title("3.12  src/gradcam.py — Grad-CAM Explainability")
    pdf.body(
        "Grad-CAM (Gradient-weighted Class Activation Mapping) answers the question: "
        "'Which parts of the image most influenced the model's decision?' "
        "It produces a heatmap highlighting the most important regions."
    )
    pdf.subsection_title("How Grad-CAM Works")
    pdf.bullet([
        "Step 1 — Forward pass: Run input through the CNN, record activations at last conv layer",
        "Step 2 — Backward pass: Backpropagate gradients for the target class",
        "Step 3 — Pool gradients: Global average of gradients gives importance weight per feature map",
        "Step 4 — Weight activations: Multiply weights × activation maps and sum",
        "Step 5 — ReLU: Keep only positive contributions",
        "Step 6 — Resize: Upsample to input image size",
        "Step 7 — Normalise: Scale to [0, 1]",
        "Step 8 — Colorise: Apply JET colormap (blue=low, red=high importance)",
    ])
    pdf.subsection_title("PyTorch Hooks Used")
    pdf.body(
        "Hooks are callbacks that execute during forward/backward passes. Two hooks are registered:\n"
        "- forward_hook: Captures the activation tensor output of the target layer\n"
        "- backward_hook (full_backward): Captures the gradient tensor flowing through the layer\n\n"
        "This non-invasive approach doesn't require modifying the model architecture."
    )
    pdf.subsection_title("get_gradcam_for_siamese()")
    pdf.body(
        "Special handling for Siamese: since it has no class output, Grad-CAM uses the L2 norm "
        "(magnitude) of the embedding vector as the target signal. This shows which patch regions "
        "most contribute to the ink representation."
    )

    # ── utils.py ──
    pdf.section_title("3.13  src/utils.py — Shared Utilities")
    pdf.bullet([
        "set_seed(seed=42): Sets Python random, NumPy, and PyTorch seeds for reproducibility",
        "save_figure(fig, name): Saves matplotlib figure to outputs/figures/ at 150 DPI",
        "count_parameters(model): Counts trainable parameters (useful for model size reports)",
        "ensure_dir(path): Creates a directory if it doesn't exist (makedirs with exist_ok)",
        "EarlyStopping class: Monitors validation loss; stops training when stuck for 'patience' epochs",
        "AverageMeter class: Tracks running mean of values (loss, accuracy) within an epoch",
    ])

    # ── Helper Scripts ──
    pdf.section_title("3.14  Helper & Utility Scripts (Root Level)")
    pdf.table(
        headers=["Script", "Purpose"],
        rows=[
            ["generate_sample_cheques.py", "Creates 20 realistic sample cheques using PIL + OpenCV. "
             "Simulates bank cheques with correct layout, security patterns, signatures."],
            ["rebuild_samples.py",         "Recreates the 20 samples from scratch with high-contrast "
             "Blue+RED+GREEN ink combinations for maximum model detectability."],
            ["regen_failing_cheques.py",   "Targeted regeneration of specific fraud samples that were "
             "hard for models to detect (uses extreme ink contrast)."],
            ["model_comparison.py",        "Batch-tests all 3 models on all 20 samples, computes "
             "accuracy metrics, saves results to CSV and JSON files."],
            ["test_detection.py",          "Quick accuracy test showing pass/fail for each model "
             "on each of the 20 sample images with a summary bar chart."],
        ],
        col_widths=[60, 110]
    )


def write_section_4(pdf):
    pdf.add_page()
    pdf.chapter_title("4. Logic & Execution Flow")

    pdf.section_title("4.1  Step-by-Step Execution Flow")
    pdf.body("Here is exactly what happens when you click 'Detect Fraud' in the app:")

    steps = [
        ("Step 1: Image Load", "app.py reads the uploaded file bytes. cv2.imdecode() converts "
         "the raw bytes into a numpy array. cv2.cvtColor() converts BGR (OpenCV default) to RGB."),
        ("Step 2: Preprocessing", "preprocess_cheque(image) is called. The image is resized "
         "to 256x512 using INTER_AREA interpolation. Pixel values divided by 255 → float32 in [0,1]. "
         "LAB and grayscale versions are computed."),
        ("Step 3: Ink Mask", "extract_ink_mask(rgb_image) applies adaptive Gaussian thresholding. "
         "Morphological opening removes noise dots. Closing fills small gaps. Result: True/False mask."),
        ("Step 4: Patch Extraction", "extract_patches_sliding() slides a 64x64 window across the "
         "image with stride=32. Only patches with >= 5% ink pixels are kept. Typically 50-200 patches."),
        ("Step 5: Region Assignment", "Patches are split into left (pen A) and right (pen B) "
         "groups based on their x-coordinate relative to image midpoint."),
        ("Step 6A: Siamese Detection", "Every left patch is compared to every right patch. "
         "Both patches are converted to tensors and fed through the Siamese model. "
         "get_similarity() returns exp(-distance/margin) for each pair."),
        ("Step 6B: CNN Detection", "Each patch is classified as class 0 or class 1. "
         "If significant class mixing is found, it signals different inks."),
        ("Step 6C: Classical Detection", "Each patch is converted to a 146-dim feature vector "
         "(GLCM+LBP+LAB). SVM or RF classifies it. Class mixing ratio determines fraud."),
        ("Step 7: Color Divergence", "_compute_color_divergence() extracts mean A,B chromaticity "
         "from dark, coloured ink pixels in left vs right regions. Euclidean distance in AB space."),
        ("Step 8: Fraud Decision", "Four signals are combined into a fraud_score. "
         "If fraud_score >= 0.55 → FRAUD. confidence = min(1.0, fraud_score)."),
        ("Step 9: Visualization", "Suspicious patches are highlighted with red rectangles. "
         "Similarity map is built by averaging scores across patch positions. "
         "Grad-CAM is computed for a sample patch."),
        ("Step 10: Display", "app.py receives the result dict and renders verdict, stats, "
         "highlighted image, heatmap, histogram, and Grad-CAM using Streamlit components."),
    ]

    for title, desc in steps:
        pdf.subsection_title(title)
        pdf.body(desc)

    pdf.section_title("4.2  Training Flow (when you run src/train.py)")
    pdf.code_block(
        "1. set_seed(42)                          # Reproducibility\n"
        "2. load_dataset()                        # Real or synthetic data\n"
        "3. generate_pairs(dataset)               # Create Siamese training pairs\n"
        "4. generate_single_patches(dataset)      # Create CNN/Classical patches\n"
        "5. split_data(pairs, 70/15/15)           # Train/Val/Test split\n"
        "6. train_siamese(pairs):\n"
        "   a. Create DataLoaders\n"
        "   b. For each epoch:\n"
        "      i.  Train: forward, loss, backward, optimizer.step()\n"
        "      ii. Validate: no gradients, compute val_loss, accuracy\n"
        "      iii.Save if best val_loss\n"
        "      iv. Check early stopping\n"
        "   c. Load best weights, plot curves, save metadata\n"
        "7. train_cnn(patches)    [same structure, CrossEntropyLoss]\n"
        "8. train_classical(patches)  [sklearn fit, no backprop]\n"
        "9. Print total time elapsed"
    )


def write_section_5(pdf):
    pdf.add_page()
    pdf.chapter_title("5. Models & Algorithms — Deep Dive")

    pdf.section_title("5.1  Siamese Network — The Primary Model")
    pdf.subsection_title("Concept")
    pdf.body(
        "A Siamese network is not just a model — it is a learning paradigm. Instead of learning "
        "'what class does this belong to?', it learns 'are these two things similar?'. "
        "This is called metric learning.\n\n"
        "Analogy: You train a dog to recognise its owner not by memorising a single photo, "
        "but by learning the concept of similarity. That's metric learning.\n\n"
        "The Siamese architecture uses a SINGLE neural network branch (the 'twin') that processes "
        "both input patches. Because both branches share weights, they transform inputs into the "
        "same embedding space. Similar inputs end up close together in this space; dissimilar "
        "inputs are far apart."
    )
    pdf.subsection_title("Why Siamese for This Problem?")
    pdf.bullet([
        "Small dataset: Metric learning generalises better than classification on small data "
        "(generates N^2 training pairs from N images)",
        "No class labels needed: We don't need to label every pen type — just same/different",
        "Generalises to new pen types: The similarity metric works on unseen inks",
        "Naturally handles comparison: Fraud detection IS a comparison task",
    ])
    pdf.subsection_title("Embedding Space Visualisation")
    pdf.body(
        "After training, same-ink patches cluster together in 64-dimensional space. "
        "Different-ink patches are separated by at least 'margin' distance (=2.0). "
        "The fraud detector computes distances between left-region and right-region embeddings — "
        "large distances indicate different inks."
    )
    pdf.subsection_title("Similarity Score Formula")
    pdf.code_block(
        "distance  = sqrt(sum((emb1 - emb2)^2))     # Euclidean distance\n"
        "similarity = exp(-distance / margin)         # Exponential decay\n"
        "\n"
        "When distance = 0      -> similarity = exp(0) = 1.0  (identical)\n"
        "When distance = margin -> similarity = exp(-1) = 0.37 (threshold)\n"
        "When distance >> margin-> similarity -> 0.0  (completely different)"
    )

    pdf.add_page()
    pdf.section_title("5.2  CNN Baseline")
    pdf.subsection_title("Concept")
    pdf.body(
        "The CNN baseline treats ink detection as a standard image classification problem. "
        "Each 64x64 patch is classified as 'pen A region' (class 0) or 'pen B region' (class 1). "
        "If many patches from the left region are classified as class 1 (or vice versa), "
        "it suggests ink inconsistency."
    )
    pdf.subsection_title("Limitations vs. Siamese")
    pdf.bullet([
        "Position-dependent: Assumes pen A is always on the left, pen B on the right",
        "Struggles with novel pen types unseen during training",
        "May overfit on small datasets",
        "Cannot quantify HOW different two inks are, only that they're classified differently",
    ])
    pdf.subsection_title("When CNN Outperforms Siamese")
    pdf.body(
        "On well-trained datasets with consistent left/right pen assignments, the CNN can achieve "
        "higher accuracy because it's a simpler, more direct task than metric learning."
    )

    pdf.section_title("5.3  Classical ML Pipeline")
    pdf.subsection_title("Philosophy")
    pdf.body(
        "Classical ML requires domain experts to design features. The three feature types "
        "were specifically chosen because they capture different aspects of ink appearance:\n"
        "- GLCM: How ink pixels relate spatially (texture of the stroke)\n"
        "- LBP: Local patterns at ink edges (microstructure of pen strokes)\n"
        "- LAB histograms: The actual color distribution of the ink"
    )
    pdf.subsection_title("SVM vs. Random Forest Trade-offs")
    pdf.table(
        headers=["Aspect", "SVM (RBF)", "Random Forest"],
        rows=[
            ["Decision boundary", "Single curved hyperplane", "Many piecewise boundaries"],
            ["Interpretability", "Low (kernel trick)", "Medium (feature importance)"],
            ["Speed (inference)", "Fast", "Moderate"],
            ["Overfitting risk", "Low (margin maximisation)", "Low (ensemble averaging)"],
            ["Best when", "Features well-separated", "Complex non-linear patterns"],
            ["Handles noise", "Well (C parameter)", "Well (averaging)"],
        ],
        col_widths=[50, 60, 60]
    )

    pdf.section_title("5.4  Full Model Comparison")
    pdf.table(
        headers=["Aspect", "Siamese", "CNN Baseline", "Classical SVM", "Classical RF"],
        rows=[
            ["Parameters",    "~200K",         "~100K",        "N/A",        "N/A"],
            ["Training data", "Pairs",          "Single patches","Single patches","Single patches"],
            ["Loss function", "Contrastive",    "Cross-Entropy", "Hinge",      "Gini/Entropy"],
            ["Inference",     "Pairwise dist.", "Softmax class", "Hyperplane", "Vote average"],
            ["Scalability",   "Good",           "Good",          "Poor (N^2)", "Good"],
            ["Explainability","Grad-CAM",       "Grad-CAM",      "Feature imp.","Feature imp."],
            ["Best for",      "Small datasets", "Baseline",      "Speed",      "Robustness"],
        ],
        col_widths=[32, 35, 35, 35, 33]
    )


def write_section_6(pdf):
    pdf.add_page()
    pdf.chapter_title("6. Feature Engineering & Data Processing")

    pdf.section_title("6.1  LAB Color Space — The Key to Ink Detection")
    pdf.body(
        "The most important single insight in this project is the use of LAB color space. "
        "Here's why it matters more than RGB:"
    )
    pdf.table(
        headers=["Color Space", "Channels", "Problem for Ink Detection"],
        rows=[
            ["RGB",  "Red, Green, Blue",              "Color and brightness mixed — hard to compare"],
            ["HSV",  "Hue, Saturation, Value",        "Hue is circular, unstable for subtle differences"],
            ["LAB",  "Luminance, Green-Red, Blue-Yellow", "Perceptually uniform — ideal for comparison"],
        ],
        col_widths=[30, 65, 75]
    )
    pdf.body(
        "In LAB space, the A channel captures green-red tint (blue pens have different A values) "
        "and the B channel captures blue-yellow tint. Two blue pens with slightly different "
        "formulations will show measurable AB differences even if they look identical to humans."
    )

    pdf.section_title("6.2  GLCM — Texture Analysis Explained")
    pdf.body(
        "Imagine a 64x64 greyscale patch. GLCM asks: 'How often does pixel value 50 appear "
        "directly to the right of pixel value 70?'. It builds a frequency table of ALL such "
        "value-pair co-occurrences.\n\n"
        "Different pens produce different stroke textures — a ball-point pen makes smoother "
        "strokes than a felt-tip. GLCM captures this. "
        "The five derived statistics (contrast, homogeneity, etc.) summarise this texture in "
        "a compact feature vector."
    )
    pdf.code_block(
        "# Quantize to 64 levels (reduces computation)\n"
        "patch_q = patch // 4\n"
        "\n"
        "# Compute GLCM at distances=[1,3] and angles=[0,45,90,135 degrees]\n"
        "glcm = graycomatrix(patch_q, distances=[1,3], angles=[...], levels=64)\n"
        "\n"
        "# Extract 5 properties x 2 distances x 4 angles = 40 features\n"
        "for prop in ['contrast','dissimilarity','homogeneity','energy','correlation']:\n"
        "    vals = graycoprops(glcm, prop).flatten()  # shape: (2,4) -> (8,)\n"
        "    features.extend(vals)"
    )

    pdf.section_title("6.3  LBP — Local Binary Patterns")
    pdf.body(
        "For each pixel at position (x,y), LBP looks at its 8 surrounding neighbours. "
        "It compares each neighbour's value to the centre:\n"
        "  - Neighbour >= centre: bit = 1\n"
        "  - Neighbour < centre:  bit = 0\n\n"
        "The 8 bits form a number (0-255). 'Uniform' LBP uses only patterns with at most 2 "
        "transitions between 0 and 1 (lines, edges, corners). These give 10 unique pattern types."
    )

    pdf.section_title("6.4  Data Augmentation — Preventing Overfitting")
    pdf.body(
        "With a small dataset, the model may memorise training examples rather than learning "
        "general ink characteristics. Augmentation creates artificial variety:"
    )
    pdf.table(
        headers=["Augmentation", "Range", "Simulates"],
        rows=[
            ["Random rotation",     "+/- 15 degrees",   "Tilted writing, scanning angle variation"],
            ["Gaussian noise",      "std=0.01",          "Scanner noise, paper grain"],
            ["Brightness variation","+/- 20%",           "Different scan settings, lighting"],
        ],
        col_widths=[45, 45, 80]
    )
    pdf.body(
        "Each augmentation is applied with 50% probability (controlled by rng.random() > 0.5), "
        "and uses a fixed NumPy RandomState for reproducibility."
    )

    pdf.section_title("6.5  Ink Mask Extraction — Filtering Background")
    pdf.body(
        "Before comparing patches, the system tries to analyse only the ink pixels and ignore "
        "the paper background. The adaptive thresholding step:"
    )
    pdf.bullet([
        "Converts image to grayscale",
        "Applies cv2.adaptiveThreshold with GAUSSIAN_C method: for each pixel, computes "
        "threshold from the local 11x11 neighbourhood mean minus a constant (C=5)",
        "This handles non-uniform illumination — works even if the cheque is not evenly lit",
        "Morphological opening (erosion then dilation): removes tiny noise dots",
        "Morphological closing (dilation then erosion): fills small gaps in ink strokes",
        "Result: clean binary mask, True = ink, False = paper",
    ])


def write_section_7(pdf):
    pdf.add_page()
    pdf.chapter_title("7. Visual Elements & Outputs")

    visuals = [
        ("Similarity Heatmap", "outputs/figures/", "roc_curves.png",
         "A 2D colour map overlaid on the cheque dimensions. Each pixel's colour encodes the "
         "average similarity score of all patch pairs that overlap that position. "
         "Green = high similarity (same ink), Red = low similarity (different ink). "
         "Generated by _build_similarity_map() using weighted accumulation."),
        ("Confusion Matrix", "outputs/figures/", "siamese_confusion.png, cnn_confusion.png, ...",
         "A 2x2 grid showing True Positives (same ink, correctly predicted same), "
         "False Positives (different ink, predicted same), etc. "
         "Generated with seaborn.heatmap() with annotation and Blues colormap."),
        ("ROC Curves", "outputs/figures/", "roc_curves.png",
         "Receiver Operating Characteristic — plots True Positive Rate vs False Positive Rate "
         "as the decision threshold varies. Area Under Curve (AUC) is a model quality metric. "
         "AUC=1.0 is perfect, AUC=0.5 is random. All models plotted together for comparison."),
        ("Training Curves", "outputs/figures/", "siamese_training.png, cnn_training.png",
         "Two side-by-side plots: (1) train loss and val loss vs. epoch — shows if overfitting "
         "is occurring (val loss rising while train loss falls); (2) validation accuracy vs epoch. "
         "Generated by _plot_training_curves() in train.py."),
        ("Distance Distribution", "outputs/figures/", "siamese_distance_dist.png",
         "Histogram showing the distribution of embedding distances for same-ink pairs (green) "
         "vs different-ink pairs (pink). Good separation between the distributions means the "
         "model has learned a useful metric. The decision threshold (margin/2) is shown as a "
         "red dashed vertical line."),
        ("Model Comparison Bar Chart", "outputs/figures/", "model_comparison.png",
         "Grouped bar chart with 4 colour-coded metric groups (Accuracy, Precision, Recall, F1) "
         "for each model. Allows instant visual comparison of all models."),
        ("Highlighted Image", "Streamlit UI", "Displayed in app",
         "The original cheque with red bounding boxes drawn around suspicious patches. "
         "A semi-transparent red overlay (alpha=0.3) fills suspicious regions. "
         "Exclamation marks label the most suspicious spots."),
        ("Grad-CAM Overlay", "Streamlit UI", "Displayed in app",
         "A 64x64 patch with the neural network's attention heatmap blended over it "
         "using JET colormap (blue=low, red=high importance). Shows which pixel regions "
         "the model focuses on when making its ink assessment."),
        ("Score Distribution Histogram", "Streamlit UI", "Displayed in app",
         "Bar chart of all pairwise similarity scores from a single cheque analysis. "
         "A red dashed vertical line marks the similarity threshold. Scores left of the line "
         "are classified as suspicious. The spread of the distribution indicates ink consistency."),
    ]

    for name, location, files, desc in visuals:
        pdf.subsection_title(f"{name}")
        pdf.body(f"Location: {location}   |   Files: {files}\n{desc}")
        pdf.ln(1)


def write_section_8(pdf):
    pdf.add_page()
    pdf.chapter_title("8. Mathematical & Technical Concepts")

    pdf.section_title("8.1  Contrastive Loss — Explained Simply")
    pdf.body("The contrastive loss formula controls what the Siamese network learns:")
    pdf.code_block(
        "L = label * 0.5 * D^2   +   (1 - label) * 0.5 * max(0, M - D)^2\n"
        "\n"
        "Variables:\n"
        "  D = Euclidean distance between the two embedding vectors\n"
        "  M = Margin = 2.0 (minimum desired separation for different inks)\n"
        "  label = 1 (same ink) or 0 (different ink)\n"
        "\n"
        "Case 1: Same ink (label = 1)\n"
        "  L = 0.5 * D^2\n"
        "  -> Loss is high when D is large (embeddings far apart)\n"
        "  -> Gradient pushes embeddings CLOSER together\n"
        "\n"
        "Case 2: Different ink (label = 0)\n"
        "  L = 0.5 * max(0, 2.0 - D)^2\n"
        "  -> Loss is high when D < 2.0 (embeddings too close)\n"
        "  -> Gradient pushes embeddings FURTHER apart\n"
        "  -> When D >= 2.0, loss = 0 (already well separated, no gradient)",
        title="Contrastive Loss"
    )
    pdf.info_box(
        "Analogy: Think of embeddings as people in a room. For 'same ink' pairs, "
        "a rubber band connects them, pulling them together. For 'different ink' pairs, "
        "a spring pushes them apart, but only until they're 2 metres away (the margin)."
    )

    pdf.section_title("8.2  Euclidean Distance")
    pdf.code_block(
        "Given two embedding vectors:\n"
        "  emb1 = [0.3, 0.7, -0.1, ...]   (64 numbers)\n"
        "  emb2 = [0.1, 0.6, -0.2, ...]   (64 numbers)\n"
        "\n"
        "Euclidean distance = sqrt( (0.3-0.1)^2 + (0.7-0.6)^2 + (-0.1+0.2)^2 + ... )\n"
        "                   = sqrt( 0.04 + 0.01 + 0.01 + ... )\n"
        "\n"
        "In PyTorch: F.pairwise_distance(emb1, emb2)",
        title="Euclidean Distance"
    )

    pdf.section_title("8.3  Similarity Score Conversion")
    pdf.code_block(
        "similarity = exp(-distance / margin)\n"
        "\n"
        "distance = 0.0  -> similarity = exp(0)    = 1.000  (identical patches)\n"
        "distance = 1.0  -> similarity = exp(-0.5) = 0.607\n"
        "distance = 2.0  -> similarity = exp(-1.0) = 0.368  (at the margin)\n"
        "distance = 4.0  -> similarity = exp(-2.0) = 0.135  (very different)\n"
        "distance = inf  -> similarity = 0.000  (completely different)\n"
        "\n"
        "Threshold at similarity = 0.5 corresponds to distance = 1.386 (= -ln(0.5) * margin)"
    )

    pdf.section_title("8.4  Grad-CAM Mathematics")
    pdf.code_block(
        "Let A^k = activation maps at last conv layer (k channels, H' x W')\n"
        "Let y^c = score for class c (or embedding norm for Siamese)\n"
        "\n"
        "Step 1: Compute gradient of y^c w.r.t. each activation map\n"
        "        grad_A^k = d(y^c) / d(A^k)    shape: (k, H', W')\n"
        "\n"
        "Step 2: Global average pooling of gradients\n"
        "        alpha^k = (1/Z) * sum(grad_A^k)    shape: (k,)\n"
        "        (Z = H' * W' = number of spatial locations)\n"
        "\n"
        "Step 3: Weighted combination of activation maps\n"
        "        L_Grad-CAM = ReLU( sum_k( alpha^k * A^k ) )    shape: (H', W')\n"
        "\n"
        "Step 4: Upsample to input size (64x64) using bilinear interpolation\n"
        "Step 5: Normalise to [0, 1]"
    )

    pdf.section_title("8.5  Adaptive Thresholding")
    pdf.code_block(
        "For each pixel (x, y):\n"
        "  threshold(x,y) = mean_of_11x11_neighborhood(x,y) - C\n"
        "  (where C = 5 in this project)\n"
        "\n"
        "  pixel is INK if: intensity < threshold(x,y)\n"
        "  (ink is darker than local average)\n"
        "\n"
        "This adapts to uneven illumination across the cheque,\n"
        "unlike global thresholding which uses a single fixed value."
    )

    pdf.section_title("8.6  LAB Color Divergence Computation")
    pdf.code_block(
        "For each region (left / right):\n"
        "  1. Convert patches to LAB\n"
        "  2. Select ink pixels: L < 150 AND |A-128| > 5 OR |B-128| > 5\n"
        "     (dark pixels with some chromaticity — excludes grey printed text)\n"
        "  3. Compute mean_A and mean_B across all ink pixels\n"
        "\n"
        "AB distance = sqrt( (left_A - right_A)^2 + (left_B - right_B)^2 )\n"
        "\n"
        "Also compute chromaticity standard deviation across all patches:\n"
        "  chroma_std = sqrt( std(all_A)^2 + std(all_B)^2 )\n"
        "\n"
        "Final divergence = 0.6 * AB_distance + 0.4 * chroma_std\n"
        "\n"
        "Threshold: divergence > 7.0 -> FRAUD signal\n"
        "(Genuine cheques typically show divergence < 7)"
    )


def write_section_9(pdf):
    pdf.add_page()
    pdf.chapter_title("9. Code Logic & Design Decisions")

    pdf.section_title("9.1  Why patch-based instead of whole-image analysis?")
    pdf.body(
        "Processing entire cheque images at once would lose local spatial information. "
        "Ink differences are LOCAL — a fraudster only changes one field, not the whole cheque. "
        "Patches allow the model to compare specific regions. A 64x64 patch contains about "
        "2-3 words of handwriting — enough context to capture ink texture and colour."
    )

    pdf.section_title("9.2  Why 50% sliding window overlap (stride=32)?")
    pdf.body(
        "A stride equal to patch_size/2 ensures that every ink region is covered by at least "
        "two overlapping patches. This prevents important regions from being missed at patch "
        "boundaries and provides more data for the similarity map."
    )

    pdf.section_title("9.3  Why separate left/right regions?")
    pdf.body(
        "The IDRBT dataset has each cheque written with two pens. The left half of each cheque "
        "is written with pen A, the right half with pen B. Comparing within a region (same pen) "
        "should give high similarity. Comparing across regions (different pen) should give low "
        "similarity for genuine cheques that happen to have two pens AND for fraud cheques.\n\n"
        "Wait — why high similarity for genuine cheques then? Because genuine cheques in this "
        "context means the cheque's TOTAL content was written by the same person at the same "
        "time. The fraud signal comes from comparing the ORIGINAL ink regions to the TAMPERED "
        "ink regions — which map to different halves."
    )

    pdf.section_title("9.4  Why EarlyStopping instead of fixed epochs?")
    pdf.body(
        "Training for a fixed number of epochs (e.g., 30) wastes time if the model converges "
        "after 8 epochs and then starts overfitting. EarlyStopping monitors validation loss "
        "and stops training when it hasn't improved by at least min_delta=0.001 for 5 "
        "consecutive epochs. The best weights are saved and reloaded after stopping."
    )

    pdf.section_title("9.5  Why ReduceLROnPlateau scheduler?")
    pdf.body(
        "The learning rate controls how big each gradient step is. Too large = overshoots, "
        "too small = slow. ReduceLROnPlateau starts with lr=0.001 and halves it whenever "
        "validation loss doesn't improve for 3 epochs. This adaptive approach often finds "
        "a good final solution faster than a fixed schedule."
    )

    pdf.section_title("9.6  Why BatchNorm after every Conv layer?")
    pdf.body(
        "Batch Normalisation normalises the activations within each mini-batch, reducing "
        "'internal covariate shift'. This stabilises training, allows higher learning rates, "
        "and acts as a mild regulariser. Without BN, the Siamese network would be much "
        "harder to train with a contrastive loss."
    )

    pdf.section_title("9.7  Why AdaptiveAvgPool instead of fixed-size FC layer?")
    pdf.body(
        "The final pooling uses AdaptiveAvgPool2d(1) which outputs a 1x1 spatial map regardless "
        "of input size. This means the model can theoretically handle different patch sizes "
        "without changing the architecture. It also averages out spatial information, which "
        "is intentional — the embedding should capture ink TYPE, not WHERE on the patch the ink is."
    )

    pdf.section_title("9.8  Why the hybrid 4-signal fraud detection?")
    pdf.body(
        "A single threshold on average similarity fails when:\n"
        "- The model is not well-trained (random weights)\n"
        "- The similarity scores are all high (model sees everything as similar)\n"
        "- The scores are all low (model sees everything as different)\n\n"
        "The 4-signal hybrid is robust:\n"
        "- If the model is trained, Signal 1 (absolute threshold) works\n"
        "- If scores are noisy, Signal 2 (spread) detects distribution inconsistency\n"
        "- Signal 3 (adaptive outliers) catches relative anomalies\n"
        "- Signal 4 (LAB color) works directly from pixel data, independent of model\n\n"
        "Any signal alone reaching its threshold contributes to the fraud score. "
        "This OR-based logic maximises sensitivity (recall) while the threshold=0.55 "
        "maintains reasonable precision."
    )


def write_section_10(pdf):
    pdf.add_page()
    pdf.chapter_title("10. Deployment & Execution Guide")

    pdf.section_title("10.1  Requirements")
    pdf.table(
        headers=["Package", "Version", "Purpose"],
        rows=[
            ["torch + torchvision", ">= 2.0.0", "Deep learning (Siamese, CNN)"],
            ["opencv-python",       ">= 4.8.0", "Image reading, processing, drawing"],
            ["Pillow",              ">= 10.0.0","PIL image operations (cheque generation)"],
            ["scikit-image",        ">= 0.21.0","GLCM + LBP feature extraction"],
            ["numpy",               ">= 1.24.0","All numerical operations"],
            ["pandas",              ">= 2.0.0", "Metadata Excel reading"],
            ["scikit-learn",        ">= 1.3.0", "SVM, Random Forest, metrics"],
            ["matplotlib + seaborn",">= 3.7.0", "All plots and figures"],
            ["streamlit",           ">= 1.28.0","Web application"],
            ["fpdf2",               ">= 2.7.0", "PDF report generation"],
            ["tqdm",                ">= 4.65.0","Progress bars"],
            ["openpyxl",            ">= 3.1.0", "Reading .xlsx metadata files"],
        ],
        col_widths=[50, 30, 90]
    )

    pdf.section_title("10.2  Installation & Setup")
    pdf.code_block(
        "# 1. Open terminal / PowerShell\n"
        "# 2. Navigate to project directory\n"
        "cd d:\\Shanky\n"
        "\n"
        "# 3. Create virtual environment (recommended)\n"
        "python -m venv venv\n"
        "venv\\Scripts\\activate          # Windows\n"
        "# source venv/bin/activate       # Linux/Mac\n"
        "\n"
        "# 4. Install all dependencies\n"
        "pip install -r requirements.txt\n"
        "\n"
        "# 5. (Optional) Download real dataset from Kaggle:\n"
        "# https://www.kaggle.com/datasets/jdranpariya/cheque-data/data\n"
        "# Extract contents into data/raw/"
    )

    pdf.section_title("10.3  Training")
    pdf.code_block(
        "# Train ALL three models at once (~2-5 min on CPU)\n"
        "python src/train.py\n"
        "\n"
        "# This generates:\n"
        "#   outputs/models/siamese_best.pth\n"
        "#   outputs/models/cnn_best.pth\n"
        "#   outputs/models/classical_svm.pkl\n"
        "#   outputs/models/classical_rf.pkl\n"
        "#   outputs/figures/siamese_training.png\n"
        "#   outputs/figures/cnn_training.png"
    )

    pdf.section_title("10.4  Evaluation")
    pdf.code_block(
        "# Evaluate all models and generate comparison charts\n"
        "python src/evaluate.py\n"
        "\n"
        "# Generates:\n"
        "#   outputs/figures/siamese_confusion.png\n"
        "#   outputs/figures/cnn_confusion.png\n"
        "#   outputs/figures/classical_rf_confusion.png\n"
        "#   outputs/figures/classical_svm_confusion.png\n"
        "#   outputs/figures/roc_curves.png\n"
        "#   outputs/figures/model_comparison.png\n"
        "#   outputs/figures/siamese_distance_dist.png"
    )

    pdf.section_title("10.5  Running the Web App")
    pdf.code_block(
        "# Start Streamlit web application\n"
        "streamlit run app.py\n"
        "\n"
        "# Opens browser at http://localhost:8501\n"
        "# Choose model from sidebar\n"
        "# Upload a cheque OR select from 20 sample images\n"
        "# Click 'Detect Fraud'"
    )

    pdf.section_title("10.6  Running Tests")
    pdf.code_block(
        "# Run full pytest test suite\n"
        "python -m pytest tests/test_pipeline.py -v\n"
        "\n"
        "# Quick accuracy test on 20 sample cheques\n"
        "python test_detection.py\n"
        "\n"
        "# Full model comparison report\n"
        "python model_comparison.py"
    )

    pdf.section_title("10.7  Generating Sample Cheques")
    pdf.code_block(
        "# Generate 20 realistic sample cheques (5 genuine + 15 fraud)\n"
        "python generate_sample_cheques.py\n"
        "\n"
        "# Rebuild with maximum ink contrast\n"
        "python rebuild_samples.py\n"
        "\n"
        "# Regenerate specific failing samples\n"
        "python regen_failing_cheques.py"
    )

    pdf.section_title("10.8  GPU vs CPU")
    pdf.body(
        "The system auto-detects GPU via torch.cuda.is_available() in config.py. "
        "With GPU (NVIDIA CUDA): training is 5-10x faster. With CPU only: training takes "
        "2-5 minutes for all models on the synthetic dataset. No configuration needed — "
        "DEVICE is set automatically."
    )


def write_section_11(pdf):
    pdf.add_page()
    pdf.chapter_title("11. Testing — What's Verified")

    pdf.section_title("11.1  Test Structure (tests/test_pipeline.py)")
    pdf.body("The test suite uses pytest and covers 8 test classes:")

    tests = [
        ("TestConfig",           "Verifies all directories exist, hyperparameters are valid "
                                 "(positive values, LR between 0 and 1, etc.)"),
        ("TestPreprocessing",    "Tests resize_and_normalize (shape, dtype, range), "
                                 "to_grayscale, to_lab, apply_augmentation, preprocess_cheque, "
                                 "and extract_ink_mask outputs"),
        ("TestSyntheticData",    "Generates 3 synthetic cheques and verifies files are created "
                                 "with correct pen assignments. Tests load_dataset() works."),
        ("TestPatchGeneration",  "Tests sliding window extraction (correct patch shape), "
                                 "contour extraction, and generate_pairs() output format"),
        ("TestModels",           "Forward pass shapes for Siamese and CNN, similarity range [0,1], "
                                 "contrastive loss non-negativity, parameter count < 500K"),
        ("TestGradCAM",          "Heatmap shape (64x64), range [0,1], overlay output (uint8)"),
        ("TestFraudPipeline",    "Full detect() call on random image, verifies result dict "
                                 "has verdict in ['FRAUD','GENUINE'], confidence in [0,1]"),
        ("TestPyTorchDatasets",  "PatchPairDataset and SinglePatchDataset tensor shapes, "
                                 "correct C,H,W ordering"),
    ]
    pdf.table(
        headers=["Test Class", "What It Tests"],
        rows=tests,
        col_widths=[45, 125]
    )

    pdf.section_title("11.2  Running Tests")
    pdf.code_block(
        "python -m pytest tests/test_pipeline.py -v\n"
        "\n"
        "# Expected output:\n"
        "# tests/test_pipeline.py::TestConfig::test_directories_exist  PASSED\n"
        "# tests/test_pipeline.py::TestConfig::test_hyperparameters    PASSED\n"
        "# tests/test_pipeline.py::TestPreprocessing::test_resize ...  PASSED\n"
        "# ... (all tests should PASS)"
    )


def write_section_12(pdf):
    pdf.add_page()
    pdf.chapter_title("12. Limitations & Future Improvements")

    pdf.section_title("12.1  Current Limitations")
    pdf.table(
        headers=["Limitation", "Impact", "Notes"],
        rows=[
            ["Small dataset (112 images)",
             "Models may not generalise to unseen pen types",
             "Synthetic fallback mitigates this"],
            ["Left/right region assumption",
             "Fails if tampering is not region-constrained",
             "Future: spatial clustering"],
            ["No pixel-level segmentation",
             "Cannot precisely outline tampered text",
             "Future: U-Net approach"],
            ["Visible light only",
             "Near-identical inks hard to differentiate",
             "Future: multi-spectral imaging"],
            ["Binary verdict only",
             "No indication of WHICH field was tampered",
             "Future: field-level detection"],
            ["CPU training (slow with large data)",
             "Not suited for very large datasets",
             "Future: GPU training pipeline"],
            ["Fixed patch size (64x64)",
             "Misses very fine ink details",
             "Future: multi-scale patches"],
        ],
        col_widths=[50, 65, 55]
    )

    pdf.section_title("12.2  Possible Improvements")
    pdf.bullet([
        "U-Net Segmentation: Add pixel-level ink boundary detection with semantic segmentation",
        "Vision Transformers (ViT): Self-attention captures global ink context across entire cheque",
        "Transfer Learning: Fine-tune ResNet/EfficientNet pre-trained on ImageNet for better features",
        "Multi-spectral Imaging: Near-IR and UV channels reveal ink differences invisible in visible light",
        "Online Learning: Continuous model update as new fraud patterns emerge",
        "Field-Level Detection: Identify WHICH field (date, amount, payee) was tampered",
        "Multi-class Ink Identification: Determine specific ink manufacturer from image",
        "Confidence Calibration: Use temperature scaling to make confidence scores more reliable",
        "Explainability Dashboard: Interactive exploration of model decisions",
        "Mobile Deployment: Export to ONNX format for deployment on mobile bank apps",
    ])

    pdf.section_title("12.3  Research Directions")
    pdf.bullet([
        "Apply to other documents: cheques are one use case; same approach works on wills, contracts",
        "Writer verification: Combine ink analysis with handwriting analysis for stronger fraud detection",
        "Adversarial robustness: Test against adversarial attacks (deliberately crafted images)",
        "Cross-scanner generalisation: Models trained on one scanner type may fail on another",
        "Few-shot learning: Using only 1-5 reference patches of known ink to authenticate",
    ])


def write_section_13(pdf):
    pdf.add_page()
    pdf.chapter_title("13. Glossary & Quick Reference")

    terms = [
        ("Adaptive Thresholding", "A binarisation method that computes local thresholds from pixel neighbourhoods, handling uneven lighting."),
        ("Augmentation",         "Artificial modifications (rotation, noise, brightness) applied to training data to prevent overfitting."),
        ("AUC",                  "Area Under (ROC) Curve. Score 0.5=random, 1.0=perfect. Measures classification quality."),
        ("BatchNorm",            "Batch Normalisation — normalises layer activations to stabilise and speed up training."),
        ("BGR",                  "Blue-Green-Red colour channel order used by OpenCV (opposite of RGB)."),
        ("Contrastive Loss",     "Training objective for Siamese networks that pulls same-class pairs together and pushes different-class pairs apart."),
        ("Confusion Matrix",     "2x2 table of TP, FP, TN, FN predictions for binary classification evaluation."),
        ("CNN",                  "Convolutional Neural Network — uses convolution operations to extract spatial features from images."),
        ("DEVICE",               "Compute device (GPU/CPU). PyTorch auto-detects via torch.cuda.is_available()."),
        ("Dropout",              "Regularisation: randomly zeros some activations during training to prevent co-adaptation."),
        ("Early Stopping",       "Stops training when validation loss stops improving, saving the best weights."),
        ("Embedding",            "A compact vector representation learned by the network to encode important features."),
        ("Euclidean Distance",   "sqrt(sum of squared differences) between two vectors. Measures how far apart two embeddings are."),
        ("F1-Score",             "Harmonic mean of Precision and Recall. Balanced measure for imbalanced datasets."),
        ("GLCM",                 "Gray-Level Co-occurrence Matrix — encodes spatial relationships between pixel brightness values for texture analysis."),
        ("Grad-CAM",             "Gradient-weighted Class Activation Mapping — shows which image regions influenced a CNN's prediction."),
        ("Hyperparameter",       "Model settings set before training (learning rate, batch size, etc.) — not learned from data."),
        ("IDRBT",                "Institute for Development and Research in Banking Technology — provided the cheque dataset."),
        ("Ink Mask",             "Binary image where True=ink pixel, False=paper background. Created by adaptive thresholding."),
        ("LAB Color Space",      "Perceptually uniform colour space with L(luminance), A(green-red), B(blue-yellow) channels."),
        ("LBP",                  "Local Binary Pattern — encodes local texture by comparing pixel to its neighbours."),
        ("Margin",               "In contrastive loss, the minimum desired distance between different-class embeddings (=2.0)."),
        ("MaxPool",              "Max Pooling — reduces spatial dimensions by taking maximum value in each window."),
        ("Metric Learning",      "Training a model to learn a distance metric such that similar items are close in embedding space."),
        ("MICR",                 "Magnetic Ink Character Recognition — bottom-of-cheque machine-readable line."),
        ("Morphological Ops",    "Image processing operations (open=erosion+dilation, close=dilation+erosion) that clean binary masks."),
        ("Overfitting",          "Model memorises training data, performs poorly on new data. Prevented by augmentation, dropout, early stopping."),
        ("Patch",                "A small square crop (64x64 pixels) extracted from the cheque image for analysis."),
        ("Precision",            "Of all predicted FRAUD cases, what fraction were actually FRAUD. TP / (TP + FP)."),
        ("Random Forest",        "Ensemble of decision trees, each trained on random data/feature subsets; averages their votes."),
        ("Recall",               "Of all actual FRAUD cases, what fraction were correctly identified. TP / (TP + FN)."),
        ("ROC Curve",            "Plot of True Positive Rate vs False Positive Rate at varying decision thresholds."),
        ("Siamese Network",      "Neural network architecture with two identical branches (shared weights) for comparing pairs."),
        ("Similarity Score",     "exp(-distance/margin) — value in [0,1] where 1=identical, 0=completely different."),
        ("Sliding Window",       "Systematically moving a fixed-size patch across an image with a fixed step (stride)."),
        ("StandardScaler",       "Normalises features to zero mean and unit variance before classical ML classifiers."),
        ("Stride",               "Step size of the sliding window (32 pixels = 50% overlap between adjacent patches)."),
        ("SVM",                  "Support Vector Machine — finds optimal hyperplane separating classes, maximising margin."),
        ("Verdict",              "Final binary output of the detection pipeline: 'FRAUD' or 'GENUINE'."),
        ("Weight Decay",         "L2 regularisation on model weights to prevent overfitting (=0.0001 in this project)."),
    ]

    self = pdf
    self.set_font("Helvetica", "", 9)
    for term, definition in terms:
        self.set_font("Helvetica", "B", 9)
        self.set_text_color(15, 52, 96)
        self.set_x(20)
        self.cell(45, 6, term + ":", new_x="RIGHT", new_y="TOP")
        self.set_font("Helvetica", "", 9)
        self.set_text_color(30, 30, 30)
        self.multi_cell(0, 6, definition)
        self.ln(0.5)

    pdf.ln(6)
    pdf.set_font("Helvetica", "B", 11)
    pdf.set_text_color(233, 69, 96)
    pdf.cell(0, 8, "Quick Command Reference", new_x="LMARGIN", new_y="NEXT")
    pdf.set_text_color(0, 0, 0)
    pdf.code_block(
        "python src/train.py                   # Train all models\n"
        "python src/evaluate.py                # Evaluate & generate charts\n"
        "streamlit run app.py                  # Launch web application\n"
        "python -m pytest tests/ -v            # Run all unit tests\n"
        "python test_detection.py              # Quick 20-sample accuracy test\n"
        "python model_comparison.py            # Full comparison report\n"
        "python generate_sample_cheques.py     # Generate demo cheques\n"
        "python rebuild_samples.py             # Rebuild with high-contrast inks"
    )

    # References
    pdf.add_page()
    pdf.chapter_title("References")
    refs = [
        ("1", "P. Dansena, S. Bag, and R. Pal, \"Differentiating Pen Inks in Hand-written Bank Cheques "
              "Using Multi-Layer Perceptron\", Proc. 7th ICPRMI, Kolkata, India, December 2017."),
        ("2", "J. Bromley, I. Guyon, Y. LeCun, E. Säckinger, and R. Shah, \"Signature Verification Using "
              "a 'Siamese' Time Delay Neural Network\", Advances in NIPS, 1994."),
        ("3", "G. Koch, R. Zemel, and R. Salakhutdinov, \"Siamese Neural Networks for One-shot Image "
              "Recognition\", ICML Deep Learning Workshop, 2015."),
        ("4", "R.M. Haralick, K. Shanmugam, and I. Dinstein, \"Textural Features for Image Classification\", "
              "IEEE Trans. Systems, Man, and Cybernetics, 1973."),
        ("5", "T. Ojala, M. Pietikäinen, and D. Harwood, \"A Comparative Study of Texture Measures with "
              "Classification Based on Feature Distributions\", Pattern Recognition, 1996."),
        ("6", "R.R. Selvaraju et al., \"Grad-CAM: Visual Explanations from Deep Networks via Gradient-based "
              "Localization\", ICCV 2017."),
        ("7", "R. Ioffe and C. Szegedy, \"Batch Normalization: Accelerating Deep Network Training by "
              "Reducing Internal Covariate Shift\", ICML 2015."),
        ("8", "D.P. Kingma and J. Ba, \"Adam: A Method for Stochastic Optimization\", ICLR 2015."),
    ]
    pdf.set_font("Helvetica", "", 10)
    for num, ref in refs:
        pdf.set_x(20)
        pdf.set_font("Helvetica", "B", 10)
        pdf.set_text_color(233, 69, 96)
        pdf.cell(10, 7, f"[{num}]")
        pdf.set_font("Helvetica", "", 10)
        pdf.set_text_color(30, 30, 30)
        pdf.multi_cell(0, 7, ref)
        pdf.ln(1)


# ════════════════════════════════════════════════════════════════════════
# MAIN
# ════════════════════════════════════════════════════════════════════════

def main():
    print("=" * 60)
    print("  CHEQUE FRAUD DETECTION — PDF DOCUMENTATION GENERATOR")
    print("=" * 60)
    print(f"  Output: {OUTPUT_PATH}\n")

    pdf = DocPDF()
    pdf.set_title("Cheque Fraud Detection — Complete Project Documentation")
    pdf.set_author("AI Documentation Generator")

    print("  [1/15] Cover page...")
    pdf.cover_page()

    print("  [2/15] Table of Contents...")
    pdf.toc_page()

    print("  [3/15] Section 1: Project Overview...")
    write_section_1(pdf)

    print("  [4/15] Section 2: Project Structure...")
    write_section_2(pdf)

    print("  [5/15] Section 3: File-by-File Breakdown...")
    write_section_3(pdf)

    print("  [6/15] Section 4: Logic & Flow...")
    write_section_4(pdf)

    print("  [7/15] Section 5: Models & Algorithms...")
    write_section_5(pdf)

    print("  [8/15] Section 6: Feature Engineering...")
    write_section_6(pdf)

    print("  [9/15] Section 7: Visual Elements...")
    write_section_7(pdf)

    print("  [10/15] Section 8: Mathematics...")
    write_section_8(pdf)

    print("  [11/15] Section 9: Code Logic & Design...")
    write_section_9(pdf)

    print("  [12/15] Section 10: Deployment...")
    write_section_10(pdf)

    print("  [13/15] Section 11: Testing...")
    write_section_11(pdf)

    print("  [14/15] Section 12: Limitations & Improvements...")
    write_section_12(pdf)

    print("  [15/15] Section 13: Glossary & References...")
    write_section_13(pdf)

    print("\n  Saving PDF...")
    pdf.output(OUTPUT_PATH)

    size_kb = os.path.getsize(OUTPUT_PATH) // 1024
    print(f"\n  [OK] PDF saved: {OUTPUT_PATH}")
    print(f"  [OK] Size: {size_kb} KB")
    print(f"  [OK] Pages: {pdf.page}")
    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()
