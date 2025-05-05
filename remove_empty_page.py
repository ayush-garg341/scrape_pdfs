from pypdf import PdfReader, PdfWriter
from pathlib import Path


def remove_last_page_if_empty(input_path, output_path):
    reader = PdfReader(input_path)
    writer = PdfWriter()

    last_page = reader.pages[-1]
    text = last_page.extract_text()
    print("text === ", text)

    num_pages = len(reader.pages)
    # If the last page is empty (no text), remove it
    for i in range(num_pages - 1):
        writer.add_page(reader.pages[i])

    with open(output_path, "wb") as f:
        writer.write(f)


def process_all_pdfs_in_directory(directory_path):
    pdf_files = Path(directory_path).glob("*.pdf")
    for pdf_file in pdf_files:
        output_file = pdf_file.parent / f"{pdf_file.stem}_cleaned.pdf"
        remove_last_page_if_empty(pdf_file, output_file)
        print(f"Processed: {pdf_file.name} → {output_file.name}")


process_all_pdfs_in_directory("/Users/elliott/personal/scrape_pdfs/real_world_sd_copy")
