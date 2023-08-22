print("BMI CALCULATOR")
h = float(input("Digit your height:"))
w = float(input("Digit your weight:"))
print(w/h**2)
if w /h**2 < 16:
    print("Severe Thinness")
elif w /h**2 < 17:
    print("Moderate Thinness")
elif w /h**2 < 18.5:
    print("Mild Thinness")
elif w /h**2 < 25:
    print("Normal")
elif w /h**2 < 30:
    print("Overweight")
elif w /h**2 < 35:
    print("Overweight Class I")
elif w /h**2 < 40:
    print("Overweight Class II")
else:
    print("Overweight Class III")
