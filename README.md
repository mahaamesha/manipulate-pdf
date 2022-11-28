# read-write-pages


### About
I have bulk certificate that has been generated from mail merge Word. There are multiple pdf files, I put them inside `./input` folder.

### Problem
Files generated from that has one addition page after the certifiate page, its only white page. I need to keep the first page (the certificate page) and delete others.

### Algorithm
1. Importing library needed.
2. Read files inside `./input` folder, then save it into a list. This will save the filenames.
3. Define the input and output path.
    By default, I assume that:
    ```py
    input_path = "./input/filename.pdf"
    output_path = "./output/filename.pdf"
    ```
4. Run the `manipulate()`:
    - Copy the original file
    - Adding page that I want to keep. In this case, I only need to keep the first page
    - Write the output
