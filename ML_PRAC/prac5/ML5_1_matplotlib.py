'''
ML5_1

    Matplotlib
    
    추천 튜토리얼 + 참고자료 :
        - https://github.com/matplotlib/matplotlib
        - https://wikidocs.net/92071
'''
from stylemod import *
import matplotlib.pyplot as plt
import numpy as np


'''
(1) linear line chart : 선형 그래프

    plt.plot() 메소드는 따로 종류를 지정하지 않을 경우
    해당하는 선형플롯을 디폴트값으로 한다.
'''
# div(1)

# xpoints = np.array([0, 6]) # x 좌표 2개
# ypoints = np.array([0, 250]) # y 좌표 2개

# plt.plot(xpoints,ypoints)   # 두 점을 이은 선형그래프 생성
# plt.show()


# # 선 말고 점으로 플롯그리기
# sp()

# xpoints = np.array([1, 8])
# ypoints = np.array([3, 10])

# plt.plot(xpoints, ypoints, 'o')
# plt.show()

# # 3개 이상의 다수의 점으로 플롯만들기
# sp()

# xpoints = np.array([1, 2, 6, 8])
# ypoints = np.array([3, 8, 1, 10])

# plt.plot(xpoints,ypoints)
# plt.show()

# # 플롯의 x,y축에 라벨 추가하기
# sp()
# x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
# y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

# plt.plot(x,y)

# plt.xlabel('Average Pulse')
# plt.ylabel('Calorie Burnage')
# plt.show()


'''
(2) 산점도 : scatter chart

    plt.scatter() 메소드
'''
# div(2)

# x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
# y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

# plt.scatter(x,y)
# plt.show()


'''
(3) 막대그래프 : bar chart

    plt.bar() , plt.barh() 메소드 사용
'''
# div(3)

# car_brand = np.array(['BMW', 'Avante', 'Audi'])
# car_avgSpeed = np.array([180,120,150])

# plt.bar(car_brand,car_avgSpeed)

# plt.xlabel('Brand')  # x라벨
# plt.ylabel('Speed')  # y라벨

# plt.show()

# # horizontal chart : barh() 메소드 사용
# sp()

# plt.barh(car_brand,car_avgSpeed)
# plt.show()


'''
(4) 히스토그램 : Histograms

    plt.hist() 메소드 사용
    
    - 히스토그램이란 구간별로 데이터를 나누어 보여주는 차트
    
'''
# div(4)

# # 정규분포의 랜덤값 생성
# x = np.random.normal(170,10,250) 
# print(x)

# # 히스토그램 생성
# sp()
# plt.hist(x)

# plt.show()


'''
(5) 파이차트 : Pie chart

    plt.pie() 메소드 사용
    
'''
# div(5)

# y = np.array([35,25,25,15]) 

# plt.pie(y)
# plt.show()

# # 라벨 부착
# sp()
# mylabels = ['Apples', 'Bananas', 'Cherries', 'Dates'] 
# plt.pie(y, labels = mylabels)
# plt.show()


 



