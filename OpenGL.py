#Universidad del Valle de Guatemala
#Laurelinda Gómez
#25/11/2021
#Ultimo proyecto... :)
#main
import pygame
from pygame.locals import *
from pygame import mixer
from gl import Renderer, Model
import glm
import shaders
deltaTime = 0.0

# pygame
pygame.init()
clock = pygame.time.Clock()
screenSize = (970, 570)
screen = pygame.display.set_mode(screenSize, DOUBLEBUF | OPENGL)

# OpenGL
r = Renderer(screen)
r.camPosition.z = 3
r.pointLight.x = 5

r.setShaders(shaders.vertex_shader, shaders.fragment_shader)

# modelo de los lentes
r.modelList.append(Model('./models/camera.obj', './models/camera.bmp', scale = glm.vec3(1, 1, 1)))

mixer.music.load('./music/musica.mp3')
mixer.music.play(-1)

isPlaying = True
while isPlaying:
    keys = pygame.key.get_pressed()
    # El movimiento de la cámara
    if keys[K_d]:
        r.camPosition.x += 1 * deltaTime
    if keys[K_a]:
        r.camPosition.x -= 1 * deltaTime
    if keys[K_w]:
        r.camPosition.z -= 1 * deltaTime
    if keys[K_s]:
        r.camPosition.z += 1 * deltaTime
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            isPlaying = False
        elif ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_1:
                r.filledMode()
            elif ev.key == pygame.K_2:
                r.wireframeMode()
            elif ev.key == pygame.K_ESCAPE:
                isPlaying = False
            elif ev.key == pygame.K_SPACE:
                r.activeModel = (r.activeModel + 1) % len(r.modelList)
    r.render()
    pygame.display.flip()
    clock.tick(60)
    deltaTime = clock.get_time() / 1000
    

pygame.quit()
