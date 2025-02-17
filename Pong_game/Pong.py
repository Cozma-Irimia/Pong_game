import pygame
import random

pygame.init()

#initializari
WIDTH, HEIGHT = 1000, 600
wn = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PONG GAME")
run = True

#variables for angles
direction  =[0, 1]
angle = [0, 1, 2]

#colors RGB
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#ball
radius = 15
ball_x, ball_y = WIDTH/2 - radius, HEIGHT/2 - radius
ball_velocity_x = 0.7
ball_velocity_y = 0.7

#pozitii palete
paddle_width = 20
paddle_height = 120
left_paddle_y = right_paddle_y = HEIGHT/2 - paddle_height/2
left_paddle_x = 100 - paddle_width/2
right_paddle_x = WIDTH - (100 - paddle_width/2) 
right_paddle_vellocity = left_paddle_vellocity = 0

#gadgets
left_gadgets = 0
right_gadgets = 0
left_gadgets_remaining = 5
right_gadgets_remaining = 5

#main loop
while run:
    wn.fill(BLACK)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_UP:
                right_paddle_vellocity = -0.9
            if i.key == pygame.K_DOWN:
                right_paddle_vellocity = 0.9
            if i.key == pygame.K_RIGHT and right_gadgets_remaining > 0:
                right_gadgets = 1       
            if i.key == pygame.K_w:
                left_paddle_vellocity = -0.9
            if i.key == pygame.K_s:
                left_paddle_vellocity = 0.9
            if i.key == pygame.K_d and left_gadgets_remaining>0:
                left_gadgets = 1


        if i.type == pygame.KEYUP:
            right_paddle_vellocity = 0
            left_paddle_vellocity = 0  

    #Miscarile controlate ale mingii
    #verific daca mingea iese in afara ferestrei
    if ball_y <= 0 + radius or ball_y >= HEIGHT - radius:
        ball_velocity_y *= -1
        #the ball bounces of the wall
    
    #verific contactul cu margina din partea dreapta
    if ball_x >= WIDTH - radius:
        ball_x, ball_y = WIDTH/2 - radius, HEIGHT/2 - radius #initial position
        dir = random.choice(direction)
        ang = random.choice(angle)
        if dir == 0:
            if ang == 0:
                ball_velocity_x = -1.4
                ball_velocity_y = 0.7
            if ang == 1: 
                ball_velocity_x = -0.7
                ball_velocity_y = 0.7
            if ang == 2:
                ball_velocity_x = 0.7
                ball_velocity_y = 1.4
        if dir == 0:
            if ang == 0:
                ball_velocity_x = -1.4
                ball_velocity_y = 0.7
            if ang == 1:
                ball_velocity_x = -0.7
                ball_velocity_y = 0.7
            if ang == 2:
                ball_velocity_x = 0.7
                ball_velocity_y = 1.4          
        ball_velocity_x *= -1
        ball_velocity_y *= -1
        
    #verific contactul cu marginea din stanga     
    if ball_x <= 0+radius:
        ball_x, ball_y = WIDTH/2 - radius, HEIGHT/2 - radius
        dir = random.choice(direction)
        ang = random.choice(angle)
        if dir == 0:
            if ang == 0:
                ball_velocity_x = 1.4
                ball_velocity_y = 0.7 
            if ang == 1:
                ball_velocity_x = 0.7
                ball_velocity_y = 0.7
            if ang == 2:
                ball_velocity_x = 0.7
                ball_velocity_y = 1.4
        if dir == 0:
            if ang == 0:
                ball_velocity_x = -1.4
                ball_velocity_y = 0.7
            if ang == 1:
                ball_velocity_x = -0.7
                ball_velocity_y = 0.7
            if ang == 2:
                ball_velocity_x = 0.7
                ball_velocity_y = 1.4  
        ball_velocity_x = 0.7
        ball_velocity_y = 0.7 #imitial speed

    #Miscari
    ball_x += ball_velocity_x
    ball_y += ball_velocity_y
    right_paddle_y += right_paddle_vellocity
    left_paddle_y += left_paddle_vellocity

    #movements control
    if left_paddle_y >= HEIGHT -paddle_height:
        left_paddle_y =  HEIGHT -paddle_height 
    if left_paddle_y <= 0 :
        left_paddle_y = 0
    if right_paddle_y >= HEIGHT -paddle_height:
        right_paddle_y =  HEIGHT -paddle_height
    if right_paddle_y <= 0:
        right_paddle_y = 0

    #coliziuni
    #left_paddle
    if left_paddle_x <= ball_x<= left_paddle_x + paddle_width:
        if left_paddle_y <= ball_y <= left_paddle_y + paddle_height:
            ball_x = left_paddle_x + paddle_height
            ball_velocity_x = ball_velocity_x * (-1)

    #right_paddle
    if right_paddle_x <= ball_x <= right_paddle_x + paddle_width:
        if right_paddle_y <= ball_y <= right_paddle_y + paddle_height:
            ball_x = right_paddle_x - radius - 1 
            ball_velocity_x = ball_velocity_x * (-1)

    #gadgets action
    if left_gadgets ==1:
        if left_paddle_x <= ball_x<= left_paddle_x + paddle_width:
            if left_paddle_y <= ball_y <= left_paddle_y + paddle_height:
                ball_x = left_paddle_x + paddle_height
                ball_velocity_x = ball_velocity_x * (-3.5)
                left_gadgets = 0
                left_gadgets_remaining = left_gadgets_remaining - 1
    
    if right_gadgets == 1:
        if right_paddle_x <= ball_x <= right_paddle_x + paddle_width:
            if right_paddle_y <= ball_y <= right_paddle_y + paddle_height:
                ball_x = right_paddle_x - radius - 1 
                ball_velocity_x = ball_velocity_x * (-3.5)
                ball_velocity_x *= (-3.5)
                right_gadgets = 0
                right_gadgets_remaining = right_gadgets_remaining - 1        


    pygame.draw.circle(wn, BLUE, (ball_x, ball_y), radius)
    pygame.draw.rect(wn, RED, pygame.Rect(left_paddle_x, left_paddle_y, paddle_width, paddle_height))
    pygame.draw.rect(wn, RED, pygame.Rect(right_paddle_x, right_paddle_y, paddle_width, paddle_height))
    
    if left_gadgets == 1:
        pygame.draw.circle(wn,WHITE,(left_paddle_x + 10,left_paddle_y + 10), 4)
    if right_gadgets == 1:
        pygame.draw.circle(wn,WHITE,(right_paddle_x + 10, right_paddle_y + 10), 4)
    pygame.display.update()