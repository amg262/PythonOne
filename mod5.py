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


even_letters()
