# Vevhu Land Allocation Data - Project Instructions

This repository contains the structured datasets and handwritten ledger images for the Vevhu Land Allocation project. The data is partitioned into distinct batches based on plot sizes, allocation dates, and demographic groupings.

---

## 📂 Repository Structure

The repository is organized into self-contained batch folders to maintain clean organization and maximum portability:

```
vevhu-data/
├── batch_[name]/
│   ├── batch_[name].csv      # Standardized CSV of the transcribed ledger data
│   ├── [image_1].jpg          # Original handwritten ledger page scan
│   ├── [image_2].jpg          # Original handwritten ledger page scan
│   └── ...
├── master_vevhu_database.csv  # Consolidated master database of all batches (1,280 rows)
├── DATA_QUALITY_AUDIT_REPORT.md# Automatically generated audit report flagging anomalies
├── consolidate_database.py    # Recursive script to compile all batches into the master CSV
├── generate_audit_report.py   # Script to analyze conflicts, duplicate IDs, and missing values
└── INSTRUCTIONS.md            # This documentation file
```

---

## 🛠️ Scripts & Database Management

To maintain and query the database, run the helper scripts located in the root of the repository:

### 1. Rebuild Consolidated Master Database
To scan all subfolders and recompile the master database file (`master_vevhu_database.csv`), execute:
```bash
python3 consolidate_database.py
```
*This script recursively searches for `batch_*.csv` files, processes row states (Active, Crossed Out, Blank), cleans names/stands, and produces a single unified CSV file.*

### 2. Regenerate Quality Audit Report
To check for duplicate stands, shared IDs, or missing columns across all batches, execute:
```bash
python3 generate_audit_report.py
```
*This will analyze the master database and generate a markdown report (`DATA_QUALITY_AUDIT_REPORT.md`) detailing the quality metrics and conflicts.*

---

## 📋 Transcription Rules & Field Standards

All transcriptions are conducted according to strict transcription laws:

1. **Literal Accuracy**: Maintain spelling errors, letter cases, and punctuation exactly as written.
2. **Blank Cells**: Leave empty cell values as blank in the CSV (do not insert placeholders or row indices).
3. **Crossed-out Fields**: If a cell/row is crossed out, transcribe the text anyway and prefix the `Comments` column with `[CROSSED OUT]`.
4. **Multiple Values**: Separate multiple cell/phone numbers in a single column using ` / ` (space-slash-space).
5. **Illegible Text**: Character-level illegibility is marked with an asterisk (`*`) and flagged in the `Comments` column.
