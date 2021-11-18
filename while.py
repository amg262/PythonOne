def go_while():
    count = 0
    net = 0
    steps = float(input(f"Sales Day 1 (-1 to exit)"))
    net += steps

    count += 1
    while steps != -1:
        steps = float(input(f"Sales Day {count + 1}: (-1 to exit)"))
        net += steps
        count += 1

    count -= 1
    net += 1

    print(f"Days: {count} - Sales: ${net:.2f} - Avg: ${net / count:.2f}")


go_while()
