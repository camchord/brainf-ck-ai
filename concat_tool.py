import os

# for dir in ["brainfuckCode", "brainfuckCode2", "brainfuckCode3"]:
#     for f in os.listdir(dir):
#         f = os.path.join(dir, f)
#         print(open(f).read())
#         print()


def walk(path):
    if path.endswith(".h") or path.endswith(".cpp"):
        print(open(path).read())
    elif os.path.isdir(path):
        for sub in os.listdir(path):
            walk(os.path.join(path, sub))


walk("../bitcoin")
