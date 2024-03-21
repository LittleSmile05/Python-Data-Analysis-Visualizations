import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

def load_and_preprocess_data(file_path):
    my_data = pd.read_csv(file_path, header=0, names=["Date", "Programming Lang", "Posts"])
    my_data['Date'] = pd.to_datetime(my_data['Date'])
    my_data = my_data.pivot_table(index="Date", columns="Programming Lang", values="Posts", aggfunc='sum', fill_value=0)
    return my_data

def plot_advanced_data(data):
    plt.figure(figsize=(12, 8))

    palette = sns.color_palette("husl", len(data.columns))

    for i, column in enumerate(data.columns):
        plt.plot(data.index, data[column], label=column, color=palette[i])
    
    plt.xlabel("Years")
    plt.ylabel("Post Numbers")
    plt.title("Data of Programming Languages", fontsize=14)
    plt.ylim(0, data.values.max() + 5000)  
    
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

file_path = r"C:\Users\gunel\Desktop\Python DA\Lesson 2 Visual\QueryResults.csv"

my_data = load_and_preprocess_data(file_path)

plot_advanced_data(my_data)