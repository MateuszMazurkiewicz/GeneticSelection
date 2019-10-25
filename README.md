# GeneticSelection
Use of genetic algorithm for feature selection

GeneticSelector - genetic_selection/genetic_selector.py, uses evolutionary methods (tournamemnt selection, crossover, mutation, elite) to select k from 0..n values based on provided fitness function (user has to implement class inheriting from ScoreProvider - genetic_selection/score_provider.py). 

To visualize progress of genetic algorithm it is necessary to save logs to csv file and run in parallel ProgressVisualizer.visualize() method - genetic_selection/progress_visualization.py (as another process).

Algorithm can be applied for example to find best k features for building Machine Learning model.

Check 'examples' folder to see how to use.