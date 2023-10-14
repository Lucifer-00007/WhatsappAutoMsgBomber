import random
import pyautogui as pg
import time

#---------------------- (Type1) ----------------------#
# animal = ('Dog', 'Monkey', 'Cow', 'Buffalow' , 'Elephant', 'Donkey', 'Cat')

# time.sleep(10)

# for i in range (1000):
#     a  = random.choice(animal)
#     pg.write('You Are a ' + a)
#     pg.press('enter')



#---------------------- (Type2) ----------------------#
animal = ('Dog', 'Monkey', 'Cow', 'Buffalow' , 'Elephant', 'Donkey', 'Cat')
preInputTxt = input('Enter your text: ');

time.sleep(10)

for i in range (1000):
    randomAnimal = random.choice(animal)
    pg.write(f"{preInputTxt} {randomAnimal}?")
    pg.press('enter')


