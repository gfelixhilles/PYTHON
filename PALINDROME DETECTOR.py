print("PALINDROME DETECTOR")
p = input("Digit the word/phrase:");
if " " in p:
    p2 = p.replace(" ", "")
    if len(p2) % 2 == 0:
        if p2 == p2[::-1]:
            print(f"The phrase {p} is a palindrome.")
        else:
            print(f"The phrase {p} is not a palindrome.")
    else:
        if p == p[::-1]:
            print(f"The phrase {p} is a palindrome.")
        else:
            print(f"The phrase {p} is not a palindrome.")
else:
    if len(p) % 2 == 0:
        if p == p[::-1]:
            print(f"The phrase {p} is a palindrome")
        else:
            print(f"The phrase {p} is not a palindrome.")
    else:
        if p == p[::-1]:
            print(f"The phrase {p} is a palindrome")
        else:
            print(f"The phrase {p} is not a palindrome.")
