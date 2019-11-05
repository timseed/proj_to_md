from tim.utils.proj2md import dir_tree, get_arguments
from tim.utils.proj2md.fakedown import *

args = get_arguments()
proj = args.dir
t, files = dir_tree(proj)
print(level(1, "Project " + proj))
print(text("\n Layout of this project is ...\n"))
print(level(3, "Layout"))
print(code("text", t))
print(level(2, "Code Listing"))
for f in files:
    print(level(3, f))
    print(dump_file("python", f))
