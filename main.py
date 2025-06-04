import os

import keyboard

from app import board
from app import card
from app import helpers

deck = []
for i in ["kier", "karo", "pik", "trefl"]:
    for j in ['a ','2 ','3 ','4 ','5 ','6 ','7 ','8 ','9 ','10', 'j ', 'q ', "k "]:
        deck.append(card.Card(i, j))
if __name__ == '__main__':
    def up():
        os.system("cls")
        gboard.up()
        gboard.print_self()
        print("up")
 


    def down():
        os.system("cls")
        gboard.down()
        gboard.print_self()
        print("down")


    def left():
        os.system("cls")
        gboard.left()
        gboard.print_self()
        print("left")


    def right():
        os.system("cls")
        gboard.right()
        gboard.print_self()
        print("right")

    def space():
        os.system("cls")
        gboard.space()
        gboard.print_self()
        print("space")

    helpers.shuffle(deck)
    gboard = board.Board(deck)
    gboard.print_self()
    running = True
    keyboard.add_hotkey("w", up)
    keyboard.add_hotkey("s", down)
    keyboard.add_hotkey("a", left)
    keyboard.add_hotkey("d", right)
    keyboard.add_hotkey("space", space)
    keyboard.wait("esc")