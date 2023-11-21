import pandas as pd
import pickle
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

def load_model_and_scaler(modelPath, scalerPath):
    with open(modelPath, 'rb') as model_file:
        model = pickle.load(model_file)
    with open(scalerPath, 'rb') as scaler_file:
        scaler = pickle.load(scaler_file)
    return model, scaler

def analyze_clusters(data, model, scaler, k):
    # Updated to include 'Sales based on Ratings' in the feature set
    features = data[['RAM', 'Memory', 'Battery Capacity', 'Item Weight', 'Screen Size', 'Sales based on Ratings']]
    scaledFeatures = scaler.transform(features)

    # Predict clusters
    data['cluster'] = model.predict(scaledFeatures)

    # Analyze cluster centroids
    centroids = model.cluster_centers_
    centroids = scaler.inverse_transform(centroids)
    centroidDF = pd.DataFrame(centroids, columns=features.columns)
    print(f"Cluster Centroids for k = {k}:\n", centroidDF)

    # Dimensionality Reduction for Visualization
    pca = PCA(n_components=2)
    principalComponents = pca.fit_transform(scaledFeatures)
    data['PC1'], data['PC2'] = principalComponents[:, 0], principalComponents[:, 1]

    # Visualization
    plt.figure(figsize=(12, 8))
    sns.scatterplot(data=data, x='PC1', y='PC2', hue='cluster', palette='viridis')
    plt.title('Clusters Visualization')
    plt.show()

    return data

if __name__ == "__main__":
    # Paths to the model and scaler for k = 3
    modelPath3 = 'models/kmeans_model_k_3.pkl'
    scalerPath3 = 'models/scaler_k_3.pkl'

    # Paths to the model and scaler for k = 4
    modelPath4 = 'models/kmeans_model_k_4.pkl'
    scalerPath4 = 'models/scaler_k_4.pkl'

    # Paths to the model and scaler for k = 5
    modelPath5 = 'models/kmeans_model_k_5.pkl'
    scalerPath5 = 'models/scaler_k_5.pkl'

    # Paths to the model and scaler for k = 8
    modelPath8 = 'models/kmeans_model_k_8.pkl'
    scalerPath8 = 'models/scaler_k_8.pkl'

    # Load the model and scaler
    model3, scaler3 = load_model_and_scaler(modelPath3, scalerPath3)
    model4, scaler4 = load_model_and_scaler(modelPath4, scalerPath4)
    model5, scaler5 = load_model_and_scaler(modelPath5, scalerPath5)
    model8, scaler8 = load_model_and_scaler(modelPath8, scalerPath8)

    # Load the dataset
    data_path = 'data_processing/training_set.csv'
    data = pd.read_csv(data_path)

    # Analyze Clusters for k = 3
    clustered_data_3 = analyze_clusters(data, model3, scaler3, 3)
    clustered_data_4 = analyze_clusters(data, model4, scaler4, 4)
    clustered_data_5 = analyze_clusters(data, model5, scaler5, 5)
    clustered_data_8 = analyze_clusters(data, model8, scaler8, 8)