import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1 Load the Data
df = pd.read_csv('medical_examination.csv')

# 2 Transform the Height column and Create the BMI

df['height'] = df['height']/100
df['bmi'] = round((df['weight']/(df['height'])**2), 2)

# 3 Create the overweight column
df['overweight'] = [1 if x > 25 else 0 for x in df['bmi']]


# 4
df['cholesterol'] = [0 if x <= 1 else 1 for x in df['cholesterol']]
df['gluc'] = [0 if x <= 1 else 1 for x in df['gluc']]

def draw_cat_plot():
    # 5 Select the variables you want to plot
    variables = ['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke']

    # 6 Melt the DataFrame to long format
    df_cat = df.melt(id_vars='cardio', value_vars=variables, var_name='variable', value_name='value')


    # 7 Create a grouped bar plot using catplot
    fig = sns.catplot(
        data=df_cat,
        x='variable', y=None,
        hue='value', col='cardio',
        kind='count', height=5, aspect=1.2
    )

    # 8
    plt.tight_layout()

    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11 Filter the Data
    df['ap_lo'] = [x if x > y else y for x, y in zip(df['ap_lo'], df['ap_hi'])]
    lower_height, upper_height = df['height'].quantile([0.025, 0.975])
    lower_weight, upper_weight = df['weight'].quantile([0.025, 0.975])

    df_heat = df.loc[(df['height'].between(lower_height, upper_height)) &
                     (df['weight'].between(lower_weight, upper_weight))]


    # 12 Create the Correlation Matrix
    corr = df_heat.corr()

    # 13 Create the Figure Formation and Plot the Heatmap
    mask = np.triu(np.ones_like(corr, dtype=bool))
    sns.heatmap(corr, xticklabels=corr.columns, yticklabels=corr.columns, cmap='coolwarm', annot=True, fmt='.2f', mask=mask)
    plt.tight_layout()

    # 14
    fig, ax = plt.subplots()

    # 15

    # 16
    fig.savefig('heatmap.png')
    return fig

