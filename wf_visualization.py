# Importing necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import os

def graphs(dataSet):
    sns.set(style="whitegrid")

    # Define the list of quantitative and qualitative features
    quantFeatures = ['Item Weight', 'Memory', 'Price', 'Battery Capacity']
    qualFeatures = ['Brand']

    # Generate scatter plots for all pairs of quantitative features
    sns.pairplot(dataSet[quantFeatures])
    plt.suptitle('Scatter Plots for Pairs of Quantitative Features', y=1.02)
    # Save the plot to a file
    plt.savefig('visuals/scatter_plots.png')
    plt.show()

    # Generate histograms for qualitative features
    for feature in qualFeatures:
        plt.figure(figsize=(10, 6))
        sns.countplot(data=dataSet, y=feature, order=dataSet[feature].value_counts().index)
        plt.title(f'Histogram for {feature}')
        plt.xlabel('Count')
        plt.ylabel(feature)
        histogram_path = os.path.join('visuals/', f'histogram_{feature}.png')
        # Save the plot to a file
        plt.savefig(histogram_path)
        plt.show()

def stats(dataSet):
    # Features Selected:
    # Quantitative: Item Weight, Memory, Price, Battery Capacity
    # Qualitative: Brand

    # Computing statistics for quantitative features
    quantFeatures = ['Item Weight', 'Memory', 'Price', 'Battery Capacity']
    quantSummary = dataSet[quantFeatures].agg(['min', 'max', 'median'])

    # Computing statistics for qualitative feature
    qualFeatures = 'Brand'
    qualSummary = dataSet[qualFeatures].value_counts()
    numCategory = len(qualSummary)
    freqCategory = qualSummary.idxmax()
    lessFreqCategory = qualSummary.idxmin()

    # Creating the summary
    finalSummary = f"Summary:\n\n"

    # Adding quantitative summary
    finalSummary += "Quantitative Features:\n"
    for feature in quantFeatures:
        finalSummary += f"{feature}:\n"
        finalSummary += f"Min: {quantSummary.loc['min', feature]}\n"
        finalSummary += f"Max: {quantSummary.loc['max', feature]}\n"
        finalSummary += f"Median: {quantSummary.loc['median', feature]}\n"

    # Adding qualitative summary
    finalSummary += f"\nQualitative Features:\n"
    finalSummary += f"{qualFeatures}:\n"
    finalSummary += f"Number of Categories: {numCategory}\n"
    finalSummary += f"Most Frequent Category: {freqCategory}\n"
    finalSummary += f"Least Frequent Category: {lessFreqCategory}\n"

    # Saving the summary to a text file
    with open('data_processing/summary.txt', 'w') as f:
        f.write(finalSummary)

def correlation(dataSet):
    # Extract the features
    quantFeatures = ['Item Weight', 'Memory', 'Price', 'Battery Capacity']
    quantData = dataSet[quantFeatures]

    # Calculate the correlation matrix
    corrMatrix = quantData.corr()

    # Create a half-matrix by setting the upper triangle and diagonal to NaN
    for i in range(corrMatrix.shape[0]):
        for j in range(i, corrMatrix.shape[1]):
            corrMatrix.iloc[i, j] = np.nan

    # Save the half-matrix to a text file
    corrMatrix.to_csv('data_processing/correlations.txt', sep='\t')
    
def visualizationMain():
    # Load the dataset
    data = pd.read_csv('data_processing/processedData.csv')
    
    # Calling functions
    graphs(data)
    stats(data)
    correlation(data)

if __name__ == '__main__':
    warnings.filterwarnings("ignore")
    visualizationMain()