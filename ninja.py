import pygame, random
from math import sqrt

pygame.init()

screen = pygame.display.set_mode((600, 400))
background = pygame.image.load('files/background.jpg')

pygame.display.set_caption('ninja')
icon = pygame.image.load('files/ninja.png')
pygame.display.set_icon(icon)

playerImg = pygame.image.load('files/ninja.png')
playerX = 295
playerY = 340
playerX_change = 0

weaponImg = pygame.image.load('files/kunai.png')
weaponX = 0
weaponY = 400
weaponX_change = 0.1
weaponY_change = 0.5
weapon_state = True

samuraiImg = []
samuraiX = []
samuraiY = []
samuraiX_change = []
samuraiY_change = []
samurai_count = 3
for i in range(samurai_count):
	samuraiImg.append(pygame.image.load('files/samurai.png'))
	samuraiX.append(random.randint(0,539))
	samuraiY.append(random.randint(50, 150))
	samuraiX_change.append(0.1)
	samuraiY_change.append(20)

kill_count = 0
kill_text = pygame.font.Font('freesansbold.ttf',32)
kill_textX = 10
kill_textY = 10

you_die = pygame.font.Font('freesansbold.ttf',64)

def death_msg():
	dm = you_die.render("You Died! ",True, (255,0 ,0))
	screen.blit(dm, (150,200))

def kill_display(x, y):
	kills = kill_text.render(f"Kills: {kill_count}",True, (255, 255 ,255))
	screen.blit(kills, (x,y))

def player(x,y):
	screen.blit(playerImg, (x,y))

def samurai(x,y, i):
	screen.blit(samuraiImg[i], (x,y))

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
				playerX_change = -0.4
			elif event.key == pygame.K_RIGHT:
				playerX_change = 0.4
			elif event.key == pygame.K_UP:
				if weapon_state is True:
					throw_sfx = pygame.mixer.Sound('files/throwv2.wav')
					throw_sfx.play()
					weaponX =  playerX
					atk(weaponX,weaponY)

		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				playerX_change = 0

	for i in range(samurai_count):
		if samuraiY[i] > 270:
			for x in range(samurai_count):
				samuraiY[x] = 2000
			death_msg()
			break

		samuraiX[i] += samuraiX_change[i]
		if samuraiX[i] <= 0:
			samuraiX_change[i] = 0.2
			samuraiY[i] += samuraiY_change[i]
		elif samuraiX[i] >= 540:
			samuraiX_change[i] = -0.2
			samuraiY[i] += samuraiY_change[i]

		collision = isCollision(samuraiX[i], samuraiY[i], weaponX, weaponY)
		if collision:
			hit_sfx = pygame.mixer.Sound('files/hitv2.wav')
			hit_sfx.play()
			weaponY = 400
			weapon_state = True
			kill_count+=1
			samuraiX[i] = random.randint(0,539)
			samuraiY[i] = random.randint(50, 150)

		samurai(samuraiX[i], samuraiY[i], i)

	playerX += playerX_change
	if playerX <= 0:
		playerX=0
	elif playerX >= 540:
		playerX = 540

	if weaponY <= 0:
		weaponY = 400
		weapon_state = True
	elif weapon_state is False:
		atk(weaponX, weaponY)
		weaponY -= weaponY_change

	kill_display(kill_textX,kill_textY)
	player(playerX, playerY)
	pygame.display.update()
