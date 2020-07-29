import random


class Game:
    def __init__(self):
        """
        Создание основных переменных класса

        :param Game.player_One: Поле с кораблями Первого игрока
        :param Game.player_Two: Поле с кораблями Второго игрока
        :param Game.player_One_attempt: Поле попыток первого игрока
        :param Game.player_Two_attempt: Поле попыток второго игрока
        :param Game.player_One_ships: Корабли первого игрока
        :param Game.player_Two_ships: Корабли второго игрока
        :param Game.data_lst: Список данных веденных пользователем
        """
        self.player_One = None
        self.player_Two = None
        self.player_One_attempt, self.player_Two_attempt = None, None
        self.player_One_ships, self.player_Two_ships = 8, 8
        self.data_lst = list()

    def generation(self):
        """
        Генирация массива 10 на 10 символами тильды(пропуски)
        Генирирует два рандомных числа и использует их, для замены в массиве
        тильды, на букву 'o'(корабль) столько раз  сколько равен param: ships_spawn_count

        :return: Сгенирированный двумерный список
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
        Выводит в консоль поля, активного игока

        :param player_active_field: Поле с короблями активного игрока
        :param player_active_attempt: Поле попыток активного игрока
        :return: None
        """
        print('Ваши корабли')
        for row in player_active_field:
            print(" ".join([str(column) for column in row]))
        print("\n")
        print("Ваши попытки")
        for row in player_active_attempt:
            print(" ".join([str(column) for column in row]))

    def parse(self, in_str):
        """
        Проверяет содержит ли строка только числа, колличество этих чисел и диапозон значений

        :param in_str: Строка которую ввел польователь
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
        Замена эллементов списков игроков при попадании, при повторе значений смена хода

        Проверка на то, закончились ли корабли у атакованного игрока
        :param data_lst: Список значений введенных игроком
        :param field_Noactive_player: Поле игрока по которому производиться атака
        :param field_active_attempt: Поле попыток атакуещего игрока
        :param player_ships: Колличество кораблей атакованного игрока
        :param cell_second_player: Элемент списка по которому происходит замена значений
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

    def turn(self, player_active_field, player_active_attempt, player_Noactive_field, player_Noactive_ships):
        """
        Запуск хода игрока

        :param player_active_field: Поле корабей активного игрока
        :param player_active_attempt: Поле попыток активного игрока
        :param player_Noactive_field: Поле кораблей неактивного игрока
        :param player_Noactive_ships: Кол-во кораблей неактивного игрокак
        :var turn.data: Ввод данных пользователем
        :return: None
        """
        self.rendering(player_active_field, player_active_attempt)
        while True:
            data = input(">>> ")
            if self.parse(data):
                self.fire(self.data_lst, player_Noactive_field, player_active_attempt, player_Noactive_ships)
                break

    def run(self):
        """
        Запуск цилка игры с переменной поочередностью хода
        """
        self.player_One = self.generation()
        self.player_Two = self.generation()
        while True:
            self.turn(self.player_One, self.player_One_attempt, self.player_Two, self.player_Two_ships)
            self.turn(self.player_Two, self.player_Two_attempt, self.player_One, self.player_One_ships)


b = Game()
b.run()
