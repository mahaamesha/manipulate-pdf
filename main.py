# !/usr/bin/python
# Remove the first two pages (cover sheet) from the PDF
import os
from pdfrw import PdfReader, PdfWriter

# read files in the input/ folder
def read_files_path(folder_path="./input"):
    arr_namefiles = []
    print("Read files in %s:" %folder_path)
    for (root, dirs, file) in os.walk(folder_path):
        for f in file:
            if '.pdf' in f:
                arr_namefiles.append(f)
                print("\t%s" %f)
    print("\t...\n\t%s files detected." %len(arr_namefiles))
    return arr_namefiles

def manipulate(filename="file.pdf", input_path="./input", output_path="./output"):
    print("\tManipulate %s" %filename, end="... ")
    input = os.path.join(input_path, filename)
    output = os.path.join(output_path, filename)
    
    # Define the reader and writer objects
    reader_input = PdfReader(input)
    writer_output = PdfWriter()

    # Go through the pages one after the next
    for i in range(len(reader_input.pages)):
        if i < 1:    # i want to extract first page
            writer_output.addpage(reader_input.pages[i])

    # Write the modified content to disk
    writer_output.write(output)
    print("Done")


if __name__ == "__main__":
    arr_namefiles = read_files_path(folder_path="./input")

    print("Running main.py:")
    for f in arr_namefiles:
        manipulate(filename=f, input_path="./input", output_path="./output")