"""
File: bouncing_ball.py
Name: Yvonne Chan
-------------------------
This file uses the campy module to
simulates a bouncing ball.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

window = GWindow(800, 500, title='bouncing_ball.py')

time = 0  # 重複幾次
is_start = False # 開關
ball = GOval(SIZE, SIZE)
vy = 1


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    global time, is_start, vy

    ball.filled = True
    window.add(ball, START_X, START_Y)
    onmouseclicked(bouncing)

    while True:
        if is_start:
            if time < 3:
                while True:
                    ball.move(VX, vy)
                    vy += GRAVITY

                    if ball.y + ball.height >= window.height:
                        vy = -vy * REDUCE  # 反彈
                    if ball.x + ball.width >= window.width:
                        # 回到原點
                        ball.x = START_X
                        ball.y = START_Y
                        window.add(ball)

                        is_start = False
                        break
                    pause(DELAY)
                time += 1
        pause(DELAY)


def bouncing(event):
    # 開關開始彈跳
    global is_start
    is_start = True


if __name__ == "__main__":
    main()
