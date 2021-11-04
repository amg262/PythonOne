# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

def get_age():
    age = int(input("Age:"))
    print(age)

    return age

def do_age_stuff():
    print(f'The age is', get_age())

def go():
    var = "boss man"
    print(f'Hey', {})
    return  var

def length():
    print(f'Length is ',len("hey bossman "))


if __name__ == '__main__':
    do_age_stuff()
    go()
    length()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
