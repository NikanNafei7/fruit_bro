import pygame
import OpenGL.GL as gl
import imgui
from imgui.integrations.pygame import PygameRenderer

size = 800, 600
pygame.display.set_mode(size, pygame.OPENGL | pygame.DOUBLEBUF)

imgui.create_context()

io = imgui.get_io()
io.display_size = size

renderer = PygameRenderer()

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        renderer.process_event(event)
    
    imgui.new_frame()
    renderer.process_inputs()

    imgui.begin("shop")

    imgui.text("hello")

    imgui.end()

    gl.glClearColor(0.145, 0.34, 0.123, 1)
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)
    imgui.render()
    renderer.render(imgui.get_draw_data())
    pygame.display.flip()
    clock.tick(60)

renderer.shutdown()
pygame.quit()