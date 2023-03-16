import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df =  pd.read_csv('medical_examination.csv')

# Add 'overweight' column
bmi = df['weight'] / (df['height']/100)**2
df['overweight'] = (bmi > 25).astype(int)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.

df['gluc'] = (df['gluc'] > 1).astype(int)
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'])
    

    # Draw the catplot with 'sns.catplot()'
    chart = sns.catplot(data=df_cat, kind='count', x='variable', hue='value', col='cardio')
    chart.set_axis_labels('Variable', 'Total')
    chart.set_titles('{col_name}')
    plt.show()


    # Get the figure for the output
    fig = chart.fig


    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat =  df[(df['ap_lo'] <= df['ap_hi'])
        & (df['height'] >= df['height'].quantile(0.025))
        & (df['height'] <= df['height'].quantile(0.975))
        & (df['weight'] >= df['weight'].quantile(0.025))
        & (df['weight'] <= df['weight'].quantile(0.975))]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.zeros_like(corr, dtype=bool)
    mask[np.triu_indices_from(mask)] = True

    # Set up the matplotlib figure
    fig, ax =  plt.subplots(figsize=(11, 9))

    # Draw the heatmap with 'sns.heatmap()'
    cmap = sns.diverging_palette(230, 20, as_cmap=True)
    sns.heatmap(corr, mask=mask, annot=True, cmap=cmap, vmax=.3, center=0, fmt='.1f', square=True, linewidths=.5, cbar_kws={"shrink": .5})
    plt.show()
    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
 