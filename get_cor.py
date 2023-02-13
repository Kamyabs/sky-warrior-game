from turtle import Screen

screen = Screen()
screen.setup(900,800)
screen.bgpic('img/gg.gif')

def get_cor(x,y):
    print(x,y)

screen.onclick(get_cor)




screen.mainloop()