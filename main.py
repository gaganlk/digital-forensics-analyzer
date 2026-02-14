import argparse
from core.scanner import scan_directory
from core.anomaly_detector import detect_anomalies
from database.db_handler import init_db, create_case, store_files, store_anomalies
from report_generator import generate_pdf_report


def run_scan(case, investigator, path):
    print("\n=== DIGITAL FORENSICS TIMELINE GENERATOR ===\n")

    init_db()
    case_id = create_case(case, investigator)

    print(f"\n[+] Case Created | ID: {case_id}")
    print("\n[+] Scanning files...")

    files = scan_directory(path)
    anomalies = detect_anomalies(files)

    store_files(case_id, files)
    store_anomalies(case_id, anomalies)

    pdf = generate_pdf_report(case_id, case, investigator, files, anomalies)

    print("\n✅ Scan Completed Successfully")
    print(f"Files scanned   : {len(files)}")
    print(f"Anomalies found : {len(anomalies)}")
    print(f"Report saved at : {pdf}")


def interactive_mode():
    case = input("Enter Case Name: ")
    investigator = input("Investigator Name: ")
    path = input("Enter directory to scan: ")

    run_scan(case, investigator, path)


def main():
    parser = argparse.ArgumentParser(description="Digital Forensics Timeline Generator")

    parser.add_argument("--case", help="Case name")
    parser.add_argument("--investigator", help="Investigator name")
    parser.add_argument("--path", help="Directory path to scan")

    args = parser.parse_args()

    # If CLI args provided → run CLI mode
    if args.case and args.investigator and args.path:
        run_scan(args.case, args.investigator, args.path)
    else:
        # Otherwise fallback to interactive
        interactive_mode()


if __name__ == "__main__":
    main()