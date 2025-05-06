from pypdf import PdfWriter
import os

# Set the directory where your one-page PDFs are stored
pdf_dir = ""
output_file = ".pdf"

# Create a PdfMerger object
merger = PdfWriter()

pdf_num_map = dict()
for f in os.listdir(pdf_dir):
    if f.lower().endswith(".pdf"):
        num = int(f.split("_")[1])
        pdf_num_map[num] = f"{pdf_dir}/{f}"

# Get a sorted list of all PDF files
pdf_files = sorted(
    [int(f.split("_")[1]) for f in os.listdir(pdf_dir) if f.lower().endswith(".pdf")]
)

print("pdf files == ", pdf_files)
print("pdf num map == ", pdf_num_map)

# Append each file to the merger
for num in pdf_files:
    merger.append(pdf_num_map[num])
#
# # Write out the combined PDF
merger.write(output_file)
merger.close()

print(f"Combined PDF saved as {output_file}")
