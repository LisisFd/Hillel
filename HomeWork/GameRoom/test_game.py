import unittest
from .game import Game
from .game import Room

class TestGame(unittest.TestCase):
    def setUp(self):
        self.room1 = Room(0, 0, "Main room", "", ["north"])
        self.room2 = Room(0, -1, "Second room", "", ["south"])
        self.map = {(self.room1.x, self.room1.y): self.room1,
               (self.room2.x, self.room2.y): self.room2
               }
        self.game = Game(self.ma    p)
        self.game.current_room = self.game._get_room(0, 0)

    def test_move_positive(self):
        '''
        Проверка на возврат True при суествующих координатах
        комнаты
        '''
        self.game._move(0, -1)
        self.assertTrue(self.game.new_room)

    def test_move_negative(self):
        '''
        Проверка на возврат False при  НЕ суествующих координатах
        комнаты
        '''
        self.game._move(0, 2)
        self.assertFalse(self.game.new_room)

    def test_parse(self):
        self.assertFalse(self.game._parse(f'go sadasdsad'))
        self.game._parse(f'go north')
        self.assertIsNotNone(self.game.new_coords)
        self.assertIn(self.game.new_coords, self.game.map.keys())

if __name__ == '__main__':
    unittest.main()
