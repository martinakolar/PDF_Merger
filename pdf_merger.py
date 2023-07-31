from PyPDF2 import PdfMerger
import os

directory = input("Insert the directory your pdf's are stored in: ")
print("Processing...")

merger = PdfMerger()

# Going through pdfs in the path
for file in os.listdir(directory):
    if file.endswith(".pdf"): 
        pdf_full_path = os.path.join(directory, file) 
        with open(pdf_full_path, 'rb') as pdf_file:
            merger.append(pdf_file)


merged_pdfs_path = os.path.join(directory, "merged_pdfs.pdf")
with open(merged_pdfs_path, 'wb') as merged_pdfs: 
    merger.write(merged_pdfs)

merger.close()
