from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# Python version
import sys
print('Python: {}'.format(sys.version))
# numpy
import numpy
print('numpy: {}'.format(numpy.__version__))
# matplotlib
import matplotlib
print('matplotlib: {}'.format(matplotlib.__version__))

# pandas
import pandas
print('pandas: {}'.format(pandas.__version__))
print('Test for pandas:')
names = ['Bob','Jessica','Mary','John','Mel']
births = [968, 155, 77, 578, 973]
BabyDataSet = list(zip(names,births))
print( pandas.DataFrame(data = BabyDataSet, columns=['Names', 'Births']))

# scikit-learn
import sklearn
print('sklearn: {}'.format(sklearn.__version__))

# tensorflow
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

import tensorflow as tf
print('tensorflow: %s' % tf.__version__)
print('Test for tensorflow:')
hello = tf.constant("Hello, World, from tensorflow!")
sess = tf.Session()
print (sess.run(hello))
a = tf.constant(10)
b = tf.constant(32)
print (sess.run(a+b))

# keras
import keras
print('keras: %s' % keras.__version__)
