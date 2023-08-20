from pygame import *
font.init()

class Wall(sprite.Sprite):
    def __init__(self,color_1,color_2,color_3,wall_x,wall_y,wall_width,wall_height):
        sprite.Sprite.__init__(self)
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.wall_width = wall_width
        self.wall_height = wall_height

        self.image = Surface([wall_width,wall_height])

        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

    def draw_wall(self):
        draw.rect(window,(self.color_1,self.color_2,self.color_3), (self.rect.x,self.rect.y,self.wall_width,self.wall_height))

    def draw_circle(self):
        draw.circle(window,(self.color_1,self.color_2,self.color_3), (self.rect.x,self.rect.y),(self.wall_width))

class Enemy(sprite.Sprite):
    def __init__(self,color_1,color_2,color_3,wall_width,wall_height,start_x,start_y,end_x,end_y,direction,speed,wall_x,wall_y):
        sprite.Sprite.__init__(self)
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.wall_width = wall_width
        self.wall_height = wall_height
        self.speed = speed

        self.wall_x = wall_x
        self.wall_y = wall_y

        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y
        self.direction = direction

        self.image = Surface([wall_width,wall_height])

        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    
    def update(self):
        if self.direction == "horizontal":
            if self.rect.x <= self.start_x:
                self.side = "right"
            if self.rect.x >= self.end_x:
                self.side = "left"
            if self.side == "left":
                self.rect.x -= self.speed
            if self.side == "right":
                self.rect.x += self.speed
        elif self.direction == "vertical":
            if self.rect.y <= self.start_y:
                self.side = "right"
            if self.rect.y >= self.end_y:
                self.side = "left"
            if self.side == "left":
                self.rect.y -= self.speed
            if self.side == "right":
                self.rect.y += self.speed
        else:
            print("error")

    def draw_wall(self):
        draw.rect(window,(self.color_1,self.color_2,self.color_3), (self.rect.x,self.rect.y,self.wall_width,self.wall_height))

class Player(Wall):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x >= 0:
            self.rect.x -= 2
            if square_collide() != "None":
                self.rect.x += 2
        if keys[K_RIGHT] and self.rect.x <= 1370:
            self.rect.x += 2
            if square_collide() != "None":
                self.rect.x -= 2
        if keys[K_UP] and self.rect.y >= 0:
            self.rect.y -= 2
            if square_collide() != "None":
                self.rect.y += 2
        if keys[K_DOWN] and self.rect.y <= 770:
            self.rect.y += 2
            if square_collide() != "None":
                self.rect.y -= 2


class Phrase():
    def __init__(self,color1,color2,color3,font_type,text,x_pos,y_pos,font_size):
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3
        self.font_type = font_type
        self.text = text
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.font_size = font_size
    def draw_text(self):
        self.font = font.SysFont(self.font_type,self.font_size)
        screen_text = self.font.render(self.text, True,(self.color1,self.color2,self.color3))
        window.blit(screen_text, (self.x_pos,self.y_pos))

def background():
    draw.rect(window,(200,200,200), (0,0,1400,800))
    for i in range(20):
        for j in range(10):
            draw.rect(window,(255,255,255), (i * 80,j * 80,40,40))
        for j in range(10):
            draw.rect(window,(255,255,255), (i * 80 + 40,j * 80 + 40,40,40))

def square_collide():
    for i in range(len(wall_list)):
        if sprite.collide_rect(wall_list[i],square):
            return(wall_list[i])
    return("None")

def circle_collide():
    for i in range(len(circle_list)):
        if sprite.collide_rect(circle_list[i],square):
            return(i)
    return("None")

def win_collide():
    if sprite.collide_rect(wall_goal2,square):
        return("Victory")
    return("None")

def enemy_collide():
    for i in range(len(enemy_list)):
        if sprite.collide_rect(enemy_list[i],square):
            return("Dead")
    return("None")

