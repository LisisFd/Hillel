import logging

class My_logger(logging.Logger):
    def __init__(self, name):
        super().__init__(name)
        self.name = name
        logging.getLogger(self.name)
        self.setLevel(logging.DEBUG)

        fh = logging.FileHandler('spam.log')
        fh.setLevel(logging.DEBUG)

        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        self.addHandler(fh)
        self.addHandler(ch)

class Room:
    """
    Base class for Room
    """
    def __init__(self, x, y, name, description, exits):
        """
        :param x: room x
        :param y: room y
        :param name: room name
        :param description: room description
        """
        self.x = x
        self.y = y
        self.name = name
        self.description = description
        self.exits = exits
        self.logger = My_logger('debag.log')

    def __str__(self):
        return f'{self.name}\n{self.description}'

    def _check_exit(self, direction):
        self.logger.debug('Check exit')
        self.logger.info(f'Exit is {direction in self.exits}')

        return direction in self.exits


class Game:
    Directions = {
        "north": (0, -1),
        "south": (0, 1),
        "west": (-1, 0),
        "east": (1, 0)
    }

    def __init__(self, map):
        self.logger = My_logger('debag.log')
        self.player_x = 0
        self.player_y = 0
        self.map = map
        self.current_room = self._get_room(0, 0)
        self.logger.info(f'Поиск комнаты')
        self.logger.debug(f'Комната {self.current_room} готова')
        self._look_at(self.current_room)

    def _move(self, x, y):
        self.logger.info(f'Проверка координат..')
        self.room_x = self.player_x + x
        self.room_y = self.player_y + y
        self.new_room = self._get_room(self.room_x, self.room_y)

        if self.new_room:
            self.current_room = self.new_room
            self.player_x += x
            self.player_y += y
            self.logger.debug(f'Найдена комната {self.current_room}, переходим')
            self._look_at(self.current_room)
        else:
            self.logger.debug('Error: missing room')

    def _get_room(self, x, y):
        coords = (x, y)
        room = self.map.get(coords)
        return room

    @staticmethod
    def _look_at(obj):
        print(obj)

    def _parse(self, in_str):
        if in_str == 'exit':
            quit()
        if in_str.startswith('go '):
            direction = in_str[3:]
            if self.current_room._check_exit(direction):
                self.new_coords = self.Directions[direction]
                self._move(*self.new_coords)

    def run(self):
        while True:
            action = input('>>> ')
            self._parse(action)


room1 = Room(0, 0, "Main room", "", ["north"])
room2 = Room(0, -1, "Second room", "", ["south"])
map = {(room1.x, room1.y): room1,
       (room2.x, room2.y): room2
       }
game = Game(map)

if __name__ == '__main__':
    game.run()
