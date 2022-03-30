'''
StyleSheet

    MatPlot의 스타일링에 관해 수업 외 조사, 실습한 내용


    Ref :
        - 스타일시트 :   https://hong-yp-ml-records.tistory.com/88
        - 그 외 스타일 : https://teddylee777.github.io/visualization/matplotlib-tutorial
'''
from stylemod import *

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

import random

'''
1. 스타일시트 지정

plt.style.available : 스타일시트 목록 확인
plt.style.use() : 스타일시트 설정
'''
div(1)

series = pd.Series(random.sample(range(100, 1000), 10), 
                   index = list('matplotlib')) 


# 스타일시트 목록 확인
print(plt.style.available)
'''
['Solarize_Light2', '_classic_test_patch', '_mpl-gallery', '_mpl-gallery-nogrid', 'bmh', 'classic', 'dark_background', 'fast', 'fivethirtyeight', 'ggplot', 'grayscale', 'seaborn', 'seaborn-bright', 'seaborn-colorblind', 'seaborn-dark', 'seaborn-dark-palette', 'seaborn-darkgrid', 'seaborn-deep', 'seaborn-muted', 'seaborn-notebook', 'seaborn-paper', 'seaborn-pastel', 'seaborn-poster', 'seaborn-talk', 'seaborn-ticks', 'seaborn-white', 'seaborn-whitegrid', 'tableau-colorblind10']
'''

    # (1) default
sp()

plt.style.use("default")  # 스타일시트 설정 코드 : default로 설정
plt.bar(series.index, series.values)
plt.show()

    # (2) bmh 스타일시트
sp()

plt.style.use('bmh')
plt.bar(series.index, series.values)
plt.show()

    # (3) classic 스타일시트
sp()

plt.style.use('classic')
plt.bar(series.index, series.values)
plt.show()

    # (4) dark_background 스타일시트
sp()

plt.style.use('dark_background')
plt.bar(series.index, series.values)
plt.show()

    # (5) Solarize_Light2 스타일시트
sp()

plt.style.use('Solarize_Light2')
plt.bar(series.index, series.values)
plt.show()


