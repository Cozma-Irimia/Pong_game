import pygame

pygame.init()

#initializari
WIDTH, HEIGHT = 1000, 600
wn = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PONG GAME")
run = True

#colors RGB
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

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
            if i.key == pygame.K_w:
                left_paddle_vellocity = -0.9
            if i.key == pygame.K_s:
                left_paddle_vellocity = 0.9

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
        ball_velocity_x *= -1
        ball_velocity_y *= -1
        
    #verific contactul cu marginea din stanga     
    if ball_x <= 0+radius:
        ball_x, ball_y = WIDTH/2 - radius, HEIGHT/2 - radius
        ball_velocity_x = 0.7
        ball_velocity_y = 0.7 #imitial speed

    #Miscari
    ball_x += ball_velocity_x
    ball_y += ball_velocity_y
    right_paddle_y += right_paddle_vellocity
    left_paddle_y += left_paddle_vellocity

    pygame.draw.circle(wn, BLUE, (ball_x, ball_y), radius)
    pygame.draw.rect(wn, RED, pygame.Rect(left_paddle_x, left_paddle_y, paddle_width, paddle_height))
    pygame.draw.rect(wn, RED, pygame.Rect(right_paddle_x, right_paddle_y, paddle_width, paddle_height))
    pygame.display.update()