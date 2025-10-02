# Junyoung Seo

Hi, my name is Junyoung Seo and my favorite programming language is Python because it allows me to work flexibly across data analysis, machine learning, and web development.


#example code

```python

import tensorflow as tf
import numpy as np

X = np.array([1, 2, 3, 4, 5], dtype=float)
y = 2 * X + 1

model = tf.keras.Sequential([
    tf.keras.layers.Dense(units=1, input_shape=[1])
])

model.compile(optimizer='sgd', loss='mean_squared_error')

model.fit(X, y, epochs=100, verbose=0)

new_x = 6.0
pred = model.predict([new_x])
```


This code trains a simple linear model using TensorFlow and makes a prediction for a new input.
