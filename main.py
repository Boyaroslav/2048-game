import random
import pygame

pygame.init()
positions = [[0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]]

root = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
font = pygame.font.Font('TinyIslanders-nOYg.ttf', 30)
BG = (227, 233, 255)
EDGE = (5, 50, 50)

colors = {
    2 : (202, 192, 70),
    4 : (156, 148, 184),
    8 : (255, 148, 184),    #rgb
    16 : (103, 146, 129),
    32 : (203, 146, 129),
    64 : (59, 107, 197)

}


def add_new():
    newx = random.randint(0, 3)
    newy = random.randint(0, 3)
    bads = set()
    count = 0
    for i in positions:
        count += len(i)
    if len(bads) == count:
        return 0
    if positions[newy][newx] != 0:
        bads.add((newy,newx))
        add_new()
    positions[newy][newx] = 2
def draw_window():                  # 50px |100px|100px|100px|100px| 50px
    for y in range(0, 4):
        for x in range(0, 4):
            if positions[y][x] != 0:
                pygame.draw.rect(root, colors[positions[y][x]], (50 + (x * 100), 50 + (y * 100), 95, 95))
                text = font.render(str(positions[y][x]), True, EDGE)
                root.blit(text, (50 + (x * 100) + 40, 80 + (y * 100)))
def draw_edges():           # Im so clever...
    root.fill(BG)
    pygame.draw.rect(root, EDGE, (50, 45, 400, 5))
    pygame.draw.rect(root, EDGE, (50, 145, 400, 5))
    pygame.draw.rect(root, EDGE, (50, 245, 400, 5))
    pygame.draw.rect(root, EDGE, (50, 345, 400, 5))
    pygame.draw.rect(root, EDGE, (50, 445, 400, 5))

    pygame.draw.rect(root, EDGE, (45, 45, 5, 405))
    pygame.draw.rect(root, EDGE, (145, 45, 5, 405))
    pygame.draw.rect(root, EDGE, (245, 45, 5, 405))
    pygame.draw.rect(root, EDGE, (345, 45, 5, 405))
    pygame.draw.rect(root, EDGE, (445, 45, 5, 405))


def left():
    key = 0
    for i in range(0, 4):
        for y in range(0, 4):
            for x in range(1, 4):
                if positions[y][x] != 0:
                    if positions[y][x-1] == 0 or (positions[y][x-1] == positions[y][x]):
                        positions[y][x-1] += positions[y][x]
                        positions[y][x] = 0
                        key = 1
    if key:
        add_new()
def right():
    key = 0
    for i in range(0, 4):
        for y in range(0, 4):
            for x in range(2, -1, -1):
                if positions[y][x] != 0:
                    if positions[y][x + 1] == 0 or positions[y][x + 1] == positions[y][x]:
                        positions[y][x + 1] += positions[y][x]
                        positions[y][x] = 0
                        key = 1
    if key:
        add_new()
def up():
    key = 0
    for i in range(0, 4):
        for x in range(0, 4):
            for y in range(1, 4):
                if positions[y][x] != 0:
                    if positions[y - 1][x] == 0 or positions[y - 1][x] == positions[y][x]:
                        positions[y - 1][x] += positions[y][x]
                        positions[y][x] = 0
                        key = 1
    if key:
        add_new()
def down():
    key = 0
    for i in range(0, 4):
        for x in range(0, 4):
            for y in range(2, -1, -1):
                if positions[y][x] != 0:
                    if positions[y + 1][x] == 0 or positions[y + 1][x] == positions[y][x]:
                        positions[y + 1][x] += positions[y][x]
                        positions[y][x] = 0
                        key = 1
    if key:
        add_new()

add_new()


while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            quit()
        if i .type == pygame.KEYDOWN:
            if i.key == pygame.K_LEFT:
                left()
            elif i.key == pygame.K_RIGHT:
                right()
            elif i.key == pygame.K_UP:
                up()
            elif i.key == pygame.K_DOWN:
                down()
    draw_edges()
    draw_window()
    sm = 0
    for i in positions:
        sm += sum(i)
    text = font.render(str(sm), True, EDGE)
    root.blit(text, (20, 20))
    pygame.display.update()
    clock.tick(60)