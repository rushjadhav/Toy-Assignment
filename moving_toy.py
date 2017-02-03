"""
Application for simulation of a toy robot moving on a square tabletop
"""

TABLE_LENGTH = 5
TABLE_WIDTH = 5
CORNER = (0, 0)
DIRECTIONS = ['EAST', 'NORTH', 'WEST', 'SOUTH']

class Table():

    """
    Class Representing a table on which toy can move.
    """

    def __init__(self, length=None, width=None):

        self.length = length
        self.width = width
        self.corner = CORNER

    def is_point_on_table(self, x_position, y_position):

        """
        Checks weather given cordinates will be valid or not
        """

        return (self.corner[0] <= x_position <= self.length) and (self.width >= y_position >= self.corner[1])

    def __str__(self):

        return "Table : %s * %s" %(self.length, self.width)

class Toy():

    """
    Class Representing a toy.
    """

    def __init__(self, x_position=None, y_position=None, direction=None):

        self.x_position = x_position
        self.y_position = y_position
        self.direction = direction

    def is_placed(self):

        """
        Checks weather toy is placed on table or not
        """

        return self.x_position != None and self.y_position != None and self.direction != None

    def place(self, x_position, y_position, direction, tbl_obj):

        """
        Method to place the toy on table
        """

        if tbl_obj.is_point_on_table(x_position, y_position) and direction in DIRECTIONS:

            self.x_position = x_position
            self.y_position = y_position
            self.direction = direction
        else:
            print "Can not place toy in this position. Please enter another position"

    def move(self, tbl_obj, step=1):

        """
        Will move toy in current direction with given number of steps
        """

        if self.direction == 'EAST':
            new_x_position = self.x_position + step
            new_y_position = self.y_position

        if self.direction == 'WEST':
            new_x_position = self.x_position - step
            new_y_position = self.y_position

        if self.direction == 'SOUTH':
            new_x_position = self.x_position
            new_y_position = self.y_position - step

        if self.direction == 'NORTH':
            new_x_position = self.x_position
            new_y_position = self.y_position + step

        if tbl_obj.is_point_on_table(new_x_position, new_y_position):
            self.x_position = new_x_position
            self.y_position = new_y_position
        else:
            print "This move is not allowed..."

    def left(self):

        """
        Method to change direction to left
        """

        try:
            self.direction = DIRECTIONS[DIRECTIONS.index(self.direction) + 1]
        except IndexError:
            self.direction = DIRECTIONS[0]

    def right(self):

        """
        Method to change direction to right
        """

        try:
            self.direction = DIRECTIONS[DIRECTIONS.index(self.direction) - 1]
        except IndexError:
            self.direction = DIRECTIONS[3]


    def report(self):

        """
        Displays current position of toy on table
        """

        print "%s, %s, %s" %(self.x_position, self.y_position, self.direction)

    def __str__(self):

        return "TOY AT POSITION - (%s, %s) " %(self.x_position, self.y_position)

def show_place_message():

    """
    Prints the validation message on console
    """

    print "PLACE command must be used before this"

def show_invalid_command_error():

    """
    Prints the validation message on console
    """

    print """Please enter valid command. Available commands are
                1. PLACE X,Y,F
                2. MOVE
                3. LEFT
                4. RIGHT
                5. REPORT"""

def perform_command(tbl, toy, user_input):
    """
    Finds particular command from user input and execute it
    """

    if cmd == 'PLACE':
        try:
            args = user_input[1]
            args = args.split(',')
            toy.place(int(args[0]), int(args[1]), args[2], tbl)
        except IndexError:
            print "PLACE COMMAND USAGE --> PLACE x,y,d"

    elif cmd == 'LEFT':
        if toy.is_placed():
            toy.left()
        else:
            show_place_message()

    elif cmd == 'RIGHT':
        if toy.is_placed():
            toy.right()
        else:
            show_place_message()

    elif cmd == 'REPORT':
        if toy.is_placed():
            toy.report()
        else:
            show_place_message()

    elif cmd == 'MOVE':
        if toy.is_placed():
            toy.move(tbl)
        else:
            show_place_message()
    else:
        show_invalid_command_error()

if __name__ == '__main__':

    tbl = Table(TABLE_LENGTH, TABLE_WIDTH)
    toy = Toy()
    while True:
        user_input = raw_input("Waiting for command:")
        user_input = user_input.split(' ', 1)
        if user_input:
            cmd = user_input[0]
            perform_command(tbl, toy, user_input)
        else:
            show_invalid_command_error()
