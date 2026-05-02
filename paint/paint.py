import pygame
import math

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    radius = 15
    mode = 'blue'
    shape_mode = 'circle' 
    points = [] 
    
    while True:
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
            
                if event.key == pygame.K_r: mode = 'red'
                elif event.key == pygame.K_g: mode = 'green'
                elif event.key == pygame.K_b: mode = 'blue'

                elif event.key == pygame.K_q: shape_mode = 'square'
                elif event.key == pygame.K_w: shape_mode = 'right_triangle'
                elif event.key == pygame.K_e: shape_mode = 'equilateral_triangle'
                elif event.key == pygame.K_a: shape_mode = 'rhombus'
                elif event.key == pygame.K_t: shape_mode = 'circle'
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: 
                    radius = min(200, radius + 1)
                elif event.button == 3: 
                    radius = max(1, radius - 1)
            
            if event.type == pygame.MOUSEMOTION:
                position = event.pos
                points.append((position, radius, mode, shape_mode))
                points = points[-256:] 
                
        screen.fill((0, 0, 0))
        
        for i in range(len(points)):
            pos, size, col_m, shp_m = points[i]
            color = get_color(i, col_m)
            draw_shape(screen, pos, size, color, shp_m)
        
        pygame.display.flip()
        clock.tick(60)

def get_color(index, color_mode):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))
    if color_mode == 'blue': return (c1, c1, c2)
    if color_mode == 'red': return (c2, c1, c1)
    if color_mode == 'green': return (c1, c2, c1)
    return (255, 255, 255)

def draw_shape(screen, pos, size, color, shape):
    x, y = pos
    
    if shape == 'circle':
        pygame.draw.circle(screen, color, pos, size)
    
    elif shape == 'square':
        pygame.draw.rect(screen, color, (x - size, y - size, size * 2, size * 2))
    
    elif shape == 'right_triangle':
        pts = [(x, y), (x + size * 2, y), (x, y - size * 2)]
        pygame.draw.polygon(screen, color, pts)
        
    elif shape == 'equilateral_triangle':
        height = size * math.sqrt(3)
        pts = [
            (x, y - size), 
            (x - height/2, y + size/2), 
            (x + height/2, y + size/2)
        ]
        pygame.draw.polygon(screen, color, pts)
        
    elif shape == 'rhombus':
        pts = [
            (x, y - size), 
            (x + size * 1.5, y), 
            (x, y + size), 
            (x - size * 1.5, y)
        ]
        pygame.draw.polygon(screen, color, pts)

if __name__ == "__main__":
    main()