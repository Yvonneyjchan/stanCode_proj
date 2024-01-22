"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, x=(window_width-paddle_width)/2, y=window_height-paddle_offset-paddle_height)

        self.window_height = window_height
        self.paddle_offset = paddle_offset
        self.paddle_height = paddle_height

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.window.add(self.ball, x=(window_width-ball_radius)/2, y=(window_height-ball_radius)/2)

        self.original_x = self.ball.x
        self.original_y = self.ball.y

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # Initialize our mouse listeners
        onmousemoved(self.paddle_move)

        onmouseclicked(self.start)
        self.game_start = False

        # Draw bricks
        for i in range(brick_rows):
            for j in range(brick_cols):
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                self.brick.fill_color = 'gold'
                self.brick.color = 'gold'
                self.window.add(self.brick,
                                x=j*(brick_width+brick_spacing), y=brick_offset+i*(brick_height+brick_spacing))

        self.brick_rows = brick_rows
        self.brick_cols = brick_cols
        self.brick_remove = 0

        # Default object x and y
        self.obj_x = 0
        self.obj_y = 0

    def paddle_move(self, mouse):
        """
        Moves paddle by the change in mouse x
        and keeps paddle the same y.
        """
        if mouse.x + (self.paddle.width/2) > self.window.width:
            self.paddle.x = self.window.width - self.paddle.width
        elif mouse.x - (self.paddle.width / 2) <= 0:
            self.paddle.x = 0
        else:
            self.paddle.x = mouse.x - (self.paddle.x / 2)
            self.paddle.y = self.window_height - self.paddle_offset - self.paddle_height

    def start(self, _):
        self.game_start = True
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx
        self.__dy = INITIAL_Y_SPEED

    # get ball velocity
    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy

    def set_dx(self):
        self.__dx = -self.__dx

    def set_dy(self):
        self.__dy = -self.__dy

    def collisions(self):
        # wall collision
        if self.ball.x <= 0 or self.ball.x + self.ball.width >= self.window.width:
            self.__dx = -self.__dx
        if self.ball.y <= 0:
            self.__dy = -self.__dy

        for i in range(2):
            for j in range(2):
                obj = self.window.get_object_at(self.ball.x + j*self.ball.width, self.ball.y + i*self.ball.height)

                if obj:
                    if obj == self.paddle:  # 板子 → 球反彈
                        if self.__dy > 0:
                            if self.__dx > 0:
                                if self.ball.x + self.ball.width <= self.paddle.x + self.paddle.width/2:
                                    self.__dx = -self.__dx
                            self.__dy = -self.__dy
                    else:  # 磚塊 → 球反彈&移除磚塊
                        if obj.width == BRICK_WIDTH:
                            self.obj_x = obj.x
                            self.obj_y = obj.y
                            self.__dy = -self.__dy
                            self.brick_remove += 1
                            self.window.remove(obj)
                    break
