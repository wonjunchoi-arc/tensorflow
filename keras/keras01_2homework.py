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

#3. 컴파일, 훈련
model.compile(loss='mse', optimizer='adam')
model.fit(x,y, epochs=2500, batch_size=1)

#4. 평가, 예측
loss = model.evaluate(x,y)
print('loss', loss)

result =model.predict(x_pred)
print('6의 예측값', result)

