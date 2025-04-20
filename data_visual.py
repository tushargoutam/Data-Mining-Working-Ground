class Data_Visualization:

    def __init__(self,data):
        self.data = data


    def histogram(self,*args):
        import matplotlib.pyplot as plt
        # add constraint for numeric data only it should be possible
        if len(args)==1:
            plt.hist(self.data[args[0]])
            plt.savefig("1dhist.png",dpi=300,bbox_inches = 'tight')
            plt.close()
        elif len(args)==2:
            plt.hist2d(self.data[args[0]],self.data[args[1]])
            plt.savefig("2dhist.png",dpi=300,bbox_inches = 'tight')
            plt.close()
        else:
            return "Error"
        
    def box_plt(self,feature_name):
        import matplotlib.pyplot as plt
        plt.boxplot(self.data[feature_name])
        plt.savefig('boxplot.png',dpi=300,bbox_inches = 'tight')
        plt.close()

    
    def violin_plot(self,feature_name):
        import matplotlib.pyplot as plt
        plt.violinplot(self.data[feature_name])
        plt.savefig('violinplot.png',dpi=300,bbox_inches = 'tight')
        plt.close()

    def barplot(self,feature_name):
        import matplotlib.pyplot as plt
        plt.bar(self.data[feature_name])
        plt.savefig('barplot.png',dpi=300,bbox_inches = 'tight')
        plt.close()

    
    def piechart(self,feature_name):
        import matplotlib.pyplot as plt
        plt.pie(self.data[feature_name])

    
    def scatter_plot(self,*args):
        import matplotlib.pyplot as plt
        import seaborn as sns
        if len(args) == 1:
            sns.scatterplot(self.data[args[0]])
            plt.savefig('scatter.png',dpi=300,bbox_inches = 'tight')
            plt.close()
        else:
            sns.scatterplot(self.data[args[0]],self.data[args[1]])
            plt.savefig('scatter.png',dpi=300,bbox_inches = 'tight')
            plt.close()

        
    def line_plot(self,*args):
        import matplotlib.pyplot as plt
        plt.plot(self.data[args[0]],self.data[args[1]])
        plt.savefig('line.png',dpi=300,bbox_inches = 'tight')
        plt.close()


    def hexbin_density_plot(self,*args):
        import matplotlib.pyplot as plt
        plt.hexbin(self.data[args[0]],self.data[args[1]])

    def heatmaps(self):
        import matplotlib.pyplot as plt
        import seaborn as sns

        sns.heatmap(self.data.corr())
        plt.savefig('heatmap.png',dpi=300,bbox_inches = 'tight')
        plt.close()