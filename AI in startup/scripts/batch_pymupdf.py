import pymupdf4llm
from pathlib import Path

input_dir = Path(".")
output_dir = Path("output_pymupdf")
output_dir.mkdir(parents=True, exist_ok=True)

pdfs = list(input_dir.rglob("*.pdf"))
print(f"Verarbeite {len(pdfs)} PDFs...")

for i, pdf in enumerate(pdfs, 1):
    print(f"[{i}/{len(pdfs)}] {pdf.name}")
    try:
        md = pymupdf4llm.to_markdown(str(pdf))
        out = output_dir / pdf.with_suffix(".md").name
        out.write_bytes(md.encode())
        print(f"  OK")
    except Exception as e:
        print(f"  Fehler: {e}")

print("Fertig!")