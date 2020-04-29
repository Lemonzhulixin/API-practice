import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import scipy



'''np.random.seed(sum(map(ord, "aesthetics")))
#data = np.random.normal(size=(20, 6)) + np.arange(6) / 2
#sns.boxplot(data)
sns.set_style("ticks")
#sns.set_style("dark")
sns.set_style("white")
#sns.set_style("whitegrid")
#sns.axes_style("ticks")'''


def sinplot(flip=1):
    x = np.linspace(0, 14, 100)
    for i in range(1, 7):
        plt.plot(x, np.sin(x + i * .5) * (7 - i) * flip)

sns.despine(sinplot())
#sinplot()
plt.show()