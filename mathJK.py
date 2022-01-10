import os
import numpy as np



def get_dist_point_line_2D( a, b, c, x, y):
    '''Calculate the distance between a point(x,y) and the line(ax+by+c=0)'''
    return abs(a*x + b*y + c)/np.sqrt(a*a+b*b)


def get_tangent_yIntercept(p1, p2):
    '''
    Get the tangent and y-intercept of a line(y=ax+b) from points p1 and p2

    p1 = (x1, y1)
    p2 = (x2, y2)

    y=ax+b
    y-y2 = (y2-y1)/(x2-x1) * (x-x1) 
    a = (y2-y1)/(x2-x1)
    b = -a*x1 + y2
    return a, b
    '''
    a = (p2[1] - p1[1])/(p2[0] - p1[0])
    b = -a*p1[0] + p2[1]
    return a, b



def main():
    a = np.arange(10)
    b = np.arange(10)    

    print(get_dist_point_line_2D(1,2,2, 1,2))


if __name__ == '__main__':
    main()