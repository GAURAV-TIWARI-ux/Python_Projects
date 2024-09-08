def st_line(x1,y1,x2,y2,x,y3):
# we will find the determinant which is twice the area of triangle.
    determinant = x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)
# if the determinant is zero means the lines are collinear.
    if determinant==0:
        return True
    else:
        return False 

x1=float(input('enter the point:'))
y1=float(input('enter the point:'))
x2=float(input('enter the point:'))
y2=float(input('enter the point:'))
x3=float(input('enter the point:'))
y3=float(input('enter the point:'))
result= st_line(x1,y1,x2,y2,x3,y3)
print(result)
