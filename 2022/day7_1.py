#### all functions converting format of text into dictionary
#### dict is called dir_dict (or the directories dictionary)
#### every entry is of the format:
#### {directory_name:(a, b)}
#### where a is an array of directory names [dir1, dir2, ...]
#### these are the names of the directories INSIDE directory_name
#### and where b is the sizes of the files INSIDE directory_name (but not inside sub-directories)
def list_to_string(s):
    new = ""
    for x in s:
        if x != '':
            new = new + "|" + x
    return new


def check_path(dir_dict, path, line):
    keywords = line.split(' ')
    if keywords[0] == '$':
        if keywords[1] == "cd":
            if keywords[2] == "..":
                split = path.split("|")
                split = split[:-1]
                path = list_to_string(split)
            else:
                path = path + "|" + keywords[2]
    elif keywords[0] == "dir":
        add_dir(dir_dict, path, keywords[1])
    else:
        filesize = int(keywords[0])
        add_file(dir_dict, path, filesize)
    return dir_dict, path

def add_file(dir_dict, path, filesize):
    curr_value = dir_dict.get(path, "does not exist")
    if curr_value == "does not exist":
        dir_dict[path] = ([], filesize)
    else:
        newfilesize = dir_dict[path][1]
        newfilesize += filesize
        dir_dict[path] = (dir_dict[path][0], newfilesize)
        

def add_dir(dir_dict, path, dir_name):
    curr_value = dir_dict.get(path, "does not exist")
    if curr_value == "does not exist":
        dir_dict[path] = ([dir_name], 0)
    else:
        ### need to distinguish between adding a REPEAT directory (in a separate location)
        ### or if we're appending to the same directory
        ### this is why we're identifying with PATHS now! Earlier this caused a massive issue
        ### as some different directories were named the same so dicitonary was updated
        newdirs = dir_dict[path][0]
        newdirs.append(dir_name)
        dir_dict[path] = (newdirs, dir_dict[path][1])


##### functions for part A about navigating through the dictionary
def should_add(dir_dict, parent_dir, maxsize):
    filesize = dir_dict[parent_dir][1]
    
    if filesize > maxsize:
        return False
    else:
        subdirs = dir_dict[parent_dir][0]
        for d in subdirs:
            directoryname = parent_dir + "|" + d
            d_should_add = should_add(dir_dict,directoryname, maxsize)
            if d_should_add == False:
                return False
    return True

def totaldir_filesize(dir_dict, parent_dir, maxsize):
    filesize = dir_dict[parent_dir][1]
    ### base case, no directories inside parent_dir
    if dir_dict[parent_dir][0] == []:
        ### just return the filesize
        return filesize
    else:
        ### iterate through each subdirectory and get THEIR filesize
        subdirs = dir_dict[parent_dir][0]
        for d in subdirs:
            directoryname = parent_dir + "|" + d
            d_filesize = totaldir_filesize(dir_dict,directoryname, maxsize)
            if d_filesize != -1:
                filesize += d_filesize
    return filesize
            

with open('directories.txt') as file:
    path = ""
    ### dict will be of the form
    ### {dir: ([], total_filesize)}
    ### where dir is the most IMMEDIATE directory
    ### {dir: ([dir1, dir2], file_size)}
    ### where dir1 and dir2 are directories IN dir
    ### so you need to search dictionary for THEIR filezies to count for dir
    dir_dict = {}
    i = 0
    for line in file:
            line = line.strip()
            dir_dict, path = check_path(dir_dict, path, line)

    ### getting ALL names of directories
    all_dirs = list(dir_dict.keys())
    all_dirs = all_dirs[1:]
    maxsize = 100000
    total_sum = 0
    for d in all_dirs:
        d_add = should_add(dir_dict, d, maxsize)
        if d_add:
            d_filesize = totaldir_filesize(dir_dict, d, maxsize)
            total_sum += d_filesize
    
    print("### TOTAL SUM ###")
    print(total_sum)