from ast import Delete
from os import stat
from typing import Type
import pygame
from board import *
from alfa import *
from Globals import *
import numpy as np
pygame.init()

programIcon = pygame.image.load('./FREE_v4/icon2.png')
pygame.display.set_icon(programIcon)

win = pygame.display.set_mode((1000,600))
pygame.display.set_caption("Quarto")
win.fill(BLACK)  # Fills the screen with black
Board.board_set_up(win)

def Delete_button (button , ss):
        button.delete(win)
        ss.save_type(None)
        ss.change_clk(3)

def Ty_check(TYPE):

        if TYPE  == 9:
            S.change_clk(10)
            print('reset routine')
            

        if TYPE  != None and TYPE  != 9 :
            S.save_type(TYPE)
            S.change_clk(1)   
            print('s.type', S.type)






B1 = Button(17,pawn['SQ_H'],win)
B2 = Button(18,pawn['SQ_L'],win)
B3 = Button(19,pawn['SQH_H'],win)
B4 = Button(20,pawn['SQH_L'],win)
B5 = Button(21,pawn['C_H'],win)
B6 = Button(22,pawn['C_L'],win)
B7 = Button(23,pawn['CH_H'],win)
B8 = Button(24,pawn['CH_L'],win)
R  = Button(25,9,win)

S = FSM()

#Buttons of the  table 
T1 = Table_button(1,win)
T2 	=Table_button(2	,win)
T3	=Table_button(3	,win)
T4	=Table_button(4	,win)
T5	=Table_button(5	,win)
T6	=Table_button(6	,win)
T7	=Table_button(7	,win)
T8	=Table_button(8	,win)
T9	=Table_button(9	,win)
T10	=Table_button(10,win)
T11	=Table_button(11,win)
T12	=Table_button(12,win)
T13	=Table_button(13,win)
T14	=Table_button(14,win)
T15	=Table_button(15,win)
T16	=Table_button(16,win)

TYPE =  0
TY1	=	0
TY2	=	0
TY3	=	0
TY4	=	0
TY5	=	0
TY6	=	0
TY7	=	0
TY8	=	0

run = True
state = 0


def colorwin(num):
    if (num ==	1):	T1.set_pos(1,Ghost_t.Ghost_board[0],BLU); T6.set_pos(1,Ghost_t.Ghost_board[5],BLU); T9.set_pos(1,Ghost_t.Ghost_board[8],BLU); T13.set_pos(1,Ghost_t.Ghost_board[12],BLU); pygame.display.update() 
    
# 0 = None, no button selected
# 1 = button cliked, type extracted
# 

##                 ##
#   HERE THE logic  #
##                 ##

Ghost_t = Ghost()
AI_t    =  AI()            


# two clik
def set_pawn_on_grid (Table) :
         Table.push_area(M_pos,S.type,0)
         if  Table.clk == True:
            Ghost_t.Ghost_board[Table.Pos -1] = S.type
         #    print(Ghost_t.Ghost_board)
            Table.active = False
            AI_t.remove_position(Table.Pos) #ai notes the player movment
            S.change_clk(2)

def set_pawn_ai (Table) :
         Table.push_area(M_pos,S.type,0)
         if  Table.clk == True:
            Ghost_t.Ghost_board[Table.Pos -1] = S.type
         #    print(Ghost_t.Ghost_board)
            Table.active = False
            AI_t.remove_position(Table.Pos) #ai notes the player movment
            S.change_clk(2)

