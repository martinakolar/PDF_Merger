from pypdf import PdfMerger
import os

merger = PdfMerger()

def merging_pdfs(path, merged_pdfs_file_name):
    # going through pdfs in the path
    for file in os.listdir(path):
        if file.endswith(".pdf"): 
            pdf_full_path = os.path.join(path, file) 
            with open(pdf_full_path, 'rb') as pdf_file:
                merger.append(pdf_file)

    # "putting" the files together
    merged_pdfs_path = os.path.join(path, merged_pdfs_file_name)
    with open(merged_pdfs_path, 'wb') as merged_pdfs: 
        merger.write(merged_pdfs)

    merger.close()
    

# defining the folder path
while True:
    directory = input("Insert the directory your pdf's are stored in: ")
    if os.path.isdir(directory):
        break
    else:
        print("The directory you've entered doesn't exist. Make sure you are pasting the full path.")
    
# defining the merged PDF file name
merged_pdfs_fname = input("What would you like the merged PDF file to be called? ")   
print("Processing...")

merging_pdfs(directory, merged_pdfs_fname)


