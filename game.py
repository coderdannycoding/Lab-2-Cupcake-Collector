import pygame
import sys
import random

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Cupcake Collector")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)


player_x = 50
player_y = 300
player_dy = 0
gravity = 0.5
jump_speed = -10
on_ground = True
score = 0


player_image = pygame.image.load("player.png").convert_alpha()
player_image = pygame.transform.scale(player_image, (50, 50))

cupcake_image = pygame.image.load("cupcake.png").convert_alpha()
cupcake_image = pygame.transform.scale(cupcake_image, (30, 30))
bg_image = pygame.image.load("background.png").convert()
bg_image = pygame.transform.scale(bg_image, (600, 400))


platforms = [
    pygame.Rect(0, 350, 600, 50),   
    pygame.Rect(100, 270, 150, 20),
    pygame.Rect(350, 220, 150, 20),
    pygame.Rect(50, 150, 100, 20),   
    pygame.Rect(450, 120, 100, 20),  
    pygame.Rect(250, 60, 100, 20)    
]

cupcakes = []


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    while len(cupcakes) < 5:
        cx = random.randint(20, 550)
        cy = random.randint(20, 310)
        cupcakes.append(pygame.Rect(cx, cy, 30, 30))


    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= 5
    if keys[pygame.K_RIGHT]:
        player_x += 5


    if keys[pygame.K_UP] and on_ground:
        player_dy = jump_speed
        on_ground = False

    player_dy += gravity
    player_y += player_dy


    player_rect = pygame.Rect(player_x, player_y, 50, 50)


    on_ground = False
    for platform in platforms:
        if player_rect.colliderect(platform):
            if player_dy > 0:  
                player_y = platform.top - 50  
                player_dy = 0
                on_ground = True

 
    if player_y >= 300:
        player_y = 300
        player_dy = 0
        on_ground = True


    player_rect.y = player_y


    for cupcake in cupcakes[:]:
        if player_rect.colliderect(cupcake):
            cupcakes.remove(cupcake)
            score += 1


    screen.blit(bg_image, (0, 0))


    for platform in platforms:
        pygame.draw.rect(screen, (0, 0, 0), platform)

   
    for cupcake in cupcakes:
        screen.blit(cupcake_image, (cupcake.x, cupcake.y))


    screen.blit(player_image, (player_x, player_y))


    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))


    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
