import pygame

pygame.init()
pygame.font.init()

white = (255, 255, 255)
screen = pygame.display.set_mode((600, 600))
background = pygame.image.load('background.png')

pygame.display.set_caption("Reaction Timer")

font = pygame.font.Font('freesansbold.ttf', 32)

start_text = font.render('Get ready...', True, white)
text_stop = font.render('Press [Space] to stop the timer', True, white)
text1 = font.render('Your Reaction Time here is...', True, white)
text_exit = font.render('Press [Space] to quit', True, white)


game_run = True
start_scene = True
display_scene = True
wait_timer = 0
while start_scene:
    screen.fill((0, 0, 0))
    screen.blit(text_stop, (50,200))
    screen.blit(start_text, (200, 300))
    wait_timer += 0.01
    if wait_timer > 10:
        start_scene = False
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start_scene = False
            game_run = False
            display_scene = False
timer = 0
i = 4
stop = False
while game_run:
    timer += 0.01
    timer_length_before = len(str(timer)[:i])
    text2 = font.render(str(timer)[:i], True, white)
    if str(timer)[:i][-2] == '.':
        i += 1
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    screen.blit(text1, (75, 100))
    screen.blit(text2, (275, 150))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_run = False
            display_scene = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_run = False
    pygame.display.update()

while display_scene:
    new_time = str(timer)[:i]
    text3 = font.render(str(new_time), True, white)
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    screen.blit(text1, (75, 100))
    screen.blit(text3, (275, 150))
    screen.blit(text_exit, (125, 200))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            display_scene = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                display_scene = False
    pygame.display.update()
