import os

for dir in ["brainfuckCode", "brainfuckCode2", "brainfuckCode3"]:
    for f in os.listdir(dir):
        f = os.path.join(dir, f)
        print(open(f).read())
        print()