def main_screen():
    global wall_list
    wall_list = []
    square = Player(0,0,255,700,400,30,30)
    button_press = False
    while button_press == False:
        background()

        draw.rect(window,(0,0,0),(120,600,240,120))
        draw.rect(window,(0,0,0),(480,600,360,120))

        for i in range(len(main_screen_text_list)):
            main_screen_text_list[i].draw_text()

        square.update()
        square.draw_wall()

        for e in event.get():
            if e.type == MOUSEBUTTONDOWN:
                if e.button == 1 and 120 <= e.pos[0] and 600 <= e.pos[1] and 360 >= e.pos[0] and 720 >= e.pos[1]:
                    button_press = True
                if e.button == 1 and 480 <= e.pos[0] and 600 <= e.pos[1] and 840 >= e.pos[0] and 720 >= e.pos[1]:
                    Instructions()
                    button_press = True
        
        display.update()

def Instructions():
    time.delay(5)

    background()

    draw.rect(window,(0,0,0),(40,40,360,120))
    
    for i in range(len(instructions_text_list)):
        instructions_text_list[i].draw_text()

    display.update()

    button_press = False
    while button_press == False:

        for e in event.get():
            if e.type == MOUSEBUTTONDOWN:
                if e.button == 1 and 10 <= e.pos[0] and 10 <= e.pos[1] and 210 >= e.pos[0] and 110 >= e.pos[1]:
                    main_screen()
                    button_press = True

window_width = 1400
window_height = 800
display.set_caption("World's Hardest Game")
window = display.set_mode((window_width,window_height))

level = 1


text1 = Phrase(0,0,0,"C:/Users/joshu/AppData/Local/Microsoft/Windows/INetCache/IE/9EP3SYSI/Authentic_Script_Rough[1].ttf","Inferno Studios Inc",50,50,100)
text2 = Phrase(0,0,0,"C:/Users/joshu/AppData/Local/Microsoft/Windows/INetCache/IE/9EP3SYSI/Authentic_Script_Rough[1].ttf","Presents",50,250,100)
text3 = Phrase(0,0,0,"C:/Users/joshu/AppData/Local/Microsoft/Windows/INetCache/IE/9EP3SYSI/Authentic_Script_Rough[1].ttf","The Worlds",50,50,100)
text4 = Phrase(0,0,0,"C:/Users/joshu/AppData/Local/Microsoft/Windows/INetCache/IE/9EP3SYSI/Authentic_Script_Rough[1].ttf","Hardest Game",50,250,100)
text6 = Phrase(0,0,0,"C:/Users/joshu/AppData/Local/Microsoft/Windows/INetCache/IE/9EP3SYSI/Authentic_Script_Rough[1].ttf","Press Space To Play",50,350,90)

main_screen_text_list = []
main_screen_text_list.append(Phrase(0,0,0,"C:/Users/joshu/AppData/Local/Microsoft/Windows/INetCache/IE/9EP3SYSI/Authentic_Script_Rough[1].ttf","Worlds Hardest Game",50,50,170))
main_screen_text_list.append(Phrase(255,255,255,"C:/Users/joshu/AppData/Local/Microsoft/Windows/INetCache/IE/9EP3SYSI/Authentic_Script_Rough[1].ttf","Play!",130,620,120))
main_screen_text_list.append(Phrase(255,255,255,"C:/Users/joshu/AppData/Local/Microsoft/Windows/INetCache/IE/9EP3SYSI/Authentic_Script_Rough[1].ttf","Instructions",490,630,80))

instructions_text_list = []
instructions_text_list.append(Phrase(0,0,0,"C:/Users/joshu/AppData/Local/Microsoft/Windows/INetCache/IE/9EP3SYSI/Authentic_Script_Rough[1].ttf","Instructions",320,50,170))
instructions_text_list.append(Phrase(0,0,0,"C:/Users/joshu/AppData/Local/Microsoft/Windows/INetCache/IE/9EP3SYSI/Authentic_Script_Rough[1].ttf","Main Screen",45,45,100))