# stat3
def set_pown_AI (pawn_ai,pos_ai,COLOR):
    if (pos_ai ==	1	 ):	T1.set_pos(pos_ai,pawn_ai,COLOR); Ghost_t.Ghost_board[T1.Pos -1] = pawn_ai
    if (pos_ai ==	2	 ):	T2.set_pos(pos_ai,pawn_ai,COLOR); Ghost_t.Ghost_board[T2.Pos -1] = pawn_ai
    if (pos_ai ==	3	 ):	T3.set_pos(pos_ai,pawn_ai,COLOR); Ghost_t.Ghost_board[T3.Pos -1] = pawn_ai
    if (pos_ai ==	4	 ):	T4.set_pos(pos_ai,pawn_ai,COLOR); Ghost_t.Ghost_board[T4.Pos -1] = pawn_ai
    if (pos_ai ==	5	 ):	T5.set_pos(pos_ai,pawn_ai,COLOR); Ghost_t.Ghost_board[T5.Pos -1] = pawn_ai
    if (pos_ai ==	6	 ):	T6.set_pos(pos_ai,pawn_ai,COLOR); Ghost_t.Ghost_board[T6.Pos -1] = pawn_ai
    if (pos_ai ==	7	 ):	T7.set_pos(pos_ai,pawn_ai,COLOR); Ghost_t.Ghost_board[T7.Pos -1] = pawn_ai
    if (pos_ai ==	8	 ):	T8.set_pos(pos_ai,pawn_ai,COLOR); Ghost_t.Ghost_board[T8.Pos -1] = pawn_ai
    if (pos_ai ==	9	 ):	T9.set_pos(pos_ai,pawn_ai,COLOR); Ghost_t.Ghost_board[T9.Pos -1] = pawn_ai
    if (pos_ai ==	10	 ):	T10.set_pos(pos_ai,pawn_ai,COLOR); Ghost_t.Ghost_board[T10.Pos -1] = pawn_ai
    if (pos_ai ==	11	 ):	T11.set_pos(pos_ai,pawn_ai,COLOR); Ghost_t.Ghost_board[T11.Pos -1] = pawn_ai
    if (pos_ai ==	12	 ):	T12.set_pos(pos_ai,pawn_ai,COLOR); Ghost_t.Ghost_board[T12.Pos -1] = pawn_ai
    if (pos_ai ==	13	 ):	T13.set_pos(pos_ai,pawn_ai,COLOR); Ghost_t.Ghost_board[T13.Pos -1] = pawn_ai
    if (pos_ai ==	14	 ):	T14.set_pos(pos_ai,pawn_ai,COLOR); Ghost_t.Ghost_board[T15.Pos -1] = pawn_ai
    if (pos_ai ==	15	 ):	T15.set_pos(pos_ai,pawn_ai,COLOR); Ghost_t.Ghost_board[T15.Pos -1] = pawn_ai
    if (pos_ai ==	16	 ):	T16.set_pos(pos_ai,pawn_ai,COLOR); Ghost_t.Ghost_board[T16.Pos -1] = pawn_ai


