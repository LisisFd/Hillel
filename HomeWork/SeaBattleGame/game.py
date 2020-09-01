import random


class Game:
    def __init__(self):
        """
        :param Game.player_One: First player field
        :param Game.player_Two: Second player field
        :param Game.player_One_attempt: First player attempt field
        :param Game.player_Two_attempt: Second player attempt field
        :param Game.player_One_ships: First player ships
        :param Game.player_Two_ships: Second player attempt field
        :param Game.data_lst: Сoordinates entered by users
        """
        self.player_One = None
        self.player_Two = None
        self.player_One_attempt, self.player_Two_attempt = None, None
        self.player_One_ships, self.player_Two_ships = 8, 8
        self.data_lst = list()


    def run(self):
        """
        Launch game
        """
        self.player_One = self.generation()
        self.player_Two = self.generation()
        while True:
            self.turn(self.player_One, self.player_One_attempt, self.player_Two, self.player_Two_ships)
            self.turn(self.player_Two, self.player_Two_attempt, self.player_One, self.player_One_ships)


    def generation(self):
        """
        Generating a 10 by 10 array with tilde (gaps)
        Generates two random numbers and uses them to replace in an array
        tildes, with the letter 'o' (ship) as many times as param: ships_spawn_count

        :return: Player field with ships
        """
        self.player_One_attempt, self.player_Two_attempt = [['~' for j in range(10)] for i in range(10)], \
                                                           [['~' for j in range(10)] for i in range(10)]
        player_field = [['~' for j in range(10)] for i in range(10)]
        ships_spawn_count = 8
        while ships_spawn_count:
            random_row = random.randint(1, 9)
            random_column = random.randint(1, 9)
            if player_field[random_row][random_column] == '~':
                player_field[random_row][random_column] = 'o'
                ships_spawn_count -= 1
        return player_field

    @staticmethod
    def rendering(player_active_field, player_active_attempt):
        """
       Shows active player field

        :param player_active_field: Active player field
        :param player_active_attempt: Active player field attempt
        :return: None
        """
        print('Ваши корабли')
        for row in player_active_field:
            print(" ".join([str(column) for column in row]))
        print("\n")
        print("Ваши попытки")
        for row in player_active_attempt:
            print(" ".join([str(column) for column in row]))


    def turn(self, player_active_field, player_active_attempt, player_Noactive_field, player_Noactive_ships):
        """
        starting a player's turn

        :param player_active_field:Active player field
        :param player_active_attempt: Active players field attempt
        :param player_Noactive_field:No active players field
        :param player_Noactive_ships: No active player count of ships
        :return: None
        """
        self.rendering(player_active_field, player_active_attempt)
        while True:
            data = input(">>> ")
            if self.parse(data):
                self.fire(self.data_lst, player_Noactive_field, player_active_attempt, player_Noactive_ships)
                break

    def parse(self, in_str):
        """
        Checks if a string contains only numbers, the number of these numbers and a range of values

        :param in_str: User input
        :return: True or False
        """
        self.data_lst = in_str.split()
        for i in self.data_lst:
            if not i.isdigit() or len(self.data_lst) != 2 or int(i) <= 0 or int(i) >= 11:
                print("sorry , TRY")
                return False
        return True

    def fire(self, data_lst, field_Noactive_player, field_active_attempt, player_ships):
        """
        Replacing the elements of the lists of players on hit, when repeating values, change the move
        Checking if the attacked player has run out of ships

        :param data_lst: User input coordinates
        :param field_Noactive_player: Attacked player's field
        :param field_active_attempt: Attacking player's attempt field
        :param player_ships: Count of ships, attacked player's
        :param cell_second_player: Coordinate cell
        :return: None
        """

        cell_second_player = field_Noactive_player[int(data_lst[0]) - 1][int(data_lst[1]) - 1]
        if field_active_attempt[int(data_lst[0]) - 1][int(data_lst[1]) - 1] == '*' \
                or field_active_attempt[int(data_lst[0]) - 1][int(data_lst[1]) - 1] == "x":
            print("Вы уже туда стреляли\n----------")
            return
        if cell_second_player == "o":
            player_ships -= 1
            if not player_ships:
                choise = input("Ура, вы выйгали\nЖелаете сыграть ещё?-- y/n ")
                quit() if choise == 'n' else self.run()
            print(f"Попадание, осталось: {player_ships}\n----------")
            field_active_attempt[int(data_lst[0]) - 1][int(data_lst[1]) - 1] = "x"
        else:
            print("Уфф промах\n----------")
            field_active_attempt[int(data_lst[0]) - 1][int(data_lst[1]) - 1] = '*'


b = Game()
b.run()
