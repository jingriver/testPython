import numpy
import theano.tensor as T
from theano import function
from theano import pp
x = T.dscalar('x')
y = T.dscalar('y')
z = x + y
f = function([x, y], z)
print f(2, 3)

#in Theano, all symbols must be typed. In particular, T.dscalar is the type 
#we assign to '0-dimensional arrays (scalar) of doubles (d)'. It is a Theano Type.

#dscalar is not a class. Therefore, neither x nor y are actually instances of dscalar. 
#They are instances of TensorVariable. x and y are, however, assigned the theano Type dscalar 
#in their type field, as you can see here:
# >>> type(x)
# <class 'theano.tensor.var.TensorVariable'>
# >>> x.type
# TensorType(float64, scalar)
# >>> T.dscalar
# TensorType(float64, scalar)
# >>> x.type is T.dscalar
# True

#By calling T.dscalar with a string argument, you create a Variable representing a 
#floating-point scalar quantity with the given name.
 
x = T.dmatrix('x')
y = T.dmatrix('y')
z = x + y
f = function([x, y], z)
print f([[1, 2], [3, 4]], [[10, 20], [30, 40]])
print pp(z)

a =  T.vector() # declare variable
out = a + a ** 10               # build symbolic expression
f = function([a], out)   # compile function
print(f([0, 1, 2]))


x = T.dmatrix('x')
s = 1 / (1 + T.exp(-x))
logistic = function([x], s)
print logistic([[0, 1], [-1, -2]])

s2 = (1 + T.tanh(x / 2)) / 2
logistic2 = function([x], s2)
print logistic2([[0, 1], [-1, -2]])


a, b = T.dmatrices('a', 'b')
diff = a - b
abs_diff = abs(diff)
diff_squared = diff**2
f = function([a, b], [diff, abs_diff, diff_squared])
print f([[1, 1], [1, 1]], [[0, 1], [2, 3]])
print pp(abs_diff)

