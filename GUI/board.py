from ast import Pass, Return
from pickle import NONE
from Globals import BLU, GOLD, WHITE,BLACK,central_dot,radius
SQ_R = 50
import pygame 
import sys
pygame.init()

#Font = pygame.font.SysFont('timesnewroman',  30,0,0,None)
Font  = pygame.font.Font('freesansbold.ttf', 32)
H =Font.render("H", False, BLACK,None)
L =Font.render("L", False, BLACK ,None )


pawn = {
    
    'SQ_H' : 1 ,   'SQ_L' : 2, 
    'SQH_H': 3 ,   'SQH_L': 4,        
    'C_H'  : 5 ,   'C_L'  : 6,
    'CH_H' : 7 ,   'CH_L' : 8,
 }
class Board:

    def board_set_up (self):


        self.fill((0,0,0))  # Fills the screen with black
        pygame.draw.circle(self, WHITE, [350, central_dot], 290,1)
        #low line 1
        pygame.draw.circle(self, WHITE, [350, central_dot - 6*radius], radius,2)
        #low line 2
        pygame.draw.circle(self, WHITE, [280, central_dot - 4*radius], radius,2)
        pygame.draw.circle(self, WHITE, [420, central_dot - 4*radius], radius,2)
        #up line 3
        pygame.draw.circle(self, WHITE, [210, central_dot - 2*radius], radius,2)
        pygame.draw.circle(self, WHITE, [350, central_dot - 2*radius], radius,2)
        pygame.draw.circle(self, WHITE, [490, central_dot - 2*radius], radius,2) 
        #central line
        pygame.draw.circle(self, WHITE, [140, central_dot], radius,2)
        pygame.draw.circle(self, WHITE, [280, central_dot], radius,2)
        pygame.draw.circle(self, WHITE, [420, central_dot], radius,2)
        pygame.draw.circle(self, WHITE, [560, central_dot], radius,2)
        #central line
        #low line 3
        pygame.draw.circle(self, WHITE, [210, central_dot + 2*radius], radius,2)
        pygame.draw.circle(self, WHITE, [350, central_dot + 2*radius], radius,2)
        pygame.draw.circle(self, WHITE, [490, central_dot + 2*radius], radius,2)     
        #low line 2
        pygame.draw.circle(self, WHITE, [280, central_dot + 4*radius], radius,2)
        pygame.draw.circle(self, WHITE, [420, central_dot + 4*radius], radius,2)
        #low line 1
        pygame.draw.circle(self, WHITE, [350, central_dot + 6*radius], radius,2)
        pygame.display.update() 

        #List of all the powns
        pygame.draw.circle(self, WHITE, [350, central_dot + 6*radius], radius,2)

        HIGS = 94
        pygame.draw.line(self,GOLD, (660, HIGS), (930, HIGS))

        fonts = pygame.font.SysFont("Game Over",50)
        textfy =fonts.render("Pawns available ", True, GOLD,)
        self.blit(textfy, (670, HIGS-30))


    def get_position (pos):
        if pos == 1:
            return 350, central_dot - 6*radius
        if pos == 2:
            return 420, central_dot - 4*radius
        if pos == 3:
            return 490, central_dot - 2*radius         
        if pos == 4:
            return 560, central_dot            
        if pos == 5:
            return 280, central_dot - 4*radius
        if pos == 6:
            return 350, central_dot - 2*radius
        if pos == 7:
            return 420, central_dot
        if pos == 8:
            return 490, central_dot + 2*radius
        if pos == 9:
            return 210, central_dot - 2*radius
        if pos == 10:
            return 280, central_dot
        if pos == 11:
            return 350, central_dot + 2*radius
        if pos == 12:
            return 420, central_dot + 4*radius
        if pos == 13:
            return 140, central_dot
        if pos == 14:
            return 210, central_dot + 2*radius 
        if pos == 15:
            return 280, central_dot + 4*radius
        if pos == 16:
            return 350, central_dot + 6*radius
        if pos == 17:
            return 750, central_dot - 4*radius
        if pos == 18:
            return 850, central_dot - 4*radius
        if pos == 19:
            return 750, central_dot - 2*radius
        if pos == 20:
            return 850, central_dot - 2*radius
        if pos == 21:
            return 750, central_dot - radius +40
        if pos == 22:
            return 850, central_dot - radius +40
        if pos == 23:
            return 750, central_dot + 2*radius +10
        if pos == 24:
            return 850, central_dot + 2*radius +10

    def draw_pawn (self,color,type,pos): #,type,cio ,x,y,color

        x,y = Board.get_position(pos)

        

        #circle
        if type == 1: #'SQ_H'
            pygame.draw.circle(self, BLACK, list(Board.get_position(pos)), radius-2,0)
            pygame.draw.rect(self, color, [x-25, y-25 , SQ_R, SQ_R], 0)
            self.blit(H,(x-10,y-10))         
        if type == 2: #'SQ_L'
            pygame.draw.circle(self, BLACK, list(Board.get_position(pos)), radius-2,0)
            pygame.draw.rect(self, color, [x-25, y-25 , SQ_R, SQ_R], 0)
            self.blit(L,(x-10,y-10))
        if type == 3: #'SQH_H'
            pygame.draw.circle(self, BLACK, list(Board.get_position(pos)), radius-2,0)
            H_W =Font.render("H", False, color,None)
            pygame.draw.rect(self, color, [x-25, y-25 , SQ_R, SQ_R], 12)
            self.blit(H_W,(x-10,y-10))
        if type == 4: #'SQH_L'
            pygame.draw.circle(self, BLACK, list(Board.get_position(pos)), radius-2,0)
            L_W =Font.render("L", False, color ,None )
            pygame.draw.rect(self, color, [x-25, y-25 , SQ_R, SQ_R], 12)
            self.blit(L_W,(x-10,y-10))
        if type == 5: #'C_H'
            pygame.draw.circle(self, BLACK, list(Board.get_position(pos)), radius-2,0)
            pygame.draw.circle(self, color, list(Board.get_position(pos)), radius,0)
            self.blit(H,(x-10,y-10))
        if type == 6: #'C_L'
            pygame.draw.circle(self, BLACK, list(Board.get_position(pos)), radius-2,0)
            pygame.draw.circle(self, color, list(Board.get_position(pos)), radius,0)
            self.blit(L,(x-10,y-10))
        if type == 7: #'CH_H'
            pygame.draw.circle(self, BLACK, list(Board.get_position(pos)), radius-2,0)
            H_W =Font.render("H", False, color,None)
            pygame.draw.circle(self, color, list(Board.get_position(pos)), radius,12)
            self.blit(H_W,(x-10,y-10))
        if type == 8: #'CH_L'
            pygame.draw.circle(self, BLACK, list(Board.get_position(pos)), radius-2,0)
            L_W =Font.render("L", False, color ,None )
            pygame.draw.circle(self, color, list(Board.get_position(pos)), radius,12)
            self.blit(L_W,(x-10,y-10))

    


    

