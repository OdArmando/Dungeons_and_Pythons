class TextFunctions:
    @staticmethod
    def intro():
        print(
            'Welcome, stranger!\n'
            'Here in Osgiliath you are going to fight all sorts of creatures, conquer dungeons and lands!\n'
            'In a country where magic rules anything is possible.\n'
            'It all depends on what you want to fight this creatures with,\n'
            'Is it magic, or brute force?\n')
        print('Press enter to start the adventure or any other key to exit...')

    @staticmethod
    def choose_character():
        print('Choose a character (type 1, 2 or 3):\n'
              '1. Warrior\n'
              '2. Sorcerer\n'
              '3. Healer\n')

    @staticmethod
    def enter_name():
        print('Type your name.')

    @staticmethod
    def intro_warrior():
        print('Great choice warrior, you chose the original fighters for the common people,\n\n'
              'Warriors are brave and they do not run from the danger\n'
              'They use their great swords and brute force.\n')

    @staticmethod
    def intro_sorcerer():
        print('The sorcerers are the first people who learned to use magic in order to protect the people,\n'
              'Their powers are great,\n '
              'They have powerful protecting spells but can use destructive force when is needed!\n')

    @staticmethod
    def intro_healer():
        print('The healers are good hearted magicians\n'
              'They devoted all their life gaining powers to protect the people,\n\n'
              'A healer is in great demand in a journey where danger is waiting at every stone in Osgiliath lands!.\n')

    @staticmethod
    def please_choose():
        print('Please type only 1, 2 or 3!')

    @staticmethod
    def choose_path():
        print('You can hear the rumbling thunder, you can see the sky lightning your ways\n'
              'And now you are scratching your head thinking which way to take, because,\n'
              'In front of you is a crossroad with 3 paths. Choose your path (type 1, 2 or 3):\n\n'
              '1. To a dark forest\n'
              '2. To a mysterious town\n'
              '3. To a scary dungeon\n')

    @staticmethod
    def forest_path():
        print('You chose the forest path!\n\n')

    @staticmethod
    def town_path():
        print('You chose the town path!\n\n')

    @staticmethod
    def dungeon_path():
        print('You chose the dungeon path!\n\n')

    @staticmethod
    def loading():
        print('Loading...')

    @staticmethod
    def exit_game():
        print('Such a shame, begone coward, there are others waiting to the gate!')

