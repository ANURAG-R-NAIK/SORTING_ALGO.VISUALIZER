import pygame
import random #TO GENERATE THE INITIAL LIST TO BE SORTED

pygame.init()

class DrawInformation:
    BLACK = 0, 0, 0
    WHITE = 255, 255, 255 #COMBINATIONS OF RGB FOR DIFFERENT COLOURS
    GREEN = 0, 255, 0
    RED = 255, 0, 0
    GREY = 128, 128, 128
    BACKGROUND_COLOR = WHITE
    
    SIDE_PAD = 100 
    #ENSURES WE HAVE 50 PIXELS OF PADDING IN EITHER SIDES AND IT DONT TOUVH THE SCREEN
    TOP_PAD = 150
    #THIS IS TO LEAVE SPACE FOR INSTRUCTIONS OF THE CODE
    
    def __init__(self, width, height, lst):  #lst IS THE LIST THAT WE ARE GOING TO SORT
        self.width = width
        self.height = height
        
        self.window = pygame.display.set_mode((width, height)) 
        #THE WINDOW THAT WE WILL BE ACCESSING, WE PASS THE WID AND 
        #HEIGHT AS A TUPLE AND USE PYGAME MODULE
        
        pygame.display.set_caption("Sorting Algorithm Visualization") #HEADING OF WINDOW
        self.set_list(lst)
        
    def set_list(self, lst):
        self.lst = lst #TO STORE LIST INTERNALLY
        self.min_val = min(lst)        
        self.max_val = max(lst)   
        
        self.block_width = round((self.width - self.SIDE_PAD) / len(lst))
        #WE SUB THE PADDING FROM THE TOTAL WIDTH OF THE SCREEN AND DIVIDE BY THE LENGTH OF THE LIST TO BE SORTED
        #THE VALUE IS ROUNDED OFF AS WE CANNOT GO FOR FRACTIONAL VALUES
        
        self.block_height = round((self.height - self.TOP_PAD) / (self.max_val - self.min_val))
        self.start_x = self.SIDE_PAD // 2
        
    def generate_starting_list(n, min_val, max_val):
        #N IS THE NO. OF ELEMENTS IN STARTING LIST , MIN AND MAX ARE THE MIN AND MAX POSSIBLE VALUES
        lst = []
        
        for _ in range(n):
            val = random.randint(min_val, max_val)
            #WILL PROVIDE WITH A RANDOM NUMBER INCLUSIVE OF THE LIMITS THAT ARE MAX AND MIN
            lst.append(val)
            
        return lst
    
    def main():
        run = True
        clock = pygame.time.Clock()
        
        while run: #ENSURES THE LOOP KEEPS ON GOING IN THE BACKGROUND AND MAKE CHANGES
            clock.tick(60)
            
            pygame.display.update()
            
            for event in pygame.event.get(): #RETURNS A LIST OF EVENTS OCCURED SINCE LAST LOOP
                if event == pygame.QUIT: #IF WE HIT THE CLOSE BUTTON THEN THE WINDOW SHOULD CLOSE DOWN
                    run = False
        pygame.quit()
        
    if __name__ == "__main__":
        main()
            
        
            