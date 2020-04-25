import numpy as np
import random
import matplotlib.pyplot as plt

def create_dataset(n, slope):
	data = np.empty([n, 2])
	for i in range(n):
		x = random.randint(-100, 100)
		y = slope*x
		data[i][0], data[i][1] = x, y

	return data

def lr_predict(X, w):
	y_pred = X*w[0]
	return y_pred

def lr_cost(y_pred, Y):
	rms = np.sqrt(np.sum(np.square(y_pred-Y)))
	return rms

def lr_grad(w, Y, y_pred, X, alpha):
	dw = [0]
	dw[0] = np.mean(X*(y_pred-Y))
	w[0] = w[0] - alpha*dw[0]
	return w

def lr_approach(iterations, data):
	w = [0]
	c = 0
	for i in range(iterations):
		y_pred = lr_predict(data.T[0], w)
		#print(y_pred)
		rms = lr_cost(y_pred, data.T[1])
		#print(rms)
		w = lr_grad(w, data.T[1], y_pred, data.T[0], 0.0001)
		#print(w)
		if int(w[0]+1) == 602:
			break
		c += 1
	return w, c

def linear_regression(iterations=1000):
	data = create_dataset(100, 602)
	w, c = lr_approach(iterations, data)
	print(int(w[0]+1), 'at iteration', c)
	return c


""" Let us do the same thing using GA and compare the results """
# Assuming slope ranges from -1000 to 1000. This will be the sample space for our individuals.
# Assume here every individual in a generation is represented by its index numbers and its genes by the value stored within that index
def generate_parent_gen(n):
	generation = []
	for i in range(n):
		generation.append(random.randint(-1000, 1000))
	return generation

def fitness_scorer(generation, data):
	fitness = []
	for individual in range(len(generation)):
		y_pred = generation[individual]*data.T[0]
		fitness.append(np.sqrt(np.sum(np.square(y_pred-data.T[1]))))
	return fitness
# since we have only one gene here let us take the average of the parents + the fittest
def offspring_gen(gen):
	gen_new = []
	for i in range(len(gen)):
		gen_new.append((gen[0] + random.choice(gen) + random.choice(gen))/3)

	return gen_new


def genetic_algorithm():
	iterations = 10
	data = create_dataset(100, 602)
	gen = generate_parent_gen(1000)
	value = 0
	c = 0
	for i in range(iterations):
		fitness = fitness_scorer(gen, data)
		fitness, gen = (list(t) for t in zip(*sorted(zip(fitness, gen))))
		if fitness[0] == 0.0:
			value = gen[0]
			break
		# Let's fix population to 1000, so killing 500
		fitness, gen = fitness[:500], gen[:500]
		gen_new = offspring_gen(gen)
		gen = gen + gen_new
		value = gen[0]
		c += 1
	print(value, 'at iteration', c)
	return c

def imager(cga, clr):
	plt.scatter([i for i in range(cga.shape[0])], cga, color='green', marker='.')
	plt.scatter([i for i in range(cga.shape[0])], clr, color='red', marker='.')
	plt.savefig('ga_vs_lr.png')
	plt.clf()

def main():
	cga = []
	clr = []
	for i in range(100):
		cga.append(genetic_algorithm())
		clr.append(linear_regression())
	cga = np.array(cga)
	clr = np.array(clr)
	print(np.mean(cga))
	print(np.mean(clr))
	imager(cga, clr)

main()
