import random
Response = "y"
while Response == "y":
    nu = random.randint(1,6)
    if nu == 1:
        print("[-----]")
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
        print("[-----]")
    
    if nu == 2:
        print("[-----]")
        print("[  0  ]")
        print("[     ]")
        print("[  0  ]")
        print("[-----]")

    if nu == 3:
        print("[-----]")
        print("[  0  ]")
        print("[  0  ]")
        print("[  0  ]")
        print("[-----]")

    if nu == 4:
        print("[-----]")
        print("[  00 ]")
        print("[     ]")
        print("[  00 ]")
        print("[-----]")

    if nu == 5:
        print("[-----]")
        print("[  00 ]")
        print("[  0  ]")
        print("[  00 ]")
        print("[-----]")

    if nu == 6:
        print("[-----]")
        print("[  00 ]")
        print("[  00 ]")
        print("[  00 ]")
        print("[-----]")

    Response = input("Do you want to continue? Press Y to roll again and N to exit\n")

    