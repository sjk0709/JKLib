import os
import numpy as np

def MSE(y1 : list, y2 : list, axis=0):
    '''Mean Squared Error'''
    return np.mean(np.square(y1-y2), axis=axis)


def cosine_similarity(a : list, b : list):
    return np.dot(a, b) / (np.linalg.norm(a) * (np.linalg.norm(b)))




def main():
    a = np.arange(10)
    b = np.arange(10)
    print(MSE(a, b))
    print(cosine_similarity(a,b))
    

if __name__ == '__main__':
    main()