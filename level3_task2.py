import pandas as pd
import plotly.express as px
def load_dataset(file_path):
    return pd.read_csv(file_path)

def generate_visualization(df):
    line_chart = px.line(df,x='A',y='B')
    bar_chart = px.bar(df,x='A',y='B')
    scatter_plot = px.scatter(df,x='A',y='B')
    return line_chart,bar_chart,scatter_plot

def main():
    file_path=input("Enter the dataset file path:")
    df=load_dataset(file_path)

    line_chart,bar_chart,scatter_plot=generate_visualization(df)
    line_chart.show()
    bar_chart.show()
    scatter_plot.show()
    if __name__=="__main__":
        main()