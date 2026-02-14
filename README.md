# Digital Forensics Timeline & Integrity Analyzer

A Python-based forensic analysis tool designed to generate structured file system activity timelines and detect unauthorized file modifications using cryptographic hashing.

---

## 🚀 Overview

This tool scans a target directory, extracts file metadata, generates a structured activity timeline, and verifies file integrity using SHA-based hashing. It also supports differential analysis by comparing current file states with a previously stored baseline snapshot.

---

## 🔍 Features

- Extracts file metadata (Creation Time, Modification Time, Access Time, File Size)
- Generates chronological activity timeline
- Computes SHA-based cryptographic hashes for file integrity verification
- Stores baseline directory snapshot
- Performs differential scanning to detect:
  - Newly created files
  - Modified files
  - Deleted files
- The tool supports structured forensic case management with persistent evidence storage using SQLite.

---

## 🏗️ Architecture

1. **Directory Scan Module**
   - Traverses target directory recursively
   - Collects file metadata using OS file system APIs

2. **Hashing Module**
   - Generates SHA hash for each file
   - Stores file path → hash mapping

3. **Baseline Snapshot Storage**
   - Saves initial scan results in structured format (JSON)

4. **Differential Comparison Engine**
   - Loads previous snapshot
   - Compares current hash map with baseline
   - Identifies added, removed, or modified files

5. **Report Generator**
   - Outputs timeline and comparison results

---

## ⚙️ How It Works (Differential Logic)

Step 1: Perform initial scan  
Step 2: Store file metadata + hash map as baseline snapshot  
Step 3: Re-scan directory at later time  
Step 4: Compare:
    - If file exists in new scan but not baseline → NEW
    - If file exists in both but hash differs → MODIFIED
    - If file exists in baseline but not new scan → DELETED

---

## 🛠️ Tech Stack

- Python 3.x
- SQLite (Case and evidence storage)
- Hashlib (SHA hashing)
- OS / File System APIs
- ReportLab / PDF generator

---

## 📦 Installation

Clone the repository:
    https://github.com/gaganlk/digital-forensics-analyzer.git


Install dependencies:
    pip install -r requirements.txt


---

## ▶️ Usage

Interactive mode:
    python main.py

CLI mode:
    python main.py --case <case_name> --investigator <name> --path <directory>

Initial baseline scan:
    python main.py --mode baseline --path <directory_path>

Run differential comparison:
    python main.py --mode compare --path <directory_path>   


---

## 🔐 Use Case

- Incident response
- Integrity verification
- Suspicious activity detection
- Academic forensic research

---

## 📌 Future Improvements

- Add logging module
- CLI argument validation
- GUI dashboard
- Database-based snapshot storage
- Integration with cloud storage

---

## 👨‍💻 Author

Gagan L K