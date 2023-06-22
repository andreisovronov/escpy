import curses
import sys

def main(stdscr):
    while True:
        key = stdscr.getch()
        if key == 27:  # 27 - код клавиши ESC
            print('\nОстановлено пользователем.')
            sys.exit()

        if key == ord('\n'):
            stdscr.addstr('\n')
        else:
            stdscr.addstr('*')

if __name__ == "__main__":
    curses.wrapper(main)
