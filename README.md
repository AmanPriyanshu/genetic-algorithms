# genetic-algorithms
Understanding genetic algorithms

Genetic Algorithms are optimization-based algorithms. They are used during searches and optimization. It was first introduced in 1970 by John Holland. They virtually simulate the evolution of species according to Darwin's theory of Natural Selection. They are a subset of Evolutionary Algorithms. They are commonly used to generate high-quality optimizations for complex problems.

Let us begin by understanding the basics of Genetic Algorithms. GAs typically simulate natural selection, i.e. species which can adapt to the changing environment are more probable of continuing their genes. Let us define some important terms related to this algorithm.

GENERATION: Each generation basically represents the iteration at which the current simulation is taking place.
POPULATION: Population consists of individuals who are part of a generation. They consist of multiple individuals. As the generations progress, the population improves in quality regarding the problem we need to solve.
INDIVIDUALS: Individuals/chromosomes make up the population. At the end of every generation, the fittest are selected among these individuals.  Each individual basically consists of a numeric or string value which is used to evaluate it and represent its performance. 

## PSEUDO-ALGORITHM

Here, is a sequence of steps which roughly highlights the important steps involved in GA implementation.
Step 1: Individuals prepare a set of protocols and are evaluated based on this. The evaluation here can analogous to a fitness test.
Step 2: Those individuals who are successful in this "Fitness/Evaluation Test" will parent and create an offspring generation. This generation will have a fitter genome due to their parents' success.
Step 3: Genes from the most highly evaluated individual or "fittest" individual are propagated throughout the offspring generation. This allows for a better breed than the previous.

## EXPLANATIONS:

So finally, how would we go about this implementation? Firstly we can begin with an initial generation where every individual represents a solution from the sample space.  Each individual is coded as a vector (chromosome) of components. These variable components can be considered as Genes.

FITNESS SCORE is basically the gauge or the measure of the fitness a particular individual has towards solving a problem. As we have learnt the individuals having a better/higher fitness score are more likely to pass on their genes. However, during gene passing the genes of both the parents are passed, thus creating some deviation from the parent generation. This allows for the development of improved versions of the previous generation. In certain cases, we can also have individuals of the least fitness die in the case of a static population setting.
We can basically understand that under these circumstances every new generation will have better "genes" on average. Let us now discuss the different Operators involved in genetic algorithms.

## OPERATORS:
Operators are functions which help progress through different stages in Genetic Algorithm such as the selection of the fittest, selection of mates who will parent, etc. Here are the essential Operators used in GA.

1. Selection Operators:  They proffer fitter individuals and select them for the passing of genes to the next generation
2. Crossover Operators: (Mating) Two individuals are selected using selection operator and crossover sites are chosen randomly. Then the genes at these crossover sites are exchanged thus creating a completely new individual (offspring).
3. Mutation Operator: The idea behind mutation is to allow for a more diverse pool of solutions. Mutations may sometimes deter and may sometimes aid in problem-solving and thus are left to chance. The main aim is to insert random genes in offspring to maintain the diversity in population to avoid premature convergence and thus a poor solution.

## FLOW-CHART:
Now that we have understood the basic flow-chart and algorithm of Genetic Algorithms. Let us take a small look at its implementation.

![relative path is wrong](flowchart.png)

## IMPLEMENTATION:
Please take a look at the code available here: https://github.com/AmanPriyanshu/genetic-algorithms/blob/master/linear_regression_with_ga.py
