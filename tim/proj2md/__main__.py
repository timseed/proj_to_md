from tim.proj2md import dir_tree, get_arguments
from tim.proj2md.fakedown import *
import pprint
args = get_arguments()
proj = args.dir
t, files = dir_tree(proj, args.file_types)
print(level(1, "Project " + proj))
print(text("\n Layout of this project is ...\n"))
print(level(3, "Layout"))
print(code("text", t))
print(level(2, "Code Listing"))
for f in files:
    print(level(3, f))
    print(dump_file("python", f))
