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
import random
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

def get_activity(average):
    if average < 20:
        activity = "Low"
    elif average < 100:
        activity = "Average"
    elif average < 200:
        activity = "High"
    else:
        activity = "Critical"
    return activity


def run_int_detect():
    number_intrusions = int(input("Please enter the # of intrusions: "))
    number_days = int(input("Please enter the # of days: "))
    average = number_intrusions / number_days

    activity = get_activity(average)

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


def KgKmLiterConvert():
    miles = float(input("Miles: "))
    gallons = float(input("Gallons: "))
    pounds = float(input("Pounds: "))

    km = miles * 1.60934
    liters = gallons * 3.78541
    kg = pounds * 0.453592

    print(f"This calculation is: {km:.2f}km, {liters:.2f}L, {kg:.2f}kg")


def DessertCalc():
    desserts = print("How many desserts did you eat last week you fatty?: ")
    dInt = int(desserts)
    avg = dInt / 7

    print(f"Avg: {desserts:.2f}")
    if avg < 3:
        print(f"Dessert Level: Good")
    elif avg >= 3 and avg < 5:
        print(f"Dessert Level: Fine")
    else:
        print(f"Dessert Level: High")


#### END OF WEEK ONE - MODULE 1 & 2 #####

#### BEGINNING OF WEEK 2 ######

def print_cat(words):
    print(" /\\_/\\ ")
    print(f"( o.O )  {words}")
    print(f" > ^ <")


def number_guess():
    upper = int(input(f"Upper limit:"))
    guess = int(input(f"Guess: "))
    num = random.randrange(1, upper)

    while num != guess:
        if guess < num:
            print("Too low!")
        else:
            print("Too High!")
        guess = int(input(f"Guess: "))

    print(f"Number: {num}")


def calc_hours(chores, hw, sport):
    return (chores * 3) + (hw * 2) + (sport * 4)


def calc_games(a, b, c):
    return (a * 150) + (b * 75) - (c * 100)


def game_system_input():
    cost = float(input("Cost: $"))
    a_grades = int(input("# of As"))
    b_grades = int(input("# of Bs"))
    c_grades = int(input("# of C or lower"))
    hours_chores = int(input("Hours spent on chores"))
    hours_hw = int(input("Hours spent on homework"))
    hours_sport = int(input("Hours spent on sports"))

    if calc_games(a_grades, b_grades, c_grades) >= cost:
        print(f"You may buy the game system")
    else:
        print(f"You may not buy game system")

    print(f"You have earned {calc_hours(hours_chores, hours_hw, hours_sport)} hours of play time.")


def calc_step_mi(steps):
    return (steps * 2.5) / 5280


def calc_step_km(steps):
    return (steps * .762) / 1000


def step_prog():
    steps = int(input("Yesterdays steps: "))

    print(f"{steps} steps is {calc_step_mi(steps):.2f} miles and {calc_step_km(steps):.2f} km")


def step_counter():
    input2 = int(input("# steps (-1 when done): "))

    days = 0
    counter = 0
    mini = input2
    maxi = input2
    while input2 != -1:
        input2 = int(input("# steps (-1 when done): "))
        counter += input2
        days += 1

        if input2 > maxi:
            mini = input2
        elif input2 < mini:
            mini = input2

    print(f"Total steps: {counter}")
    print(f"Avg steps: {counter / days}")
    print(f"Total days: {days}")
    print(f"Min steps: {mini}")
    print(f"Max steps: {maxi}")


def savings_goal():
    goal = int(input("Savings goal: "))
    monthly_dep = int(input("Montly deposit: "))
    apr = int(input("Annual Interest: "))

    for cousins in range(1, 25):
        gift = 500
        print(f"Each of {cousins} will have to pay {gift / cousins}")


def grains():
    grains = 1
    total = 1
    for i in range(12):
        grains *= 2
        total += grains
        print(f"Square {i + 1} {total}")

    print(f"Total grains {total}")

if __name__ == '__main__':
    step_counter()
    # number_guess()
    # step_prog()
    # game_system_input()
    # run_int_detect()
    # number_guess()
    # print_cat("im on bath salts")
    # run_int_detect()
    # run_lab_c()
    # mod_2_together()
    # print()
    # go()
    # length()
    # KgKmLiterConvert()
    # DessertCalc()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