background()
text1.draw_text()
text2.draw_text()
display.update()
time.delay(1000)

background()
text3.draw_text()
text4.draw_text()
display.update()
time.delay(1000)


gameloop = True
while gameloop == True:

    main_screen()

    if level == 1:
        square = Player(0,0,255,160,160,30,30)

        circle_list = []

        for i in range(3):
            for j in range(3):
                circle_list.append(Wall(255,255,0,660 + i * 40,420 - 40 * j,10,10))

        wall_list = []

        wall1 = Wall(50,50,50,0,0,1400,120)
        wall_list.append(wall1)
        wall2 = Wall(50,50,50,0,0,120,800)
        wall_list.append(wall2)
        wall3 = Wall(50,50,50,1280,0,120,800)
        wall_list.append(wall3)
        wall4 = Wall(50,50,50,0,680,1400,120)
        wall_list.append(wall4)

        wall5 = Wall(50,50,50,240,0,40,560)
        wall_list.append(wall5)
        wall6 = Wall(50,50,50,1120,240,40,560)
        wall_list.append(wall6)

        wall_goal_list = []

        wall_goal1 = Wall(0,255,0,120,120,120,560)
        wall_goal_list.append(wall_goal1)
        wall_goal2 = Wall(0,255,0,1160,120,120,560)
        wall_goal_list.append(wall_goal2)

        game_text_list = []
        coin_counter = 0
        text_score = Phrase(255,255,255,"C:/Users/joshu/AppData/Local/Microsoft/Windows/INetCache/IE/9EP3SYSI/Authentic_Script_Rough[1].ttf","Coins: " + str(coin_counter),50,50,100)
        game_text_list.append(text_score)
        worldhardestgame = Phrase(255,255,255,"C:/Users/joshu/AppData/Local/Microsoft/Windows/INetCache/IE/9EP3SYSI/Authentic_Script_Rough[1].ttf","World's Hardest Game",600,50,100)
        game_text_list.append(worldhardestgame)
        inferno_studios = Phrase(255,255,255,"C:/Users/joshu/AppData/Local/Microsoft/Windows/INetCache/IE/9EP3SYSI/Authentic_Script_Rough[1].ttf","Inferno Studio Inc",600,720,100)
        game_text_list.append(inferno_studios)
        text_score = Phrase(255,255,255,"C:/Users/joshu/AppData/Local/Microsoft/Windows/INetCache/IE/9EP3SYSI/Authentic_Script_Rough[1].ttf","Level: " + str(level),50,720,100)
        game_text_list.append(text_score)

        enemy_list = []

        for i in range(11):
            enemy_list.append(Enemy(255,0,0,30,30,285,120,650,650,"vertical",2,285 + 80 * i,120))
            enemy_list.append(Enemy(255,0,0,30,30,285,120,650,650,"vertical",2,325 + 80 * i,650))

        enemy_list.pop()

    run = True
    while run == True:
        time.delay(5)
        
        for e in event.get():
            if e.type == QUIT:
                gameloop = False
                run = False

        background()

        for i in range(len(circle_list)):
            circle_list[i].draw_circle()

        for i in range(len(wall_list)):
            wall_list[i].draw_wall()

        for i in range(len(wall_goal_list)):
            wall_goal_list[i].draw_wall()

        square.update()
        square.draw_wall()

        if circle_collide() != "None":
            del circle_list[circle_collide()]
            coin_counter += 1
            text_score.text = "Coins: " + str(coin_counter)

        if win_collide() == "Victory" and coin_counter == 9:
            print("Victory")
        
        if enemy_collide() == "Dead":
            square = Player(0,0,255,160,160,30,30)

        for i in range(len(enemy_list)):
            enemy_list[i].update()
            enemy_list[i].draw_wall()
        
        for i in range(len(game_text_list)):
            game_text_list[i].draw_text()

        display.update()