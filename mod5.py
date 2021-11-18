import string


def simon_says():
    message = input("Enter message: ")
    shift = int(input("Number of chars to shift 1 - 26"))
    encrypt = ""
    decrypt = ""

    for letter in message:
        if letter != " ":
            encrypt += chr(ord(letter) + shift)
        else:
            encrypt += " "

    for letter in encrypt:
        if letter != " ":
            decrypt += chr(ord(letter) - shift)
        else:
            decrypt += " "

    print(f"E: {encrypt}")
    print(f"D: {decrypt}")


def email_gather_me():
    begin = 0
    end = 1
    group = []
    while begin != end:
        email = input("Enter email address: ")
        domain = email.find("@")
        per = email.rfind(".")
        print(email[email.find("@") + 1:email.rfind(".")])
        begin += 1


def even_letters():
    word = input("Word: ")
    new_word = ""
    count = 0

    for letter in word:
        if count % 2 == 0:
            new_word += letter
        count += 1
    print(new_word)


def together():
    items = []
    item = input("Enter an item to purchase NA to end")

    while item.lower() != "na":
        items.append(item)
        item = input("Enter an item to purchase NA to end")

    items.reverse()

    for item in items:
        print(item)


def participate():
    parts = ["Bob", "Sue", "Mike", "John", "Bill"]
    name = input("Name: ")

    if name in parts:
        print(f"{name} is in!")


def lab_a():
    ips = ['11.16.211.2', '133.1.1.111', '201.22.3.41', '17.55.23.123', '144.211.32.45']

    for ip in ips:
        nodes = ip.split(".")

        if int(nodes[0]) <= 127:
            print(f"{ip} Class A Host {'.'.join(nodes[1:])}")
        elif int(nodes[0]) <= 191:
            print(f"{ip} Class B Host {'.'.join(nodes[2:])}")
        else:
            print(f"{ip} Class C Host {nodes[-1]}")


def lab_c():
    phrase = input("Phrase: ")

    arr = phrase.split(" ")
    a = []
    acro = ""
    for c in arr:
        acro += c[0]

    print(f"{acro}")


lab_c()
