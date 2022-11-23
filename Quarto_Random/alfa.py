import numpy as np
import random 
class Ghost:
    def __init__(self):
        self.Ghost_board = np.array ( [ 0, 0, 0, 0,
                             0, 0, 0, 0,
                             0, 0, 0, 0,
                             0, 0, 0, 0,                
                            ] )
        self.end   =  0
        self.who   =  [0,0,0,0]


    def reset (self):
        self.Ghost_board = np.array ( [ 0, 0, 0, 0,
                             0, 0, 0, 0,
                             0, 0, 0, 0,
                             0, 0, 0, 0,                
                            ] )
        self.end   =  0
        self.who   =  [0,0,0,0]



    
        

    def  it_is_a_win (self) :

            win_set = np.array ([
            [1, 2, 3, 4] ,
            [8, 7, 6, 5] ,
            [7, 3, 4, 8] ,
            [1, 3, 5, 7] ,
            [2, 4, 6, 8] ,
            [5, 6, 2, 1] ,              
                            ])

            
            ver =  np.array ([ self.Ghost_board[0],self.Ghost_board[5],self.Ghost_board[10],self.Ghost_board[15] ])
            
            Hor =  np.array ([self.Ghost_board[12], self.Ghost_board[9], self.Ghost_board[6],self.Ghost_board[3] ])
            li1 =  np.array ([ self.Ghost_board[0 ],self.Ghost_board[4],self.Ghost_board[8],self.Ghost_board[12] ])
            li2 =  np.array ([ self.Ghost_board[1],self.Ghost_board[5],self.Ghost_board[9],self.Ghost_board[13] ])
            li3 =  np.array ([ self.Ghost_board[2],self.Ghost_board[6],self.Ghost_board[10],self.Ghost_board[14] ])
            li4 =  np.array ([ self.Ghost_board[3],self.Ghost_board[7],self.Ghost_board[11],self.Ghost_board[15] ])

            hi1 =  np.array ([ self.Ghost_board[0 ],self.Ghost_board[1],self.Ghost_board[2],self.Ghost_board[3] ])
            hi2 =  np.array ([ self.Ghost_board[4],self.Ghost_board[5],self.Ghost_board[6],self.Ghost_board[7] ])
            hi3 =  np.array ([ self.Ghost_board[8],self.Ghost_board[9],self.Ghost_board[10],self.Ghost_board[11] ])
            hi4 =  np.array ([ self.Ghost_board[12],self.Ghost_board[13],self.Ghost_board[14],self.Ghost_board[15] ])

            for i in range(0, 6):
                vertical   = np.isin( ver , win_set[i, :]).sum(0)
                Horizontal = np.isin( Hor , win_set[i, :]).sum(0)
                l1         = np.isin( li1 , win_set[i, :]).sum(0)
                l2         = np.isin( li2 , win_set[i, :]).sum(0)
                l3         = np.isin( li3 , win_set[i, :]).sum(0)
                l4         = np.isin( li4 , win_set[i, :]).sum(0)
                h1         = np.isin( hi1 , win_set[i, :]).sum(0)
                h2         = np.isin( hi2 , win_set[i, :]).sum(0)
                h3         = np.isin( hi3 , win_set[i, :]).sum(0)
                h4         = np.isin( hi4 , win_set[i, :]).sum(0)      
                print( ver , 'iesimo' , vertical)

                if vertical == 4 :  self.end = 1 ; self.who = ver
                if Horizontal == 4 :self.end = 2 ; self.who = Hor  
                if l1        == 4 : self.end = 3 ; self.who = li1                 
                if l2        == 4 : self.end = 4 ; self.who = li2 
                if l3        == 4 : self.end = 5 ; self.who = li3  
                if l4        == 4 : self.end = 6 ; self.who = li4                                           
                if h1        == 4 : self.end = 7 ; self.who = hi1                   
                if h2        == 4 : self.end = 8 ; self.who = hi2
                if h3        == 4 : self.end = 9 ; self.who = hi3 
                if h4        == 4 : self.end = 10; self.who = hi4

                if (vertical == 4 or Horizontal== 4 or
                    l1 == 4       or      l2 == 4   or
                    l3 == 4       or      l4 == 4   or
                    h1 == 4       or      h2 == 4   or
                    h3 == 4       or      h4 == 4   
                   ):
                    return True # win
                
        



class AI ():
    def __init__(self):

        self.Ai_pawns = [1,2,3,4,5,6,7,8]
        self.Ai_table = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

    def reset (self):
        self.Ai_pawns = [1,2,3,4,5,6,7,8]
        self.Ai_table = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

    def AI_algorithm (self):
            random_pawn = random.choice(self.Ai_pawns)
            random_position = random.choice(self.Ai_table)
            self.remove_pawn(random_pawn)
            self.remove_position(random_position)
            return random_pawn,random_position

    
    def remove_pawn (self,num):
        self.Ai_pawns.remove(num)

    def remove_position (self,num):
        print(num)
        self.Ai_table.remove(num)


        

       