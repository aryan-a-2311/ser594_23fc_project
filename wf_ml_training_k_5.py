from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import pickle
import pandas as pd

def load_data():
    # Reading the training data
    trainingData = pd.read_csv('data_processing/training_set.csv')
    return trainingData

def k_means_clustering(trainingData):
    # Selecting relevant features for clustering, now including Sales based on Ratings
    features = trainingData[['RAM', 'Memory', 'Battery Capacity', 'Item Weight', 'Screen Size', 'Sales based on Ratings']]

    # Data Preprocessing: Scaling the features
    scaler = StandardScaler()
    scaledFeatures = scaler.fit_transform(features)

    # Model Training: K-Means Clustering
    kmeans = KMeans(n_clusters=5, n_init=10, random_state=42)
    kmeans.fit(scaledFeatures)

    # Saving the K-Means model and scaler
    with open('models/kmeans_model_k_5.pkl', 'wb') as modelFile:
        pickle.dump(kmeans, modelFile)

    with open('models/scaler_k_5.pkl', 'wb') as scalerFile:
        pickle.dump(scaler, scalerFile)

if __name__ == "__main__":
    # Load the training data
    trainingData = load_data()

    # Develop K-Means Clustering Model
    k_means_clustering(trainingData)