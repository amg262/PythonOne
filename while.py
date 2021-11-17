
steps = int(input("Steps: (-1 to exit)"))
net = 0
count = 1


while steps != -1:
    steps = int(input(f"Steps Day {count}: (-1 to exit)"))
    net += steps
    count += 1

print(f"Days: {count} - Steps: {net} - Avg {net / count}:.2f")

