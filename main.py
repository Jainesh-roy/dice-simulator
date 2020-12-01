import random
from tkinter import *


def get_random_dice():
    global dice_list
    dice_list = [1, 2, 3, 4, 5, 6]
    dice_num = random.choice(dice_list)
    return dice_num




def main_func():
    dice_num = get_random_dice()
        
    for item in dice_list:
        if dice_num == item:
            dice_val.config(text=item)
            dice = PhotoImage(file=f'img/{dice_num}.png')
            dice_img_lable.configure(image=dice)
            dice_img_lable.image = dice



if __name__ == "__main__":
    root = Tk()
    # root.config(bg='black')
    SCREEN_HEIGHT = 500
    SCREEN_WIDTH = 300
    root.geometry(f'{SCREEN_WIDTH}x{SCREEN_HEIGHT}')
    root.maxsize(SCREEN_WIDTH, SCREEN_HEIGHT)
    root.title('DICE')

    dice_img = PhotoImage(file='img/1.png')
    dice_img_lable = Label(root, image=dice_img)
    dice_img_lable.pack(pady=(100, 30))

    dice_val = Label(root, text='1', font='Comicsaans 30 bold')
    dice_val.pack(pady=(0, 30))

    roll_button = Button(root, text='ROLL NOW', padx=13, pady=10, bg='black',
                         fg='white', font='Comicsaans 10 bold', relief=GROOVE, command=main_func)
    roll_button.pack()

    root.mainloop()