class Button():

    

    def __init__(self,Pos,type,win):
        self.Pos = Pos
        self.type = type 
        self.win = win
        self.a,self.v = Board.get_position(self.Pos)
        Board.draw_pawn(win,GOLD, self.type, self.Pos )
        self.active  =  True
        self.clicked =  False
        


    def delete(self,win):
        pygame.draw.circle(win, BLACK, list(Board.get_position(self.Pos)), radius+1,0)
        print("button distrutto")
        self.active = False
       

    def isOver(self, pos):
        a_1 = self.a + 25+10
        a_2 = self.a + 25 - 51 -17
        y_1 = self.v +25 +13
        y_2 = self.v + 25 - 51 -5

        if  y_2 < pos[1] and pos[1] < y_1 and  a_2 < pos[0] and pos[0] < a_1: 
            Board.draw_pawn(self.win,BLU, self.type, self.Pos )
            return self.type
            
        else:
            Board.draw_pawn(self.win,GOLD, self.type, self.Pos )
            self.clicked = False
            return None

    Pass



class Table_button():

    def __init__(self,Pos,win):
        self.Pos = Pos
        self.win = win
        self.a,self.v = Board.get_position(self.Pos)
        self.clk = False
        self.bl = False #BLOCKED
        self.active = True
        
    def push_area (self, pos,type,ID ):# 1 = IA , 0 = player
        a_1 = self.a + 25+10
        a_2 = self.a + 25 - 51 -17
        y_1 = self.v +25 +13
        y_2 = self.v + 25 - 51 -5

        if ID == 0:
            color = GOLD
        else:
            color = WHITE

        if  y_2 < pos[1] and pos[1] < y_1 and  a_2 < pos[0] and pos[0] < a_1: 
            Board.draw_pawn(self.win,color, type, self.Pos )                 
            self.set_clk(True)                                              



    def set_clk(self,set):
        self.clk = set 
    
    def set_bl(self,set):
        self.bl = set 



    Pass
  

class FSM ():
    
    def __init__(self):
        self.status = 0
        self.clik = 0
        self.type = 0

    def change_state(self,state):
        self.status = state 

    def change_clk(self,clikk):
        self.clik = clikk   
    def save_type(self,typee):
        self.type = typee 

 