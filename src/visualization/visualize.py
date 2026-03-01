import matplotlib.pyplot as plt
import seaborn as sns

def display_combine_plot(data, x: int,y: int, n_classes: int, cls: list):
    for i in range(n_classes):
        for j in range(i+1,n_classes):
            sns.jointplot(x=data.columns[x], y=data.columns[y], data=data[data['Class'].isin(cls)], kind='scatter', hue='Class')