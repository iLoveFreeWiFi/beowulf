#!/usr/bin/env python

''' standard '''
import pygame, random, sys
from pygame.locals import *
pygame.init()

''' engine files '''
import maps

map = maps.spawn('plain')

''' config '''
sizeX = 1360
sizeY = 800
''' window title '''
pygame.display.set_caption("Beowulf")
''' window dimensions '''
screen = pygame.display.set_mode((sizeX, sizeY), 0, 32)

''' images used '''
playerfile = "beo-overworld-front.png"

''' convert images for pygame '''
grass = {
	'grass1': pygame.image.load("tiles/grass1.png").convert(),
	'grass2': pygame.image.load("tiles/grass2.png").convert(),
	'grass3': pygame.image.load("tiles/grass3.png").convert(),
	'grass4': pygame.image.load("tiles/grass4.png").convert(),
}
player = pygame.image.load(playerfile).convert_alpha()
fireball = pygame.image.load("fireball.png").convert_alpha()

playerpos = {'x': sizeX / 2, 'y': sizeY / 2}
fireballs = {}

fireballcount = 0

''' limits frame rate '''
clock = pygame.time.Clock()
                                                                                                             
''' hide system cursor '''
pygame.mouse.set_visible(True)

count = 0
grasstiles = {}
for y in range(0,sizeY,16):
		for x in range(0,sizeX,16):
			grasstiles[count] = {'x': x, 'y': y, 'pos': random.randrange(1, 5)}
			count += 1

while True:
	for event in pygame.event.get():
		if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
			pygame.quit()
			sys.exit()
			
	''' Now we have initialized everything, lets start with the main part '''
	
	for count in grasstiles:
		screen.blit(grass['grass' + str(grasstiles[count]['pos'])], (grasstiles[count]['x'],grasstiles[count]['y']))
	
	''' WASD movement '''
	if event.type == KEYDOWN and event.key == K_w:
		playerpos['y'] -= 1
	if event.type == KEYDOWN and event.key == K_s:
		playerpos['y'] += 1
	if event.type == KEYDOWN and event.key == K_a:
		playerpos['x'] -= 1
	if event.type == KEYDOWN and event.key == K_d:
		playerpos['x'] += 1
		
	''' fireballs '''	
	if event.type == KEYDOWN and event.key == K_q:
		fireballcount += 1
		fireballs[fireballcount] = {'x': playerpos['x'] + 16, 'y': playerpos['y'] + 16, 'active': 0}
		
	for ball in fireballs:
		fireballs[ball]['x'] -= fireballs[ball]['active'] * 0
		fireballs[ball]['y'] -= fireballs[ball]['active'] * 1.2
		screen.blit(fireball, (fireballs[ball]['x'], fireballs[ball]['y']))
		fireballs[ball]['active'] += 1

	screen.blit(player, (playerpos['x'],playerpos['y']))
	
	pygame.display.flip()
	
	''' Finish off by updating our display '''
	pygame.display.update()