import tkinter as tk
from tkinter import filedialog, messagebox
from core.scanner import scan_directory
from core.timeline_builder import build_timeline
from core.anomaly_detector import detect_anomalies
from database.db_handler import init_db, store_files, store_anomalies
from report_generator import generate_report


class ForensicsGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Digital Forensics Timeline Generator")
        self.root.geometry("600x400")

        self.path_label = tk.Label(root, text="No folder selected", fg="blue")
        self.path_label.pack(pady=10)

        self.select_btn = tk.Button(root, text="Select Folder", command=self.select_folder)
        self.select_btn.pack(pady=5)

        self.scan_btn = tk.Button(root, text="Run Forensic Scan", command=self.run_scan)
        self.scan_btn.pack(pady=5)

        self.status = tk.Text(root, height=12)
        self.status.pack(pady=10)

    def select_folder(self):
        self.folder = filedialog.askdirectory()
        self.path_label.config(text=self.folder)

    def run_scan(self):
        if not hasattr(self, 'folder') or not self.folder:
            messagebox.showerror("Error", "Please select a folder first")
            return

        self.status.insert(tk.END, "Initializing database...\n")
        init_db()

        self.status.insert(tk.END, "Scanning files...\n")
        files = scan_directory(self.folder)

        self.status.insert(tk.END, "Building timeline...\n")
        timeline = build_timeline(files)

        self.status.insert(tk.END, "Detecting anomalies...\n")
        anomalies = detect_anomalies(files)

        store_files(files)
        store_anomalies(anomalies)

        report_path = generate_report(files, timeline, anomalies)

        self.status.insert(tk.END, "\nSCAN COMPLETED SUCCESSFULLY\n")
        self.status.insert(tk.END, f"Files scanned: {len(files)}\n")
        self.status.insert(tk.END, f"Anomalies detected: {len(anomalies)}\n")
        self.status.insert(tk.END, f"Report saved at:\n{report_path}\n")

        messagebox.showinfo("Done", "Forensic Scan Completed Successfully!")


if __name__ == "__main__":
    root = tk.Tk()
    app = ForensicsGUI(root)
    root.mainloop()
