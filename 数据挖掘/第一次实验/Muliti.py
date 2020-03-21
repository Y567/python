import numpy as np
import matplotlib.pyplot as plt

# 分别取fix_num = 1,7,9,10,15。
def fit(fit_x, fit_y, fit_num=7):#fit_num表示自由度为7进行拟合数据
    fit_x = np.array(fit_x)
    fit_y = np.array(fit_y)
    f1 = np.polyfit(fit_x, fit_y, fit_num)
    p1 = np.poly1d(f1)#p1为生成的拟合多项式
    # yfit = p1(fit_x)
    print(p1)
    print("\n")
    return p1


# Get data:
file = open('lorenza.dat')  # 打开文档
original = file.readlines()
x = []
y = []
for i in range(20):
    x.append(i+1)
    y.append(float(original[i]))

fit(x,y)
fitx = []
iu = 0
while iu <= 17:
    iu += 0.01
    fitx.append(iu)
plt.plot(x,y)
plt.plot(fitx,list(map(fit(x,y),fitx)),label='fit_lorenza') # map为python的内置函数，可以将函数分别作用于后面的数据中
plt.legend()
plt.show()
