from random import randint


def checkforint(xory : str, tets : str):
    while True:
        value = input(f'{xory} ')
        try:
            value = int(value)
            if tets == "gm":
                break; 
            elif tets == "guessx" and value >=1 and value <= len(grid[0]) -1:
                break; 
            elif tets == "guessy" and value >= 1 and value <= len(grid) -1:
                break; 
            elif tets == "placeholder":
                pass
            else:
                ValueError 
        except:
            ValueError
    return value
def gridmaker(x_range : int, y_range : int):
    grid = { 0: ["x"], }

    for n in range(y_range):
       grid [n+ 1] = [n+1]
    for n in range (x_range):
        grid[0].append(f' {n+1} ')
        for n in range(y_range):
            grid[n+1].append("[O]")
    
    return grid

def printinggrid(grid : dict):
    for n in range(len(grid)):
        print(*grid[n], )

def positionpicker(x : int ,y : int ,grid : dict, change : str):
    grid[y].__setitem__(x, change)
    return grid


grid = gridmaker(checkforint("X-Axis", "gm"), checkforint("Y-Axis", "gm"),)
printinggrid(grid)
randompoint = [randint(1, len(grid) - 1), randint(1, len(grid[0]) - 1)]
print (randompoint)
guess = []
while True:
    guess = [checkforint("X", "guessx"), checkforint("Y","guessy")]
    if guess == randompoint:
        newgrid = positionpicker(randompoint[0], randompoint[1], grid, "[$]")
        printinggrid(newgrid)
        break; 

    else:
        grid = positionpicker(guess[0], guess[1], grid, "[x]")
        printinggrid(grid)
        print(" ")

