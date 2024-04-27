from src.game import game
from screeninfo import get_monitors
from src.constants import WIDTH, HEIGHT

if __name__ == '__main__':
    monitor = get_monitors()[0]

    WIDTH = int(monitor.width * 0.625)
    HEIGHT = int(monitor.height * 0.625)

    gm = game()
    print("Good buy!")


