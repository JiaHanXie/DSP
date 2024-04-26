import cmath
import random
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

#sequence
class Finite_Sequence:
	__index = []
	__value = []
	__name = ''
	def __init__(self, name = 'x', first_index = 0, last_index = 10, min_value = -1, max_value = 1):
		self.__name = name
		self.__index = list(range(first_index, last_index+1))
		self.__value = []
		for i in range(last_index-first_index+1):
			self.__value.append(complex(min_value + random.random() * (max_value-min_value), 
			min_value + random.random() * (max_value-min_value)))
	def __del__(self):
		print('Finite Sequence ' + self.__name + ' deleted!')
	#set value
	def set_sequence(self, index = [], value = []):
		self.__index = []
		self.__value = []
		if len(index) != len(value):
			print('Error! The length of index and value not matched!')
			return
		for element in index:
			if isinstance(element,float) or isinstance(element, int):
				self.__index.append(int(element))
			else:
				print('Error! index must be float or integer!')
				return
		for element in value:
			if isinstance(element,float) or isinstance(element, int) or isinstance(element, complex):
				self.__value.append(complex(element))
			else:
				print('Error! value must be float, integer or complex!')
				return
	#get index
	def get_index(self):
		return self.__index
	#get value
	def get_value(self):
		return self.__value
	#get real
	def get_real(self):
		real = []
		for element in self.__value:
			real.append(element.real)
		return real
	#get imaginary
	def get_imaginary(self):
		imaginary = []
		for element in self.__value:
			imaginary.append(element.imag)
		return imaginary
	#get name
	def get_name(self):
		return self.__name
	#x[-n]
	def time_inverse(self):
		self.__value.reverse()
		self.__index.reverse()
		count = 0
		for element in self.__index:
			self.__index[count] = -element
			count += 1
	#x*[n]
	def conjugate_seq(self):
		count = 0
		for element in self.__value:
			self.__value[count] = element.conjugate()
			count += 1
	#x*[-n]
	def conj_ti(self):
		self.time_inverse()
		self.conjugate_seq()
	#-x*[-n]
	def minus_conj_ti(self):
		self.time_inverse()
		self.conjugate_seq()
		minus_complex = []
		for element in self.__value:
			minus_complex.append(-element)
		self.__value = minus_complex
	#x[n-k] shift right is positive
	def time_shift(self, time_shift = 0):
		count = 0
		for element in self.__index:
			self.__index[count] = element + time_shift
			count += 1
	#plot
	def plot_3d(self, figure):
		plt.figure(figure)
		ax = plt.axes(projection ='3d')
		x = self.get_index()
		y = self.get_real()
		z = self.get_imaginary()
		ax.stem(z,x,y)
		#plt.title('')
		ax.set_ylabel('n')
		ax.set_zlabel('Real')
		ax.set_xlabel('Imaginary')
		ax.grid('true')
		plt.show(block=False)
		input('Press Enter to continue...')
	def plot_R(self, figure):
		plt.figure(figure)
		x = self.get_index()
		y = self.get_real()
		plt.xlabel('n')
		plt.ylabel('Real')
		plt.stem(x, y)
		plt.show(block=False)
		input('Press Enter to continue...')
	def plot_I(self, figure):
		plt.figure(figure)
		x = self.get_index()
		y = self.get_imaginary()
		plt.xlabel('n')
		plt.ylabel('Imaginary')
		plt.stem(x, y)
		plt.show(block=False)
		input('Press Enter to continue...')
	#x[n] = xcs[n] + xca[n]
	
	
#delta[n]
def unit_sample(first_index = 0, last_index = 0):
	unit_sample = Finite_Sequence('unit-sample', first_index, last_index)
	unit_sample_index = unit_sample.get_index()
	unit_sample_value = unit_sample.get_value()
	value = []
	count = 0
	for element in unit_sample_value:
		if count == -first_index:
			value.append(complex(1))
		else:
			value.append(complex(0))
		count += 1
	unit_sample.set_sequence(unit_sample_index, value)
	return unit_sample
#u[n]
def unit_step(first_index = 0, last_index = 0):
	unit_step = Finite_Sequence('unit-step', first_index, last_index)
	unit_step_index = unit_step.get_index()
	unit_step_value = unit_step.get_value()
	value = []
	count = 0
	for element in unit_step_value:
		if count >= -first_index:
			value.append(complex(1))
		else:
			value.append(complex(0))
		count += 1
	unit_step.set_sequence(unit_step_index, value)
	return unit_step


#
if __name__ == '__main__':
	x = complex(2.0 , -2.0)

	print('phase = ' + str(cmath.phase(x)/cmath.pi) + 'pi')

	y = []
	for i in range(10):
		y.append(complex(random.random(), random.random()))

	print(str(x))
	print(type(x))


	plt.figure(1)
	ax = plt.axes(projection ='3d')
	x = list(range(10))
	y = list(range(10))
	z = list(range(10))
	#
	ax.stem(x,y,z)
	#plt.title('')
	ax.set_xlabel('n')
	ax.set_ylabel('R')
	ax.set_zlabel('I')
	ax.grid('true')
	plt.show(block=False)
	input()
	#
	plt.figure(2)
	x = [1,2,3,4,5,6,7,8,9,10]
	y = [11,8,26,16,9,17,23,4,14,10]
	plt.xlabel('n')
	plt.ylabel('Real')
	plt.stem(x, y)
	plt.show(block=False)
	input()

	exit()