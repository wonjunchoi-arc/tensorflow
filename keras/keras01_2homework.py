#완성한뒤 출력결과값 스샷
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np

#1. 데이터
x=np.array([1,2,3,4,5])
y=np.array([1,2,4,3,5])
x_pred = np.array([6])



#2. 모델 구성

model =Sequential()
model.add(Dense(1,input_dim=1))

