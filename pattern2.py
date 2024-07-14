from turtle import *

speed('fastest')
s=5
d=100

for i in range(s):
    fd(d)
    lt(360/s)
    write(i, font=('Arial', 25, 'normal'))
    dot(360/s)

mainloop()



