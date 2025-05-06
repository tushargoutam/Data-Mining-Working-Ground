class Data_Visualization:

    def __init__(self, data):
        self.data = data

    def histogram(self, *args):
        import matplotlib.pyplot as plt
        if len(args) == 1:
            plt.hist(self.data[args[0]])
            plt.savefig("plots/1dhist.png", dpi=300, bbox_inches='tight')
            plt.close()
        elif len(args) == 2:
            plt.hist2d(self.data[args[0]], self.data[args[1]])
            plt.savefig("plots/2dhist.png", dpi=300, bbox_inches='tight')
            plt.close()
        else:
            return "Error"

    def box_plt(self, feature_name):
        import matplotlib.pyplot as plt
        plt.boxplot(self.data[feature_name])
        plt.savefig('plots/boxplot.png', dpi=300, bbox_inches='tight')
        plt.close()

    def violin_plot(self, feature_name):
        import matplotlib.pyplot as plt
        plt.violinplot(self.data[feature_name])
        plt.savefig('plots/violinplot.png', dpi=300, bbox_inches='tight')
        plt.close()

    def barplot(self, feature_name):
        import matplotlib.pyplot as plt
        feature_series = self.data[feature_name].value_counts()
        plt.bar(feature_series.index, feature_series.values)
        plt.savefig('plots/barplot.png', dpi=300, bbox_inches='tight')
        plt.close()

    def grouped_barplot(self, x, y, hue):
        import matplotlib.pyplot as plt
        import seaborn as sns
        sns.barplot(data=self.data, x=x, y=y, hue=hue)
        plt.savefig('plots/grouped_barplot.png', dpi=300, bbox_inches='tight')
        plt.close()

    def stacked_barplot(self):
        import matplotlib.pyplot as plt
        self.data.plot(kind='bar', stacked=True)
        plt.savefig('plots/stacked_barplot.png', dpi=300, bbox_inches='tight')
        plt.close()

    def piechart(self, feature_name):
        import matplotlib.pyplot as plt
        feature_counts = self.data[feature_name].value_counts()
        plt.pie(feature_counts.values, labels=feature_counts.index, autopct='%1.1f%%')
        plt.savefig('plots/piechart.png', dpi=300, bbox_inches='tight')
        plt.close()

    def scatter_plot(self, *args):
        import matplotlib.pyplot as plt
        import seaborn as sns
        if len(args) == 1:
            sns.scatterplot(x=self.data.index, y=self.data[args[0]])
        else:
            sns.scatterplot(x=self.data[args[0]], y=self.data[args[1]])
        plt.savefig('plots/scatter.png', dpi=300, bbox_inches='tight')
        plt.close()

    def bubble_chart(self, x, y, size):
        import matplotlib.pyplot as plt
        plt.scatter(self.data[x], self.data[y], s=self.data[size]*100, alpha=0.5)
        plt.savefig('plots/bubble_chart.png', dpi=300, bbox_inches='tight')
        plt.close()

    def line_plot(self, *args):
        import matplotlib.pyplot as plt
        plt.plot(self.data[args[0]], self.data[args[1]])
        plt.savefig('plots/line.png', dpi=300, bbox_inches='tight')
        plt.close()

    def area_plot(self, feature_name):
        import matplotlib.pyplot as plt
        self.data[[feature_name]].plot(kind='area', stacked=False)
        plt.savefig('plots/areaplot.png', dpi=300, bbox_inches='tight')
        plt.close()

    def hexbin_density_plot(self, *args):
        import matplotlib.pyplot as plt
        plt.hexbin(self.data[args[0]], self.data[args[1]], gridsize=30, cmap='Blues')
        plt.colorbar()
        plt.savefig('plots/hexbin.png', dpi=300, bbox_inches='tight')
        plt.close()

    def kde_plot(self, feature_name):
        import seaborn as sns
        import matplotlib.pyplot as plt
        sns.kdeplot(self.data[feature_name], fill=True)
        plt.savefig('plots/kde_plot.png', dpi=300, bbox_inches='tight')
        plt.close()

    def corr_heatmaps(self):
        import matplotlib.pyplot as plt
        import seaborn as sns
        numeric_data = self.data.select_dtypes(include='number')
        sns.heatmap(numeric_data.corr(), annot=True, cmap='coolwarm')
        plt.savefig('heatmap.png', dpi=300, bbox_inches='tight')
        plt.close()

    def count_plot(self, feature_name):
        import seaborn as sns
        import matplotlib.pyplot as plt
        sns.countplot(x=self.data[feature_name])
        plt.savefig('plots/count_plot.png', dpi=300, bbox_inches='tight')
        plt.close()

    def pair_plot(self):
        import seaborn as sns
        import matplotlib.pyplot as plt
        sns.pairplot(self.data)
        plt.savefig('plots/pair_plot.png', dpi=300, bbox_inches='tight')
        plt.close()

    def treemap(self, size_column, label_column):
        import matplotlib.pyplot as plt
        import squarify
        squarify.plot(sizes=self.data[size_column], label=self.data[label_column], alpha=.7)
        plt.axis('off')
        plt.savefig('plots/treemap.png', dpi=300, bbox_inches='tight')
        plt.close()

    def parallel_coordinates_plot(self, class_column):
        from pandas.plotting import parallel_coordinates
        import matplotlib.pyplot as plt
        parallel_coordinates(self.data, class_column)
        plt.savefig('plots/parallel_coordinates.png', dpi=300, bbox_inches='tight')
        plt.close()





