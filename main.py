from Text_Functions import *

if Start.game_intro():
    Start.game()
    while Start.play_again():
        Start.game_intro()
        Start.game()

