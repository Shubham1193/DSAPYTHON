
# 2 pointer watere is decided  by small wall and diff means width
# move small becase in search of new water


def maxwater(walls):
    i = 0
    j = len(walls) - 1
    maxwater = 0
    while i < j :
        if walls[i] > walls[j]:
            water = walls[j] * (j - i)
            j -= 1
        else :
            water =  walls[i] * (j - 1)
            i += 1
        if water > maxwater:
            maxwater = water
    return maxwater 

if __name__ == "__main__":
    walls = [1, 5 , 6 , 3 ,4 ,2]
    water = maxwater(walls)
    print(water)