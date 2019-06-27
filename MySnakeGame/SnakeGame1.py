import pygame
import random
import collections

pygame.init()

window = pygame.display.set_mode(size=(500, 500))
pygame.display.set_caption("Snake v.over9000")


def main():
    direction = "R"
    snake_head = collections.deque([110, 50])

    snake_position = collections.deque([100, 50])
    snake_body = collections.deque([[snake_head[0], snake_head[1]], [100, 50], [90, 50], [80, 50], [100, 50]])
    body_picture = pygame.image.load("body.png")
    rabbit = pygame.image.load("rabbit.png")
    food = [random.randint(1, 47) * 10, random.randint(1, 47) * 10]
    food_spawn = True
    pygame.display.update()

    run = True
    while run:
        pygame.time.delay(20)
        window.fill((150, 150, 150))
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            """Set a direction of the snake"""
            if keys[pygame.K_RIGHT] and direction != "L":
                direction = "R"
            elif keys[pygame.K_LEFT] and direction != "R":
                direction = "L"
            elif keys[pygame.K_DOWN] and direction != "U":
                direction = "D"
            elif keys[pygame.K_UP] and direction != "D":
                direction = "U"

        """Mechanic of the snake: check direction via user input, don`t let snake go out the screen border, 
        set the head of the snake in the beginnig of the snake"""
        if direction == "R" and snake_head[0] < 490:
            if snake_head[0] >= snake_position[0]:
                snake_position[0] = snake_head[0] - 10
                snake_position[1] = snake_head[1]
            snake_head[0] += 10
            snake_position[0] += 10
        elif direction == "L" and snake_head[0] > 0:
            if snake_head[0] >= snake_position[0]:
                snake_position[0] = snake_head[0] + 10
                snake_position[1] = snake_head[1]
            snake_head[0] -= 10
            snake_position[0] -= 10
        elif direction == "D" and snake_head[1] < 490:
            if snake_head[1] >= snake_position[1]:
                snake_position[0] = snake_head[0]
                snake_position[1] = snake_head[1] - 10
            snake_head[1] += 10
            snake_position[1] += 10
        elif direction == "U" and snake_head[1] > 0:
            if snake_head[1] >= snake_position[1]:
                snake_position[0] = snake_head[0]
                snake_position[1] = snake_head[1] + 10
            snake_head[1] -= 10
            snake_position[1] -= 10

        """Move snake on the sreen"""
        snake_body.appendleft(list(snake_position))
        snake_body.pop()

        """Checks if snake eat the rabbit and add length to it"""
        for number in range(0, 30, 10):
            if snake_head[0] == food[0] + number:
                for number_1 in range(0, 35, 5):
                    if snake_head[1] == food[1] + number_1:
                        food_spawn = False
                        snake_body.append(snake_position)

        """Checks if snake already eat the rabbit and create new rabbit"""
        if not food_spawn:
            food = [random.randint(1, 47) * 10, random.randint(1, 47) * 10]

        food_spawn = True

        """Draw every element in body of the snake and give it a picture"""
        for position in snake_body:
            pygame.draw.rect(window, (139, 0, 0), (position[0], position[1], 10, 10))
            window.blit(body_picture, (position[0], position[1]))

        """Give a picture to the snake head and rabbit"""
        window.blit(snake_head_picture, (snake_head[0], snake_head[1]))
        window.blit(rabbit, (food[0], food[1]))

        pygame.display.flip()


if __name__ == "__main__":
    main()
