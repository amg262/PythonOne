import pathlib


def path_lib_testing():
    print(f"{pathlib.Path} : {pathlib.Path.cwd()}")
    print(f"{pathlib.Path} : {pathlib.Path.cwd()}")


def mod_7_together():
    char_input = pathlib.Path.cwd() / "characters.txt"
    i = 0
    with char_input.open() as my_file:
        for line in my_file.readlines():
            print(line.strip())

            arr = line.strip().split("|")
            if (len(arr) == 3):
                i += int(arr[2])

    print(f"{i}")


def mod_7_together2():
    char_input = pathlib.Path.cwd() / "characters.txt"
    i = 0
    j = 1
    with char_input.open() as my_file:
        for line in my_file.readlines():
            print(line.strip())

            if "|" in line:
                i += int(line.strip()[-1])
                j += 1
            else:
                i += int(line.strip()[0])
                j += 1

    print(f"Total: {i}")
    print(f"Avg: {i / j:.2f}")


mod_7_together2()
