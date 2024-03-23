import turtle

"""hash of the last commit: 529544858e35c41eaa19e07b0d302d1f6c0b70cc"""


BOARD_COLOR = "black"
CIRCLE_COLOR = "red"
CROSS_COLOR = "blue"
GAME_OVER = False


class Figure:
    def __init__(self, color):
        self.__position = (0, 0)
        self.__visible = False
        self.__color = color

    def set_position(self, position: tuple):
        self.__position = position

    def get_position(self):
        return self.__position

    def draw(self, color):
        raise Exception("Don't call this method")

    def show(self):
        if not self.__visible:
            self.draw(self.__color)
            self.__visible = True

    def hide(self):
        if self.__visible:
            self.draw(turtle.bgcolor())
            self.__visible = False


class Board(Figure):
    def draw(self, color):
        turtle.color(color)
        turtle.speed(10)

        turtle.penup()
        turtle.width(2)
        turtle.goto(-75, -225)
        turtle.pendown()
        turtle.left(90)
        turtle.forward(450)
        turtle.penup()

        turtle.goto(75, -225)
        turtle.pendown()
        turtle.forward(450)
        turtle.penup()

        turtle.goto(-225, -75)
        turtle.setheading(0)
        turtle.pendown()
        turtle.forward(450)
        turtle.penup()

        turtle.goto(-225, 75)
        turtle.setheading(0)
        turtle.pendown()
        turtle.forward(450)
        turtle.penup()


class Circle(Figure):
    def draw(self, color):
        turtle.color(color)
        turtle.speed(0)
        turtle.width(4)

        pos = self.get_position()
        turtle.penup()
        turtle.goto(pos[0], pos[1] - 50)
        turtle.setheading(0)
        turtle.pendown()
        turtle.circle(50, steps=150)


class Cross(Figure):
    def draw(self, color):
        turtle.color(color)
        turtle.speed(0)
        turtle.width(4)

        pos = self.get_position()
        turtle.penup()

        turtle.goto(pos[0] - 50, pos[1] - 50)
        turtle.pendown()
        turtle.setheading(45)
        turtle.goto(pos[0] + 50, pos[1] + 50)
        turtle.penup()

        turtle.goto(pos[0] - 50, pos[1] + 50)
        turtle.pendown()
        turtle.setheading(-45)
        turtle.goto(pos[0] + 50, pos[1] - 50)
        turtle.penup()


def handle_click(x, y):
    global turn
    global table
    if -225 <= x <= 225 and -225 <= y <= 225:
        print(detect_center(x, y))
        coordinates = detect_center(x, y)
        table_coord = coordinates[1]

        if turn == 'x':
            if table[table_coord[0]][table_coord[1]] == '-':
                cross = Cross(CROSS_COLOR)
                cross.set_position(detect_center(x, y)[0])
                cross.show()
                table[table_coord[0]][table_coord[1]] = 'x'
                turn = 'o'
            else:
                print('The field is not empty!')
        else:
            if table[table_coord[0]][table_coord[1]] == '-':
                circle = Circle(CIRCLE_COLOR)
                circle.set_position(detect_center(x, y)[0])
                circle.show()
                table[table_coord[0]][table_coord[1]] = 'o'
                turn = 'x'
            else:
                print('The field is not empty!')

    if check_for_win(table):
        screen.clear()
        if turn == 'x':
            turn = 'o'
        else:
            turn = 'x'
        turtle.write(f'{turn} is the winner!!!', align='center', font=('Arial', 15, 'normal'))
        turtle.hideturtle()
    else:
        print(table)


def detect_center(x, y):
    cx, cy = 0, 0
    ax, ay = 0, 0
    for i in range(3):
        if -225 + i * 150 <= x <= -75 + i * 150:
            cx, ax = ((-225 + i * 150) + (-75 + i * 150)) // 2, i
        if -225 + i * 150 <= y <= -75 + i * 150:
            cy, ay = ((-225 + i * 150) + (-75 + i * 150)) // 2, 2 - i
    return (cx, cy), (ax, ay)


def check_for_win(t):
    for i in range(3):
        if len(set(t[i])) == 1 and t[i][0] != '-':
            return True
    for i in range(3):
        row = [t[i][j] for j in range(3)]
        if len(set(row)) == 1 and row[0] != '-':
            return True
    for i in range(3):
        row = [t[i][i] for i in range(3)]
        if len(set(row)) == 1 and row[0] != '-':
            return True
        row = [t[i][2-i] for i in range(3)]
        if len(set(row)) == 1 and row[0] != '-':
            return True
    return False


if __name__ == '__main__':
    screen = turtle.Screen()
    turtle.hideturtle()
    board = Board(BOARD_COLOR)
    board.show()
    table = [['-' for _ in range(3)] for _ in range(3)]
    fig = int(input("Please, choose who will start, 1 for Cross, 2 for Circle: "))
    if fig == 1:
        print('Cross starts')
        turn = 'x'
        screen.onscreenclick(handle_click)
    else:
        print('Circle starts')
        turn = 'o'
        screen.onscreenclick(handle_click)
    turtle.mainloop()
