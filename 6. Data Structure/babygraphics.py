"""
File: babygraphics.py
Name: Yvonne Chan
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000
Y_GAP = (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) / MAX_RANK  # y每個rank高度多少


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    dis = (width - GRAPH_MARGIN_SIZE*2) // len(YEARS)  # 兩線的間距
    x_coordinate = GRAPH_MARGIN_SIZE + dis * year_index  # index == 0 -> GRAPH_MARGIN_SIZE (初始的X座標)
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #

    # 上面的橫線
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)
    # 下面的橫線
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE)

    # 直線
    for i in range(len(YEARS)):  # 重複YEARS的index個數次
        x_coordinate = get_x_coordinate(CANVAS_WIDTH, i)
        canvas.create_line(x_coordinate, 0, x_coordinate, CANVAS_HEIGHT)
        canvas.create_text(x_coordinate + TEXT_DX, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, text=YEARS[i], anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # ----- Write your code below this line ----- #
    for lookup_name in lookup_names:
        for i in range(len(YEARS)):
            color = COLORS[lookup_names.index(lookup_name) % len(COLORS)]  # 取餘數選擇使用的顏色順序

            if i == 0:  # 線頭
                x_coordinate0 = get_x_coordinate(CANVAS_WIDTH, 0)

                if str(YEARS[i]) in name_data[lookup_name]:
                    y0 = GRAPH_MARGIN_SIZE + Y_GAP * int(name_data[lookup_name][str(YEARS[i])])
                    label = lookup_name + '' + name_data[lookup_name][str(YEARS[i])]
                    canvas.create_text(x_coordinate0, y0, text=label, anchor=tkinter.SW, fill=color)

                else:  # 超過1000
                    y0 = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                    label = lookup_name + '' + '*'
                    canvas.create_text(x_coordinate0, y0, text=label, anchor=tkinter.SW, fill=color)
            else:  # 線尾
                x_coordinate1 = get_x_coordinate(CANVAS_WIDTH, i)

                if str(YEARS[i]) in name_data[lookup_name]:
                    y1 = GRAPH_MARGIN_SIZE + Y_GAP * int(name_data[lookup_name][str(YEARS[i])])
                    label = lookup_name + '' + name_data[lookup_name][str(YEARS[i])]
                    canvas.create_text(x_coordinate1, y1, text=label, anchor=tkinter.SW, fill=color)

                else:  # 超過1000
                    y1 = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                    label = lookup_name + '' + '*'
                    canvas.create_text(x_coordinate1, y1, text=label, anchor=tkinter.SW, fill=color)

                # 線頭接線尾
                canvas.create_line(x_coordinate0, y0, x_coordinate1, y1, fill=color, width=LINE_WIDTH)

                # 線尾更新成下一個線頭
                x_coordinate0 = x_coordinate1
                y0 = y1

                # main() code is provided, feel free to read through it but DO NOT MODIFY


def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
