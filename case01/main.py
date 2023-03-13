# remove the first page of two pages PDF file
import os, sys
from pdfrw import PdfReader, PdfWriter

module_folder_path = os.path.abspath( os.getcwd() )
sys.path.append(module_folder_path)
import myfunc as f

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
    arr_namefiles = f.read_files_path(folder_path="./case01/input/")

    print("Running main.py:")
    for f in arr_namefiles:
        manipulate(filename=f, input_path="./case01/input/", output_path="./case01/output/")