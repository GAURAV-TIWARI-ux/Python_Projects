def position_quad(x,y):
    if x>0 and y>0:
        return 1
    elif x<0 and y>0:
        return 2
    elif x<0 and y<0:
        return 3
    elif x>0 and y<0:
        return 4
    elif x==0 and y==0:
        return "O"
    elif x==0 and y>0:
        return 12
    elif x==0 and y<0:
        return 34
    elif x>0 and y==0:
        return 41
    elif x<0 and y==0:
        return 23
x=float(input('enter the point:'))
y=float(input('enter the point:'))
result=position_quad(x,y)
print(result)
   
