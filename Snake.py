from curses import wrapper, curs_set, newwin
import time
from random import randrange

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
        self.grow_at.append(self.posArr[0])
    

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
        
        if newPos.x < 1 or newPos.x > self.WIDTH - 2:
            raise GameLost('You hit the border')
        
        if newPos.y < 1 or newPos.y >= self.LENGTH - 1:
            raise GameLost('You hit the border')

        self.posArr.insert(0, newPos)
        
        if len(self.grow_at) > 0 and self.posArr[-1] ==  self.grow_at[0]:
            self.grow_at.pop(0)
        else:
            self.posArr.pop()

    def draw(self, stdscr):
        ''' Draw the snake on stdscr '''

        # IMPLEMENT
    
        # USE
        for pos in self.posArr:
            stdscr.addstr(pos.y, pos.x, '*')

    def randomApple(self, LENGTH, WIDTH):
        applex = randrange(1, WIDTH-2)
        appley = randrange(1, LENGTH-2)
        for pos in self.posArr:
            while(applex == pos.x and appley == pos.y):
                applex = randrange(WIDTH)
                appley = randrange(LENGTH)
        return (applex, appley)
        
    def printApple(self, stdscr, applex, appley):
        stdscr.addstr(appley, applex, '#')
    

def main(stdscr):   
    LENGTH = 12
    WIDTH = 12
    applex = 3
    appley = 6
    app = True

    
    LEGNTH, WIDTH =  stdscr.getmaxyx()
    
    snake = Snake(LENGTH, WIDTH)

    stdscr.nodelay(True)
    curs_set(0)
    WON_MSG = 'You Won'
    LOST_MSG = 'You Lost'

    start = time.time()
    
    snakeSpeed = 0.4
      
    while True:
        timeNow = time.time() 
        if (timeNow - start) >= snakeSpeed:
            try:
                snake.move_forward()
                if(app == True):
                    applex, appley = snake.randomApple(LENGTH,WIDTH)
                if(snake.posArr[0] == Pos(x = applex, y = appley)):
                    snake.grow()
                    applex, appley = snake.randomApple(LENGTH, WIDTH)
                    snakeSpeed = snakeSpeed - 0.01
                    if(snakeSpeed == 0):
                        stdscr.clear()
                        stdscr.addstr(LENGTH, (WIDTH - len(LOST_MSG))//2, WON_MSG)
                        stdscr.refresh()
                        time.sleep(3)
                        break
                stdscr.clear()
                app = False
                start = time.time()
                
            except GameLost:
                stdscr.clear()
                stdscr.addstr(LENGTH//2,(WIDTH - len(LOST_MSG))//2, LOST_MSG)
                stdscr.refresh()
                time.sleep(3)
                break
                
            start = timeNow
        else:
            
            try:
                key = stdscr.getkey()
                
                if key == 'KEY_UP':
                    snake.turn_north();
                elif key == 'KEY_DOWN':
                    snake.turn_south();
                elif key == 'KEY_RIGHT':
                    snake.turn_east();
                elif key == 'KEY_LEFT':
                    snake.turn_west();
            
            except Exception: # IllegalMove and no input
                continue

            
        
        stdscr.clear()
        snake.draw(stdscr)
        stdscr.border(0)
        snake.printApple(stdscr, applex, appley) 
        stdscr.refresh()
        

if __name__ == '__main__':
   wrapper(main)
    # Wrapper does the setup and then calls main
    # after main is done, it puts back everything as it was

        

  
