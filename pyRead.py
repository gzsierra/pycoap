import sys, os

# Check Arguments
def checkArg(argv):
    if len(argv) != 2:
        print("Need an argument")
        print("python " + argv[0] + " [file_name]")
        sys.exit(2)

    # Check If EXIST and not EMPTY
    file = argv[1]
    if not os.path.isfile(file):
        print("File not existing")
        sys.exit(2)
    if os.stat(file).st_size == 0:
        print("File empty")
        sys.exit(2)

# Read file line by line and split
def readFile(file):
    f = open(file,"r")
    return f
