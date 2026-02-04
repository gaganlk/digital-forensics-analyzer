def build_timeline(file_data):
    timeline = []

    for file in file_data:
        if "error" in file:
            continue

        timeline.append({
            "time": file["created"],
            "event": "File Created",
            "file": file["file_path"]
        })

        timeline.append({
            "time": file["modified"],
            "event": "File Modified",
            "file": file["file_path"]
        })

        timeline.append({
            "time": file["accessed"],
            "event": "File Accessed",
            "file": file["file_path"]
        })

    timeline.sort(key=lambda x: x["time"])
    return timeline
