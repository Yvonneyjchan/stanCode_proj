"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    lives = NUM_LIVES

    # Add the animation loop here!
    while True:
        if lives > 0:
            if graphics.game_start:
                while True:
                    dx = graphics.get_dx()
                    dy = graphics.get_dy()

                    # Win the game
                    if graphics.brick_remove == graphics.brick_rows * graphics.brick_cols:
                        break

                    graphics.ball.move(dx, dy)

                    graphics.collisions()

                    # Reset the game
                    reset = graphics.ball.y + graphics.ball.height > graphics.paddle.y + graphics.paddle.height
                    if reset:
                        graphics.ball.x = graphics.original_x
                        graphics.ball.y = graphics.original_y
                        graphics.window.add(graphics.ball)
                        graphics.game_start = False
                        lives -= 1
                        break
                    pause(FRAME_RATE)
        else:
            break
        pause(FRAME_RATE)


if __name__ == '__main__':
    main()
