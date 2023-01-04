# Merge PDF Files from your chosen Directory using python script.
# Requirement Modules: PyPDF2, OS(just a built-in Function buddy, no need to install it :) 

import os
import PyPDF2

class PDFMerger:
    def __init__(self, path, save_path):
        self.path = path
        self.save_path = save_path
        self.pdf_files = []

    def get_pdf_files(self):
        # r=root, d=directories, f=files
        for r, d, f in os.walk(self.path):
            for file in f:
                if '.pdf' in file:
                    self.pdf_files.append(os.path.join(r, file))
    
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
pdf_merger.get_pdf_files()
pdf_merger.merge_pdfs()