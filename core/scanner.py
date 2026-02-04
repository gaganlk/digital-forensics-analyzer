import os
import time
from datetime import datetime
from core.hash_checker import calculate_hash

SKIP_DIRS = [
    "windows", "program files", "program files (x86)",
    "programdata", "$recycle.bin", "system volume information"
]

SUSPICIOUS_EXT = [".exe", ".bat", ".ps1", ".vbs"]

def count_files(path):
    total = 0
    for root, _, files in os.walk(path):
        if any(skip in root.lower() for skip in SKIP_DIRS):
            continue
        total += len(files)
    return total


def scan_directory(path):
    file_data = []

    total = count_files(path)
    print(f"\n[+] Total files found: {total}")

    scanned = 0
    start = time.time()

    for root, _, files in os.walk(path):
        if any(skip in root.lower() for skip in SKIP_DIRS):
            continue

        for name in files:
            try:
                full_path = os.path.join(root, name)
                stats = os.stat(full_path)

                file_info = {
                    "file_name": name,
                    "file_path": full_path,
                    "size": stats.st_size,
                    "created": datetime.fromtimestamp(stats.st_ctime),
                    "modified": datetime.fromtimestamp(stats.st_mtime),
                    "accessed": datetime.fromtimestamp(stats.st_atime)
                }

                if full_path.lower().endswith(tuple(SUSPICIOUS_EXT)):
                    file_info["hash"] = calculate_hash(full_path)
                else:
                    file_info["hash"] = "Skipped"

                file_data.append(file_info)

                scanned += 1
                percent = (scanned / total) * 100
                elapsed = int(time.time() - start)

                print(
                    f"\rScanning: {scanned}/{total} ({percent:.2f}%) | Time: {elapsed}s",
                    end=""
                )
            except:
                continue

    print("\n[✓] Scan Completed")
    return file_data
