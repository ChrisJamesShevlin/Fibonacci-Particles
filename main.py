import py5
import math

def setup():
    py5.size(1920, 1080)
    py5.background(0)
    py5.no_stroke()
    
n = 0
cx = 960
cy = 540
angle = n * 137.5
    
def draw():
    global n
    angle = n * 137.5
    angle_rad = math.radians(angle)
    radius = 4 * math.sqrt(n)
    x = cx + radius * math.cos(angle_rad)
    y = cy + radius * math.sin(angle_rad)
    py5.fill(py5.random(255), py5.random(255), py5.random(255))
    py5.circle(x, y, 8)
    n += 1
    
def key_pressed():
    if py5.key == 's':
        py5.save_frame('fibonacci.png')
        
py5.run_sketch()
    
    
    
