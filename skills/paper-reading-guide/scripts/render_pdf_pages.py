#!/usr/bin/env python3
"""Render all pages of a PDF to PNG images using pypdfium2.

Usage:
    python render_pdf_pages.py <pdf_path> <output_dir> [--scale 2]

Output:
    Creates page_1.png, page_2.png, ... in output_dir.
    Prints JSON summary: {"total_pages": N, "output_dir": "...", "files": [...]}
"""
import argparse, json, pathlib, sys

def main():
    parser = argparse.ArgumentParser(description="Render PDF pages to PNG images")
    parser.add_argument("pdf_path", help="Path to the PDF file")
    parser.add_argument("output_dir", help="Directory to save PNG images")
    parser.add_argument("--scale", type=int, default=2, help="Render scale factor (default: 2)")
    args = parser.parse_args()

    pdf_path = pathlib.Path(args.pdf_path)
    output_dir = pathlib.Path(args.output_dir)

    if not pdf_path.exists():
        print(f"Error: PDF file not found: {pdf_path}", file=sys.stderr)
        sys.exit(1)

    output_dir.mkdir(parents=True, exist_ok=True)

    try:
        import pypdfium2 as pdfium
    except ImportError:
        print("Installing pypdfium2...", file=sys.stderr)
        import subprocess
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pypdfium2", "-q"])
        import pypdfium2 as pdfium

    pdf = pdfium.PdfDocument(str(pdf_path))
    total = len(pdf)
    files = []

    for i in range(total):
        page = pdf[i]
        bitmap = page.render(scale=args.scale)
        img = bitmap.to_pil()
        fname = f"page_{i+1}.png"
        img.save(output_dir / fname)
        files.append(fname)
        print(f"  Rendered page {i+1}/{total}", file=sys.stderr)

    pdf.close()

    result = {"total_pages": total, "output_dir": str(output_dir), "files": files}
    print(json.dumps(result))

if __name__ == "__main__":
    main()
