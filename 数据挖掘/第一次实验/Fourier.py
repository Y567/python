import numpy as np
from scipy.fftpack import fft,ifft
import matplotlib.pyplot as plt
# import seaborn

# Get data:
file = open('lorenza.dat')  # 打开文档
original = file.readlines()

# 采样点选择128个，因为设置的信号频率分量最高为max_data
x = []
for i in range(128):
    x.append(float(original[i]))

print(x)
x.sort()
max_data = max(x)



# 采样点选择1400个，因为设置的信号频率分量最高为600赫兹，根据采样定理知采样频率要大于信号频率2倍，所以这里设置采样频率为1400赫兹（即一秒内有1400个采样点，一样意思的）
x = np.array(x)
print("最大数"+str(max_data))
print(x)

# 设置需要采样的信号，频率分量有180，390和600
y=7*np.sin(2*np.pi*11*x) + 2.8*np.sin(2*np.pi*15*x)+5.1*np.sin(2*np.pi*20*x)

yy=fft(y)                     # 快速傅里叶变换
yreal = yy.real               # 获取实数部分
yimag = yy.imag               # 获取虚数部分

yf = abs(fft(y))             # 取绝对值
print(yf)
for i in range(len(yf)):  # 对数据进行降噪处理
    if yf[i] > 55:
        yf[i] = 0

print("傅里叶预处理")
print(yf)
yf1=yf/len(x)           # 归一化处理
yf2 = yf1[range(int(len(x)/2))]  # 由于对称性，只取一半区间

xf = np.arange(len(y))        # 频率
xf1 = xf
xf2 = xf[range(int(len(x)/2))]  # 取一半区间


plt.subplot(221)
plt.plot(x,y)
plt.title('Original wave')

plt.subplot(222)
plt.plot(xf,yf,'r')
plt.title('FFT of Mixed wave(two sides frequency range)',fontsize=7,color='#7A378B')  #注意这里的颜色可以查询颜色代码表

plt.subplot(223)
plt.plot(xf1,yf1,'g')
plt.title('FFT of Mixed wave(normalization)',fontsize=9,color='r')

plt.subplot(224)
plt.plot(xf2,yf2,'b')
plt.title('FFT of Mixed wave)', fontsize=10,color='#F08080')


plt.show()