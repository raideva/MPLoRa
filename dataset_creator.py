# import math
# import sys
#
# import pygame
# from pygame.locals import *
#
# pygame.init()
# vec = pygame.math.Vector2  # 2 for two dimensional
#
# HEIGHT = 713
# WIDTH = 940
# FPS = 60
#
# FramePerSec = pygame.time.Clock()
#
# displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Game")
# displaysurface.fill((120, 130, 100))
# img = pygame.image.load("data/img.png")
# displaysurface.blit(img, (0, 0))
#
# base_station_coordinate = (800, 318)
#
# while True:
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             pygame.quit()
#             sys.exit()
#
#         if event.type == pygame.MOUSEBUTTONUP:
#             pos = pygame.mouse.get_pos()
#             print(pos)
#             distance_of_propagation = math.sqrt((pos[0] - base_station_coordinate[0]) ** 2 + (pos[1] - base_station_coordinate[1]) ** 2)
#             print(distance_of_propagation)
#
#     pygame.display.update()
#     FramePerSec.tick(FPS)


from PIL import Image
im = Image.open('data/img copy.png')
v = list(im.getdata())
arr = [[0] * 940 for _ in range(713)]
i1 = Image.new('RGB', (940, 713))
i1_data = i1.load()


for i in range(940 * 713):
    if v[i][0] == v[i][1] == v[i][2] == 0:
        i1_data[i % 940, i // 940] = (255, 0, 0)

im = Image.open('data/img copy 2.png')
v = list(im.getdata())
for i in range(940 * 713):
    if v[i][0] == v[i][1] == v[i][2] == 0:
        i1_data[i % 940, i // 940] = (0, 255, 0)

im = Image.open('data/img copy 3.png')
v = list(im.getdata())
for i in range(940 * 713):
    if v[i][0] == v[i][1] == v[i][2] == 0:
        i1_data[i % 940, i // 940] = (0, 0, 255)

im = Image.open('data/img.png')
v = list(im.getdata())
for i in range(940 * 713):
    if v[i][0] + 20 < v[i][1] > v[i][2] + 20:
        i1_data[i % 940, i // 940] = (0, 255, 255)

im = Image.open('data/img copy 4.png')
v = list(im.getdata())
for i in range(940 * 713):
    if v[i][0] == v[i][1] == v[i][2] == 0:
        i1_data[i % 940, i // 940] = (255, 0, 255)





i1.show()
#
# -91 -88 -94 -97 -90

