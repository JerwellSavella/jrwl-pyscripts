# Merge PDF Files from your chosen Directory using python script.
# Requirement Modules: PyPDF2, OS(just a built-in Function buddy, no need to install it :) 

import os
import PyPDF2
import glob

class PDFMerger:
    def __init__(self, path, save_path):
        self.path = path
        self.save_path = save_path

    def merge_pdfs(self):
        # Find PDF files in the directory
        pdf_files = glob.glob(os.path.join(self.path, '*.pdf'))
    
    def merge_pdfs(self):                
        # Show files that will be merging
        print("The following PDF files will be merged:")
        for pdf in self.pdf_files:
            #Extract the filename from the path
            file_name = os.path.basename(pdf)
            print(file_name)

        # Ask for confirmation before merging the files
        response = input("Do you want to merge these files (y/n)?: ")
        if response.lower() != 'y':
            return
        merger = PyPDF2.PdfFileMerger()

        for pdf in self.pdf_files:
            merger.append(pdf)

        # Specify the save path for the merged PDF file
        merger.write(os.path.join(self.save_path, 'merged_pdf.pdf'))
        merger.close()

# Your Chosen Folders:
path = " " # Source Folder
save_path = " " # Save Path

pdf_merger = PDFMerger(path, save_path)
pdf_merger.merge_pdfs()