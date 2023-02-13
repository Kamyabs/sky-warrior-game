from turtle import Screen
from random import randint
import gameclass
from soundeffect import Sound
from scoreboard import Scoreboard

def game_loop():
    screen = Screen()

    screen.setup(900,800)
    screen.tracer(0)
    screen.title('Sky Warrior')
    background = 'img/gg.gif'
    screen.bgpic(background)

    myjetp = 'img/jet.gif'
    enemyjetp = 'img/enemy.gif'
    cloudp = 'img/cloud.gif'
    misslep= 'img/missle.gif'

    screen.register_shape(myjetp)
    screen.register_shape(enemyjetp)
    screen.register_shape(cloudp)
    screen.register_shape(misslep)

    game = gameclass.Game()
    sound = Sound()
    sound.playback()
    user_name = screen.textinput('enter your name','whats your name? ')

    screen.listen()
    screen.onkey(game.creat_missle,'f')
    screen.onclick(game.move_player_jet)


    game_on = True
    game_scoreboard = Scoreboard(user_name)
    game_scoreboard.write_score_screen(game.hp)
    
    while game_on:
        
        screen.update()
        
        randomnumber = randint(0,2000)
        if randomnumber == 50:
            game.creat_jets()
            game.manage_jets()
        game.move_enemy()
        game.move_missle()
        if game.key_press == True:
            sound.missle_shot()
            game.key_press_false()

        if game.lose_hp():
            game_scoreboard.write_score_screen(game.hp)
            sound.crashsound()
            
        if game.missle_impact():
            sound.jet_explosion()
            game_scoreboard.score += 100
            game.enemy_move_speed += 0.009
            game_scoreboard.write_score_screen(game.hp)
        if game.hp < 1 :
            game_scoreboard.write_gameover()
            game_on = False
        if game_on == False:
                play_again = screen.textinput('play again?','play again? y/n')
                if play_again == 'y':
                    screen.clear()
                    game_loop()
                else:
                    screen.bye()
                
            
    game_scoreboard.write_highscore_file(user_name)
    screen.mainloop()

game_loop()




    


