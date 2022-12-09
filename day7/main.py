# Filesystem
# Tree of files and directories with sub directories
# Root /
# $ = command
# ls => dir a (means there is a directory a in that dir) 123 abc (means a file in that dir)
# => find the total size of each dir
#       Sum of all files and sub dir with files
# Task: Find all dirs with total size <= 100000 and calculate sum of all those

import re

SIZE_TH = 100000
TOTAL_DISK_SPACE = 70000000
UPDATE_SIZE = 30000000

cd_command = re.compile("\$ cd (.+)")
cd_back = ".."
ls_command = "$ ls"
dir_format = re.compile("dir (.+)")
file_format = re.compile("(\d+) (.+)")

def parse_directory(i, content):
    try:
        directory_content = {
            "size": 0,
            "directories": {},
            "files": {}
        }
        while i < len(content):
            is_file = file_format.search(content[i])
            if is_file:
                size = int(is_file.group(1))
                directory_content["files"][is_file.group(2)] = size
                directory_content["size"] += size

            is_cd = cd_command.search(content[i])
            if is_cd:
                directory = is_cd.group(1)
                if directory == cd_back:
                    break
                else:
                    i, sub_dir = parse_directory(i + 1, content)
                    directory_content["directories"][directory] = sub_dir
                    directory_content["size"] += sub_dir["size"]

            i+=1

        return i, directory_content
    except Exception as e:
        raise e

def task1(structure, size_th, total_size_above_th):
    if "directories" in structure:
        for directory in structure["directories"]:
            total_size_above_th = task1(structure["directories"][directory], size_th, total_size_above_th)
    
    if structure["size"] <= size_th:
        total_size_above_th += structure["size"]

    return total_size_above_th

def task2(structure, size_th, smallest_above_th):
    if "directories" in structure:
        for directory in structure["directories"]:
            smallest_above_th = task2(structure["directories"][directory], size_th, smallest_above_th)

    if structure["size"] <= smallest_above_th and structure["size"] >= size_th:
        smallest_above_th = structure["size"]

    return smallest_above_th

def run(day_input):
    inp = day_input.strip().split("\n")

    ind, directory_structure = parse_directory(0, inp)

    total_size = directory_structure["size"]
    task2_required_additional = UPDATE_SIZE - (TOTAL_DISK_SPACE - total_size)

    task1_res = task1(directory_structure, SIZE_TH, 0)
    task2_res = task2(directory_structure, task2_required_additional, total_size)

    return task1_res, task2_res

if __name__ == '__main__':
    #--- Tests
    test_input = "$ cd /\n$ ls\ndir a\n14848514 b.txt\n8504156 c.dat\ndir d\n$ cd a\n$ ls\ndir e\n29116 f\n2557 g\n62596 h.lst\n$ cd e\n$ ls\n584 i\n$ cd ..\n$ cd ..\n$ cd d\n$ ls\n4060174 j\n8033020 d.log\n5626152 d.ext\n7214296 k"
    test_expected_task_1 = 95437
    test_expected_task_2 = 24933642

    test_total_size_below_th, test_smallest_above_th = run(test_input)

    assert test_total_size_below_th == test_expected_task_1, f"Expected task 1 to return size {test_expected_task_1}, got {test_total_size_below_th}"
    assert test_smallest_above_th == test_expected_task_2, f"Expected task 2 to return size {test_expected_task_2}, got {test_smallest_above_th}"

    #--- Tasks
    with open("data/inputd7.txt") as f:
        content = f.read()

    task1_res, task2_res = run(content)

    print(f"Task 1: Total size of dirs below size th is {task1_res}")
    print(f"Task 2: Size of dir the meets the criteria {task2_res}")