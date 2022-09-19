from Text_Functions import TextFunctions
from playsound import playsound
playsound('C:/ITSchoolPython/Dungeons and Pythons/Main_Menu.wav')

TextFunctions.intro_message()

print('*______________________________________________________________________*')

answer = None
while answer not in ("Yes", 'yes' "No", 'no'):
    answer = input("Enter yes or no: ")
    if answer == "yes":
        print("Much appreciated, your help is so much needed. Next we will proceed in choosing your fighter class")
        break

    elif answer == ("no", "No"):
        print("Such a shame, begone coward!")

    else:
        print("Please enter Yes or No.")


