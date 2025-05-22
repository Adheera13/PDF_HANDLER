from PyPDF2 import PdfMerger, PdfReader, PdfWriter
import os

def merge_pdfs(pdf_list, output_path):
    merger = PdfMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    merger.write(output_path)
    merger.close()
    print(f"Merged PDFs into: {output_path}")

def split_pdf(file_path):
    reader = PdfReader(file_path)
    for i, page in enumerate(reader.pages):
        writer = PdfWriter()
        writer.add_page(page)
        output_path = f"output/split_page_{i+1}.pdf"
        os.makedirs("output", exist_ok=True)
        with open(output_path, "wb") as f:
            writer.write(f)
        print(f"Saved: {output_path}")
