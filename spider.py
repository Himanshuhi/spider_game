import pygame
import random

#in this game we need to touch sider for points
pygame.init()

screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Hunt the Spider")

clock = pygame.time.Clock()

spider_image = pygame.image.load("spider.jpeg").convert_alpha()

spider_size = spider_image.get_size()
spider_pos = [random.randint(0, screen_width - spider_size[0]), 
              random.randint(0, screen_height - spider_size[1])]
spider_speed = 3


score = 0
font = pygame.font.Font(None, 36)


running = True
while running:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if spider_pos[0] <= mouse_pos[0] <= spider_pos[0] + spider_size[0] \
                    and spider_pos[1] <= mouse_pos[1] <= spider_pos[1] + spider_size[1]:
                score += 1
                spider_pos = [random.randint(0, screen_width - spider_size[0]), 
                              random.randint(0, screen_height - spider_size[1])]
    
    
    spider_pos[0] += random.randint(-spider_speed, spider_speed)
    spider_pos[1] += random.randint(-spider_speed, spider_speed)
    if spider_pos[0] < 0:
        spider_pos[0] = 0
    elif spider_pos[0] > screen_width - spider_size[0]:
        spider_pos[0] = screen_width - spider_size[0]
    if spider_pos[1] < 0:
        spider_pos[1] = 0
    elif spider_pos[1] > screen_height - spider_size[1]:
        spider_pos[1] = screen_height - spider_size[1]
    
   
    screen.fill((255, 255, 255))
    screen.blit(spider_image, spider_pos)
    score_text = font.render("Score: " + str(score), True, (0, 0, 0))
    screen.blit(score_text, (10, 10))
    pygame.display.flip()
    
    
    clock.tick(60)


pygame.quit()
