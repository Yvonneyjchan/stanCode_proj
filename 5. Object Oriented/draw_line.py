"""
File: draw_line.py
Name: Yvonne Chan
-------------------------
This file uses the campy module to
draw lines which starts from odd click and ends to even click.
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

# This constant controls the size of the hole.
SIZE = 10

window = GWindow()

is_start = 0   # 判斷起點為奇數點擊
X = 0
Y = 0


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw_line)


def draw_line(event):
    global is_start
    global X
    global Y

    if is_start == 0:
        hole = GOval(SIZE, SIZE, x=event.x-SIZE/2, y=event.y-SIZE/2)
        window.add(hole)

        X = event.x
        Y = event.y

        is_start += 1

    else:
        maybe_obj = window.get_object_at(X, Y)
        window.remove(maybe_obj)

        line = GLine(X, Y, event.x, event.y)
        window.add(line, X, Y)

        X = 0
        Y = 0

        is_start -= 1


if __name__ == "__main__":
    main()
