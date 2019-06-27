

class Snake:

    def __init__(self, x, y, picture):
        self.x = x
        self.y = y
        self.picture = picture

    def _set_snake(self):
        self.snake_head = collections.deque([self.x, self.y])
        self.snake_position = collections.deque([self.x - 10, self.y])
        self.snake_body = collections.deque([[self.snake_head[0], self.snake_head[1]],
                                             [self.snake_position[0], self.snake_position[1]],
                                             [90, 50], [80, 50], [100, 50]])

    def _snake_move(self, windows):
        keys = pygame.key.get_pressed()
        self.direction = "R"
        if keys[pygame.K_RIGHT] and self.direction != "L":
            self.direction = "R"
        elif keys[pygame.K_LEFT] and self.direction != "R":
            self.direction = "L"
        elif keys[pygame.K_DOWN] and self.direction != "U":
            self.direction = "D"
        elif keys[pygame.K_UP] and self.direction != "D":
            self.direction = "U"

        if self.direction == "R":
            if self.snake_head[0] >= self.snake_position[0]:
                self.snake_position[0] = self.snake_head[0] - 10
                self.snake_position[1] = self.snake_head[1]
            self.snake_head[0] += 10
            self.snake_position[0] += 10
            windows.blit(self.head_picture_list_load[1], (self.snake_head[0], self.snake_head[1]))
        elif self.direction == "L":
            if self.snake_head[0] >= self.snake_position[0]:
                self.snake_position[0] = self.snake_head[0] + 10
                self.snake_position[1] = self.snake_head[1]
            self.snake_head[0] -= 10
            self.snake_position[0] -= 10
            windows.blit(self.head_picture_list_load[3], (self.snake_head[0], self.snake_head[1]))
        elif self.direction == "D":
            if self.snake_head[1] >= self.snake_position[1]:
                self.snake_position[0] = self.snake_head[0]
                self.snake_position[1] = self.snake_head[1] - 10
            self.snake_head[1] += 10
            self.snake_position[1] += 10
            windows.blit(self.head_picture_list_load[2], (self.snake_head[0], self.snake_head[1]))
        elif self.direction == "U":
            if self.snake_head[1] >= self.snake_position[1]:
                self.snake_position[0] = self.snake_head[0]
                self.snake_position[1] = self.snake_head[1] + 10
            self.snake_head[1] -= 10
            self.snake_position[1] -= 10
            windows.blit(self.head_picture_list_load[0], (self.snake_head[0], self.snake_head[1]))

    head_picture_list_load = [
        pygame.image.load("head.png"),
        pygame.image.load("head1.png"),
        pygame.image.load("head2.png"),
        pygame.image.load("head3.png")
    ]
