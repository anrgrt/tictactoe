'''
                        HOW TO PLAY

1.  enter coordinates:
    eg. 1 1 or 2 2 or 3 2 or 1 2 etc.
    -------------------
    |1 3    2 3    3 3|
    |                 |
    |1 2    2 2    3 2|   <------ THIS IS THE STRUCTURE
    |                 |
    |1 1    2 1    3 1|
    -------------------

2.  if you enter 1 1 your move will be stored in bottom left corner
    or if you enter 3 3 your move will be stored in top left corner
    etc.

3.  game will end when someone wins or draw

4.  first user is "X" and second user is "O"

'''







val = '_________'
for a in range(1,10):
    cells = list(val)
    print('---------')
    print('| ' + val[0] + ' ' + val[1] + ' ' + val[2] + ' |')
    print('| ' + val[3] + ' ' + val[4] + ' ' + val[5] + ' |')
    print('| ' + val[6] + ' ' + val[7] + ' ' + val[8] + ' |')
    print('---------')

    allowed = '0123456789'
    cond = True
    cond1 = True
    cond2 = True
    while cond2:
        while cond1:
            while cond:
                move = input('Enter the coordinates:')
                if len(move) < 3 or move[1] != ' ':
                    print('bad input try again!')
                elif (move[0] in allowed) and (move[2] in allowed):
                    cond = False    
                else:
                    print('You should enter numbers!')
        
        
            if((move[0] == '1' or move[0] == '2' or move[0] == '3') and
               (move[2] == '1' or move[2] == '2' or move[2] == '3')):
                cond1 = False
            else:
                print('Coordinates should be from 1 to 3!')
                cond = True
     
        def new(z):
            global cond_2
            global cond_1
            global cond_0
            global val2
            val2 = val
            val2_list = list(val2)
            if (val2_list[z] == '_'):
                odd = [1,3,5,7,9]
                even = [2,4,6,8]
                if a in odd:
                    val2_list[z] = 'X'
                elif a in even:
                    val2_list[z] = 'O'

            
                #val2_list[z] = 'X'
                val2 = ''.join(val2_list)
                cond_2 = cond_1 = cond_0 = False
            else:
                print('This cell is occupied! Choose another one!')
                cond_2 = True
                cond_1 = True
                cond_0 = True
        
        if move == '1 3':
            new(0)
        elif move == '2 3':
            new(1)
        elif move == '3 3':
            new(2)
        elif move == '1 2':
            new(3)
        elif move == '2 2':
            new(4)
        elif move == '3 2':
            new(5) 
        elif move == '1 1':
            new(6)
        elif move == '2 1':
            new(7)
        elif move == '3 1':
            new(8)
        cond = cond_0
        cond1 = cond_1
        cond2 = cond_2
        
    val = val2
    
    
    new1 = []
    new2 = []
    z = 0
    for _ in range(9):
        if(val2[z] == 'X'):
            new1.append(val2[z])
        if(val2[z] == 'O'):
            new2.append(val2[z])
        z += 1

    if (len(new1) == len(new2) + 1 or len(new1) == len(new2) or len(new1) == len(new2) - 1):
        cond = 1
    else:
        #print('Impossible')
        cond = 0
            
    if (cond == 1):            
            
        cond1 = val2[0] == val2[1] == val2[2]
        cond2 = val2[3] == val2[4] == val2[5]
        cond3 = val2[6] == val2[7] == val2[8]
        cond4 = val2[0] == val2[3] == val2[6]
        cond5 = val2[1] == val2[4] == val2[7]
        cond6 = val2[2] == val2[5] == val2[8]
        cond7 = val2[0] == val2[4] == val2[8]
        cond8 = val2[2] == val2[4] == val2[6]

        use = []
        if(cond1):
            x = val2[0]
            use.append(x)
        if(cond2):
            x = val2[3]
            use.append(x)
        if(cond3):
            x = val2[6]
            use.append(x)
        if(cond4):
            x = val2[0]
            use.append(x)
        if(cond5):
            x = val2[1]
            use.append(x)
        if(cond6):
            x = val2[2]
            use.append(x)
        if(cond7):
            x = val2[0]
            use.append(x)
        if(cond8):
            x = val2[2]
            use.append(x)
    
    #print(use)    
        if(len(use) == 1):
            if (str(use[0]) == 'X') or (str(use[0]) == 'O'):
                print('---------')
                print('| ' + val[0] + ' ' + val[1] + ' ' + val[2] + ' |')
                print('| ' + val[3] + ' ' + val[4] + ' ' + val[5] + ' |')
                print('| ' + val[6] + ' ' + val[7] + ' ' + val[8] + ' |')
                print('---------')
                print(str(use[0]) + ' wins')
                exit()
        elif(len(use) < 1):
            z = -1
            a = []
            for _ in range(9):
                z += 1
                if val2[z] == '_':
                    a.append(val2[z])
            if '_' in a:
                pass
                #print('Game not finished')                
            else:
                print('---------')
                print('| ' + val[0] + ' ' + val[1] + ' ' + val[2] + ' |')
                print('| ' + val[3] + ' ' + val[4] + ' ' + val[5] + ' |')
                print('| ' + val[6] + ' ' + val[7] + ' ' + val[8] + ' |')
                print('---------')
                print('Draw')
                exit()
        #elif(len(use) > 1):
         #   print('Impossible')

