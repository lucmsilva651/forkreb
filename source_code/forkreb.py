import pygame
import random
import math
import os
from pygame.locals import *

# Adicionais
os.system("cls")
print("Do never close the Prompt Command window! (it's a unfunny joke)")
print()
print("Demo made by Lucas Gabriel (lucmsilva) | In 23/07/2023 at ~23hr (UTC -03:00)")
print("Made with so much love for Kreb!")


# Inicialização do Pygame
pygame.init()

# Dimensões da janela
WIDTH, HEIGHT = 640, 480

# Cores
BLACK = (0, 0, 0)
CUSTOM = (43, 42, 51)

# Variáveis para controlar a troca de cor
start_time = pygame.time.get_ticks()
color_change_time = 11500  # 11 segundos em milissegundos

# Inicialização do mixer
pygame.mixer.init()

# Carregando a música XM
music_file = "cleared_for_take-off.s3m"
pygame.mixer.music.load(music_file)

# Reproduzindo a música em loop
pygame.mixer.music.play(-1)

# Inicialização da janela
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Demo: For Kreb | Lucas Gabriel (lucmsilva) | 23/07/2023")

# Função para desenhar uma face do cubo
def draw_face(surface, color, vertices):
    pygame.draw.polygon(surface, color, vertices)

# Função para rotacionar o cubo em torno do eixo y
def rotate_around_y(angle, vertices):
    new_vertices = []
    for vertex in vertices:
        x = vertex[0] * math.cos(angle) + vertex[2] * math.sin(angle)
        y = vertex[1]
        z = -vertex[0] * math.sin(angle) + vertex[2] * math.cos(angle)
        new_vertices.append((x, y, z))
    return new_vertices

# Definindo as coordenadas dos vértices do cubo
cube_vertices = [
    (-50, -50, -50),
    (-50, -50, 50),
    (-50, 50, 50),
    (-50, 50, -50),
    (50, -50, -50),
    (50, -50, 50),
    (50, 50, 50),
    (50, 50, -50),
]

# Definindo as faces do cubo
cube_faces = [
    (0, 1, 2, 3),
    (4, 5, 6, 7),
    (0, 1, 5, 4),
    (2, 3, 7, 6),
    (1, 2, 6, 5),
    (0, 3, 7, 4),
]

# Font settings
font_size = 17
font = pygame.font.Font("pixel.ttf", font_size)
text_color = (255, 255, 255)  # White

# Text to be displayed
text_to_display = "For Kreb (It's not much but it's what I could do)"

# Render the text surface
text_surface = font.render(text_to_display, True, text_color)

# Calculate the position to center the text on the screen
text_width, text_height = text_surface.get_size()
x_pos = (WIDTH - text_width) // 2
y_pos = (HEIGHT - text_height) // 2

# Main loop
angle_y = 0
zoom_factor = 1 # Fator de zoom centrado
rotation_speed = 0.025
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    
    # Calcula o tempo decorrido desde o início do jogo em milissegundos
    elapsed_time = pygame.time.get_ticks() - start_time

    # Troca a cor de fundo após 11 segundos
    if elapsed_time >= color_change_time:
        screen.fill(CUSTOM)
    else:
        screen.fill(BLACK)

    # Rotacionando o cubo
    angle_y += rotation_speed
    rotated_vertices = rotate_around_y(angle_y, cube_vertices)

    # Projeção em 2D dos vértices do cubo com efeito de zoom centrado
    projected_points = []
    for vertex in rotated_vertices:
        x = vertex[0] * (zoom_factor * WIDTH / 2) / (zoom_factor * WIDTH / 2 - vertex[2])
        y = vertex[1] * (zoom_factor * HEIGHT / 2) / (zoom_factor * HEIGHT / 2 - vertex[2])
        projected_points.append((x + WIDTH / 2, y + HEIGHT / 2))

    # Desenhando as faces do cubo
    for face in cube_faces:
        draw_face(screen, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), [projected_points[i] for i in face])

    # Atualizando a janela
    screen.blit(text_surface, (x_pos, y_pos))

    # Update the display
    pygame.display.flip()
    clock.tick(60)

# Encerrando o Pygame
pygame.quit()
