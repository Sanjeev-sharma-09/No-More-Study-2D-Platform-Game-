import pygame
from sys import exit
from random import randint, choice


#Creating a class for the Player
class Player(pygame.sprite.Sprite):

    def __init__(self):
        
        super().__init__()

        #Importing the walking animation frames
        player_walk_1= pygame.image.load("characters/player/player walk/player_walk_frame_1.png").convert_alpha()
        player_walk_2= pygame.image.load("characters/player/player walk/player_walk_frame_2.png").convert_alpha()
        player_walk_3= pygame.image.load("characters/player/player walk/player_walk_frame_3.png").convert_alpha()
        player_walk_4= pygame.image.load("characters/player/player walk/player_walk_frame_4.png").convert_alpha()

        #Importing the jumping animation frames
        player_jump_1= pygame.image.load("characters/player/player jump/player_jump_frame_1.png").convert_alpha()
        player_jump_2= pygame.image.load("characters/player/player jump/player_jump_frame_2.png").convert_alpha()
        player_jump_3= pygame.image.load("characters/player/player jump/player_jump_frame_3.png").convert_alpha()
        player_jump_4= pygame.image.load("characters/player/player jump/player_jump_frame_4.png").convert_alpha()
        player_jump_5= pygame.image.load("characters/player/player jump/player_jump_frame_5.png").convert_alpha()
        player_jump_6= pygame.image.load("characters/player/player jump/player_jump_frame_6.png").convert_alpha()
        player_jump_7= pygame.image.load("characters/player/player jump/player_jump_frame_7.png").convert_alpha()
        player_jump_8= pygame.image.load("characters/player/player jump/player_jump_frame_8.png").convert_alpha()
        player_jump_9= pygame.image.load("characters/player/player jump/player_jump_frame_9.png").convert_alpha()
        player_jump_10= pygame.image.load("characters/player/player jump/player_jump_frame_10.png").convert_alpha()


        #Creating list for walking and jumping animations
        self.player_walk= [player_walk_1, player_walk_2, player_walk_3, player_walk_4]
        self.player_jump= [player_jump_1, player_jump_2, player_jump_3, player_jump_4, player_jump_5,
                           player_jump_6, player_jump_7, player_jump_8, player_jump_9, player_jump_10]
        
        #I forgot to resize the images accordingly so i have to write this extra line of codes
        self.player_walk = [pygame.transform.rotozoom(img, 0, 0.5) for img in self.player_walk]
        self.player_jump = [pygame.transform.rotozoom(img, 0, 0.7) for img in self.player_jump]

        self.player_index= 0

        self.image= self.player_walk[self.player_index]
        self.rect= self.image.get_rect(midbottom= (170, 640))
        self.gravity= 0


    #Function for player inputs
    def player_inputs(self):
        
        keys= pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom>= 640:
            self.gravity= -27
            snd_jump.play()


    #Function for applying gravity
    def apply_gravity(self):

        self.gravity+= 1
        self.rect.y+= self.gravity
        
        if self.rect.bottom>= 640: self.rect.bottom= 640


    #Function for animation
    def animation(self):

        if self.rect.bottom< 640:
            self.player_index+= 0.1
            if self.player_index>= len(self.player_jump): self.player_index= 0

            self.image= self.player_jump[int(self.player_index)]

        else:
            self.player_index+= 0.1
            if self.player_index>= len(self.player_walk): self.player_index= 0

            self.image= self.player_walk[int(self.player_index)]


    #Function for updating all the necessary funtions of the class
    def update(self):
        
        self.player_inputs()
        self.apply_gravity()
        self.animation()


