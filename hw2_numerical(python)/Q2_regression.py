import math
import numpy as np




temp1 =np.array([-16, -6, 11, 34, 65])


y = np.array([10, 20, 60, 200, 760])




temp2 = np.array(([]))
for i in y:
    temp2=np.append(temp2,math.log(i))




temp=temp1.dot(temp2)


temp1_y=np.sum((temp1.dot(y)))



temp2_y=np.sum((temp2.dot(y)))


temp1_pow=temp1**2
temp2_pow=temp2**2

org=np.array([[5,np.sum(temp1),np.sum(temp2)],
                   [np.sum(temp1),np.sum(temp1_pow),np.sum(temp)],
                   [np.sum(temp2),np.sum(temp),np.sum(temp2_pow)]])

inv=np.linalg.inv(org)

ysum=np.array([np.sum(y),temp1_y,temp2_y])




ans=inv.dot(ysum)


print("answer : \n")

print("a0 =",ans[0]," , a1 =",ans[1]," , a2 =",ans[2])