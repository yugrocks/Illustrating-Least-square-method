#Uses the least square methos=d to train a hypothesis
import matplotlib.pyplot as plt
from numpy import arange


#Getting the data ready
x=[i for i in arange(-8,10,1)]
y=[i*i for i in x]

#Plot initial points:
for _ in range(len(x)):
    plt.plot(x,y,'or')


#Calculations (Training):
sum_x=sum(x)
sum_y=sum(y)
sum_xsq=sum([k*k for k in x])
sum_ysq=sum([k*k for k in y])
sum_xcbe=sum([k*k*k for k in x])
sum_xquad=sum([k*k*k*k for k in x])
sum_xy=0
sum_xsqy=0
d=len(x)
for _ in range(len(x)):
    sum_xy+=x[_]*y[_]

for _ in range(len(x)):
    sum_xsqy+=x[_]*x[_]*y[_]

c=-((sum_x*sum_xcbe-sum_xsq*sum_xsq)*(sum_x*sum_y-d*sum_xy)+(sum_xsq*d-sum_x*sum_x)*(sum_x*sum_xsqy-sum_xsq*sum_xy))/((sum_x*sum_xsq-d*sum_xcbe)*(sum_x*sum_xcbe-sum_xsq*sum_xsq)-(sum_x*sum_x-sum_xsq*d)*(sum_xsq*sum_xcbe-sum_x*sum_xquad))

a=(sum_x*(c*sum_xcbe-sum_xy)-sum_xsq*(c*sum_xsq-sum_y))/(sum_xsq*d-sum_x*sum_x)

b=(sum_x*(c*sum_xsq-sum_y)-d*(c*sum_xcbe-sum_xy))/(sum_xsq*d-sum_x*sum_x)


#Finally the hyopthesis
print(a)
print(b)
print(c)

#Plot the curve finally
x2=arange(-10,10,0.1)
y2=[a+(b*i)+(c*i*i) for i in x2]
plt.plot(x2,y2)
plt.show()

