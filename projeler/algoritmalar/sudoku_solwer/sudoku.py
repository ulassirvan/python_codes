import numpy as np

sudoku=np.array(([2,0,9,0,0,0,6,0,0],
                 [0,4,0,8,7,0,0,1,2],
                 [8,0,0,0,1,9,0,4,0],
                 [0,3,0,7,0,0,8,0,1],
                 [0,6,5,0,0,8,0,3,0],
                 [1,0,0,0,3,0,0,0,7],
                 [0,0,0,6,5,0,7,0,9],
                 [6,0,4,0,0,0,0,2,0],
                 [0,8,0,3,0,1,4,5,0]
                 ),int)


sudoku_prob=np.zeros((9,9,1),int)
prob=set(np.arange(0,10))

def blok_bulucu(kordinat):# girilen row ve colum degerlerinin hangi bloğa ait olugunu bulur
    geri_donuş=[]
    for i in kordinat:
        if i<3:
            geri_donuş.append([0,3])
        elif (3 <= i < 6):
            geri_donuş.append([3, 6])
        else:
            geri_donuş.append([6, 9])
    return geri_donuş

def prb_finder(x,y,sudoku):#girilen row ve colum kordinatındaki sudoku bloguna gleebilecek olası sayıları bulur ve liste olarak geri dondurur
    row_p=(prob-set(sudoku[x]))
    colum_list=[]
    for colum in np.arange(len(sudoku[0])):
        colum_list.append(sudoku[colum][y])
    colum_p=(prob-set(colum_list))
    blok_list=[]
    blok=blok_bulucu([x,y])
    for row in np.arange(blok[0][0], blok[0][1]):
        for colum in np.arange(blok[1][0], blok[1][1]):
            blok_list.append(sudoku[row][colum])
    blok_p=(prob-set(blok_list))
    return list(colum_p&row_p&blok_p)

print(sudoku)
print("-"*40)
while True:
    for row in np.arange(len(sudoku[0])):
        for colum in np.arange(len(sudoku[0])):
            olasılıklar=prb_finder(row,colum,sudoku)
            if (sudoku[row][colum] == 0) & (len(olasılıklar)==1):
                sudoku[row][colum]=olasılıklar[0]
    if not (0 in set(sudoku.flatten())) :
        break
print(sudoku)

