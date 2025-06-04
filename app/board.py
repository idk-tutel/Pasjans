from colorama import Fore, Style # ej co jagby zrobic taki algorytm sortujący ktory daje liczby na postą liste ale z miejscami a potem ją po prostu splaszczyć tak ze [1,2,3,4,5,6,7,3,7,3,,5,31,34,513,4531,45,13,45,1,34,5,13,45,2,452,45,] n długa lista gdzie n to największa liczba chociaz moze nie...
class Board:
    def __init__(self, odeck):
        deck = odeck
        self.finish_set = [0,0,0,0]
        self.order = [' ','a','2','3','4','5','6','7','8','9','10', 'j', 'q', "k"]
        self.main_set = [[],[],[],[],[],[],[]]
        for i in range(7):
            for j in range(i+1):
                #if j != i:deck[0].inv = True
                self.main_set[i].append(deck[0])
                deck.pop(0)
        self.draw_set = deck
        self.cursor = 1
        self.selectednum = 0
        self.selectedrow = 1

    def draw_cycle(self):
        self.draw_set.append(self.draw_set[0])
        self.draw_set.pop(0)


    def print_self(self):
        self.print_self_top()
        self.print_self_bottom()


    def print_self_top(self): #abominacja #1
        print(Style.RESET_ALL+" ______   ", end="")
        if self.draw_set[0].red:
            print(Fore.RED, end="")
        print(" _____           "+Fore.RED+" _____    _____  "+Style.RESET_ALL+"  _____    _____ ")
        print("/  ●  \\\\", end="")
        if len(self.draw_set) > 0:
            if self.draw_set[0].red:
                print(Fore.RED, end="")
            if self.selectedrow == -2:
                print(Fore.YELLOW, end="")
            print("  / "+self.draw_set[0].printcard()+" \          ",end="")
        else:
            print("  / nic \          ",end="")
        print(+Fore.RED+"/  "+self.order[self.finish_set[0]]+"  \  /  "+self.order[self.finish_set[1]]+"  \ "+Style.RESET_ALL+" /  "+self.order[self.finish_set[2]]+"  \  /  "+self.order[self.finish_set[3]]+"  \ ")
        for i in range(2):
            print("|     ||", end="")
            if self.draw_set[0].red:
                print(Fore.RED, end="")
            print("  |     |          " + Fore.RED + "|     |  |     | " + Style.RESET_ALL + " |     |  |     |")
        print("\_____//", end="")
        if self.draw_set[0].red:
            print(Fore.RED, end="")
        print("  \_____/          " + Fore.RED + "\_____/  \_____/ " + Style.RESET_ALL + " \_____/  \_____/")
        if self.cursor < 0:
            if self.cursor == -1:
                print(Fore.YELLOW+"========\n")
            elif self.cursor == -2:
                print(Fore.YELLOW+"          =======\n")
            else:
                print("                           ", end="")
                for i in range(-1*self.cursor-3):
                    print("         ", end="")
                print(Fore.YELLOW+"=======\n")
        else: print("\n")


    def print_self_bottom(self): #abominacja #2 nawet nie proboj sie rozczytać
        for i in range(7):
            if len(self.main_set[i]) == 0:
                print("         ", end="")
                continue
            elif self.main_set[i][0].inv or self.main_set[i][0].red == False:
                print(Style.RESET_ALL + " _____   ", end="")
                continue
            else:
                print(Fore.RED + " _____   ", end="")
        print("\n", end="")
        for m in range(max(len(self.main_set[0]),len(self.main_set[1]),len(self.main_set[2]),len(self.main_set[3]),len(self.main_set[4]),len(self.main_set[5]),len(self.main_set[6]))+2):
            for i in range(7):
                if len(self.main_set[i]) == m - 1 and self.cursor == i+1:
                    print(Fore.YELLOW + "=======  ", end="")
                    continue
                if len(self.main_set[i]) <= m - 1:
                    print("         ", end="")
                    continue
                if len(self.main_set[i]) == m:
                    if self.main_set[i][m-1].red:
                        print(Fore.RED + "|     |  ", end="")
                        continue
                    else:
                        print(Style.RESET_ALL + "|     |  ", end="")
                elif self.main_set[i][m].inv:
                    print(Style.RESET_ALL + "/  ●  \  ", end="")
                    continue
                elif len(self.main_set[i]) - m <= self.selectednum and i == self.selectedrow-1:
                    print(Fore.YELLOW + "/ " + self.main_set[i][m].printcard() + " \  ", end="")
                    continue
                elif self.main_set[i][m].red:
                    print(Fore.RED + "/ "+self.main_set[i][m].printcard()+" \  ", end="")
                    continue
                else:
                    print(Style.RESET_ALL + "/ "+self.main_set[i][m].printcard()+" \  ", end="")
            print("\n", end="")
            for i in range(7):

                if len(self.main_set[i]) <= m - 1:
                    print("         ", end="")
                    continue
                if len(self.main_set[i]) == m:
                    if self.main_set[i][m-1].red:
                        print(Fore.RED + "\_____/  ", end="")
                        continue
                    else:
                        print(Style.RESET_ALL + "\_____/  ", end="")
                elif self.main_set[i][m].inv or self.main_set[i][m].red == False:
                    if len(self.main_set[i]) <= m+1:
                        print(Style.RESET_ALL + "|     |  ", end="")
                        continue
                    else:
                        print(Style.RESET_ALL + "|_____|  ", end="")
                        continue
                else:
                    if len(self.main_set[i]) <= m+1:#[1,2,3] len to 3 a m + 1 to 4
                        print(Fore.RED + "|     |  ", end="")
                        continue
                    else:
                        print(Fore.RED + "|_____|  ", end="")
                        continue
            print("\n", end="")
    def selectcard(self, card):
        pass
    def up(self):
        if self.cursor == -1:
            self.draw_cycle()
        elif self.cursor == -2:
            self.selectedrow = -2
            self.selectednum = 1
        elif self.cursor == self.selectedrow and self.cursor > 0:
            if len(self.main_set[self.cursor-1]) == self.selectednum:
                self.selectednum = 0
            else:self.selectednum += 1
        else:
            self.selectedrow = self.cursor
            self.selectednum = 1
        print(str(self.selectednum) + " "+ str(self.selectedrow))


    def down(self):
        dict1 = {
            1:-1,2:-2,3:-2,4:-3,5:-4,6:-5,7:-6}
        dict2 = {
            -1:1,-2:2,-3:4,-4:5,-5:6,-6:7}
        if self.cursor < 0:
            self.cursor = dict2.get(self.cursor)
        else:
            self.cursor = dict1.get(self.cursor)


    def left(self):
        if self.cursor < 0 and self.cursor + 1 != 0:
            self.cursor += 1
        elif self.cursor > 0 and self.cursor - 1 != 0:
            self.cursor -= 1


    def right(self):
        if self.cursor > 0 and self.cursor + 1 != 8:
            self.cursor += 1
        elif self.cursor < 0 and self.cursor - 1 != -7:
            self.cursor -= 1

    def space(self):
        if self.cursor == -1:
            self.draw_cycle()
        elif self.cursor > 0:
            for i in range(self.selectednum):
                if self.selectedrow == -2:
                    self.main_set[self.cursor-1].append(self.draw_set[0])
                    self.draw_set.pop(0)












