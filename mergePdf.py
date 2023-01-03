# Merge PDF Files from your chosen Directory using python script.
# Requirement Modules: PyPDF2, OS(just a built-in Function buddy, no need to install it :) 

import os
import PyPDF2

def merge_pdfs(path, save_path):
    pdf_files = []
    # r=root, d=directories, f=files
    for r, d, f in os.walk(path):
        for file in f:
            if '.pdf' in file:
                pdf_files.append(os.path.join(r, file))
    # Show files that will be merging
    print("The following PDF files will be merged:")
    for pdf in pdf_files:
        file_name = os.path.basename(pdf)
        print(file_name)

    # Ask for confirmation before merging the files
    response = input("Do you want to merge these files (y/n)?: ")
    if response.lower() != 'y':
        return
    merger = PyPDF2.PdfFileMerger()

    for pdf in pdf_files:
        merger.append(pdf)

    # Specify the save path for the merged PDF file
    merger.write(os.path.join(save_path, 'merged_pdf.pdf'))
    merger.close()

# Your Chosen Folders:
path = "C:\\Users\\Jerwell\\Desktop\\MergePDF" # Source Folder
save_path = "C:\\Users\\Jerwell\\Desktop\\MergePDF" # Save Path
merge_pdfs(path, save_path)
