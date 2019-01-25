from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate
import scipy as sp

# a, c, E의 numpy array 생성
y = np.zeros(7)
x = np.zeros(9)
a,c = np.meshgrid(x,y) # 7x9 짜리 meshgrid 생성
E = np.zeros(63, dtype='f')

# 파일 열기
f = open('ev.txt', 'r')

# 첫 줄은 정보가 없으므로 읽고 버림
f.readline()
i = 0       # 라인 넘버 의미, 자료들의 인덱스

# 두번 째줄부터 담긴 정보 읽기
while True:
    line = f.readline()

    # 파일 다 읽었을 경우 종료
    if not line:
        break
        
    j1 = int(i/9)
    j2 = int(i%9)
    
    # 탭으로 자료 나누기
    line = line.split('\t')
    a[j1][j2] = float(line[0])
    c[j1][j2] = float(line[1])
    E[i] = float(line[2])
    i += 1


# # Cubic Spline Interpolation
En = np.zeros((a.size, E.size))
spline = sp.interpolate.Rbf(a, c, E, function='cubic')
En = spline(a, c)

# Drawing 3D contour
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.contourf(a, c, En,1000,cmap='rainbow')

# x,y,z축에 각 각 라벨링
ax.set_xlabel('a (Angstrom)	')
ax.set_ylabel('c (Angstrom)	')
ax.set_zlabel('E (ev)')

# figure(contour)을 보여주는 함수
plt.show()
