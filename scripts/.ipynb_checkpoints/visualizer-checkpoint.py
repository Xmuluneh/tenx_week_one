import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

class Plotter:
    def __init__(self, data):
        self.data = data

    def plot_horizontal_bar_chart(self, x_values, y_values, title="Horizontal Bar Chart", xlabel="X Axis", ylabel="Y Axis"):
        plt.figure(figsize=(10, 6))
        sns.barplot(x=x_values, y=y_values, data=self.df, palette='viridis')
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        plt.show()

    def plot_heatmap(self, title="Heatmap"):
        plt.figure(figsize=(8, 6))
        sns.heatmap(self.data, annot=True, cmap="YlGnBu", fmt=".2f", linewidths=0.5)
        plt.title(title)
        plt.show()

    def plot_scatter_plot(
        self, x_values, y_values, title="Scatter Plot", xlabel="X Axis", ylabel="Y Axis"
    ):
        plt.figure(figsize=(8, 6))
        plt.scatter(x_values, y_values)
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.show()
    
