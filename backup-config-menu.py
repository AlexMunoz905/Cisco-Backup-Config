# v1 Written by Alex Munoz
# GitHub: AlexMunoz905
# 9-7-16

print("1. IOS Router")
print("2. IOS Switch")
print("3. NxOS")
print("4. ASA")
# print("5. WLC")

OurInput = input("Choose your number: ")

if OurInput == "1":
    import backup-config-Router
elif OurInput == "2":
    import backup-config-Switch
elif OurInput == "3":
    import backup-config-nxos
elif OurInput == "4":
    import backup-config-asa
elif OurInput == "5":
    import backup-config-wlc
else:
    print("Please print a correct input")