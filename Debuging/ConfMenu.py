# Written by Alex Munoz
# GitHub: AlexMunoz905
# 9-7-16

print("1. IOS")
print("2. ASA")
print("3. NxOS")
print("4. WLC")

OurInput = input("Choose your number: ")

if OurInput == "1":
    import test
elif OurInput == "2":
    import testa
elif OurInput == "3":
    import testb
elif OurInput == "4":
    import testc
else:
    print("Please print a correct input: ")