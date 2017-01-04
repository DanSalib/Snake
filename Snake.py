from curses import wrapper
import time
from collections import namedtuple
'''
def main(stdscr):
    stdscr.clear()


    y = 2
    x = 10
    stdscr.addstr(y, x, 'Hello world!')
    stdscr.refresh()

    for i in range(10):
        got = stdscr.getkey()

        print(got)
        '''


if __name__ == '__main__':
    wrapper(main)
    # Wrapper does the setup and then calls main
    # after main is done, it puts back everything as it was


class GameLost(Exception):
    pass

class Snake:

    def __init__(self, posTup, posSet, LENGTH, WIDTH, cdir):
        self.posTup = namedtuple('Pos', ['x', 'y'])
        self.posSet = [Pos(x = 3, y = 3)]
        self.cdir = 'e'
        LENGTH = 12
        WIDTH = 8

    def turn_north(self):
        self.posSet.insert(0, Pos(x, y++)
        del self.posSet[len(posSet-1)]
        cdir = 'n'
        return cdir
        
    def turn_south(self):
        self.posSet.insert(0, Pos(x, y--)
        del self.posSet[len(posSet-1)]
        cdir = 's'
        return cdir
        
    def turn_east(self):
        self.posSet.insert(0, Pos(x++, y)
        del self.posSet[len(posSet-1)]
        cdir = 'e'
        return cdir
                           
    def turn_west(self):
        self.posSet.insert(0, Pos(x--, y)
        del self.posSet[len(posSet-1)]
        cdir = 'w'
        return cdir

    def grow(self):
        growx = self.posSet[0, Pos(x)]
        growy = self.posSet[0, Pos(y)]
        if(self.posSet[len(posSet-1), Pos(x = growx + 1, y)] or self.posSet[len(posSet-1), Pos(x, y = growy + 1)])
            self.posSet.append(Pos[x = growx, y = growy])
    

    def move_forward(self, cdir):
        if(self.cdir == 'e')
            return self.turn_east()
        if(self.cdir == 'w')
            return self.turn_west()
        if(self.cdir == 'n')
            return self.turn_north()
        if(self.cdir == 's')
            return self.turn_south()

    def spawnApple(self):
        applex = randint(0,12)
        appley = randint(0,8)
        if(posSet[0] == Pos(applex, appley))
            return true
        else
            return false
        
                           
        raise GameLost('Looser!!')
