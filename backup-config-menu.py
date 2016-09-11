# v1 Written by Alex Munoz
# GitHub: AlexMunoz905
# 9-7-16

print("1. IOS Router")
print("2. IOS Switch")
print("3. NxOS")
print("4. ASA")
print("5. WLC")

OurInput = input("Choose your number: ")

if OurInput == "1":
    import Router
elif OurInput == "2":
    import Switch
elif OurInput == "3":
    import NXOS
elif OurInput == "4":
    import ASA
elif OurInput == "5":
    import WLC
else:
    print("Please print a correct input")