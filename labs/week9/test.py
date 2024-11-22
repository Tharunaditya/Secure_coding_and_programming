from pathlib import Path
current_path = Path.cwd()
newdir = current_path / 'output'
# newdir.mkdir(parents=True,exist_ok = True)
new_file = newdir/'result2.txt'
# new_file.write_text("This is the results file for week 9")
for item in current_path.iterdir():
     print(item)

# datafile = current_path / 'result.txt'
# if datafile.exists():
#     content = datafile.read_text()
#     print("Contents of datafile ", content)
# else:
#     print("Result.txt does not exist.")
    