def win_size ( a , b):
                # color_Win = BLU
                color_Win = RED
                if a == 1 : set_pown_AI (b[0],1,color_Win) ; set_pown_AI (b[1],6,color_Win) ;set_pown_AI (b[2],11,color_Win); set_pown_AI (b[3],16,color_Win)
                if a == 2 : set_pown_AI (b[0],12,color_Win); set_pown_AI (b[1],9,color_Win) ;set_pown_AI (b[2],6,color_Win) ; set_pown_AI (b[3],3,color_Win)



                if a == 7 : set_pown_AI (b[0],0+1,color_Win) ; set_pown_AI (b[1],1+1,color_Win) ;  set_pown_AI (b[2],2+1,color_Win) ; set_pown_AI (b[3],3+1,color_Win) 
                if a == 8 : set_pown_AI (b[0],4+1,color_Win) ; set_pown_AI (b[1],5+1,color_Win) ;  set_pown_AI (b[2],6+1,color_Win) ; set_pown_AI (b[3],7+1,color_Win)
                if a == 9 : set_pown_AI (b[0],8+1,color_Win) ; set_pown_AI (b[1],9+1,color_Win) ;  set_pown_AI (b[2],10+1,color_Win) ; set_pown_AI (b[3],11+1,color_Win)
                if a == 10 : set_pown_AI (b[0],12+1,color_Win) ; set_pown_AI (b[1],13+1,color_Win) ;  set_pown_AI (b[2],14+1,color_Win) ;set_pown_AI (b[3],15+1,color_Win)  


                if a == 3 : set_pown_AI (b[0],0+1,color_Win) ; set_pown_AI (b[1],4+1,color_Win) ;  set_pown_AI (b[2],8+1,color_Win) ; set_pown_AI (b[3],12+1,color_Win) 
                if a == 4 : set_pown_AI (b[0],1+1,color_Win) ; set_pown_AI (b[1],5+1,color_Win) ;  set_pown_AI (b[2],9+1,color_Win) ; set_pown_AI (b[3],13+1,color_Win)
                if a == 5 : set_pown_AI (b[0],2+1,color_Win) ; set_pown_AI (b[1],6+1,color_Win) ;  set_pown_AI (b[2],10+1,color_Win) ; set_pown_AI (b[3],14+1,color_Win)
                if a == 6 : set_pown_AI (b[0],3+1,color_Win) ; set_pown_AI (b[1],7+1,color_Win) ;  set_pown_AI (b[2],11+1,color_Win) ;set_pown_AI (b[3],15+1,color_Win) 





                
                 