#Creating a class for the enemies
class Enemy(pygame.sprite.Sprite):

    def __init__(self, type):

        super().__init__()

        #[type, 1= Maths enemy, 2= Physics enemy, and 3= DSA enemy]
        if type== 1:

            math_walk_1= pygame.image.load("characters/enemies/math walk/math_frame_1.png").convert_alpha()
            math_walk_2= pygame.image.load("characters/enemies/math walk/math_frame_2.png").convert_alpha()
            math_walk_3= pygame.image.load("characters/enemies/math walk/math_frame_3.png").convert_alpha()
            math_walk_4= pygame.image.load("characters/enemies/math walk/math_frame_4.png").convert_alpha()

            self.enemy= [math_walk_1, math_walk_2, math_walk_3, math_walk_4]

            #Same as here, i forgot to resize it.
            self.enemy = [pygame.transform.rotozoom(img, 0, 0.4) for img in self.enemy]

            y_pos= 640

        elif type== 2:

            einstein_walk_1= pygame.image.load("characters/enemies/einstein walk/einstein_walk_frame_1.png")
            einstein_walk_2= pygame.image.load("characters/enemies/einstein walk/einstein_walk_frame_2.png")
            einstein_walk_3= pygame.image.load("characters/enemies/einstein walk/einstein_walk_frame_3.png")
            einstein_walk_4= pygame.image.load("characters/enemies/einstein walk/einstein_walk_frame_4.png")

            self.enemy= [einstein_walk_1, einstein_walk_2, einstein_walk_3, einstein_walk_4]

            #Same as here, i forgot to resize it.
            self.enemy = [pygame.transform.rotozoom(img, 0, 0.7) for img in self.enemy]

            y_pos= 640

        else:

            dsa_walk_1= pygame.image.load("characters/enemies/computer walk/computer_walk_frame_1.png")            
            dsa_walk_2= pygame.image.load("characters/enemies/computer walk/computer_walk_frame_2.png")            
            dsa_walk_3= pygame.image.load("characters/enemies/computer walk/computer_walk_frame_3.png")            
            dsa_walk_4= pygame.image.load("characters/enemies/computer walk/computer_walk_frame_4.png")            
            dsa_walk_5= pygame.image.load("characters/enemies/computer walk/computer_walk_frame_5.png")            
            dsa_walk_6= pygame.image.load("characters/enemies/computer walk/computer_walk_frame_6.png")            

            self.enemy= [dsa_walk_1, dsa_walk_2, dsa_walk_3, dsa_walk_4, dsa_walk_5, dsa_walk_6]

            #Same as here, i forgot to resize it.
            self.enemy = [pygame.transform.rotozoom(img, 0, 0.2) for img in self.enemy]

            y_pos= 640

        #Setting the right enemy on right position
        self.animation_index= 0
        self.image= self.enemy[self.animation_index]
        self.rect= self.image.get_rect(midbottom= (randint(1300, 1450), y_pos))

        self.passed= False


    #Function for animation
    def animation(self):

        self.animation_index+= 0.1
        if self.animation_index>= len(self.enemy): self.animation_index= 0
        self.image= self.enemy[int(self.animation_index)]


    #Function for remove the enemy after going out from the screen
    def destroy(self):

        if self.rect.x<= -200:
            self.kill()


    #Function for updating all the necessary function in the class
    def update(self):

        self.animation()
        self.destroy() 
        self.rect.x-= 8      


#Function for displaying the score             
def Display_score():

    current_time= int(pygame.time.get_ticks()/ 1000)- start_time

    score_surface= font.render(f"Score: {current_time}", False, (0, 0, 0))
    score_rect= score_surface.get_rect(center= (640, 40))

    screen.blit(score_surface, score_rect)

    return current_time


#Function for checking the collision
def collision():
    
    if pygame.sprite.spritecollide(player.sprite, enemy_group, False, pygame.sprite.collide_rect_ratio(0.65)):
        
        snd_collision.play()
        pygame.mixer.music.stop()
        enemy_group.empty()
        return False
    
    else: return True


#Funtion for intro screen
def intro_screen():

    screen.blit(intro_background_surface, intro_background_rect)
    screen.blit(intro_surface, intro_rect)

    
#Function for game over screen
def  Game_over():

    msg= font.render(f"Your Score: {score}", False, (0, 0, 0))
    msg= pygame.transform.rotozoom(msg, 0, 2)
    msg_rect= msg.get_rect(center= (640, 60))

    screen.blit(game_over_background, game_over_background_rect)
    screen.blit(game_over_surface, game_over_rect)
    screen.blit(msg, msg_rect)

    game_active= False


pygame.mixer.pre_init(44100, -16, 2, 256) #To reduce the buffer of the audios
pygame.init()
pygame.mixer.init()

