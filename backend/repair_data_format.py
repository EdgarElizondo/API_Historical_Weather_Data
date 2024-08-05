import glob


def change_data_format(main_path):
    # Get File
    with open(file, "r", encoding="utf8") as f:
        text = f.readlines()

    # Get data starting line
    num_line = 0
    for line in text:
        if line[:5] == "STAID":
            break
        num_line +=1
    # Delete white spaces
    text[num_line] = text[num_line].replace(" ", "")
    # Save Changes
    with open(file, "w", encoding="utf8") as f:
        f.writelines(text)

if __name__ == "__main__":
    files = glob.glob("backend\\src\\wheather_data\\TG_*")
    for index,file in enumerate(files):
        if index % 50 == 0:
            print(f"Number of Files modified: {index}")
        change_data_format(file)