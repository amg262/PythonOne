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
import string


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

    if average < 20:
        activity = "Low"
    elif average < 100:
        activity = "Average"
    elif average < 200:
        activity = "High"
    else:
        activity = "Critical"

    print(f"Average per day: {average:.2f}")
    print(f"Activity Level: {activity}")


def run_lab_c():
    a = 5
    b = 6
    c = 11

    if a > b:
        print(a)
    else:
        print(b)

    a = 5
    b = 6
    c = 11

    if a > b:
        print("A")
    elif a + b == c:
        print("C")
    else:
        print("B")

    a = 5
    b = 6

    print(a == b)

    a = 5
    b = 6
    c = 11
    print((a + b) > (b + c) or (a + b) == c)


def mod_2_together():
    last_name = input("Last Name: ")
    income = float(input("Income: "))
    credits = int(input("Credits: "))
    print("You get financial aid " + str(income <= 60000 and credits >= 6))

    grade = int(input("Grade: "))
    last_name = input("Last Name: ")

    if grade > 90:
        print("Honor Roll!")
    elif grade >= 73:
        print("You pass!")
    else:
        print("You Fail")

    print("Orientation of Thursday " + str(grade == 9 and last_name < "n"))

    if (last_name.lower() < "i"):
        print("Register on Monday")
    elif (last_name.lower() < "q"):
        print("Register on Wednesday")
    else:
        print("Register on Friday")

    sport = input("Golf or B-ball: ")
    player_a = int(input("Player 1:"))
    player_b = int(input("Player 2:"))

    if player_a == player_b:
        print("They tied")
    elif sport == "golf" and player_a < player_b:
        print(f"Player A wins in {sport} by {player_b - player_a}")
    elif sport == "golf" and player_b < player_a:
        print(f"Player A wins in {sport} by {player_a - player_b}")
    if sport == "bball" and player_a < player_b:
        print(f"Player B wins in {sport} by {player_b - player_a}")
    elif sport == "bball" and player_b < player_a:
        print(f"Player A wins in {sport} by {player_a - player_b}")

    print("END")


if __name__ == '__main__':
    # run_int_detect()
    # run_lab_c()
    mod_2_together()
    print()
    # go()
    # length()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
