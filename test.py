import os
os.environ['MPLCONFIGDIR'] = os.path.expanduser('~/.matplotlib')

import pandas
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import seaborn
 
print("sucess")