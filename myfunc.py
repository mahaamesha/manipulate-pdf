import os

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