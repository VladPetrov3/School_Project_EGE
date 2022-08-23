def F(x,y,h):
    if x + y >=69 and h == 4:
        return True 
    elif x + y < 69 and h == 4:
        return False 
    elif x + y >= 69 and h < 4:
        return False 
    if h % 2 == 0:
        return  F(x + 1, y, h + 1) and F(x , y + 1, h + 1) and F(x * 2, y, h + 1) and F(x, y * 2, h + 1) 
    else: 
        return  F(x + 1, y, h + 1) or F(x , y + 1, h + 1) or F(x * 2, y, h + 1) or F(x, y * 2, h + 1) 

for i in range(1, 64): 
    if F(i, 5, 1):
        print(i)