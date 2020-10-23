

def lines_of_python(directory):
    # hold number of python files
    python_files = 0

    # hold the number of lines of code
    loc = 0

    # get the current working directory files and folders
    cur_dir_items = os.walk(directory)

    # unpack the tuple and return the files only
    for root, folder, files in cur_dir_items:
        for file in files:

            # check the file extension
            if file[-3:len(file)] == '.py':
                if file == 'None':
                    break
                print(file)
            #     python_files += 1
            #
            #     # open file
            #     f = open(file, mode='r', encoding='utf-8')
            #     lines = f.readlines()


    # return python_files


if __name__ == '__main__':
    import os
    current_directory = os.getcwd()
    # py_files = lines_of_python(current_directory)
    # print(py_files)
    print(lines_of_python(current_directory))