import unittest

from moving_toy import Toy, Table

class ToyTestCase(unittest.TestCase):

    def setUp(self):

        self.toy = Toy()
        self.table = Table(5, 5)

    def test_table_size(self):
        
        self.assertEqual(self.table.length, 5)
        self.assertEqual(self.table.width, 5)

    def test_toy_place(self):
        
        self.toy.place(1, 1, 'NORTH', self.table)
        self.assertEqual(self.toy.x_position, 1)
        self.assertEqual(self.toy.y_position, 1)
        self.assertEqual(self.toy.direction, 'NORTH')

        self.toy.place(2, 4, 'EAST', self.table)
        self.assertEqual(self.toy.x_position, 2)
        self.assertEqual(self.toy.y_position, 4)
        self.assertEqual(self.toy.direction, 'EAST')

        self.toy.place(3, 7, 'NORTH', self.table)
        self.assertNotEqual(self.toy.x_position, 3)
        self.assertNotEqual(self.toy.y_position, 7)
        self.assertNotEqual(self.toy.direction, 'NORTH')

    def test_toy_move(self):

        self.toy.place(1, 1, 'NORTH', self.table)

        self.toy.move(self.table)
        self.assertEqual(self.toy.x_position, 1)
        self.assertEqual(self.toy.y_position, 2)
        self.assertEqual(self.toy.direction, 'NORTH')

        self.toy.move(self.table)
        self.assertEqual(self.toy.x_position, 1)
        self.assertEqual(self.toy.y_position, 3)
        self.assertEqual(self.toy.direction, 'NORTH')

        self.toy.move(self.table)
        self.assertEqual(self.toy.x_position, 1)
        self.assertEqual(self.toy.y_position, 4)
        self.assertNotEqual(self.toy.direction, 'EAST')

        self.toy.move(self.table)
        self.assertEqual(self.toy.x_position, 1)
        self.assertEqual(self.toy.y_position, 5)
        self.assertEqual(self.toy.direction, 'NORTH')

        self.toy.move(self.table)
        self.assertEqual(self.toy.x_position, 1)
        self.assertEqual(self.toy.y_position, 5)
        self.assertEqual(self.toy.direction, 'NORTH')

    def test_toy_left(self):

        self.toy.place(1, 1, 'NORTH', self.table)

        self.toy.left()
        self.assertEqual(self.toy.x_position, 1)
        self.assertEqual(self.toy.y_position, 1)
        self.assertEqual(self.toy.direction, 'WEST')

        self.toy.left()
        self.assertEqual(self.toy.x_position, 1)
        self.assertEqual(self.toy.y_position, 1)
        self.assertEqual(self.toy.direction, 'SOUTH')

        self.toy.left()
        self.assertEqual(self.toy.x_position, 1)
        self.assertNotEqual(self.toy.y_position, 2)
        self.assertNotEqual(self.toy.direction, 'SOUTH')

    def test_toy_right(self):

        self.toy.place(1, 1, 'NORTH', self.table)

        self.toy.right()
        self.assertEqual(self.toy.x_position, 1)
        self.assertEqual(self.toy.y_position, 1)
        self.assertEqual(self.toy.direction, 'EAST')

        self.toy.right()
        self.assertEqual(self.toy.x_position, 1)
        self.assertEqual(self.toy.y_position, 1)
        self.assertEqual(self.toy.direction, 'SOUTH')

        self.toy.right()
        self.assertEqual(self.toy.x_position, 1)
        self.assertNotEqual(self.toy.y_position, 2)
        self.assertNotEqual(self.toy.direction, 'SOUTH')

if __name__ == '__main__':

    unittest.main()
