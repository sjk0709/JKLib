import os

def create_folder(folder_path):
    try:
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print("%s has been created.")
        else:
            print("The folder already exists.")
    except OSError:
        print('Error: create_folder(). : ' + folder_path)

