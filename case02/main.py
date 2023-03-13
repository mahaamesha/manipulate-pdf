# remove the odd page (cause it all same)
# save the odd page as single file
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
    writer_output2 = PdfWriter()

    # Go through the pages one after the next
    for i in range(len(reader_input.pages)):
        if i % 2 == 0:      # i want to extract even page
            if i != 0:      # the first is sample, so i dont need it
                writer_output.addpage(reader_input.pages[i])
        elif i == len(reader_input.pages) - 1:  # save the odd page (similar pages) as single file
            writer_output2.addPage(reader_input.pages[i])

    # Write the modified content to disk
    writer_output.write(output)
    writer_output2.write(os.path.join(output_path, "back page.pdf"))
    print("Done")


if __name__ == "__main__":
    arr_namefiles = f.read_files_path(folder_path="./case02/input/")

    print("Running main.py:")
    for f in arr_namefiles:
        manipulate(filename=f, input_path="./case02/input/", output_path="./case02/output/")