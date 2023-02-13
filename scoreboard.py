from turtle import Turtle
import pandas

class Scoreboard(Turtle):

    def __init__(self,usrname):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.read_highscore_file(usrname)
        
        

    def write_score_screen(self,playerhp):
        self.clear()
        self.goto(250,292)
        self.write(f'High score= {self.high_score}',font=('Arial',15,'bold'))
        self.goto(-406,292)
        self.write(f'Score = {self.score}',font=('Arial',15,'bold'))
        self.write_programmer()
        self.goto(-406,262)
        self.write(f'Hp={playerhp}/5 ',font=('Arial',15,'bold'))
        


    def write_highscore_file(self,name):
        if self.score > self.high_score:
            self.high_score = self.score
            high_score_csvfile = pandas.read_csv('data.csv')
            csv_todic = high_score_csvfile.to_dict('list')
            if name in csv_todic['users']:
                name_index = csv_todic['users'].index(name)
                csv_todic['scores'][name_index] = self.high_score
            else:
                csv_todic['users'].append(name)
                csv_todic['scores'].append(self.high_score)
            new_csv_df = pandas.DataFrame(csv_todic)
            new_csv_df.to_csv('data.csv',index=False)

            
            
        
        
    def read_highscore_file(self,name):

        high_score_csvfile = pandas.read_csv('data.csv')
        users_list = high_score_csvfile.users.to_list()

        if name in users_list:
            self.high_score = int(high_score_csvfile[high_score_csvfile.users == name].scores)
        else:
            self.high_score = 0

    
    def write_gameover(self):
        self.goto(0,240)
        self.write('Game Over!',font=('Arial',15,'bold'))

    def write_programmer(self):
        self.goto(250,260)
        self.write('developed by kamyab',font=('Arial',8,'bold'))
    
    def write_hp_count(self,playerhp):
        self.goto(-406,282)
        self.write(f'Hp={playerhp}/5 ',font=('Arial',15,'bold'))
