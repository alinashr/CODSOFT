# making a rock paper scissors
from random import choice
option=['rock','paper','scissors']
u_choice=''

while u_choice!='stop':
    u_choice= input('enter your choice:')
    if u_choice not in option:
        print('invalid input')


    else:
        c_choice=choice(option)
        if  c_choice== u_choice:
            print(f'Both players selected {u_choice}. It is a Tie  game!')

        #for making paper and rock and scissors
        elif c_choice=='paper' and u_choice=='rock':
            print(f'computer choose{c_choice} and you choose{u_choice}.computer wins the game')

        elif c_choice=='rock' and u_choice=='scissors':
            print(f'computer choose{c_choice} and you choose{u_choice}.computer wins the game')

        elif c_choice=='scissors' and u_choice=='paper':
            print(f'computer choose{c_choice} and you choose{u_choice}.computer wins the game')
            
        else:
            print(f'computer choose {c_choice} and you choose {u_choice}.you win the game !')








    
    
    


















