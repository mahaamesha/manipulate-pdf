# !/usr/bin/python
# Remove the first two pages (cover sheet) from the PDF
import os
from pdfrw import PdfReader, PdfWriter

# read files in the input/ folder
def read_files(folder_path="./input", func=None):
    arr_files = []
    print("Read files in %s:" %folder_path)
    for (root, dirs, file) in os.walk(folder_path):
        for f in file:
            if '.pdf' in f:
                arr_files.append(f)
                print("\t%s" %f)
    return arr_files

input_file = "./A.pdf"
output_file = "A-updated.pdf"

# Define the reader and writer objects
reader_input = PdfReader(input_file)
writer_output = PdfWriter()

# Go through the pages one after the next
for current_page in range(len(reader_input.pages)):
    if current_page > 1:
        writer_output.addpage(reader_input.pages[current_page])
        print("adding page %i" % (current_page + 1))

# Write the modified content to disk
writer_output.write(output_file)