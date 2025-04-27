import os


def combine_files_data(f_name_list, f_to_write):
    '''
    This function takes a list of file names, reads each file, and writes the
    file name, number of lines, and the content of each file to a new file.
    '''
    f_dict = {}
    for f_name in f_name_list:
        f_name = f"{f_name}"
        with open(f_name, 'r', encoding='utf-8') as f:
            f = [line.strip() for line in f]
            l = len(f)
            f_dict[f_name] = {
                "length" : l,
                "strings" : f
            }
    f_dict = sorted(f_dict.items(), 
                    key=lambda item: item[1]['length'])

    with open(f_to_write, "w", encoding="utf-8") as f:
        for f_d, l_count in f_dict:
            name = f_d
            length = l_count['length']
            strings = "\n".join(l_count['strings'])
            f.write(f"{name}\n"
                    f"{length}\n"
                    f"{strings}\n")


if __name__ == "__main__":
    f_list = os.listdir(f"{os.getcwd()}")
    f_read = [f for f in f_list if ".txt" in f and f != "answer.txt"]
    f_write = "answer.txt"
    combine_files_data(f_read, f_write)