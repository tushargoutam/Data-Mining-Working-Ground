import pandas as pd
import numpy as np
from data_visual import Data_Visualization  # Replace with actual module name if saved in a file

# Sample dataset
np.random.seed(42)
df = pd.DataFrame({
    'Category': np.random.choice(['A', 'B', 'C'], 100),
    'X': np.random.normal(0, 1, 100),
    'Y': np.random.normal(5, 2, 100),
    'Size': np.random.rand(100) * 100,
    'Labels': np.random.choice(['Label1', 'Label2', 'Label3'], 100),
    'Class': np.random.choice(['Class1', 'Class2'], 100)
})

# For treemap example, group and sum
treemap_data = df.groupby('Labels').agg({'Size': 'sum'}).reset_index()

# Initialize visualization class
viz = Data_Visualization(df)

# Run various plots
viz.histogram('X')
viz.histogram('X', 'Y')
viz.box_plt('X')
viz.violin_plot('Y')
viz.barplot('Category')
viz.grouped_barplot('Category', 'X', 'Class')
viz.stacked_barplot()
viz.piechart('Category')
viz.scatter_plot('X', 'Y')
viz.bubble_chart('X', 'Y', 'Size')
viz.line_plot('X', 'Y')
viz.area_plot('X')
viz.hexbin_density_plot('X', 'Y')
viz.kde_plot('X')
viz.corr_heatmaps()
viz.count_plot('Category')
viz.pair_plot()

# Treemap and parallel coordinates require slightly modified data
treemap_viz = Data_Visualization(treemap_data)
treemap_viz.treemap('Size', 'Labels')

parallel_viz = Data_Visualization(df[['X', 'Y', 'Size', 'Class']])
parallel_viz.parallel_coordinates_plot('Class')

print("All plots generated and saved as .png files.")