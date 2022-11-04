from ast import Delete
from os import stat
from typing import Type
import pygame
from board import *
from Globals import *
pygame.init()
#img = pygame.image.load('gfg_image.jpg')
#pygame.display.set_icon(img)

win = pygame.display.set_mode((1000,600))
pygame.display.set_caption("Quarto")
win.fill(BLACK)  # Fills the screen with black
Board.board_set_up(win)



def Ty_check(TYPE):

        if TYPE  != None:
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


# 0 = None, no button selected
# 1 = button cliked, type extracted
# 

while run:
    event = pygame.event.poll()
    M_pos = pygame.mouse.get_pos()

    
    pygame.time.delay(100)
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

                    pygame.display.update()

                if S.clik == 1:
                                            
                    if T1.active == True:
                        T1.push_area(M_pos,S.type,0)
                        if  T1.clk == True:
                            T1.active = False
                            S.change_clk(2)

                    if T2.active == True:
                        T2.push_area(M_pos,S.type,0)
                        if  T2.clk == True:
                            T2.active = False
                            S.change_clk(2)

                    if T3.active == True:
                        T3.push_area(M_pos,S.type,0)
                        if  T3.clk == True:
                              T3.active = False
                              S.change_clk(2)         

                    if T4.active == True:
                        T4.push_area(M_pos,S.type,0)
                        if  T4.clk == True:
                              T4.active = False
                              S.change_clk(2)  

                    if T5.active == True:
                        T5.push_area(M_pos,S.type,0)
                        if  T5.clk == True:
                              T5.active = False
                              S.change_clk(2)    

                    if T6.active == True:
                        T6.push_area(M_pos,S.type,0)
                        if  T6.clk == True:
                              T6.active = False
                              S.change_clk(2)
                              
                    if T7.active == True:
                        T7.push_area(M_pos,S.type,0)
                        if  T7.clk == True:
                              T7.active = False
                              S.change_clk(2)                                  

                    if T8.active == True:
                        T8.push_area(M_pos,S.type,0)
                        if  T8.clk == True:
                              T8.active = False
                              S.change_clk(2)    

                    if T9.active == True:
                        T9.push_area(M_pos,S.type,0)
                        if  T9.clk == True:
                              T9.active = False
                              S.change_clk(2)  

                    if T10.active == True:
                        T10.push_area(M_pos,S.type,0)
                        if  T10.clk == True:
                              T10.active = False
                              S.change_clk(2)  

                    if T11.active == True:
                        T11.push_area(M_pos,S.type,0)
                        if  T11.clk == True:
                            T11.active = False
                            S.change_clk(2)

                    if T12.active == True:
                        T12.push_area(M_pos,S.type,0)
                        if  T12.clk == True:
                            T12.active = False
                            S.change_clk(2)

                    if T13.active == True:
                        T13.push_area(M_pos,S.type,0)
                        if  T13.clk == True:
                              T13.active = False
                              S.change_clk(2)          

                    if T14.active == True:
                        T14.push_area(M_pos,S.type,0)
                        if  T14.clk == True:
                              T14.active = False
                              S.change_clk(2)  

                    if T15.active == True:
                        T15.push_area(M_pos,S.type,0)
                        if  T15.clk == True:
                              T15.active = False
                              S.change_clk(2)   

                    if T16.active == True:
                        T16.push_area(M_pos,S.type,0)
                        if  T16.clk == True:
                              T16.active = False
                              S.change_clk(2) 
                              
                



                    pygame.display.update()

                if S.clik == 2: #elimino,blocco  il bottone e ricomincio
                    if S.type == 1:
                        B1.delete(win)
                        S.save_type(None)
                        S.change_clk(0)

                    elif S.type == 2:
                        B2.delete(win)
                        S.save_type(None)
                        S.change_clk(0)  

                    elif S.type == 3:
                        B3.delete(win)
                        S.save_type(None)
                        S.change_clk(0)  

                    elif S.type == 4:
                        B4.delete(win)
                        S.save_type(None)
                        S.change_clk(0) 

                    elif S.type == 5:
                        B5.delete(win)
                        S.save_type(None)
                        S.change_clk(0)
                       
                    elif S.type == 6:
                        B6.delete(win)
                        S.save_type(None)
                        S.change_clk(0)
                    
                    elif S.type == 7:
                        B7.delete(win)
                        S.save_type(None)
                        S.change_clk(0)

                    elif S.type == 8:
                        B8.delete(win)
                        S.save_type(None)
                        S.change_clk(0)

    pygame.display.update()

#white   
    
pygame.quit()

