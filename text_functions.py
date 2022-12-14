"""This module contains all the methods and classes called in the program"""
import random
from useful_function import my_print, clear_screen
from enemy import Goblin, Troll, Orc
from player import Knight, Cleric, Wizard
import winsound


class Start:
    """Contains start game and in game functions and instructions"""
    @staticmethod
    def stop_sound():
        """Static method for stopping music in the game"""
        winsound.PlaySound(None, winsound.SND_PURGE)

    @staticmethod
    def play_sound_intro():
        """Start Intro Music in the game"""
        winsound.PlaySound(r'C:\Dungeons_and_Pythons\Main_Menu.wav',
                           winsound.SND_ASYNC + winsound.SND_LOOP)

    @staticmethod
    def play_sound_exploring():
        """Play Exploring music scene"""
        winsound.PlaySound(r'C:\Dungeons_and_Pythons\Exploring.wav',
                           winsound.SND_ASYNC + winsound.SND_LOOP)

    @staticmethod
    def play_sound_fight():
        """Play Fight music scene"""
        winsound.PlaySound(r'C:\Dungeons_and_Pythons\BattleFinal.wav',
                           winsound.SND_ASYNC + winsound.SND_LOOP)

    @staticmethod
    def intro_message():
        """Start Game Intro message"""
        print(
            'Welcome, stranger!\n'
            'Here in Osgiliath you are going to fight all sorts of creatures,\n'
            'Conquer dungeons and lands!\n'
            'In a country where magic rules anything is possible.\n'
            'It all depends on what you want to fight this creatures with,\n'
            'Is it magic, or brute force?\n')

    @staticmethod
    def wizard_message():
        """Wizard class intro message"""
        print('The wizards are the first people who learned to use magic,\n '
              'The magic was used in order to protect the people,\n'
              'Their powers are great,\n '
              'They have powerful protecting spells,\n '
              'But can use destructive force when is needed!\n')

    @staticmethod
    def knight_message():
        """Knight class intro message"""
        print('Great choice warrior!,\n'
              'You chose the original fighters for the common people,\n'
              'Knights are brave and they do not run from the danger\n'
              'They use their great swords and brute force.\n')

    @staticmethod
    def cleric_message():
        """Cleric class intro message"""
        print('The clerics are good hearted magicians\n'
              'They devoted all their life gaining powers to protect the people,\n'
              'A healer is in great demand in this journey.\n '
              'Danger is waiting at every stone in Osgiliath lands!.\n')

    @staticmethod
    def play_again():
        """Ask player is wants to play again function"""
        user_answer = input("""Do you want to play again?
        Press \'y\' to play or press any key to leave the game\n""")
        clear_screen()
        if user_answer == 'y':
            Start.stop_sound()
            Start.play_sound_intro()
            return True
        else:
            print('''The realm needs you!!!
            Let's hope you will come back soon.''')
            return False

    @staticmethod
    def ask_type_of_char(user):
        """Ask user to pick a character"""
        if user == '1':
            Start.wizard_message()
        elif user == '2':
            Start.knight_message()

    @staticmethod
    def choosing_path(user):
        """Ask player to choose a path to explore"""
        if user == '1':
            print('''
            A lot of brave heroes entered in this forest but only a few came back!
            Strange creatures stalk you so be aware!
            In this forest you can find hidden chests with powerful items 
            So be sure to collect them!
            ''')
        elif user == '2':
            print('''
            This town is now ruled by some scary creatures and humans are killed by them.
            So keep an eye out!
            In this town you can find hidden chests with powerful items 
            So be sure to collect them!
            ''')
        elif user == '3':
            print('''
            Dungeons are probably the scariest and you have to be aware at every sound,
            Otherwise you might be taken by surprise.
            In this dungeon you can find hidden chests with powerful items 
            So be sure to collect them!
            ''')

    @staticmethod
    def action():
        """Info message about path choosing and finding a chest, player is informed if it wants to open it"""
        user_path = input('''Now let's go to destroy our enemies.
                        You have arrived on a crossroad with 3 paths and you have to choose one!
                        1. To the forest
                        2. To the town
                        3. To the dungeon
        Please select 1, 2 or 3\n''')
        clear_screen()
        Start.choosing_path(user_path)
        clear_screen()
        user_risk = input('''You have found a chest!
                You can choose to open it and getting a better or worse weapon and armor
                or you can leave it and fight using your own items.
                What it will be?
                Do you risk or not?
        Type \'y\' to risk or press any key to keep your items\n''')
        if user_risk == 'y':
            return True
        else:
            return False

    @staticmethod
    def chose_enemy():
        """Player is informed about the type of the enemy he encountered"""
        goblin = Goblin()
        orc = Orc()
        troll = Troll()
        enemy_list = [goblin, orc, troll]
        enemy = random.choice(enemy_list)
        my_print(f'Your opponent is an {enemy.type_of} and has {enemy.hp} HP, {enemy.defence}'
                 f' defence points and he hits with a power of {enemy.power}\n')
        clear_screen()
        return enemy

    @staticmethod
    def player_no_chest(char):
        """Function in case player is not opening the chest"""
        clear_screen()
        char.gear_up()
        print(f'Your power is {char.power} and your armor is {char.defence}\n')
        Start.stop_sound()
        Start.play_sound_fight()

    @staticmethod
    def player_open_chest(char):
        """Function if the player opens chest and informed about new power"""
        clear_screen()
        char.open_chest()
        print(f'You have found a {char.weapon_type} with power of {char.weapon} and a {char.armor_type} '
              f'with extra defence of {char.armor}\n')
        char.gear_up()
        print(f'Your new power is {char.power} and your new armor is {char.defence}\n')
        Start.stop_sound()
        Start.play_sound_fight()

    @staticmethod
    def battle(enemy, char):
        """The battle information, damage, life, hits"""
        char.attack(enemy)
        my_print(f'You are attacking with a power of {char.power}, your amor has {char.defence} '
                 f'durability and {char.hp} HP left\n')
        enemy.attack(char)
        my_print(f'{enemy.type_of} is attacking you with a power of {enemy.power} and he has '
                 f'{enemy.critical}% '
                 f'chance to deal double damage. {enemy.type_of} armor has {enemy.defence} points and '
                 f'{enemy.hp} HP left\n')
        if char.hp <= 0:
            my_print(f'''Our {char.type_of} has been killed by a powerful {enemy.type_of}!!!
                            Rest in peace grand {char.type_of}\n''')
        elif enemy.hp <= 0:
            my_print(f'Well done grand {char.type_of}!!! You defeated the {enemy.type_of}\n')

    @staticmethod
    def fighting_scene(char):
        """The fighting scene, start fight, music during the fight, """
        clear_screen()
        Start.stop_sound()
        Start.play_sound_exploring()
        if Start.action():
            Start.player_open_chest(char)
            enemy = Start.chose_enemy()
            while True:
                Start.battle(enemy, char)
                if char.hp <= 0 or enemy.hp <= 0:
                    break
        else:
            Start.player_no_chest(char)
            enemy = Start.chose_enemy()
            while True:
                Start.battle(enemy, char)
                if char.hp <= 0 or enemy.hp <= 0:
                    break

    @staticmethod
    def game():
        """Start the game, player choosing name, character selection"""
        user_name = input('Enter your name brave warrior: ')
        clear_screen()
        while True:
            user_char = input(f"""What character do you want to play {user_name}:
                                1. Wizard
                                2. Knight
                                3. Cleric
            Please select 1, 2 or 3.\n""")
            clear_screen()
            Start.ask_type_of_char(user_char)
            clear_screen()
            if user_char == '1':
                wizard = Wizard(user_name)
                print(f'Thank you wizard {wizard.name} for choosing to protect us')
                Start.fighting_scene(wizard)
                break
            elif user_char == '2':
                knight = Knight(user_name)
                print(f'Thank you Sir {knight.name} for choosing to protect us')
                Start.fighting_scene(knight)
                break
            else:
                if user_char == '3':
                    cleric = Cleric(user_name)
                    print(f'Thank you Good Cleric {cleric.name} for choosing to protect us')
                    Start.fighting_scene(cleric)

    @staticmethod
    def game_intro():
        """Intro, ask player if he wants to play or not, welcome and goodbye message"""
        Start.play_sound_intro()
        Start.intro_message()
        user = input('''Do you want to play? 
        Press \'y\'to play or press any key to exit the game\n''')
        clear_screen()
        if user == 'y':
            print("""Great!
            Let's fight for this realm!
        """)
            Start.ask_type_of_char(user)
            return True
        else:
            print('Hope you will come back soon.The land needs you')
            return False
