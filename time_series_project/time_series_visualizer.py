import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from matplotlib.figure import Figure  # For type annotation

# Load and clean data
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'])
df = df.loc[
    (df['value'] >= df['value'].quantile(0.025)) &
    (df['value'] <= df['value'].quantile(0.975))
]


def draw_line_plot() -> Figure:
    fig_ax = plt.subplots(figsize=(20, 7))
    fig: Figure = fig_ax[0]
    ax = fig_ax[1]

    sns.lineplot(x='date', y='value', data=df, ax=ax)

    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')

    fig.savefig('line_plot.png')
    return fig


def draw_bar_plot() -> Figure:
    df_bar = df.copy()
    df_bar['month'] = df_bar['date'].dt.month
    df_bar['month_name'] = df_bar['date'].dt.month_name()
    df_bar['year'] = df_bar['date'].dt.year

    month_order = ['January', 'February', 'March', 'April', 'May', 'June',
                   'July', 'August', 'September', 'October', 'November', 'December']

    grouped = df_bar.groupby(['year', 'month_name']).agg({'value': 'mean'}).reset_index()
    grouped['month_name'] = pd.Categorical(grouped['month_name'], categories=month_order, ordered=True)
    grouped = grouped.sort_values(['year', 'month_name'])

    fig_ax = plt.subplots(figsize=(10, 8))
    fig: Figure = fig_ax[0]
    ax = fig_ax[1]

    sns.barplot(data=grouped, x='year', y='value', hue='month_name', palette='tab10', ax=ax)

    ax.set_title('Average Monthly Values Grouped by Year')
    ax.set_xlabel('Year')
    ax.set_ylabel('Average Value')
    ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
    ax.legend(title='Month', bbox_to_anchor=(0.15, 1))

    plt.tight_layout()
    fig.savefig('bar_plot.png')
    return fig


def draw_box_plot() -> Figure:
    df_box = df.copy()
    df_box.reset_index(drop=True, inplace=True)
    df_box['year'] = df_box['date'].dt.year
    df_box['month'] = df_box['date'].dt.strftime('%b')

    fig_ax = plt.subplots(1, 2, figsize=(20, 8))
    fig: Figure = fig_ax[0]
    (ax1, ax2) = fig_ax[1]

    # Year-wise box plot
    year_palette = sns.color_palette(n_colors=df_box['year'].nunique())
    sns.boxplot(
        x='year', y='value', data=df_box, ax=ax1, hue='year',
        palette=year_palette, fliersize=3, linewidth=1,
        flierprops=dict(marker='o', color='black', markerfacecolor='black'),
        legend=False
    )
    ax1.set_title('Year wise Box plot (Trend)')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Page Views')

    # Month-wise box plot
    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                   'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    month_palette = sns.color_palette('husl', n_colors=12)
    month_color_dict = dict(zip(month_order, month_palette))

    sns.boxplot(
        x='month', y='value', data=df_box, ax=ax2, order=month_order,
        hue='month', palette=month_color_dict, fliersize=3, linewidth=1,
        flierprops=dict(marker='o', color='black', markerfacecolor='black'),
        legend=False
    )
    ax2.set_title('Month wise Box plot (Seasonality)')
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Page Views')

    plt.tight_layout()
    fig.savefig('box_plot.png')
    return fig
