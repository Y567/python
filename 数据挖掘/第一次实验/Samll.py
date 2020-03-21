import matplotlib.pyplot as plt
import pywt

# Get data:
file = open('lorenza.dat')  # 打开文档
original = file.readlines()

index = []
data = []
for i in range(128):
    index.append(i)
    data.append(float(original[i]))

# Create wavelet object and define parameters
w = pywt.Wavelet('db8')  # 选用Daubechies8小波
maxLev = pywt.dwt_max_level(len(data), w.dec_len)
print("maximum level is " + str(maxLev))
threshold = 17  # Threshold for filtering

# Decompose into wavelet components, to the level selected:
coEffs = pywt.wavedec(data, 'db8', level=maxLev)  # 将信号进行小波分解

plt.figure()
for i in range(1, len(coEffs)):
    coEffs[i] = pywt.threshold(coEffs[i], threshold * max(coEffs[i]))  # 将噪声滤波

dataRec = pywt.waverec(coEffs, 'db8')  # 将信号进行小波重构

minTime = 0
maxTime = minTime + len(data) + 1

plt.figure()
plt.subplot(2, 1, 1)
plt.plot(index[minTime:maxTime], data[minTime:maxTime])
plt.xlabel('count (t)')
plt.ylabel('original (num-lorenza )')
plt.title("WaveShift")
plt.subplot(2, 1, 2)
plt.plot(index[minTime:maxTime], dataRec[minTime:maxTime - 1])
plt.xlabel('time (s)')
plt.ylabel('original (num-lorenza )')
plt.title("De-noised signal using wavelet techniques")

plt.tight_layout()
plt.show()


if __name__ == '__main__':
    print("main")