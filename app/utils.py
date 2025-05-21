import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def load_data():
    benin_df = pd.read_csv("../data/benin_clean.csv")
    togo_df = pd.read_csv("../data/togo_clean.csv")
    sierra_df = pd.read_csv("../data/sierraleone_clean.csv")

    df = pd.concat(
        [
            benin_df.assign(Country="Benin"),
            togo_df.assign(Country="Togo"),
            sierra_df.assign(Country="Sierra Leone")
        ],
        ignore_index=True
    )
    return df

def summarize_data(df):
    summary = df.groupby('Country')[['GHI', 'DNI', 'DHI']].agg(['mean', 'median', 'std'])
    return summary

def plot_boxplot(df, metric):
    fig, ax = plt.subplots()
    sns.boxplot(x='Country', y=metric, data=df, ax=ax, palette='Set2')
    ax.set_title(f'{metric} Distribution by Country')
    return fig

def plot_bar_avg_ghi(df):
    avg_ghi = df.groupby('Country')['GHI'].mean().sort_values(ascending=False)
    fig, ax = plt.subplots()
    avg_ghi.plot(kind='bar', ax=ax, color='skyblue')
    ax.set_title('Average GHI by Country')
    ax.set_ylabel('GHI')
    return fig
