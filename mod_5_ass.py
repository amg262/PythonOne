def mod5():
    word1 = input("Word 1: ")
    word2 = input("Word 2: ")

    s1 = word1[:len(word1)//2]
    s2 = word1[len(word1)//2:]
    print(f"{s1}{word2}{s2}")
