from curses import wrapper
import time
from collections import namedtuple


#if __name__ == '__main__':
 #   wrapper(main)
    # Wrapper does the setup and then calls main
    # after main is done, it puts back everything as it was

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
            self.cdir = 's'
            raise IllegalMove("Can't move from south to north")
        else:
            self.cdir = 'n'
        
    def turn_south(self):
        if self.cdir == 'n':
            self.cdir == 'n'
            raise IllegalMove("Can't move from north to south")
        else:
            cdir = 's'
        
    def turn_east(self):
        if self.cdir == 'w':
            self.cdir == 'w'
            raise IllegalMove("Can't move from north to south")
        else:
            cdir = 'e'
                           
    def turn_west(self):
        if self.cdir == 'e':
            self.cdir == 'e'
            raise IllegalMove("Can't move from north to south")
        else:
            cdir = 'w'

    def grow(self):
        self.grow_at.append[self.posArr[0]]
    

    def move_forward(self):
        # Check for two things
        #   1. Did the snake hit itself
        #   2. Did the snake it one of the borders?
        
        # Use array.index
        head = self.posArr[0]
        if self.cdir == 'n':
            newPos = Pos(x = head.x, y = head.y + 1)
        elif self.cdir == 's':
            newPos = Pos(x = head.x, y = head.y - 1)
        elif self.cdir == 'e':
            newPos = Pos(x = head.x + 1, y = head.y)
        elif self.cdir == 'w':
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

        
        # INSERT newPos
        self.posArr.insert(0, newPos)
        
        if not (self.grow_at is None or self.posArr[-1] != self.grow_at):
            pop.self.grow_at[-1]
        else:
            self.posArr.pop()

def randomApple(applex, appley):
    applex = randint(0, WIDTH)
    appley = randint(0, LENGTH)
    
LENGTH = 8
WIDTH = 12
applex = 8
appley = 8

snake = Snake(LENGTH, WIDTH)

while(True):
    while(snake.posArr[0] != Pos(x = applex, y = appley)):
        try:
          snake.move_forward()
        except ValueError or GameLost():
          break
    if(KEY_UP):
          snake.turn_north()
    elif(KEY_DOWN):
          snake.turn_south()
    elif(KEY_LEFT):
          snake.turn_west()
    elif(KEY_RIGHT):
          snake.turn_east()
    if(snake.posArr[0] == Pos(x = applex, y = appley)):
          snake.grow()
          randomApple(applex, appley)
    




        

  
