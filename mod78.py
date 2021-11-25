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
    j = 0
    with char_input.open() as my_file:
        for line in my_file.readlines():

            j += 1

            if "|" in line:
                i += int(line.strip()[-1])
                items = line.split("|")
                print(items[1])
            else:
                print(line.strip()[19:])
                i += int(line[0])

    # print(f"Total: {i}")
    # print(f"Avg: {i / j:.2f}")


def mod_7_b():
    char_input = pathlib.Path.cwd() / "log.txt"
    i = 0
    j = 0
    with char_input.open() as my_file:
        for line in my_file.readlines():
            if "bobsmart.html" in line:
                items = line.split(" ")
                print(f"{items[0]} {items[1]} - {items[9]}")
                position = line.find("domain1335920") + 15
                print(f"{line[:19]} {line[position:position + 15].split(' ')[0]} ")


def mod8too():
    grades = {}
    grade = input("Enter Grade x to  quit")

    while grade.lower() != "x":
        if grade in grades:
            grades[grade] += 1
        else:
            grades[grade] = 1

        grade = input("Enter Grade x to  quit")

    for grade, count in grades.items():
        print(f"{grade} - {count}")

def last_prog():
    hack_input = pathlib.Path.cwd() / "hack-source.csv"
    hackers = {}

    with hack_input.open() as my_file:
        for line in my_file.readlines():
            parts = line.split(',')
            hackers[parts[0]] = parts[1].rstrip()

    file_path = pathlib.Path.cwd() / "log.txt"
    with file_path.open() as my_file:
        for line in my_file.readlines():
            if "bobsmart.html" in line:
                items = line.split(" ")
                ip_netwwork = items[9][:items[9].rfind('.')]
                if ip_netwwork in  hackers:
                    temp = hackers[ip_netwwork]
                else:
                    temp = "Safe Source"
            print(f"{items[0]} {items[1]} - {temp}")

last_prog()