def calc_step_mi(steps):
    return (steps * 2.5) / 5280

def calc_step_km(steps):
    return (steps * .762) / 1000

def step_prog():
    steps = int(input("Yesterdays steps: "))

    print(f"{steps} steps is {calc_step_mi(steps):.2f} miles and {calc_step_km(steps):.2f} km")


if __name__ == '__main__':
    step_prog()