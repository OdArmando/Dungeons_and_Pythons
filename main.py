import os
import winsound
import time
from Text_Functions import TextFunctions

winsound.PlaySound(r'Main_Menu.wav', winsound.SND_LOOP + winsound.SND_ASYNC)

TextFunctions.intro()


if input() == '':
    os.system('cls')
    TextFunctions.loading()
    time.sleep(3)

    os.system('cls')
    TextFunctions.choose_character()
    while True:
        choose_character = input()
        if choose_character == '1':
            os.system('cls')
            TextFunctions.intro_warrior()
            TextFunctions.enter_name()
            player_name = input('Warrior name:')
            break
        elif choose_character == '2':
            os.system('cls')
            TextFunctions.intro_sorcerer()
            TextFunctions.enter_name()
            player_name = input('Sorcerer name:')
            break
        elif choose_character == '3':
            os.system('cls')
            TextFunctions.intro_healer()
            TextFunctions.enter_name()
            player_name = input('Healer name:')
            break
        else:
            TextFunctions.please_choose()
            continue

    os.system('cls')
    TextFunctions.choose_path()
    while True:
        winsound.PlaySound(r'Exploring.wav', winsound.SND_LOOP + winsound.SND_ASYNC)
        choose_path = input()
        if choose_path == '1':
            os.system('cls')
            TextFunctions.forest_path()
            break
        elif choose_path == '2':
            os.system('cls')
            TextFunctions.town_path()
            break
        elif choose_path == '3':
            os.system('cls')
            TextFunctions.dungeon_path()
            break
        else:
            TextFunctions.please_choose()
            continue

    time.sleep(3)

else:
    os.system('cls')
    TextFunctions.exit_game()
    winsound.PlaySound(None, winsound.SND_PURGE)
