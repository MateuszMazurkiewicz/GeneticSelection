import sys, os
sys.path.insert(0, os.path.abspath('..'))
from genetic_selection.progress_visualization import ProgressVisualizer
# visualizes progress of 'search_max_sum.py'
pv = ProgressVisualizer('data.csv')
pv.visualize()