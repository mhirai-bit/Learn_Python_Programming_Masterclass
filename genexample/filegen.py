import os

root = "music"

for path, directories, files in os.walk(root, topdown=True):
    print(path)
    for f in files:
        print("\t{}".format(f))