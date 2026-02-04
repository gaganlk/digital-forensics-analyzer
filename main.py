from core.scanner import scan_directory
from core.anomaly_detector import detect_anomalies
from database.db_handler import init_db, create_case, store_files, store_anomalies
from report_generator import generate_pdf_report

print("\n=== DIGITAL FORENSICS TIMELINE GENERATOR ===\n")

case = input("Enter Case Name: ")
investigator = input("Investigator Name: ")
path = input("Enter directory to scan: ")

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
