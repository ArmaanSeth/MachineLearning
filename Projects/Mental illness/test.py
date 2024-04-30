import numpy as np
import tensorflow as tf
x=[0.28, 0.  , 0.  , 0.  , 3.  , 1.  , 0.  , 0.  , 1.  , 1.  , 0.  ,
        1.  , 1.  , 1.  , 1.  , 0.  ]
x=np.array(x)[np.newaxis,:]
model=tf.keras.models.load_model('C:\\Users\\Armaan\\Downloads\\GDSC\\Model_new.h5')
print(model.predict(x))
