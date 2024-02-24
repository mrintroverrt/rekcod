import sys
from Dockerlib.Docker import Dockerhelper

if len(sys.argv) != 3:
    print("Usage: python script.py -n <path>")
    sys.exit(1)

dock = Dockerhelper()

if sys.argv[1] == '-n':
    dock.create_dcoker_file(path=sys.argv[2])
else:
    print("wrong option")