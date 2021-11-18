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


def email_gather():
    begin = 0
    end = 3
    group = []
    while begin < end:
        email = input("Enter email address: ")
        if "@" in email:
            print("EMAIL")
            begin += 1
        else:
            print("Invalid")

email_gather_me()
