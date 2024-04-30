import sys
import copy
#
sys.path.append('../Finite-Sequence/')
from Complex_Sequence import *
#
def conv(x, h):
	x_cp = copy.deepcopy(x)
	h_cp = copy.deepcopy(h)
	x_cp_index = x_cp.get_index()
	h_cp_index = h_cp.get_index()
	x_cp_value = x_cp.get_value()
	h_cp_value = h_cp.get_value()
	y_index = list(range(x_cp_index[0], x_cp_index[0] + len(x_cp_index) + len(h_cp_index) -1))
	h_cp.time_inverse()
	h_cp.time_shift(x_cp_index[0] - h_cp_index[len(h_cp_index) - 1])
	y_value = []
	for i in y_index:
		sum = 0
		for j in y_index:
			if j > h_cp_index[len(h_cp_index) - 1]:
				break
			if j > x_cp_index[len(x_cp_index) - 1]:
				break
			if  j < h_cp_index[0]:
				continue
			sum = sum + x_cp_value[x_cp_index.index(j)] * h_cp_value[h_cp_index.index(j)]
		h_cp.time_shift(1)
		y_value.append(sum)
	y = Finite_Sequence('y', 0, 0)
	y.set_sequence(y_index, y_value)
	return y
#
def corr(x, y):
	y.time_inverse()
	return conv(x, y)

#
if __name__ == '__main__':
	a_o = Finite_Sequence('a', 0, 4)
	b_o = Finite_Sequence('b', 0, 2)
	a_o.set_sequence([0, 1, 2, 3, 4, 5], [5, 0, 3, 1, 2, -1])
	b_o.set_sequence([0, 1, 2, 3, 4], [4, 6, 3, 2, 1])
	y_o = conv(a_o, b_o)
	print('y o index: ' + str(y_o.get_index()))
	print('y o value: ' + str(y_o.get_value()))
	#
	a = Finite_Sequence('a', 0, 4)
	b = Finite_Sequence('b', 0, 2)
	a.set_sequence([-1, 0, 1, 2, 3, 4], [5, 0, 3, 1, 2, -1])
	b.set_sequence([-2, -1, 0, 1, 2], [4, 6, 3, 2, 1])
	
	y = conv(a, b)
	print('y index: ' + str(y.get_index()))
	print('y value: ' + str(y.get_value()))

	print('a index: ' + str(a.get_index()))
	print('a value: ' + str(a.get_value()))
	print('b index: ' + str(b.get_index()))
	print('b value: ' + str(b.get_value()))

	y_ = conv(b, a)
	print('y bar index: ' + str(y_.get_index()))
	print('y bar value: ' + str(y_.get_value()))

	print('a index: ' + str(a.get_index()))
	print('a value: ' + str(a.get_value()))
	print('b index: ' + str(b.get_index()))
	print('b value: ' + str(b.get_value()))

	r_xy = corr(a, b)
	print('r_xy index: ' + str(r_xy.get_index()))
	print('r_xy value: ' + str(r_xy.get_value()))
