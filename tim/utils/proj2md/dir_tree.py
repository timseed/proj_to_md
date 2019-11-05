import os


def getListOfFiles(dirName: str) -> str:
    """
    create a list of file and sub directories
    names in the given directory

    :param dirName:
    :return:
    """

    listoffiles = os.listdir(dirName)
    allfiles = list()
    # Iterate over all the entries
    for entry in listoffiles:
        # Create full path
        full_path = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory
        if os.path.isdir(full_path):
            allfiles = allfiles + getListOfFiles(full_path)
        else:
            allfiles.append(full_path)

    return allfiles


def dir_tree(startpath: str, wanted_files: list = ["py", "sh"]) -> (str, list):
    rv = ""
    flz = getListOfFiles(startpath)
    wanted_flz = []
    tree_str = []
    start_level = startpath.count(os.sep)
    for f in flz:
        suffix = os.path.splitext(f)[1]
        if suffix[1:] in wanted_files:
            level = f.count(os.sep) - start_level
            index = " " * 2 * level
            tree_str.append(f"{index}{f[len(startpath):]}\n")
            wanted_flz.append(f)
    tree_str.sort(reverse=True)
    tv = "".join(n for n in tree_str)
    return tv, wanted_flz
