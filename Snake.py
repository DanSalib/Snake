from curses import wrapper
import time
from collections import namedtuple


Pos = namedtuple('Pos', ['x', 'y'])

class IllegalMove(Exception):
    pass
class GameLost(Exception):
    pass

class Snake:

    def __init__(self, LENGTH, WIDTH):
        self.posArr = [ Pos(x = 3, y = 3) ]
        self.cdir   = 'e'
        self.LENGTH = LENGTH
        self.WIDTH  = WIDTH
        
        self.grow_at = []

    def turn_north(self):
        if self.cdir == 's':
            raise IllegalMove("Can't move from south to north")
        else:
            self.cdir = 'n'

    def turn_south(self):
        if self.cdir == 'n':
            raise IllegalMove("Can't move from south to north")
        else:
            self.cdir = 's'         
        
    def turn_east(self):
        if self.cdir == 'w':
            raise IllegalMove("Can't move from west to east")
        else:
            self.cdir = 'e'
                           
    def turn_west(self):
        if self.cdir == 'e':
            raise IllegalMove("Can't move from east to west")
        else:
            self.cdir = 'w'

    def grow(self):
        self.grow_at.append[self.posArr[0]]
    

    def move_forward(self):
        '''
Move forward by one step.
Raises a GameLost exception if the snake coils on itself or if it hits the edge
    '''
        # Check for two things
        #   1. Did the snake hit itself
        #   2. Did the snake it one of the borders?
        
        # Use array.index
        head = self.posArr[0]
        if self.cdir == 'n':
            newPos = Pos(x = head.x, y = head.y - 1)
        if self.cdir == 's':
            newPos = Pos(x = head.x, y = head.y + 1)
        if self.cdir == 'e':
            newPos = Pos(x = head.x + 1, y = head.y)
        if self.cdir == 'w':
            newPos = Pos(x = head.x - 1, y = head.y)
        
        try:
            idx = self.posArr.index(newPos)
            
            raise GameLost('The snake hit itself')
        except ValueError:
            pass
        
        if newPos.x <= -1 or newPos.x >= self.WIDTH:
            raise GameLost('You hit the border')
        
        if newPos.y <= -1 or newPos.y >= self.LENGTH:
            raise GameLost('You hit the border')

        self.posArr.insert(0, newPos)
        
        if len(self.grow_at) > 0 and self.posArr[0] ==  self.grow_at[0]:
            self.grow_at.pop(0)
        else:
            self.posArr.pop()

    def draw(self, stdscr):
        ''' Draw the snake on stdscr '''

        # IMPLEMENT
    
        # USE
        for pos in self.posArr:
            stdscr.addstr(pos.y, pos.x, '*')

def randomApple(applex, appley):
    applex = randint(0, WIDTH)
    appley = randint(0, LENGTH)
    std.scr.addstr(appley, apple.x, '#')

def main(stdscr):   
    LENGTH = 8
    WIDTH = 12
    applex = 0
    appley = 0

    #randomApple(applex, appley)

    if(snake.posArr[0] == Pos(x = applex, y = appley)):
              snake.grow()
              randomApple(applex, appley)

    snake = Snake(LENGTH, WIDTH)

    while True:
        while True: #(stdscr.getkey() == or snake.posArr[0] != Pos(x=applex, y=appley)):
            try:
              snake.move_forward()
              #print and delay
              stdscr.clear()
              snake.draw(stdscr)
              stdscr.refresh()
              time.sleep(0.5)
            except ValueError or GameLost():
              break
            '''
        if(stdscr.getkey() == KEY_UP):
              snake.turn_north()
        elif(stdscr.getkey() == KEY_DOWN):
              snake.turn_south()
        elif(stdscr.getkey() == KEY_LEFT):
              snake.turn_west()
        elif(stdscr.getkey() == KEY_RIGHT):
              snake.turn_east()
        if(snake.posArr[0] == Pos(x = applex, y = appley)):
              snake.grow()
              randomApple(applex, appley)
              '''
        

if __name__ == '__main__':
   wrapper(main)
    # Wrapper does the setup and then calls main
    # after main is done, it puts back everything as it was

        

  
