import pygame 
from random import randrange

RES = 850
SIZE = 50

x, y = randrange(0, RES, SIZE), randrange(0, RES,  SIZE)
apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
directs = { 'w':True, 'a':True, 's':True, 'd':True}
length = 1
snake = [(x, y)]
dx, dy = 0, 0
fps = 5
score = 0

pygame.init()
sc = pygame.display.set_mode([RES, RES])
clock = pygame.time.Clock()
font_score = pygame.font.SysFont('Arial', 26, bold = True)

while True:
	sc.fill(pygame.Color('black'))
	# drawing snake
	[(pygame.draw.rect(sc, pygame.Color('green'), (i, j, SIZE - 2, SIZE - 2))) for i, j in snake]
	pygame.draw.rect(sc, pygame.Color('red'), (*apple, SIZE, SIZE))
	# Score
	render_score = font_score.render(f'SCORE: {score}', 1, pygame.Color('orange'))
	sc.blit(render_score, (5, 5))
	# snake movement
	x += dx * SIZE
	y += dy * SIZE
	snake.append((x, y))
	snake = snake[-length: ]
	# eating apple
	if snake[-1] == apple:
		 apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
		 length += 1	
		 fps += 1
		 score += 1
	# game over
	if x < 0 - SIZE or x > RES or y < 0 - SIZE or y > RES or len(snake) != len(set(snake)):
		break

	pygame. display.flip()
	clock.tick(fps)
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()
			
	#control
	key = pygame.key.get_pressed()
	# For W
	if key[pygame.K_w] and directs['w']:
		dx, dy = 0, -1
		directs = { 'w':True, 'a':True, 's':False, 'd':True}
	# For S
	if key[pygame.K_s] and directs['s']:
		dx, dy = 0, 1
		directs = { 'w':False, 'a':True, 's':True, 'd':True}
	# For A
	if key[pygame.K_a] and directs['a']:
		dx, dy = -1, 0
		directs = { 'w':True, 'a':True, 's':True, 'd':False}

	# For D
	if key[pygame.K_d] and directs['d']:
		dx, dy = 1, 0	
		directs = { 'w':True, 'a':False, 's':True, 'd':True}

