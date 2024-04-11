from window import Window
from maze import Maze

if __name__ == "__main__":
    rows = 12
    cols = 16
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / cols
    cell_size_y = (screen_y - 2 * margin) / rows
    win = Window(screen_x, screen_y)

    win._Window__canvas.create_rectangle(margin, margin, screen_x - margin, screen_y - margin, fill="white", outline = 'white') # trick to enter provate

    maze = Maze(margin, margin, rows, cols, cell_size_x, cell_size_y, win)
    maze.solve()

    win.wait_for_close()