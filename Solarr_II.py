import sys
import pygame
import time
import math
import random

pygame.mixer.init()
pygame.mixer_music.load("Sol2/data/tittle_music.mp3")
pygame.mixer.music.play(-1)
laser_sound=pygame.mixer.Sound("Sol2/data/laser_sound.mp3")
pygame.mixer.Sound.set_volume(laser_sound,0.2)
shoot_sound=pygame.mixer.Sound("Sol2/data/shoot_sound.mp3")
boss_attack_sound=pygame.mixer.Sound("Sol2/data/boss_attack_sound.mp3")
boss_warn=pygame.mixer.Sound("Sol2/data/boss_warn.mp3")
boss_death_sound=pygame.mixer.Sound("Sol2/data/boss_death_sound.mp3")
boss_entered=pygame.mixer.Sound("Sol2/data/boss_entered.mp3")


class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption("Solarr II")
        self.screen=pygame.display.set_mode((1500,700))

        self.clock=pygame.time.Clock()

        self.my_font = pygame.font.SysFont('Comic Sans MS', 30)
        self.text_tittle=self.my_font.render('Solarr II', False, (255, 250, 0))
        self.text_tittle=pygame.transform.scale(self.text_tittle,(400,100))
        self.text_play=self.my_font.render('Play', False, (255, 255, 255))
        self.text_play=pygame.transform.scale(self.text_play,(300,150))
        self.text_retry=self.my_font.render('Retry', False, (255, 255, 255))
        self.text_retry=pygame.transform.scale(self.text_retry,(300,150))
        
        self.m1,self.m2,self.m3=pygame.mouse.get_pressed(3)

        self.in_tittle=True

        self.boss_hp=150000

        self.flash_flag=True

        self.cloud_from_right=1600

        self.time_flag=True

        self.warn_flag=True

        self.the_time=0

        self.cloud_from_left=-400

        self.cloud_from_up=-100
        
        self.cloud1=pygame.image.load("Sol2/data/cloud.png")
        self.cloud1=pygame.transform.scale(self.cloud1,(300,200))
        self.cloud1c=pygame.Rect(-500,-500,0,0)
        self.rain1=pygame.image.load("Sol2/data/rain.png")
        self.rain1=pygame.transform.scale(self.rain1,(100,100))

        self.cloud2=pygame.image.load("Sol2/data/cloud.png")
        self.cloud2=pygame.transform.scale(self.cloud2,(300,200))
        self.cloud2c=pygame.Rect(-500,-500,0,0)
        self.rain2=pygame.image.load("Sol2/data/rain.png")
        self.rain2=pygame.transform.scale(self.rain2,(100,100))

        self.cloud3=pygame.image.load("Sol2/data/cloud.png")
        self.cloud3=pygame.transform.scale(self.cloud3,(300,200))
        self.cloud3c=pygame.Rect(-500,-500,0,0)
        self.rain3=pygame.image.load("Sol2/data/rain.png")
        self.rain3=pygame.transform.scale(self.rain3,(100,100))

        self.cloud4=pygame.image.load("Sol2/data/cloud.png")
        self.cloud4=pygame.transform.scale(self.cloud4,(300,200))
        self.cloud4c=pygame.Rect(-500,-500,0,0)
        self.rain4=pygame.image.load("Sol2/data/rain.png")
        self.rain4=pygame.transform.scale(self.rain4,(100,100))

        self.cloud5=pygame.image.load("Sol2/data/cloud.png")
        self.cloud5=pygame.transform.scale(self.cloud5,(300,200))
        self.cloud5c=pygame.Rect(-500,-500,0,0)
        self.rain5=pygame.image.load("Sol2/data/rain.png")
        self.rain5=pygame.transform.scale(self.rain5,(100,100))

        self.cloud6=pygame.image.load("Sol2/data/cloud.png")
        self.cloud6=pygame.transform.scale(self.cloud6,(300,200))
        self.cloud6c=pygame.Rect(-500,-500,0,0)
        self.rain6=pygame.image.load("Sol2/data/rain.png")
        self.rain6=pygame.transform.scale(self.rain6,(100,100))

        self.cloud7=pygame.image.load("Sol2/data/cloud.png")
        self.cloud7=pygame.transform.scale(self.cloud7,(300,200))
        self.cloud7c=pygame.Rect(-500,-500,0,0)
        self.rain7=pygame.image.load("Sol2/data/rain.png")
        self.rain7=pygame.transform.scale(self.rain7,(100,100))

        self.boss_attack=pygame.image.load("Sol2/data/boss_animation.png")
        self.boss_attack=pygame.transform.scale(self.boss_attack,(1500,150))
        
        self.boss_death=pygame.image.load("Sol2/data/boss_death.png")
        self.boss_death=pygame.transform.scale(self.boss_death,(600,600))

        self.boss_animation=pygame.image.load("Sol2/data/boss_attack.png")
        self.boss_animation=pygame.transform.rotate(self.boss_animation,90)
        self.boss_animation=pygame.transform.scale(self.boss_animation,(600,200))

        self.clouds2c=[0]

        self.clouds3c=[0]

        self.victory_music_flag=True

        self.cutscene=True

        self.boss_prep=1600

        self.victory_screen=pygame.image.load("Sol2/data/victory_screen.png")
        self.victory_screen=pygame.transform.scale(self.victory_screen,(1500,700))

        self.wave=1

        self.boss_entered_screen=pygame.image.load("Sol2/data/flash.png")
        self.boss_entered_screen=pygame.transform.scale(self.boss_entered_screen,(1500,700))

        self.col_rot_orb=pygame.Rect(0,0,0,0)

        self.col_rot_laser=pygame.Rect(0,0,0,0)

        self.wave_prep1=True

        self.wave_prep2=False

        self.boss_music_flag=True

        self.wave_prep3=False

        self.in_boss=False

        self.retry=False

        self.flag_1=True

        self.clouds2=[0]

        self.victory=False

        self.collision_attack=pygame.Rect(0,0,0,0)

        self.clouds3=[0]

        self.flag_2=False

        self.flag_3=False

        self.timed_flag=True

        self.boss_death_sound_flag=True

        self.boss_warn=pygame.Rect(0,0,0,0)

        self.r1=pygame.Rect(0,0,0,0)
        self.r2=pygame.Rect(0,0,0,0)

        self.r3=pygame.Rect(0,0,0,0)
        self.r4=pygame.Rect(0,0,0,0)

        self.r5=pygame.Rect(0,0,0,0)
        self.r6=pygame.Rect(0,0,0,0)
        self.r7=pygame.Rect(0,0,0,0)

        self.clicked=False

        self.first_attack_flag=True

        self.rn1=1200
        self.rn2=1200
        self.rn3=1200
        self.rn4=300

        self.rn5=100
        self.rn6=100
        self.rn7=100

        self.boss=pygame.image.load("Sol2/data/boss_cloud.png")
        self.boss=pygame.transform.scale(self.boss,(600,600))
        self.collision_boss=pygame.Rect(0,0,0,0)

        self.wave_music_flag=True

        self.flash_sound_flag=True

        self.v=0

        self.retry_music_flag=True

        self.tittle_screen=pygame.image.load("Sol2/data/tittle_screen.png")
        self.tittle_screen=pygame.transform.scale(self.tittle_screen,(1500,700))
        self.bg=pygame.image.load("Sol2/data/background.png")

        self.retry_screen=pygame.image.load("Sol2/data/retry_screen.png")
        self.retry_screen=pygame.transform.scale(self.retry_screen,(1500,700))

        self.collision_up=pygame.Rect(0,0,1500,5)
        self.collision_down=pygame.Rect(0,695,1500,100)
        self.collision_left=pygame.Rect(0,0,5,700)
        self.collision_right=pygame.Rect(1500,0,5,700)

        self.player_pos=[600,200]
        self.player_movement=[0,0,0,0]

        self.logo_sun=pygame.image.load("Sol2/data/sun.png")
        self.logo_sun=pygame.transform.scale(self.logo_sun,(150,150))

        self.player=pygame.image.load("Sol2/data/sun.png")
        self.player=pygame.transform.scale(self.player,(100,100))
        self.collision_player=pygame.Rect((self.player_pos),(100,100))

        self.orb=pygame.image.load("Sol2/data/orb.png")
        self.orb=pygame.transform.scale(self.orb,(100,100))

        self.laser=pygame.image.load("Sol2/data/beam_laser.png")
        self.laser=pygame.transform.scale(self.laser,(1500,100))

        self.l_box=pygame.Rect(self.player_pos[0],self.player_pos[1],0,0)

        self.ball=pygame.image.load("Sol2/data/ball.png")
        self.ball=pygame.transform.scale(self.ball,(300,300))

        self.step_x=0
        self.step_y=0

    def rotate(self,surface, angle, pivot, offset):

        rotated_image = pygame.transform.rotozoom(surface, -angle, 1)  # Rotate the image.
        rotated_offset = offset.rotate(angle)  # Rotate the offset vector.
        # Add the offset vector to the center/pivot point to shift the rect.
        rect = rotated_image.get_rect(center=pivot+rotated_offset)
        return rotated_image, rect  # Return the rotated image and shifted rect.

    def run(self):
        while True:

            while self.victory:

                self.screen.fill((0,0,0))
                self.player_movement=[0,0,0,0]
                

                for event in pygame.event.get():
                        if event.type==pygame.QUIT:
                            pygame.quit()
                            sys.exit()

                
                while self.v<300:

                    self.screen.fill((0,0,0))
                    self.player_movement=[0,0,0,0]
                    self.screen.blit(self.bg,(0,0))
                    self.screen.blit(self.player,self.player_pos)
                
                    for event in pygame.event.get():
                        if event.type==pygame.QUIT:
                            pygame.quit()
                            sys.exit()

                    self.screen.blit(self.boss_death,(900,50))
                    if self.boss_death_sound_flag:
                        pygame.mixer.Channel(5).play(pygame.mixer.Sound(boss_death_sound))
                        self.boss_death_sound_flag=False

                    self.v+=1

                    pygame.display.update()
                    self.clock.tick(60)

                if self.victory_music_flag:
                    pygame.mixer_music.stop()
                    pygame.mixer_music.load("Sol2/data/victory_music.mp3")
                    pygame.mixer_music.play(-1)
                    self.victory_music_flag=False

                self.screen.blit(self.victory_screen,(0,0))

                pygame.display.update()
                self.clock.tick(60)
            #end of victory
                
            while self.retry:

                if self.retry_music_flag:

                    pygame.mixer_music.stop()
                    pygame.mixer_music.load("Sol2/data/retry_music.mp3")
                    pygame.mixer.music.play(-1)
                    self.retry_music_flag=False

                self.screen.fill((0,0,0))
                self.screen.blit(self.retry_screen,(0,0))
                self.retry_button=pygame.rect.Rect(600,500,300,150) 
                pygame.draw.rect(self.screen,(255,0,0),self.retry_button)

                self.mouse_pos=pygame.mouse.get_pos()

                if pygame.rect.Rect.collidepoint(self.retry_button,self.mouse_pos):
                    pygame.draw.rect(self.screen,(200,0,0),self.retry_button)
                
                self.screen.blit(self.text_retry, (600,500))
                pygame.display.flip()

                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type==pygame.MOUSEBUTTONUP:
                        self.mouse_pos=pygame.mouse.get_pos()
                        if pygame.rect.Rect.collidepoint(self.retry_button,self.mouse_pos):
                            pygame.mixer_music.stop()
                            self.retry=False
                            self.wave_music_flag=True
                            self.boss_hp=150000

                            self.cloud_from_right=1600

                            self.col_rot_laser=pygame.rect.Rect(0,0,0,0)

                            self.cloud_from_left=-400

                            self.cloud_from_up=-100

                            self.wave=1

                            self.wave_prep1=True

                            self.wave_prep2=False

                            self.flash_flag=True

                            self.wave_prep3=False

                            self.victory=False

                            self.the_time=0

                            self.in_boss=False

                            self.flag_1=True

                            self.flag_2=False

                            self.cutscene=True

                            self.warn_flag=True

                            self.time_flag=True

                            self.boss_prep=1600

                            self.flag_3=False

                            self.boss_warn=pygame.rect.Rect(0,0,0,0)    

                            self.wave_music_flag=True

                            self.clouds1c=[]

                            self.clouds2c=[]

                            self.clouds3c=[]

                            self.v=0

                            self.boss_death_sound_flag=True

                            self.victory_music_flag=True

                            self.boss_music_flag=True

                            self.collision_attack=pygame.Rect=(0,0,0,0)

                            self.r1=pygame.rect.Rect(0,0,0,0)
                            self.r2=pygame.rect.Rect(0,0,0,0)
                            self.r3=pygame.rect.Rect(0,0,0,0)
                            self.r4=pygame.rect.Rect(0,0,0,0)

                            self.r5=pygame.rect.Rect(0,0,0,0)
                            self.r6=pygame.rect.Rect(0,0,0,0)
                            self.r7=pygame.rect.Rect(0,0,0,0)

                            self.clouds1=[]

                            self.clouds2=[]

                            self.clouds3=[]

                            self.first_attack_flag=True

                            self.retry_music_flag=True

                            self.flash_sound_flag=True

                            self.player_pos=[600,200]

                            self.collision_boss=pygame.rect.Rect(0,0,0,0)

                            self.timed_flag=True

                            self.step_x=0
                            self.step_y=0

                            self.rn1=1200
                            self.rn2=1200
                            self.rn3=1200
                            self.rn4=100

                            self.rn5=50
                            self.rn6=50
                            self.rn7=50

                            self.player_movement=[0,0,0,0]

            while self.in_tittle:

                self.screen.fill((0,0,0))
                self.screen.blit(self.tittle_screen,(0,0)) 
                self.screen.blit(self.logo_sun,(500,120))
                self.screen.blit(self.text_tittle,(550,150))
                self.start_button=pygame.rect.Rect(600,300,300,150) 
                pygame.draw.rect(self.screen,(255,175,0),self.start_button)

                self.mouse_pos=pygame.mouse.get_pos()
                if pygame.rect.Rect.collidepoint(self.start_button,self.mouse_pos):
                    pygame.draw.rect(self.screen,(255,0,0),self.start_button)

                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type==pygame.MOUSEBUTTONUP:
                        self.mouse_pos=pygame.mouse.get_pos()
                        if pygame.rect.Rect.collidepoint(self.start_button,self.mouse_pos):
                            pygame.mixer_music.stop()
                            self.in_tittle=False
                
                self.screen.blit(self.text_play,(600,300))
                    
                
                pygame.display.flip() 
                pygame.display.update()
                self.clock.tick(60)     
            #end of tittle

            self.le_time=int(pygame.time.get_ticks()/1000)

            if self.wave_music_flag:
                pygame.mixer_music.load("Sol2/data/wave_music.mp3")
                pygame.mixer.music.play(-1)
                self.wave_music_flag=False
  

            self.mouse_pos=pygame.mouse.get_pos()
            self.mouse_x=pygame.mouse.get_pos()[0]
            self.mouse_y=pygame.mouse.get_pos()[1]

            self.screen.fill((0,0,0))
            self.screen.blit(self.bg,(0,0))
            self.screen.blit(self.player,self.player_pos)
            self.collision_player=pygame.rect.Rect(self.player_pos[0],self.player_pos[1],70,70)

            if self.clicked and self.in_boss:
                self.mouse_y-=50
                pygame.mixer.Sound.play(laser_sound)
                self.dx=self.mouse_x-self.player_pos[0]
                self.dy=self.mouse_y-self.player_pos[1]
                self.rads=math.atan2(-self.dy,self.dx)
                self.rads%=2*math.pi
                self.degs=math.degrees(self.rads)

                self.of=pygame.math.Vector2(800,0)
                self.rot_laser,self.rect=self.rotate(self.laser,-self.degs,self.player_pos,self.of)
                self.screen.blit(self.rot_laser,(self.rect[0]+50,self.rect[1]+50))
                self.screen.blit(self.ball,(self.player_pos[0]-100,self.player_pos[1]-100))

                self.col_l_x=self.player_pos[0]
                self.col_l_y=self.player_pos[1]
                for i in range(100):
                    
                    self.col_rot_laser=pygame.rect.Rect(self.col_l_x,self.col_l_y,100,100)
                    if self.mouse_x>self.player_pos[0]:
                        self.nx=1
                    else:
                        self.nx=-1

                    if self.mouse_y>self.player_pos[1]:
                        self.ny=1
                    else:
                        self.ny=-1
                    self.col_l_x+=(self.nx*self.rect[2])/20
                    self.col_l_y+=(self.ny*self.rect[3])/20

                    if pygame.rect.Rect.colliderect(self.rect,self.collision_boss):
                        self.boss_hp-=1
                        if self.boss_hp<=0:
                            self.victory=True

            if self.wave==1:

                self.nc=0
                while self.wave_prep1:
                    self.player_movement=[0,0,0,0]
                    self.screen.fill((0,0,0))
                    self.screen.blit(self.bg,(0,0))
                    self.screen.blit(self.player,self.player_pos)
                    self.collision_player=pygame.rect.Rect(self.player_pos[0],self.player_pos[1],70,70)

                    for event in pygame.event.get():
                        if event.type==pygame.QUIT:
                            pygame.quit()
                            sys.exit()

                    self.clouds1=["self.cloud1"]
                    self.clouds1c=["self.cloud1c"]
                    self.screen.blit(self.cloud1,(self.cloud_from_right-self.nc,350))
                    self.cloud1c=pygame.rect.Rect(self.cloud_from_right-self.nc,350,150,100)
                    self.nc+=1
                    if self.nc>=400:
                        self.wave_prep1=False
                    pygame.display.update()
                    self.clock.tick(60)
                #end of prep 1
                
                
                if "self.cloud1c" in self.clouds1c:
                    self.screen.blit(self.cloud1,(1200,350))
                    self.cloud1c=pygame.rect.Rect(1300,400,150,100)
            
            if self.wave==2:
                self.nc=0
                while self.wave_prep2:
                    self.player_movement=[0,0,0,0]
                    self.flag_1=False
                    self.flag_2=True
                    self.screen.fill((0,0,0))
                    self.screen.blit(self.bg,(0,0))
                    self.screen.blit(self.player,self.player_pos)
                    self.collision_player=pygame.rect.Rect(self.player_pos[0],self.player_pos[1],70,70)

                    for event in pygame.event.get():
                        if event.type==pygame.QUIT:
                            pygame.quit()
                            sys.exit()

                    self.clouds2=["self.cloud1","self.cloud2","self.cloud3"]
                    self.clouds2c=["self.cloud1c","self.cloud2c","self.cloud3c"]
                    self.screen.blit(self.cloud1,(self.cloud_from_right-self.nc,350))
                    self.cloud1c=pygame.rect.Rect(self.cloud_from_right-self.nc+50,400,150,100)

                    self.screen.blit(self.cloud2,(self.cloud_from_right-self.nc,150))
                    self.cloud1c=pygame.rect.Rect(self.cloud_from_right-self.nc+50,200,150,100)

                    self.screen.blit(self.cloud3,(self.cloud_from_right-self.nc,550))
                    self.cloud1c=pygame.rect.Rect(self.cloud_from_right-self.nc+50,600,150,100)

                    self.nc+=1
                    self.player_pos=[self.player_pos[0],50]
                    if self.nc>=400:
                        self.wave_prep2=False
                    pygame.display.update()
                    self.clock.tick(60)
                #end of prep 2

                if "self.cloud1" in self.clouds2:
                    self.screen.blit(self.cloud1,(1200,350))
                    self.cloud1c=pygame.rect.Rect(1300,400,150,100)

                if "self.cloud2" in self.clouds2:
                    self.screen.blit(self.cloud2,(1200,150))
                    self.cloud2c=pygame.rect.Rect(1300,200,150,100)

                if "self.cloud3" in self.clouds2:
                    self.screen.blit(self.cloud3,(1200,550))
                    self.cloud3c=pygame.rect.Rect(1300,600,150,100)

            if self.wave==3:
                self.nc=0
                while self.wave_prep3:
                    self.player_movement=[0,0,0,0]
                    self.flag_2=False
                    self.flag_3=True
                    self.screen.fill((0,0,0))
                    self.screen.blit(self.bg,(0,0))
                    self.screen.blit(self.player,self.player_pos)
                    self.collision_player=pygame.rect.Rect(self.player_pos[0],self.player_pos[1],70,70)

                    for event in pygame.event.get():
                        if event.type==pygame.QUIT:
                            pygame.quit()
                            sys.exit()

                    self.clouds3=["self.cloud1","self.cloud4","self.cloud5","self.cloud6","self.cloud7"]
                    self.clouds3c=["self.cloud1c","self.cloud4c","self.cloud5c","self.cloud6c","self.cloud7c"]

                    self.screen.blit(self.cloud1,(self.cloud_from_right-self.nc,350))
                    self.cloud1c=pygame.rect.Rect(self.cloud_from_right-self.nc+50,400,150,100)

                    self.screen.blit(self.cloud4,(self.cloud_from_left+self.nc,350))
                    self.cloud4c=pygame.rect.Rect(self.cloud_from_left+self.nc+50,400,150,100)

                    self.screen.blit(self.cloud5,(250,self.cloud_from_up+self.nc/3))
                    self.cloud5c=pygame.rect.Rect(250,self.cloud_from_up+self.nc/3+50,150,100)

                    self.screen.blit(self.cloud6,(500,self.cloud_from_up+self.nc/3))
                    self.cloud6c=pygame.rect.Rect(500,self.cloud_from_up+self.nc/3+50,150,100)

                    self.screen.blit(self.cloud7,(850,self.cloud_from_up+self.nc/3))
                    self.cloud7c=pygame.rect.Rect(850,self.cloud_from_up+self.nc/3+50,150,100)

                    self.nc+=1
                    self.player_pos=[1400,600]
                    if self.nc>=400:
                        self.wave_prep3=False
                    pygame.display.update()
                    self.clock.tick(60)
                #end of prep 3

                if "self.cloud1" in self.clouds3:
                    self.screen.blit(self.cloud1,(1200,350))
                    self.cloud1c=pygame.rect.Rect(1300,400,150,100)

                if "self.cloud4" in self.clouds3:
                    self.screen.blit(self.cloud4,(100,350))
                    self.cloud4c=pygame.rect.Rect(200,400,150,100)

                if "self.cloud5" in self.clouds3:
                    self.screen.blit(self.cloud5,(250,50))
                    self.cloud5c=pygame.rect.Rect(350,100,150,100)

                if "self.cloud6" in self.clouds3:
                    self.screen.blit(self.cloud6,(500,50))
                    self.cloud6c=pygame.rect.Rect(600,100,150,100)

                if "self.cloud7" in self.clouds3:
                    self.screen.blit(self.cloud7,(850,50))
                    self.cloud7c=pygame.rect.Rect(950,100,150,100)

            if self.le_time%2==0:
                if "self.cloud1" in self.clouds1 or "self.cloud1" in self.clouds2 or "self.cloud1" in self.clouds3:
                    self.screen.blit(self.rain1,(self.rn1,400))
                    self.r1=pygame.rect.Rect(self.rn1,400,50,50)

                    self.rn1-=50

                if "self.cloud2" in self.clouds2:
                    self.screen.blit(self.rain2,(self.rn2,200))
                    self.r2=pygame.rect.Rect(self.rn2,300,50,50)

                    self.rn2-=50

                if "self.cloud3" in self.clouds2:
                    self.screen.blit(self.rain3,(self.rn3,650))
                    self.r3=pygame.rect.Rect(self.rn3,650,50,50)

                    self.rn3-=50
                
                if "self.cloud4" in self.clouds3:
                    self.screen.blit(self.rain4,(self.rn4,400))
                    self.r4=pygame.rect.Rect(self.rn4,450,50,50)

                    self.rn4+=50
                
                if "self.cloud5" in self.clouds3:
                    self.screen.blit(self.rain5,(300,self.rn5))
                    self.r5=pygame.rect.Rect(300,self.rn5,50,50)

                    self.rn5+=50

                if "self.cloud6" in self.clouds3:
                    self.screen.blit(self.rain6,(550,self.rn6))
                    self.r6=pygame.rect.Rect(550,self.rn6,50,50)

                    self.rn6+=50

                if "self.cloud7" in self.clouds3:
                    self.screen.blit(self.rain7,(900,self.rn7))
                    self.r7=pygame.rect.Rect(900,self.rn7,50,50)

                    self.rn7+=50
                
            else:
                self.rn1=1200
                self.rn2=1200
                self.rn3=1200

                self.rn4=100
                self.rn5=50
                self.rn6=50
                self.rn7=50

            if self.in_boss and not(self.victory):
                 
                while self.cutscene:
                    if self.boss_music_flag:
                        pygame.mixer_music.stop()
                        self.boss_music=pygame.mixer_music.load("Sol2/data/boss_music.mp3")
                        pygame.mixer_music.set_volume(0.5)
                        pygame.mixer_music.play(-1)
                        self.boss_music_flag=False

                    self.player_pos=[100,350]

                    self.player_movement=[0,0,0,0]
                    self.screen.fill((0,0,0))
                    self.screen.blit(self.bg,(0,0))
                    self.screen.blit(self.player,self.player_pos)

                    for event in pygame.event.get():
                        if event.type==pygame.QUIT:
                            pygame.quit()
                            sys.exit()

                    while self.flash_flag:

                        self.player_pos=[100,350]

                        self.player_movement=[0,0,0,0]

                        self.screen.fill((0,0,0))
                        self.screen.blit(self.bg,(0,0))
                        self.screen.blit(self.player,self.player_pos)

                        for event in pygame.event.get():
                            if event.type==pygame.QUIT:
                                pygame.quit()
                                sys.exit()
                        
                        if self.flash_sound_flag:
                            pygame.mixer.Sound.play(boss_entered)
                            self.flash_sound_flag=False

                        self.a=0
                        while self.a<=60:

                            for event in pygame.event.get():
                                if event.type==pygame.QUIT:
                                    pygame.quit()
                                    sys.exit()

                            self.player_movement=[0,0,0,0]
                            self.screen.fill((0,0,0))
                            self.screen.blit(self.bg,(0,0))
                            self.screen.blit(self.player,self.player_pos)

                            self.screen.blit(self.boss_entered_screen,(0,0))
                            self.a+=1
                            pygame.display.update()
                            self.clock.tick(60)
                        

                        pygame.display.update()
                        self.clock.tick(60)
                        self.flash_flag=False
                    #end of flash
                    self.screen.blit(self.boss,(self.boss_prep,50))
                    self.boss_prep-=1
                    if self.boss_prep<=900:
                        self.cutscene=False
                    pygame.display.update()
                    self.clock.tick(60)
                #end of cutscene
                
                self.screen.blit(self.boss,(900,50))
                self.collision_boss=pygame.rect.Rect(900,50,600,600)

                
                if self.the_time>90:
                    self.the_time=0
                self.collision_attack=pygame.rect.Rect(0,0,0,0)
                if self.the_time>30 and self.the_time<70:

                    if self.warn_flag:
                        self.light_y=random.randint(0,700)
                        if self.first_attack_flag:
                            self.light_y=100
                        pygame.mixer.Channel(1).play(pygame.mixer.Sound(boss_warn))
                        self.boss_warn_rect=pygame.rect.Rect(0,self.light_y,1500,150)
                        pygame.draw.rect(self.screen,(0,100,255),self.boss_warn_rect)
                        self.screen.blit(self.boss_animation,(900,250))
                        self.first_attack_flag=False
                        self.warn_flag=False
                        self.attack_flag=True

                elif self.the_time>70:

                    if self.attack_flag:

                        pygame.mixer.Channel(2).play(pygame.mixer.Sound(boss_attack_sound))
                        self.screen.blit(self.boss_attack,(0,self.light_y))
                        self.screen.blit(self.boss_attack,(0,self.light_y-50))
                        self.screen.blit(self.boss_attack,(0,self.light_y+50))
                        self.collision_attack=pygame.rect.Rect(0,self.light_y,1500,150)
                        self.attack_flag=False
                        self.warn_flag=True     

                else:
                    pass

                self.the_time+=1
            #end of boss
         

            if pygame.rect.Rect.colliderect(self.collision_player,self.collision_attack):
                self.retry=True
                        
            if pygame.rect.Rect.colliderect(self.collision_player,self.r1):
                self.retry=True

            if pygame.rect.Rect.colliderect(self.collision_player,self.r2):
                self.retry=True

            if pygame.rect.Rect.colliderect(self.collision_player,self.r3):
                self.retry=True

            if pygame.rect.Rect.colliderect(self.collision_player,self.r4):
                self.retry=True

            if pygame.rect.Rect.colliderect(self.collision_player,self.r5):
                self.retry=True

            if pygame.rect.Rect.colliderect(self.collision_player,self.r6):
                self.retry=True

            if pygame.rect.Rect.colliderect(self.collision_player,self.r7):
                self.retry=True     
            
            if pygame.rect.Rect.colliderect(self.collision_player,self.collision_up):
                self.player_movement[0]=0

            if pygame.rect.Rect.colliderect(self.collision_player,self.collision_down):
                self.player_movement[1]=0
            
            if pygame.rect.Rect.colliderect(self.collision_player,self.collision_left):
                self.player_movement[2]=0

            if pygame.rect.Rect.colliderect(self.collision_player,self.collision_right):
                self.player_movement[3]=0

            self.player_pos[0]+=self.player_movement[2]
            self.player_pos[0]+=self.player_movement[3]
            self.player_pos[1]+=self.player_movement[0]
            self.player_pos[1]+=self.player_movement[1]

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type==pygame.KEYDOWN:
                    if self.clicked:
                        self.f=7
                    else:
                        self.f=10
                    if event.key==pygame.K_w:
                        self.player_movement[0]-=self.f
                    if event.key==pygame.K_s:
                        self.player_movement[1]+=self.f
                    if event.key==pygame.K_a:
                        self.player_movement[2]-=self.f
                    if event.key==pygame.K_d:
                        self.player_movement[3]+=self.f

                if event.type==pygame.KEYUP:
                    if event.key==pygame.K_w:
                        self.player_movement[0]=0
                    if event.key==pygame.K_s:
                        self.player_movement[1]=0
                    if event.key==pygame.K_a:
                        self.player_movement[2]=0
                    if event.key==pygame.K_d:
                        self.player_movement[3]=0

                if event.type==pygame.MOUSEBUTTONDOWN:
                    if self.in_boss:
                        self.clicked=True
                    else:
                        self.mouse_y-=50
                        pygame.mixer.Sound.play(shoot_sound)
                        self.dx=self.mouse_x-self.player_pos[0]
                        self.dy=self.mouse_y-self.player_pos[1]
                        self.rads=math.atan2(-self.dy,self.dx)
                        self.rads%=2*math.pi
                        self.degs=math.degrees(self.rads)

                        self.of=pygame.math.Vector2(200,0)
                        self.rot_orb,self.rect=self.rotate(self.orb,-self.degs,self.player_pos,self.of)
                        self.screen.blit(self.rot_orb,(self.rect[0]+50,self.rect[1]+50))

                        self.col_l_x=self.player_pos[0]
                        self.col_l_y=self.player_pos[1]
                        for i in range(20):
                            
                            self.col_rot_orb=pygame.rect.Rect(self.col_l_x,self.col_l_y,100,100)
                            if self.mouse_x>self.player_pos[0]:
                                self.nx=1
                            else:
                                self.nx=-1

                            if self.mouse_y>self.player_pos[1]:
                                self.ny=1
                            else:
                                self.ny=-1
                            self.col_l_x+=(self.nx*self.rect[2])/20
                            self.col_l_y+=(self.ny*self.rect[3])/20

                        if self.wave==1 and self.flag_1:
                            if pygame.rect.Rect.colliderect(self.col_rot_orb,self.cloud1c):
                                if "self.cloud1" in self.clouds1 and "self.cloud1c" in self.clouds1c:
                                    self.clouds1.remove("self.cloud1")
                                    self.clouds1c.remove("self.cloud1c")
                                    self.cloud1c=pygame.rect.Rect(-500,-500,150,100)
                                    self.r1=pygame.rect.Rect(0,0,0,0)
                                
                                if self.clouds1c==[]:
                                    self.wave=2
                                    self.wave_prep2=True
                        #wave 1
                        if self.wave==2 and self.flag_2:
                            if pygame.rect.Rect.colliderect(self.col_rot_orb,self.cloud1c):
                                if "self.cloud1" in self.clouds2 and "self.cloud1c" in self.clouds2c:
                                    self.clouds2.remove("self.cloud1")
                                    self.clouds2c.remove("self.cloud1c")
                                    self.cloud1c=pygame.rect.Rect(-500,-500,150,100)
                                    self.r1=pygame.rect.Rect(0,0,0,0)
                                
                                if self.clouds2c==[]:
                                    self.wave=3
                                    self.wave_prep3=True

                            if pygame.rect.Rect.colliderect(self.col_rot_orb,self.cloud2c):
                                if "self.cloud2" in self.clouds2 and "self.cloud2c" in self.clouds2c:
                                    self.clouds2.remove("self.cloud2")
                                    self.clouds2c.remove("self.cloud2c")
                                    self.cloud2c=pygame.rect.Rect(-500,-500,150,100)
                                    self.r2=pygame.rect.Rect(0,0,0,0)
                                
                                if self.clouds2c==[]:
                                    self.wave=3
                                    self.wave_prep3=True

                            if pygame.rect.Rect.colliderect(self.col_rot_orb,self.cloud3c):
                                if "self.cloud3" in self.clouds2 and "self.cloud3c" in self.clouds2c:
                                    self.clouds2.remove("self.cloud3")
                                    self.clouds2c.remove("self.cloud3c")
                                    self.cloud3c=pygame.rect.Rect(-500,-500,150,100)
                                    self.r3=pygame.rect.Rect(0,0,0,0)
                                
                                if self.clouds2c==[]:
                                    self.wave=3
                                    self.wave_prep3=True
                        #wave2
                        if self.wave==3 and self.flag_3:
                            if pygame.rect.Rect.colliderect(self.col_rot_orb,self.cloud1c):
                                if "self.cloud1" in self.clouds3 and "self.cloud1c" in self.clouds3c:
                                    self.clouds3.remove("self.cloud1")
                                    self.clouds3c.remove("self.cloud1c")
                                    self.cloud1c=pygame.rect.Rect(-500,-500,150,100)
                                    self.r1=pygame.rect.Rect(0,0,0,0)
                                
                                if self.clouds3c==[]:
                                    self.wave=4
                                    self.in_boss=True

                            if pygame.rect.Rect.colliderect(self.col_rot_orb,self.cloud4c):
                                if "self.cloud4" in self.clouds3 and "self.cloud4c" in self.clouds3c:
                                    self.clouds3.remove("self.cloud4")
                                    self.clouds3c.remove("self.cloud4c")
                                    self.cloud4c=pygame.rect.Rect(-500,-500,150,100)
                                    self.r4=pygame.rect.Rect(0,0,0,0)
                                
                                if self.clouds3c==[]:
                                    self.wave=4
                                    self.in_boss=True

                            if pygame.rect.Rect.colliderect(self.col_rot_orb,self.cloud5c):
                                if "self.cloud5" in self.clouds3 and "self.cloud5c" in self.clouds3c:
                                    self.clouds3.remove("self.cloud5")
                                    self.clouds3c.remove("self.cloud5c")
                                    self.cloud5c=pygame.rect.Rect(-500,-500,150,100)
                                    self.r5=pygame.rect.Rect(0,0,0,0)
                                
                                if self.clouds3c==[]:
                                    self.wave=4
                                    self.in_boss=True

                            if pygame.rect.Rect.colliderect(self.col_rot_orb,self.cloud6c):
                                if "self.cloud6" in self.clouds3 and "self.cloud6c" in self.clouds3c:
                                    self.clouds3.remove("self.cloud6")
                                    self.clouds3c.remove("self.cloud6c")
                                    self.cloud6c=pygame.rect.Rect(-500,-500,150,100)
                                    self.r6=pygame.rect.Rect(0,0,0,0)
                                
                                if self.clouds3c==[]:
                                    self.wave=4
                                    self.in_boss=True

                            if pygame.rect.Rect.colliderect(self.col_rot_orb,self.cloud7c):
                                if "self.cloud7" in self.clouds3 and "self.cloud7c" in self.clouds3c:
                                    self.clouds3.remove("self.cloud7")
                                    self.clouds3c.remove("self.cloud7c")
                                    self.cloud7c=pygame.rect.Rect(-500,-500,150,100)
                                    self.r7=pygame.rect.Rect(0,0,0,0)
                                
                                if self.clouds3c==[]:
                                    self.wave=4
                                    self.in_boss=True
                        #wave 3


                if event.type==pygame.MOUSEBUTTONUP:
                    self.clicked=False
                    
            pygame.display.update()
            self.clock.tick(60)

Game().run()
