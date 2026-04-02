from libraries_used import pd
from libraries_used import plt
from libraries_used import sns

class DataVisualizer:

    def __init__(self,df):
        self.df = df

    #histograms - int/float value variables
    def histogram(self, var, bins=None):
        self.df[var].hist(bins)
        plt.title(f'{var} Histogram')
        plt.xlabel(var)
        plt.ylabel("Amount")
        plt.show()

    #bar plot - categorical variables
    def bar_chart(self, var):
        self.df[var].value_counts().plot(kind='bar')
        plt.title(f'{var} Bar Chart')
        plt.xlabel(var)
        plt.ylabel("Amount")
        plt.show()

    #variable vs target box plot
    def variable_vs_target(self, var, target):
        sns.boxplot(x=target, y=var, data=self.df)
        plt.title(f'{var} Versus {target}')
        plt.xlabel(target)
        plt.ylabel(var)
        plt.show()

    #correlation heatmap
    def corr_matrix(self):
        corr_mtx = self.df.corr()
        sns.heatmap(corr_mtx, square=True)
        plt.title("Correlation Matrix")
        plt.show()

    #find missing values w/ heatmap
    def missing(self):
        sns.heatmap(self.df.isnull(), cbar=False, square=True)
        plt.title("Missing Value Matrix")
        plt.show()


