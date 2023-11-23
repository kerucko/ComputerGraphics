import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math
import numpy as np


def getCircle(R, n, h):
    return [[R * math.cos(2*math.pi*(i+1)/n), -R + h, R * math.sin(2*math.pi*(i+1)/n)] for i in range(n)]


def build(h, n):
    verts = []
    faces = []
    norms = []
    ind = 0
    a = h/((2*n - 1) ** 2)
    for i in range(math.floor(n * 0.7), 2*n):
        z = a * i**2
        c = getCircle(math.sqrt(z), n, h)
        verts += c
        if i != math.floor(n * 0.7):
            for j in range(n):
                faces += [[ind + j, ind + (j + 1) % n, ind + - n + (j + 1)%n]]
        else:
            faces += [range(ind, ind + len(c))]
        if i != 2 * n - 1:
            for j in range(n):
                faces += [[ind + j, ind + j + n, ind + (j + n + 1)%n]]
        else:
            faces += [range(ind, ind + len(c))]
        ind += len(c)

    for face in faces:
        v1 = np.array(np.array(verts[face[0]]) - np.array(verts[face[1]]))
        v2 = np.array(np.array(verts[face[0]]) - np.array(verts[face[2]]))
        norm = np.cross(v1, v2)
        if np.sum(norm) != 0:
            norm = -norm / np.sqrt(np.sum(norm**2))
        norms += [norm]
    return verts, faces, np.array(norms)


def draw(verts, faces, norms):
    for i in range(len(faces)):
        glBegin(GL_POLYGON)
        glNormal3f(*norms[i])
        glColor3f(1, 0, 0)
        for vertex in faces[i]:
            glVertex3f(*verts[vertex])
        glEnd()


def main():
    pygame.init()
    display = (1280, 720)
    screen = pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glEnable(GL_LIGHTING)

    reflect_lvl = 0.2
    t = 0
    light_position = [10, 10, 10, math.sin(t)]
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)
    glLightfv(GL_LIGHT0, GL_AMBIENT, [reflect_lvl, reflect_lvl, reflect_lvl, 1])
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [0.1, 0.2, 0.8, reflect_lvl])
    glLightfv(GL_LIGHT0, GL_SPECULAR, [reflect_lvl]*4)
    glEnable(GL_LIGHT0)
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, [1.0, 1.0, 1.0, reflect_lvl])
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, [1.0, 1.0, 1.0, reflect_lvl])
    glMaterialfv(GL_FRONT_AND_BACK, GL_SHININESS, [50])
    glEnable(GL_DEPTH_TEST)
    glMatrixMode(GL_PROJECTION)


    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0, -1.65, -5)

    height = 1.5
    accurance = 10
    verts, faces, norms = build(height, accurance)
    draging = False
    last_m = [0, 0]
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:            
                    draging = True
                    last_m = event.pos

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:            
                    draging = False

            elif event.type == pygame.MOUSEMOTION:
                if draging:
                    mouse_x, mouse_y = event.pos
                    rot = np.array([0, 0])
                    rot[0] = last_m[0] - mouse_x
                    rot[1] = last_m[1] - mouse_y
                    last_m = [mouse_x, mouse_y]
                    glRotated(-360 * (rot[0]/display[0]), 0, 1, 0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    light_position[1] -= 1
                    glLightfv(GL_LIGHT0, GL_POSITION, light_position)
                elif event.key == pygame.K_DOWN:
                    light_position[1] += 1
                    glLightfv(GL_LIGHT0, GL_POSITION, light_position)
                elif event.key == pygame.K_LEFT:
                    light_position[0] -= 1
                    glLightfv(GL_LIGHT0, GL_POSITION, light_position)
                elif event.key == pygame.K_RIGHT:
                    light_position[0] += 1
                    glLightfv(GL_LIGHT0, GL_POSITION, light_position)
        
        t = (t + 0.05) % math.pi
        light_position[3] = 3 * (math.sin(2 * t) + 1)
        glLightfv(GL_LIGHT0, GL_POSITION, light_position)
        keypress = pygame.key.get_pressed()
        if keypress[pygame.K_w]:
            glTranslatef(0, 0.1, 0.0)
        if keypress[pygame.K_s]:
            glTranslatef(0, -0.1, 0.0)
        if keypress[pygame.K_z] and accurance < 40:
            accurance += 2
            verts, faces, norms = build(height, accurance)
        if keypress[pygame.K_x] and accurance > 4:
            accurance -= 2
            verts, faces, norms = build(height, accurance)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw(verts, faces, norms)
        pygame.display.flip()
        pygame.time.wait(15)

    pygame.quit()


if __name__ == "__main__":
    main()
