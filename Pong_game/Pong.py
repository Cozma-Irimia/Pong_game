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

#ball
radius = 15
ball_x, ball_y = WIDTH/2 - radius, HEIGHT/2 - radius
ball_velocity_x = 1
ball_velocity_y = 1

#pozitii palete
paddle_width = 20
paddle_height = 120
left_paddle_y = right_paddle_y = HEIGHT/2 - paddle_height/2
left_paddle_x = 100 - paddle_width/2
right_paddle_x = WIDTH - (100 - paddle_width/2)

#main loop
while run:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False

    pygame.draw.circle(wn, BLUE, (ball_x, ball_y), radius)
    pygame.draw.rect(wn, RED, pygame.Rect(left_paddle_x, left_paddle_y, paddle_width, paddle_height))
    pygame.draw.rect(wn, RED, pygame.Rect(right_paddle_x, right_paddle_y, paddle_width, paddle_height))
    pygame.display.update()