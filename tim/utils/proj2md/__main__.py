from tim.utils.proj2md import dir_tree, get_arguments
from tim.utils.proj2md.fakedown import *

def main():
    args = get_arguments()
    t, files = dir_tree(args.dir, args.types)
    print(level(1, "Project " + args.dir))
    print(text("\n Layout of this project is ...\n"))
    print(level(3, "Layout"))
    print(code('text', t))
    print(level(2, "Code Listing"))
    for f in files:
        print(level(3, f.split('/')[-1]))
        print(dump_file('python', f))
    from pprint import pprint
    pprint(args)
    print("Hi")


if __name__ == "__main__":
    main()