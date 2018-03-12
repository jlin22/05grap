from display import *
from draw import *
from parser import *
from matrix import *
import math

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = new_matrix()
'''add_circle(edges, 250, 250, 0, 100, 0.01)
add_curve(edges, 100, 100, 200, 400, 300, 100, 400, 400, 0.01, 'bezier')
print_matrix(edges)
draw_lines(edges, screen, color)
save_ppm(screen, 'img.ppm')'''
# print_matrix( make_translate(3, 4, 5) )
# print
# print_matrix( make_scale(3, 4, 5) )
# print
# print_matrix( make_rotX(math.pi/4) )
# print
# print_matrix( make_rotY(math.pi/4) )
# print
# print_matrix( make_rotZ(math.pi/4) )

parse_file( 'script', edges, transform, screen, color )
