from turtle import Turtle,Screen
from random import choice

class Game:

    ENEMY_RESPAWN_CORD = [(435,-50),(436,50),(435,150)]
    

   


    def __init__(self):
        self.jet_list = []
        self.missle_list = []
        self.player_jet = self.creat_player_jet()
        self.enemy_move_speed = 0.01
        self.hp = 5
        self.key_press= False
        
        

    def creat_jets(self):
        
        enemyjet = Turtle()
        enemyjet.shape('img/enemy.gif')
        enemyjet.penup()
        enemyjet.setheading(180)
        enemyjet.goto(choice(self.ENEMY_RESPAWN_CORD))
        self.jet_list.append(enemyjet)
    
    def creat_player_jet(self):
        player_jet = Turtle()
        player_jet.shape('img/jet.gif')
        
        player_jet.penup()
        player_jet.setheading(0)
        player_jet.goto(-400,74)

        return player_jet

    def move_enemy(self):

        for enemy in self.jet_list:
            enemy.forward(self.enemy_move_speed)
    
    def manage_jets(self):
        
        for i in range(len(self.jet_list)):
            for y in range(len(self.jet_list)):
                if i != y :
                    if self.jet_list[i].distance(self.jet_list[y]) < 70 :
                        self.jet_list[y].hideturtle()
                        self.jet_list.pop(y)
                        return True
        

    def creat_missle(self):
        missle = Turtle()
        missle.penup()
        missle.shape('img/missle.gif')
        missle.setheading(0)
        missle.goto(self.player_jet.pos())
        self.missle_list.append(missle)
        self.key_press = True
        
        
    def move_missle(self):

        for item in self.missle_list:
            item.forward(0.1)


    def missle_impact(self):
        for missle in self.missle_list:
            if missle.xcor() > 450:
                missle.hideturtle()
                self.missle_list.pop(self.missle_list.index(missle))

        for i in range(len(self.missle_list)):
            for j in range(len(self.jet_list)):
                if self.missle_list[i].distance(self.jet_list[j]) < 20:
                    self.missle_list[i].hideturtle()
                    self.jet_list[j].hideturtle()
                    self.missle_list.pop(i)
                    self.jet_list.pop(j)
                    return True
        
    def lose_hp(self):
        for enemy in self.jet_list:

            if enemy.xcor() < -450:
                self.hp -= 1
                enemy.hideturtle()                
                self.jet_list.pop(self.jet_list.index(enemy))
                return True
            
            if enemy.distance(self.player_jet) < 25:
                self.hp -= 1
                enemy.hideturtle()
                self.jet_list.pop(self.jet_list.index(enemy))
                return True
               

                


    def key_press_false(self):
        '''this function just make a variable to False to check if a key preesed later on :)'''
        self.key_press= False


    def move_player_jet(self,x,y):
        self.player_jet.goto(x,y)

    
        
   
