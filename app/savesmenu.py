from colorama import Fore # ej co jagby zrobic taki algorytm sortujący ktory daje liczby na postą liste ale z miejscami a potem ją po prostu splaszczyć tak ze [1,2,3,4,5,6,7,3,7,3,,5,31,34,513,4531,45,13,45,1,34,5,13,45,2,452,45,] n długa lista gdzie n to największa liczba chociaz moze nie...
class Saves:
    def __init__(self,lol):
        self.cursor = 0
        self.menu = True
        self.file = lol
    def print_self(self):
        file0, file1, file2 = ["[EMPTY]        ", "XXX"],["[EMPTY]        ", "XXX"],["[EMTPY]        ", "XXX"]
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
        print("|     "+file0[0]+"  "+file0[1]+" moves   |")
        print("|_______________________________|")
        print(Fore.GREEN, end="")
        if self.cursor == 1:
            print(Fore.YELLOW, end="")
        print("_________________________________")
        print("|     "+file1[0]+"  "+file1[1]+" moves   |")
        print("|_______________________________|")
        print(Fore.GREEN, end="")
        if self.cursor == 2:
            print(Fore.YELLOW, end="")
        print("_________________________________")
        print("|     "+file2[0]+"  "+file2[1]+" moves   |")
        print("|_______________________________|")
        print(Fore.GREEN, end="")
        if self.cursor == 3:
            print(Fore.YELLOW, end="")
        print("   OPEN", end="")
        print(Fore.GREEN, end="")
        if self.cursor == 4:
            print(Fore.YELLOW, end="")
        print("ERASE",end="")
        print(Fore.LIGHTBLACK_EX,end="")
        if self.cursor == 5:
            print(Fore.RED, end="")
        print("SETTINGS   ")
    def delete(self):
        pass

    def up(self):
        if 4 > self.cursor > 0:
            self.cursor -=1
        else:
            self.cursor = 2
    def down(self):
        if 0 <= self.cursor < 2:
            self.cursor += 1
        else:
            self.cursor = 0
    def space(self):
        if self.cursor == 0:
            self.file="app/file0.txt"
            self.cursor=3
        elif self.cursor == 1:
            self.file="app/file1.txt"
            self.cursor = 3
        elif self.cursor == 2:
            self.file="app/file2.txt"
            self.cursor = 3
        elif self.cursor == 3:
            self.menu = False
        elif self.cursor == 4:
            self.delete()
        elif self.cursor == 5:
            pass
    def left(self):
        if 3 <= self.cursor < 6:
            self.cursor -= 1
    def right(self):
        if 3 < self.cursor <= 6:
            self.cursor += 1
