"""

1. Open winnie_pooh.txt
2. read in 100 lines at a time
3. after each 100 lines, write those lines to a new file
4. name each file differently (create a system to auto-increment the file names)
5. place all the files in a new folder (that you needed to create earlier)


"""
import os

def split_file(file_path, chunk_size=100):

 
    output_dir = "split_files"
    os.makedirs(output_dir, exist_ok=True)

    with open(file_path, 'r') as f:
        chunk_num = 1
        lines = []
        for line in f:
            lines.append(line)
            if len(lines) == chunk_size:
                output_file = os.path.join(output_dir, f"winnie_pooh_{chunk_num}.txt")
                with open(output_file, 'w') as out_f:
                    out_f.writelines(lines)
                lines = []
                chunk_num += 1

        if lines:
            output_file = os.path.join(output_dir, f"winnie_pooh_{chunk_num}.txt")
            with open(output_file, 'w') as out_f:
                out_f.writelines(lines)

file_path = "winnie_pooh.txt"
split_file(file_path)