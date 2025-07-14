from time import sleep

from colorama import \
    Fore  # ej co jagby zrobic taki algorytm sortujący ktory daje liczby na postą liste ale z miejscami a potem ją po prostu splaszczyć tak ze [1,2,3,4,5,6,7,3,7,3,,5,31,34,513,4531,45,13,45,1,34,5,13,45,2,452,45,] n długa lista gdzie n to największa liczba chociaz moze nie...


class Saves:
    def __init__(self):
        self.cursor = 0
        self.menu = True
        self.file = "app/file0.txt"
        self.screen = "main"
        self.name = ""
        self.keys = [['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
                      ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
                          ['z', 'x', 'c', 'v', 'b', 'n', 'm'],
                                ["DONE", "BACK"]]
        self.lens = [9, 8, 6, 1]
        self.debug = ""

    def print_self(self):
        if self.screen == "main":
            file0, file1, file2 = ["[EMPTY]     ", "XXX"], ["[EMPTY]     ", "XXX"], ["[EMTPY]     ", "XXX"]
            if len(open("app/file0.txt", "r").read()) != 0:
                file0 = open("app/file0.txt", "r").read().split("\n\n")[3].split(", ")
            if len(open("app/file1.txt", "r").read()) != 0:
                file1 = open("app/file1.txt", "r").read().split("\n\n")[3].split(", ")
            if len(open("app/file2.txt", "r").read()) != 0:
                file2 = open("app/file2.txt", "r").read().split("\n\n")[3].split(", ")
            print(Fore.GREEN, end="")
            if self.cursor == 0:
                print(Fore.YELLOW, end="")
            print("_________________________________")
            print("|     " + file0[0] + "  " + file0[1] + " moves  |")
            print("|_______________________________|")
            print(Fore.GREEN, end="")
            if self.cursor == 1:
                print(Fore.YELLOW, end="")
            print("_________________________________")
            print("|     " + file1[0] + "  " + file1[1] + " moves  |")
            print("|_______________________________|")
            print(Fore.GREEN, end="")
            if self.cursor == 2:
                print(Fore.YELLOW, end="")
            print("_________________________________")
            print("|     " + file2[0] + "  " + file2[1] + " moves  |")
            print("|_______________________________|")
            print(Fore.GREEN, end="")
            if self.cursor == 3:
                print(Fore.YELLOW, end="")
            print("   OPEN    ", end="")
            print(Fore.GREEN, end="")
            if self.cursor == 4:
                print(Fore.YELLOW, end="")
            print("ERASE    ", end="")
            print(Fore.LIGHTBLACK_EX, end="")
            if self.cursor == 5:
                print(Fore.RED, end="")
            print("SETTINGS    ")
        elif self.screen == "name":
            print("\n                       NEW SAVE FILE\n                         " + self.name + "\n\n", end="")
            for i in self.keys:
                print("       ", end = "")
                if i == ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']:
                    print("  ", end="")
                elif i == ['z', 'x', 'c', 'v', 'b', 'n', 'm']:
                    print("      ", end="")
                elif i == ["DONE", "BACK"]:
                    print("            ", end="")
                for j in i:
                    if j == "BACK":
                        print("         ", end="")
                    print(Fore.GREEN, end="")
                    if self.keys[self.cursor[0]][self.cursor[1]]==j:
                        print(Fore.YELLOW, end="")
                    print(j+"    ", end="")
                print("\n ")

        elif self.screen == "accept_name":
            print(Fore.GREEN+"\n                    DO YOU ACCEPT THIS NAME?\n")
            for i in range(20-len(self.name)):
                print(" ", end = "")
            print(Fore.CYAN+ self.name, end="\n\n\n")
            if self.cursor:
                print(Fore.YELLOW + "                     YES" + Fore.GREEN + "                NO")
            else:
                print(Fore.GREEN  + "                     YES" + Fore.YELLOW+ "                NO")

        elif self.screen == "settings":
            pass

        print(Fore.GREEN + "\n\nw, a, s, d or arrow keys to move\nspace to confirm\nto quit open a save file first, then press esc")
    def delete(self):
        open(self.file, "w").write("")
        self.name = ""

    def up(self):
        if self.screen == "main":
            if 4 > self.cursor > 0:
                self.cursor -=1
            else:
                self.cursor = 2
        elif self.screen == "name":

            if self.cursor[0] != 0:
                self.cursor[0] -= 1
            else: self.cursor = [3, 0]
    def down(self):
        if self.screen == "main":
            if 0 <= self.cursor < 2:
                self.cursor += 1
            else:
                self.cursor = 0
        elif self.screen == "name":
            if self.cursor[0] != 0:
                self.cursor[0] -= 1
            else:
                self.cursor = [3, 0]
    def space(self):
        if self.screen == "main":
            if self.cursor == 0:
                self.file="app/file0.txt"
                if len(open(self.file, "r").read()) != 0:
                    self.name = open(self.file, "r").read().split("\n\n")[3].split(", ")[0]
                else: self.name = ""
                self.cursor=3
            elif self.cursor == 1:
                self.file="app/file1.txt"
                if len(open(self.file, "r").read()) != 0:
                    self.name = open(self.file, "r").read().split("\n\n")[3].split(", ")[0]
                else: self.name = ""
                self.cursor = 3
            elif self.cursor == 2:
                self.file="app/file2.txt"
                if len(open(self.file, "r").read()) != 0:
                    self.name = open(self.file, "r").read().split("\n\n")[3].split(", ")[0]
                else: self.name = ""
                self.cursor = 3
            elif self.cursor == 3:
                if self.name=="":
                    self.screen = "name"
                    self.cursor = [0,0]
                else: self.menu = False
            elif self.cursor == 4:
                self.delete()
            elif self.cursor == 5:
                pass
        elif self.screen == "name":
            keys = [['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
                    ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
                    ['z', 'x', 'c', 'v', 'b', 'n', 'm'],
                    ["DONE", "BACK"]]
            if self.cursor[0] != 3:
                self.name += keys[self.cursor[0]][self.cursor[1]]
            elif self.cursor[1] == 0 and len(self.name) > 0:
                self.screen = "accept_name"
                self.cursor = True
        elif self.screen == "accept_name":
            if self.cursor:
                self.menu = False
            else:
                self.screen = "name"
                self.cursor = [3, 0]
    def left(self):
        if self.screen == "main":
            if 3 < self.cursor < 6:
                self.cursor -= 1
            else:
                self.cursor = 5
        elif self.screen == "name":
            if self.cursor[1] != 0:
                self.cursor[1] -= 1
            else:
                self.cursor[1] = self.lens[self.cursor[0]]
        elif self.screen == "accept_name":
            self.cursor = True
    def right(self):
        if self.screen == "main":
            if 3 <= self.cursor < 5:
                self.cursor += 1
            else:
                self.cursor = 3
        elif self.screen == "name":
            if self.cursor[1] != self.lens[self.cursor[0]]:
                self.cursor[1] += 1
            else:
                self.cursor[1] = 0
        elif self.screen == "accept_name":
            self.cursor = False


if __name__ == '__main__':
    import timeit
    import os
    saves = Saves()
    open("app/file1.txt", "w").write("")

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

    def right():
        return timeit.timeit("rightf()", "from __main__ import rightf", number=1)
    def left():
        return timeit.timeit("leftf()", "from __main__ import leftf", number=1)
    def up():
        return timeit.timeit("upf()", "from __main__ import upf", number=1)
    def down():
        return timeit.timeit("downf()", "from __main__ import downf", number=1)
    def space():
        return timeit.timeit("spacef()", "from __main__ import spacef", number=1)
    print(down())
    #sleep(0.5)
    print(space())
    #sleep(0.5)
    print(space())
    #sleep(0.5)
    lol = []
    for i in range(10):
        lol.append(right())
        sleep(0.1)
    print(lol)