def go_while():
    count = 0
    net = 0
    steps = int(input(f"Steps Day 1 (-1 to exit)"))
    net += steps

    count += 1
    while steps != -1:
        steps = int(input(f"Steps Day {count + 1}: (-1 to exit)"))
        net += steps
        count += 1

    count -= 1
    net += 1

    print(f"Days: {count} - Steps: {net} - Avg {net / count}")


go_while()
