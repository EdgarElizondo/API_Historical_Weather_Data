import glob

files = glob.glob("backend\\src\\wheather_data\\TG_*")

for file in files:
    break

# Get File
with open(files[0], "r") as file:
    text = file.readlines()

# Get data starting line
num_line = 0
for line in text:
    if line[:5] == "STAID":
        break
    num_line +=1
# Delete white spaces
text[20] = text[20].replace(" ", "")

# Save Changes
with open(files[0], "w") as file:
    file.writelines(text)