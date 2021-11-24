def mod6():
    brit = ["aeroplane", "catalogue", "colour", "draught", "metre", "pyjamas", "tyre"]
    amer = ["airplane", "catalog", "color", "draft", "meter", "pajama", "tire"]

    q1 = input("What are RGB and CYMK used for?")
    q2 = input("What part of your car is damaged if you drive over nails?")
    q3 = input("What did the Wright Brothers invent?")

    b_pts = 0
    a_pts = 0

    for a in brit:
        if q1 in a:
            b_pts += 1
        if q2 in a:
            b_pts += 1
        if q2 in a:
            b_pts += 1

    for a in amer:
        if q1 in a:
            a_pts += 1
        if q2 in a:
            a_pts += 1
        if q2 in a:
            a_pts += 1

    if b_pts + a_pts > 1:
        if b_pts > a_pts:
            print(f"Ello Mate!")
        else:
            print(f"Sup bro")
    else:
        print(f"You suck")


mod6()
