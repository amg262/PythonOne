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
    return var


def length():
    print(f'Length is ', len("hey bossman "))


###### END OF MY OWN PLAYING AROUND FUNCTIONS ##########

def run_int_detect():
    number_intrusions = int(input("Please enter the # of intrusions: "))
    number_days = int(input("Please enter the # of days: "))
    average = number_intrusions / number_days
    print(f"Average per day: {average:.2f}")


if __name__ == '__main__':
    run_int_detect()

    print()
    # go()
    # length()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
