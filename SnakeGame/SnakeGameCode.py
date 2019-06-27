"""Control snake with "Right", "Left", "Up", "Down".
Press "p" for pause. You can see your score in pause menu.
Every time after the snake ate five rabbits appears Rocketman that launch the rocket
that selfing targeting to the snake. You reaches 1 point for eating rabbit
and 2 points for eating Rocketman. Every time you eats someone increase speed up"""
import pygame
import random
import collections
import time

pygame.init()

window = pygame.display.set_mode(size=(500, 500))
pygame.display.set_caption("Snake v.over9000")

direction = "R"

snake_head = collections.deque([110, 50])

snake_position = collections.deque([100, 50])
snake_body = collections.deque([
    [snake_head[0], snake_head[1]],
    [snake_position[0], snake_position[1]],
    [90, 50],
    [80, 50]
])

body_picture = pygame.image.load("body.png")
rabbit_picture_load = pygame.image.load("rabbit.png")
rabbit = [random.randint(1, 47) * 10, random.randint(1, 47) * 10]

rocket_man_picture_load = pygame.image.load("rocketman.png")
rocketman = [random.randint(1, 47) * 10, random.randint(1, 47) * 10]
rocket = [rocketman[0], rocketman[1]]
background = pygame.image.load("background.jpeg")
rocket_picture_list_load = [
    pygame.image.load("rocket.png"),
    pygame.image.load("rocket2.png"),
    pygame.image.load("rocket3.png"),
    pygame.image.load("rocket4.png")
]
head_picture_list_load = [
    pygame.image.load("head.png"),
    pygame.image.load("head1.png"),
    pygame.image.load("head2.png"),
    pygame.image.load("head3.png")
]
food_spawn = True
rocketman_spwan = True

speed = 120
score = 0

pygame.display.update()


def you_lose():
    font_game_over = pygame.font.SysFont("times new roman", 40)
    game_over_surface = font_game_over.render("Game over :(", True, (0, 0, 255))
    window.blit(game_over_surface, (135, 15))
    pygame.display.flip()
    time.sleep(5)
    pygame.quit()


def your_score():
    font_your_score = pygame.font.SysFont("times new roman", 40)
    your_score_surface = font_your_score.render(f"Your score: {score}", True, (0, 0, 255))
    window.blit(your_score_surface, (135, 150))
    pygame.display.flip()


def pause():
    background_pause = pygame.image.load("background_pause.jpg")
    window.blit(background_pause, (0, 0))
    font_your_pause = pygame.font.SysFont("times new roman", 40)
    your_pause_surface = font_your_pause.render(f"Pause", True, (0, 255, 0))
    your_pause_surface2 = font_your_pause.render(f"Your score: {score}", True, (0, 255, 0))
    window.blit(your_pause_surface, (150, 150))
    window.blit(your_pause_surface2, (150, 180))
    pygame.display.flip()


def snake_mechanic():
    """"If snake go outside the screen it appears the other side"""
    if snake_head[0] < 0:
        snake_head[0] = 500
        snake_position[0] = snake_head[0] - 10
    if snake_head[0] > 500:
        snake_head[0] = 0
        snake_position[0] = snake_head[0] - 10
    if snake_head[1] < 0:
        snake_head[1] = 500
        snake_position[1] = snake_head[1] - 10
    if snake_head[1] > 500:
        snake_head[1] = 0
        snake_position[1] = snake_head[1] - 10

    """Mechanic of the snake: check direction via user input, don`t let snake go out the screen border, 
    set the head of the snake in the beginning of the snake"""
    if direction == "R":
        if snake_head[0] >= snake_position[0]:
            snake_position[0] = snake_head[0] - 10
            snake_position[1] = snake_head[1]
        snake_head[0] += 10
        snake_position[0] += 10
        window.blit(head_picture_list_load[1], (snake_head[0], snake_head[1]))
    elif direction == "L":
        if snake_head[0] >= snake_position[0]:
            snake_position[0] = snake_head[0] + 10
            snake_position[1] = snake_head[1]
        snake_head[0] -= 10
        snake_position[0] -= 10
        window.blit(head_picture_list_load[3], (snake_head[0], snake_head[1]))
    elif direction == "D":
        if snake_head[1] >= snake_position[1]:
            snake_position[0] = snake_head[0]
            snake_position[1] = snake_head[1] - 10
        snake_head[1] += 10
        snake_position[1] += 10
        window.blit(head_picture_list_load[2], (snake_head[0], snake_head[1]))
    elif direction == "U":
        if snake_head[1] >= snake_position[1]:
            snake_position[0] = snake_head[0]
            snake_position[1] = snake_head[1] + 10
        snake_head[1] -= 10
        snake_position[1] -= 10
        window.blit(head_picture_list_load[0], (snake_head[0], snake_head[1]))


