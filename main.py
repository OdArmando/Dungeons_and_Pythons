from text_functions import *

if Start.game_intro():
    Start.game()
    while Start.play_again():
        Start.game_intro()
        Start.game()
