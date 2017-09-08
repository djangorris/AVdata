import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.patches as mpatches
from matplotlib import style
from matplotlib.font_manager import FontProperties

# style.use('ggplot')
pivoted.plot()
plt.xlabel('Year')
plt.ylabel('Average Benchmark Premium')
plt.title('Comparison of Average Benchmark Premium')
plt.grid(True)
plt.legend(loc='upper center', ncol=2, fancybox=True, shadow=True)
plt.show()