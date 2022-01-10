import os
import numpy as np

def create_folder(folder_path):
    '''Create folder'''
    try:
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print('"%s" has been created.'%(folder_path))
        else:
            print("The folder already exists.")
    except OSError:
        print('Error: create_folder(). : ' + folder_path)



def main():
    a = np.arange(10)
    b = np.arange(10)    

    

if __name__ == '__main__':
    main()