while run:
    event = pygame.event.poll()
    M_pos = pygame.mouse.get_pos()

    
    pygame.time.delay(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
        if event.type == pygame.MOUSEBUTTONDOWN:

                if S.clik == 0:
                    #condizionale se è la seconda passata
                    if B1.active == True:
                        TY1 =   B1.isOver(M_pos)
                        Ty_check(TY1)
                        
                    if B2.active == True:
                        TY2 =   B2.isOver(M_pos)
                        Ty_check(TY2)
                        
                    if B3.active == True:
                        TY3 =   B3.isOver(M_pos)
                        Ty_check(TY3)
                        
                    if B4.active == True:
                        TY4 =   B4.isOver(M_pos)
                        Ty_check(TY4)
                        
                    if B5.active == True:
                        TY5 =   B5.isOver(M_pos)
                        Ty_check(TY5)
                        
                    if B6.active == True:
                        TY6 =   B6.isOver(M_pos)
                        Ty_check(TY6)
                        
                    if B7.active == True:
                        TY7 =   B7.isOver(M_pos)
                        Ty_check(TY7)
                        
                    if B8.active == True:
                        TY8 =   B8.isOver(M_pos)
                        Ty_check(TY8)

                    if R.active == True:
                        R8 =   R.isOver(M_pos)
                        Ty_check(R8)
                    pygame.display.update()




                if S.clik == 1:
                                            
                    if T1.active == True:
                        set_pawn_on_grid (T1) 

                    if T2.active == True:
                        set_pawn_on_grid (T2)
                    if T3.active == True:
                        set_pawn_on_grid (T3)
                    if T4.active == True:
                       set_pawn_on_grid (T4)
                    if T5.active == True:
                        set_pawn_on_grid (T5)
                    if T6.active == True:
                        set_pawn_on_grid (T6)
                              
                    if T7.active == True:
                        set_pawn_on_grid (T7)                               

                    if T8.active == True:
                        set_pawn_on_grid (T8)   

                    if T9.active == True:
                        set_pawn_on_grid (T9) 

                    if T10.active == True:
                        set_pawn_on_grid (T10) 

                    if T11.active == True:
                        set_pawn_on_grid (T11)

                    if T12.active == True:
                       set_pawn_on_grid (T12)

                    if T13.active == True:
                        set_pawn_on_grid (T13)     

                    if T14.active == True:
                        set_pawn_on_grid (T14)

                    if T15.active == True:
                        set_pawn_on_grid (T15)  

                    if T16.active == True:
                       set_pawn_on_grid (T16)
                       
                    

                    pygame.display.update()

               
                              
                if S.clik == 2: #elimino,blocco  il bottone e ricomincio
                    if S.type == 1:
                        Delete_button (B1 , S)
                    elif S.type == 2:
                        Delete_button (B2 , S) 
                    elif S.type == 3:
                        Delete_button (B3 , S)
                    elif S.type == 4:
                        Delete_button (B4 , S)
                    elif S.type == 5:
                        Delete_button (B5 , S)                    
                    elif S.type == 6:
                        Delete_button (B6 , S)
                    elif S.type == 7:
                        Delete_button (B7 , S)
                    elif S.type == 8:
                        Delete_button (B8 , S)
                    pygame.display.update()







                if S.clik == 3:# check if player have won
                    
                    win_p = Ghost_t.it_is_a_win()
                    

                    if win_p == True :
                        print ('PLAYER WIN')
                        S.change_clk(6)
                        while (R8 == 9):
                            R8 =   R.isOver(M_pos)
                            Ty_check(R8)
                    else:
                        S.change_clk(4)


                if S.clik == 4: # AI turn

                    pawn_ai,pos_ai = AI_t.AI_algorithm()
                    set_pown_AI (pawn_ai,pos_ai,WHITE)
                    pygame.display.update()

                    S.change_clk(5) 


                if S.clik == 5:# check if ai have won
                    win_A = Ghost_t.it_is_a_win()


                    print(Ghost_t.Ghost_board)

                    if win_A == True :
                        print ('AI WIN')
                        S.change_clk(7)
                        while (R8 == 9):
                            R8 =   R.isOver(M_pos)
                            Ty_check(R8)
                    else:
                        
                        S.change_clk(0)
                          

                                      
            
                         

                if S.clik == 6:
                    print('status 6')
                    print ('stop condition PLAYER')
                    print('Player',Ghost_t.end ,'+ who',Ghost_t.who )
                    win_size(Ghost_t.end,Ghost_t.who)
                    Board.PL_WIN(win)
                    if R.active == True:
                        R8 =   R.isOver(M_pos)
                        Ty_check(R8)
                    pass


                if S.clik == 7:
                    print('status 7')
                    print ('stop condition AI')
                    print('AI',Ghost_t.end ,'+ who',Ghost_t.who )
                    win_size(Ghost_t.end,Ghost_t.who)
                    Board.AI_WIN(win)
                    if R.active == True:
                        R8 =   R.isOver(M_pos)
                        Ty_check(R8)
                    pass

               

                if S.clik == 10:# RESET

                        Board.reset(win);
                        Ghost_t.reset()
                        
                        AI_t.reset()
                        B1.RESET(17,pawn['SQ_H'],win)
                        B2.RESET(18,pawn['SQ_L'],win)
                        B3.RESET(19,pawn['SQH_H'],win)
                        B4.RESET(20,pawn['SQH_L'],win)
                        B5.RESET(21,pawn['C_H'],win)
                        B6.RESET(22,pawn['C_L'],win)
                        B7.RESET(23,pawn['CH_H'],win)
                        B8.RESET(24,pawn['CH_L'],win)
                        R.RESET(25,9,win)
                        S.reset()
                        T1.RESET(1,win)
                        T2.RESET(2	,win)
                        T3.RESET(3	,win)
                        T4.RESET(4	,win)
                        T5.RESET(5	,win)
                        T6.RESET(6	,win)
                        T7.RESET(7	,win)
                        T8.RESET(8	,win)
                        T9.RESET(9	,win)
                        T10.RESET(10,win)
                        T11.RESET(11,win)
                        T12.RESET(12,win)
                        T13.RESET(13,win)
                        T14.RESET(14,win)
                        T15.RESET(15,win)
                        T16.RESET(16,win)

                        
                        S.change_clk(0)
                        pygame.display.update()
                        


                
    pygame.display.update()

#COLOR   
    
pygame.quit()


