import os
import numpy as np

def create_folder(folder_path : str):
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
    create_folder("Test_folder")   

    

if __name__ == '__main__':
    main()