pygame.display.set_caption("NO MORE STUDY!!")
screen= pygame.display.set_mode((1280, 720))
clock= pygame.time.Clock()
font= pygame.font.Font("fonts/Jersey10-Regular.ttf", 40)
game_active= False
intro_active= True
intro_moving= False
game_over= False
start_time= 0
score= 0


#Making groups of sprites
player= pygame.sprite.GroupSingle()
player.add(Player())

enemy_group= pygame.sprite.Group()


#Musics
pygame.mixer.music.load("music/background/main background.wav")
pygame.mixer.music.set_volume(0.4)
snd_intro_reveal = pygame.mixer.Sound("music/background/intro screen reveal.wav")
snd_intro_reveal.set_volume(0.4)
snd_collision = pygame.mixer.Sound("music/sfx/collision.wav")
snd_jump = pygame.mixer.Sound("music/sfx/normal jump.wav")


#Map Surfaces
background_surface= pygame.image.load("background/background.png").convert_alpha()
background_surface= pygame.transform.smoothscale(background_surface, (1280, 720))

floor_surface= pygame.image.load("background/floor.png").convert_alpha()
floor_surface= pygame.transform.smoothscale(floor_surface, (1280, 720))

intro_surface= pygame.image.load("background/intro.png").convert_alpha()
intro_surface= pygame.transform.smoothscale(intro_surface, (1280, 720))
intro_rect= intro_surface.get_rect(topleft= (0, -50))

intro_background_surface= pygame.image.load("background/intro_background.jpg").convert_alpha()
intro_background_surface= pygame.transform.smoothscale(intro_background_surface, (1280, 720))
intro_background_rect= intro_background_surface.get_rect(topleft= (0, 0))

scorecard_surface= pygame.image.load("background/score card.png")
scorecard_surface= pygame.transform.smoothscale(scorecard_surface, (180, 180))
scorecard_rect= scorecard_surface.get_rect(center= (640, 43))

game_over_background= pygame.image.load("background/background1.jpg")
game_over_background= pygame.transform.smoothscale(game_over_background, (1280, 720))
game_over_background_rect= game_over_background.get_rect(topleft= (0, 0))
game_over_surface= pygame.image.load("background/game over.jpg")
game_over_surface= pygame.transform.smoothscale(game_over_surface, (740, 560))
game_over_rect= game_over_surface.get_rect(center= (640, 380))


#Timers
enemy_timer= pygame.USEREVENT+ 1
pygame.time.set_timer(enemy_timer, 1600)


while True:
    
    for event in pygame.event.get():
        
        if event.type== pygame.QUIT:
            pygame.quit()
            exit()


        #Game Starting when space is pressed
        if event.type== pygame.KEYDOWN and event.key== pygame.K_SPACE:
            if intro_active:
                if not intro_moving:
                    snd_intro_reveal.play()

                intro_moving= True
            

        #Enemy Spawing
        if game_active:
            if event.type== enemy_timer:
                enemy_group.add(Enemy(choice([1, 1, 1, 1, 1, 2, 2, 2, 3, 3])))  # 50%- Math, 30%- Physics and 20%- DSA

        if not game_active and not intro_active:
            if event.type== pygame.KEYDOWN and event.key== pygame.K_SPACE:
                game_active= True
                start_time= int(pygame.time.get_ticks()/ 1000)
                
                pygame.mixer.music.play(-1)

    screen.blit(background_surface, (0, 0))
    screen.blit(floor_surface, (0, 370))
    
    #Intro Movement logic
    if intro_active:

        intro_screen()

        if intro_moving:
            
            intro_rect.y-= 14
            intro_background_rect.y-= 14
            if intro_background_rect.y<= -720:
                
                intro_background_rect.y= -720
                intro_rect.y= -720
                intro_active= False
                game_active= True

                start_time= int(pygame.time.get_ticks()/ 1000) 

                snd_intro_reveal.fadeout(200)
                pygame.mixer.music.play(-1)


    if game_active:

        
        screen.blit(scorecard_surface, scorecard_rect)
        score= Display_score()   
        
        player.draw(screen)
        player.update()

        enemy_group.draw(screen)
        enemy_group.update()

        game_active= collision()


    else:
        
        if score== 0: intro_screen()
        else: Game_over()
        

    pygame.display.update()
    clock.tick(60)