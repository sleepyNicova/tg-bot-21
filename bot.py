import random
import time

def rnd():
    random.seed(time.time())
    addp = random.randint(2, 11)
    return addp
points = 0
rpoints = 0
while (points<21):
    print('Очки =', points, end='\n')
    print('1 = Еще, 2 = Хватит', end='\n')
    Comands = int(input())
    if (Comands==1):
        points = points + rnd()
    elif (Comands==2):
        while(rpoints<21):
            if (rpoints<11):
                rpoints = rpoints + rnd()
            elif (rpoints<=19):
                f = random.randint(0,2)
                if(f==1):
                    rpoints = rpoints + rnd()
                if(f==2):
                    rpoints = rpoints + rnd()
                elif(f==0):
                    break
            else:
                break
        break
    else:
        print('Пиши 1 или 2')
if (points==21):
    print('Очки =', points, end='\n')
    print('Вы выиграли!')
elif (points>21):
    print('Очки =', points, end='\n')
    print('Вы проиграли!')
elif (rpoints>21):
    print('Очки =', points, end='\n')
    print('Очки дилера =', rpoints, end='\n')
    print('Вы выиграли!')
else:
    if (points>rpoints):
        print('Очки =', points, end='\n')
        print('Очки дилера =', rpoints, end='\n')
        print('Вы выиграли!')
    else:
        print('Очки =', points, end='\n')
        print('Очки дилера =', rpoints, end='\n')
        print('Вы проиграли!')