SUSPICIOUS_EXTENSIONS = [".exe", ".bat", ".ps1", ".vbs"]
TEMP_KEYWORDS = ["temp", "tmp", "appdata"]

def detect_anomalies(file_data):
    anomalies = []

    for f in file_data:
        reasons = []
        severity = "Low"
        path = f["file_path"].lower()

        if path.endswith(tuple(SUSPICIOUS_EXTENSIONS)) and any(k in path for k in TEMP_KEYWORDS):
            reasons.append("Executable located in temporary directory")
            severity = "High"

        if abs((f["modified"] - f["created"]).total_seconds()) < 3:
            reasons.append("Rapid file modification")

        if len(reasons) >= 2:
            anomalies.append({
                "file": f["file_path"],
                "type": "Suspicious Activity",
                "severity": severity,
                "reason": "; ".join(reasons)
            })

    return anomalies
