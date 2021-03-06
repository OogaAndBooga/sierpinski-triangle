import pygame
pygame.init()

size = (width, height) = (1000, 1000)

screen = pygame.display.set_mode(size)
screen.fill('white')

class Coords():
    x = None
    y = None
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Triangle():
    coords1 = None
    coords2 = None
    coords3 = None
    iteration = None
    def __init__(self, c1, c2, c3, iteration = 0):
        self.coords1 = c1
        self.coords2 = c2
        self.coords3 = c3
        self.iteration = iteration

def get_middle(coords1, coords2):
    return Coords((coords1.x + coords2.x) / 2, (coords1.y + coords2.y) / 2)

def draw_triangle(triangle):
    pygame.draw.line(screen, 'black', convert_to_display(triangle.coords1), convert_to_display(triangle.coords2))
    pygame.draw.line(screen, 'black', convert_to_display(triangle.coords2), convert_to_display(triangle.coords3))
    pygame.draw.line(screen, 'black', convert_to_display(triangle.coords3), convert_to_display(triangle.coords1))
    pygame.display.flip()

def add_to_queue(triangle):
    queue.append(Triangle(triangle.coords1, get_middle(triangle.coords1, triangle.coords2), get_middle(triangle.coords1, triangle.coords3), triangle.iteration - 1))
    queue.append(Triangle(triangle.coords2, get_middle(triangle.coords2, triangle.coords3), get_middle(triangle.coords2, triangle.coords1), triangle.iteration - 1))
    queue.append(Triangle(triangle.coords3, get_middle(triangle.coords3, triangle.coords1), get_middle(triangle.coords3, triangle.coords2), triangle.iteration - 1))

def optimized_draw_and_queue(triangle):
    add_to_queue(triangle)
    pygame.draw.line(screen, 'black', convert_to_display(get_middle(triangle.coords1, triangle.coords2)), convert_to_display(get_middle(triangle.coords2, triangle.coords3)))
    pygame.draw.line(screen, 'black', convert_to_display(get_middle(triangle.coords2, triangle.coords3)), convert_to_display(get_middle(triangle.coords3, triangle.coords1)))
    pygame.draw.line(screen, 'black', convert_to_display(get_middle(triangle.coords3, triangle.coords1)), convert_to_display(get_middle(triangle.coords1, triangle.coords2)))
    pygame.display.flip()


def convert_to_display(coords):
    return (coords.x + width / 2, height / 2 - coords.y)

queue = [Triangle(Coords(-500, -500), Coords(500, -500), Coords(0, 500), 6)]

#while len(queue) > 0:
#    draw_triangle(queue[0])
#    if queue[0].iteration > 0:
#        add_to_queue(queue[0])
#    del queue[0]

draw_triangle(queue[0]) #neccesary
while len(queue) > 0:
    if queue[0].iteration > 0:
        optimized_draw_and_queue(queue[0])
    del queue[0]

print('''DONE
        DONE
        DONE
        DONE
        ''')

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
