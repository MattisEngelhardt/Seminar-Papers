import subprocess
from pathlib import Path

input_dir = Path(".")
output_dir = Path("output_marker")
output_dir.mkdir(parents=True, exist_ok=True)

pdfs = [p for p in input_dir.rglob("*.pdf") if "Döring" not in p.name and "Forschungsmethoden" not in p.name]
print(f"Verarbeite {len(pdfs)} PDFs mit marker...")

for i, pdf in enumerate(pdfs, 1):
    print(f"[{i}/{len(pdfs)}] {pdf.name}")
    try:
        subprocess.run([
           r".venv\Scripts\marker_single.exe", str(pdf),
            "--output_dir", str(output_dir),
            "--output_format", "markdown"
        ], check=True)
        print(f"  OK")
    except subprocess.CalledProcessError as e:
        print(f"  Fehler: {e}")

print("Fertig!")