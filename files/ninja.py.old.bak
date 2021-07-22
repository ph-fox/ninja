import pygame, random
from math import sqrt

pygame.init()

screen = pygame.display.set_mode((600, 400))
background = pygame.image.load('background.jpg')

pygame.display.set_caption('ninja')
icon = pygame.image.load('ninja.png')
pygame.display.set_icon(icon)

playerImg = pygame.image.load('ninja.png')
playerX = 295
playerY = 340
playerX_change = 0

weaponImg = pygame.image.load('kunai.png')
weaponX = 0
weaponY = 400
weaponX_change = 0.1
weaponY_change = 0.3
weapon_state = True

samuraiImg = pygame.image.load('samurai.png')
samuraiX = random.randint(0,539)
samuraiY = random.randint(50, 150)
samuraiX_change = 0.1
samuraiY_change = 20

score = 0

def player(x,y):
	screen.blit(playerImg, (x,y))

def samurai(x,y):
	screen.blit(samuraiImg, (x,y))

def isCollision(samuraiX, samuraiY, weaponX, weaponY):
	distance = sqrt((pow(samuraiX-weaponX,2)+pow(samuraiY-weaponY,2)))
	if distance < 27:
		return True
	else:
		return False

def atk(x,y):
	global weapon_state
	weapon_state = False
	screen.blit(weaponImg, (x+16,y+10))

running = True
while running:
	screen.fill((105,105,105))
	#screen.blit(background, (0,0))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				playerX_change = -0.2
			elif event.key == pygame.K_RIGHT:
				playerX_change = 0.2
			elif event.key == pygame.K_UP:
				if weapon_state is True:
					weaponX =  playerX
					atk(weaponX,weaponY)

		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				playerX_change = 0

	playerX += playerX_change
	if playerX <= 0:
		playerX=0
	elif playerX >= 540:
		playerX = 540

	samuraiX += samuraiX_change
	if samuraiX <= 0:
		samuraiX_change = 0.1
		samuraiY += samuraiY_change
	elif samuraiX >= 540:
		samuraiX_change = -0.1
		samuraiY += samuraiY_change

	if weaponY <= 0:
		weaponY = 400
		weapon_state = True
	elif weapon_state is False:
		atk(weaponX, weaponY)
		weaponY -= weaponY_change

	collision = isCollision(samuraiX, samuraiY, weaponX, weaponY)
	if collision:
		weaponY = 400
		weapon_state = True
		score+=1
		print(score)
		samuraiX = random.randint(0,539)
		samuraiY = random.randint(50, 150)

	player(playerX, playerY)
	samurai(samuraiX, samuraiY)
	pygame.display.update()
