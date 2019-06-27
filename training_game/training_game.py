import pygame
import sys

pygame.init()

window = pygame.display.set_mode(size=(500, 500))
pygame.display.set_caption("My game")

x = 0
y = 420
width = 60
height = 71
speed = 25

jump_count = 10
is_jump = False

left = False
right = False
anim_count = False


walk_right = [
    pygame.image.load("pygame_right_1.png"),
    pygame.image.load("pygame_right_2.png"),
    pygame.image.load("pygame_right_3.png"),
    pygame.image.load("pygame_right_4.png"),
    pygame.image.load("pygame_right_5.png"),
    pygame.image.load("pygame_right_6.png"),
]
walk_left = [
    pygame.image.load("pygame_left_1.png"),
    pygame.image.load("pygame_left_2.png"),
    pygame.image.load("pygame_left_3.png"),
    pygame.image.load("pygame_left_4.png"),
    pygame.image.load("pygame_left_5.png"),
    pygame.image.load("pygame_left_6.png"),
]

background = pygame.image.load("pygame_bg.jpg")
player_stand = pygame.image.load("pygame_idle.png")

class Whizzbang:

    def __init__(self,x,y,radius, colour, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.colour = colour
        self.facing = facing # 1 or -1
        self.speed = 55 * facing # velocity(speed)

    def draw(self, window):
        pygame.draw.circle(window,self.colour,(self.x, self.y),self.radius)


bullets = []


def display_window():
    global anim_count
    window.fill((25, 0, 0))
    window.blit(background, (0, 0))
    # pygame.draw.rect(window, (55, 150, 0), (x, y, width, height))
    if anim_count >= 30:
        anim_count = 0
    elif left:
        window.blit(walk_left[anim_count // 5], (x, y))
        anim_count += 1
    elif right:
        window.blit(walk_right[anim_count // 5], (x, y))
        anim_count += 1
    else:
        window.blit(player_stand, (x, y))

    for bullet in bullets:
        bullet.draw(window)

    pygame.display.update()


run = True


while run:
    pygame.time.delay(25)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    """Удаляем снаряд, если он вышел за рамки экрана из списка bullets"""
    for bullet in bullets:
        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.speed
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_f]:
        if right:
            facing = 1
        else:
            facing = -1
        if len(bullets) < 5:
            bullets.append(Whizzbang(x=round((x+width//2)),y=round((y+height//2)), radius=8, colour=(0,0,0), facing=facing))
    if keys[pygame.K_LEFT] and x > 0:
        left = True
        right = False
        x -= speed

    if keys[pygame.K_RIGHT] and x < 500 - width:
        left = False
        right = True
        x += speed
    if not is_jump:
        if keys[pygame.K_SPACE]:
            is_jump = True
    else:
        if jump_count >= -10:
            if jump_count < 0:
                y += (jump_count ** 2) / 2
            else:
                y -= (jump_count ** 2) / 2
            jump_count -= 1
        else:
            is_jump = False
            jump_count = 10

    display_window()
