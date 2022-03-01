import os
from tokenize import Double
import numpy as np



def get_dist_point_line_2D( a : float, b : float, c : float, x : float, y : float):
    '''Calculate the distance between a point(x,y) and the line(ax+by+c=0)'''
    return abs(a*x + b*y + c)/np.sqrt(a*a+b*b)


def get_tangent_yIntercept(p1 : list, p2 : list):
    '''
    Get the tangent and y-intercept of a line(y=ax+b) from points p1 and p2

    p1 = (x1, y1)
    p2 = (x2, y2)

    y=ax+b
    a = (y2-y1)/(x2-x1)
    y = a * (x-x1) + y1 
    y = a*x - a*x1 +y1
    b = -a*x1 + y1
    return a, b
    '''
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    a = float('inf')
    if dx != 0:
        a = dy/dx
    b = -a*p1[0] + p1[1]
    return a, b



def main():
    
    print( get_dist_point_line_2D(1,2,2, 1,2) )
    print( get_tangent_yIntercept((1,1), (1,3)) )


if __name__ == '__main__':
    main()