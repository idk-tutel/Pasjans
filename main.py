import os

import keyboard

from app import board
from app import card
from app import helpers
from app import savesmenu

menu = True

if __name__ == '__main__':
    def savesmenuf():
        def upf():
            os.system("cls")
            saves.up()
            saves.print_self()

        def downf():
            os.system("cls")
            saves.down()
            saves.print_self()

        def leftf():
            os.system("cls")
            saves.left()
            saves.print_self()

        def rightf():
            os.system("cls")
            saves.right()
            saves.print_self()
        def spacef():
            saves.space()
            os.system("cls")
            saves.print_self()

        saves = savesmenu.Saves()
        os.system("cls")
        saves.print_self()
        keyboard.add_hotkey("w", upf)
        keyboard.add_hotkey("s", downf)
        keyboard.add_hotkey("a", leftf)
        keyboard.add_hotkey("d", rightf)
        keyboard.add_hotkey("up", upf)
        keyboard.add_hotkey("down", downf)
        keyboard.add_hotkey("left", leftf)
        keyboard.add_hotkey("right", rightf)
        menu = True
        while menu:
            keyboard.wait("space")
            spacef()
            menu = saves.menu
        keyboard.clear_hotkey(upf)
        keyboard.clear_hotkey(downf)
        keyboard.clear_hotkey(leftf)
        keyboard.clear_hotkey(rightf)
        return saves.file
    savefile = savesmenuf()
    def up():
        os.system("cls")
        gboard.up()
        gboard.print_self()
        open(savefile, "w").write(gboard.save())
        #for i in range(10): keyboard.press("scroll up")


    def down():
        os.system("cls")
        gboard.down()
        gboard.print_self()
        open(savefile, "w").write(gboard.save())

    def left():
        os.system("cls")
        gboard.left()
        gboard.print_self()
        open(savefile, "w").write(gboard.save())

    def right():
        os.system("cls")
        gboard.right()
        gboard.print_self()
        open(savefile, "w").write(gboard.save())

    def space():
        gboard.space()
        os.system("cls")
        gboard.print_self()
        open(savefile, "w").write(gboard.save())

    def reset():
        open(savefile, "w").write("")
        newdeck = []
        for i in ["kier", "karo", "pik", "trefl"]:
            for j in ['A ', '2 ', '3 ', '4 ', '5 ', '6 ', '7 ', '8 ', '9 ', '10', 'J ', 'Q ', "K "]:
                newdeck.append(card.Card(i, j))
        helpers.shuffle(newdeck)
        gboard.__init__(newdeck, gboard.cursor)
        os.system("cls")
        gboard.print_self()
        print("RESET")
        open(savefile, "w").write(gboard.save())

    def load():
        if len(open(savefile).read()) != 0:
            gboard.load(open(savefile).read())
            os.system("cls")
            gboard.print_self()
            print("load")
        else:
            reset()



    deck = []
    for i in ["kier", "karo", "pik", "trefl"]:
        for j in ['A ', '2 ', '3 ', '4 ', '5 ', '6 ', '7 ', '8 ', '9 ', '10', 'J ', 'Q ', "K "]:
            deck.append(card.Card(i, j))
    helpers.shuffle(deck)
    gboard = board.Board(deck)
    if len(open(savefile).read()) != 0:
        gboard.load(open(savefile).read())
    os.system("cls")
    gboard.print_self()
    keyboard.add_hotkey("w", down)
    keyboard.add_hotkey("s", down)
    keyboard.add_hotkey("a", left)
    keyboard.add_hotkey("d", right)
    keyboard.add_hotkey("up", down)
    keyboard.add_hotkey("down", down)
    keyboard.add_hotkey("left", left)
    keyboard.add_hotkey("right", right)
    keyboard.add_hotkey("r", reset)
    keyboard.add_hotkey("l", load)
    keyboard.add_hotkey("space", space)
    keyboard.add_hotkey("x", space)
    keyboard.add_hotkey("z", up)
    keyboard.add_hotkey("shift", up)
    keyboard.wait("esc")