def move():
    """Move snake on the sreen"""
    snake_body.appendleft(list(snake_position))
    snake_body.pop()


def func_rocket():
    """Rocket aim mechanic"""
    if snake_head[0] - rocket[0] <= 0 and snake_head[1] - rocket[1] <= 0:
        window.blit(rocket_picture_list_load[3], (rocket[0], rocket[1]))
        rocket[0] -= 5
        rocket[1] -= 5
    elif snake_head[0] - rocket[0] >= 0 and snake_head[1] - rocket[1] <= 0:
        window.blit(rocket_picture_list_load[0], (rocket[0], rocket[1]))
        rocket[0] += 5
        rocket[1] -= 5
    elif snake_head[0] - rocket[0] <= 0 and snake_head[1] - rocket[1] >= 0:
        window.blit(rocket_picture_list_load[2], (rocket[0], rocket[1]))
        rocket[0] -= 5
        rocket[1] += 5
    elif snake_head[0] - rocket[0] >= 0 and snake_head[1] - rocket[1] >= 0:
        window.blit(rocket_picture_list_load[1], (rocket[0], rocket[1]))
        rocket[0] += 5
        rocket[1] += 5
    if rocket[0] == snake_head[0] and rocket[1] == snake_head[1]:
        your_score()
        you_lose()


paused = False
run = True

while run:

    pygame.time.delay(speed)

    window.blit(background, (0, 0))
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                paused = not paused
                if not paused:
                    break
                else:
                    pause()

        """Set a direction of the snake"""
        if keys[pygame.K_RIGHT] and direction != "L":
            direction = "R"
        elif keys[pygame.K_LEFT] and direction != "R":
            direction = "L"
        elif keys[pygame.K_DOWN] and direction != "U":
            direction = "D"
        elif keys[pygame.K_UP] and direction != "D":
            direction = "U"

    if not paused:

        snake_mechanic()
        move()

        """You lose if you hit yourself"""
        for position_1 in list(snake_body):
            if position_1[0] == snake_head[0] and position_1[1] == snake_head[1]:
                your_score()
                you_lose()

        """Checks if snake eat the rabbit and add length to it"""
        for number in range(0, 30, 10):
            if snake_head[0] == rabbit[0] + number:
                for number_1 in range(0, 35, 5):
                    if snake_head[1] == rabbit[1] + number_1:
                        food_spawn = False
                        rocketman_spwan = False
                        score += 1
                        speed -= 1
                        snake_body.append(snake_position)

        """Checks if snake already eat the rabbit and create new rabbit"""
        if not food_spawn:
            rabbit = [random.randint(1, 47) * 10, random.randint(1, 46) * 10]

        food_spawn = True

        """Create a hunter"""
        if len(snake_body) % 6 == 0:

            if not rocketman_spwan:
                rocketman = [random.randint(1, 47) * 10, random.randint(1, 46) * 10]
                rocket = [rocketman[0], rocketman[1]]

            rocketman_spwan = True
            window.blit(rocket_man_picture_load, (rocketman[0], rocketman[1]))

            """Checks if snake eat the rocketman and add length to it"""
            for number in range(0, 30, 10):
                if snake_head[0] == rocketman[0] + number:
                    for number_1 in range(0, 35, 5):
                        if snake_head[1] == rocketman[1] + number_1:
                            rocketman_spwan = False
                            score += 2
                            speed -= 2
                            snake_body.append(snake_position)
                            snake_body.append(snake_position)
                            break

            for position_1 in list(snake_body):
                if position_1[0] == rocket[0] and position_1[1] == rocket[1]:
                    your_score()
                    you_lose()

            func_rocket()

        """Draw every element in body of the snake and give it a picture"""
        for position in snake_body:
            window.blit(body_picture, (position[0], position[1]))

        """Give a picture to the snake head and rabbit"""
        window.blit(rabbit_picture_load, (rabbit[0], rabbit[1]))

        pygame.display.flip()
