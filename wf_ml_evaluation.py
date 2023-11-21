import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import silhouette_score, davies_bouldin_score
from sklearn.preprocessing import StandardScaler
import pickle
import subprocess

def load_data(path):
    # Load the dataset
    data = pd.read_csv(path)
    return data

def trainTestSplit(data):
    # Train-test split
    trainSet, testSet = train_test_split(data, test_size= 0.2, random_state=42)
    return trainSet, testSet
    
def save_data(trainData, testData):
    # Save the training and testing datasets in the 'data_processing' folder
    trainData.to_csv('data_processing/training_set.csv', index=False)
    testData.to_csv('data_processing/testing_set.csv', index=False)

def evaluation(data, model, scaler):
    features = data[['RAM', 'Memory', 'Battery Capacity', 'Item Weight', 'Screen Size', 'Sales based on Ratings']]
    scaledFeatures = scaler.transform(features)

    # Compute evaluation metrics
    silhouetteAvg = silhouette_score(scaledFeatures, model.labels_)
    daviesBouldin = davies_bouldin_score(scaledFeatures, model.labels_)

    return f"Silhouette Score: {silhouetteAvg}, Davies-Bouldin Score: {daviesBouldin}"

if __name__ == "__main__":
    # Load the dataset
    data = load_data('data_processing/processedData.csv')

    # Train-test split
    train, test = trainTestSplit(data)

    # Save the training and testing datasets in the 'data_processing' folder
    save_data(train, test)

    # Making the models by calling other python files
    # K-Means-3
    subprocess.run(['python', 'wf_ml_training_k_3.py'])
    # K-Means-4
    subprocess.run(['python', 'wf_ml_training_k_4.py'])
    # K-Means-5
    subprocess.run(['python', 'wf_ml_training_k_5.py'])
    # K-Means-8
    subprocess.run(['python', 'wf_ml_training_k_8.py'])

    # Making predictions by calling other python files
    subprocess.run(['python', 'wf_ml_prediction.py'])

    # # Evaluation
    # trainData = pd.read_csv('data_processing/training_set.csv')

    # # Loading K-Means-3 model and scaler
    # with open('models/kmeans_model_k_3.pkl', 'rb') as model_file:
    #     model3 = pickle.load(model_file)
    # with open('models/scaler_k_3.pkl', 'rb') as scaler_file:
    #     scaler3 = pickle.load(scaler_file)

    # # Loading K-Means-4 model and scaler
    # with open('models/kmeans_model_k_4.pkl', 'rb') as model_file:
    #     model4 = pickle.load(model_file)
    # with open('models/scaler_k_4.pkl', 'rb') as scaler_file:
    #     scaler4 = pickle.load(scaler_file)

    # # Loading K-Means-5 model and scaler
    # with open('models/kmeans_model_k_5.pkl', 'rb') as model_file:
    #     model5 = pickle.load(model_file)
    # with open('models/scaler_k_5.pkl', 'rb') as scaler_file:
    #     scaler5 = pickle.load(scaler_file)
    
    # # Loading K-Means-8 model and scaler
    # with open('models/kmeans_model_k_8.pkl', 'rb') as model_file:
    #     model8 = pickle.load(model_file)
    # with open('models/scaler_k_8.pkl', 'rb') as scaler_file:
    #     scaler8 = pickle.load(scaler_file)

    # evaluationResult3 = evaluation(trainData, model3, scaler3)
    # evaluationResult4 = evaluation(trainData, model4, scaler4)
    # evaluationResult5 = evaluation(trainData, model5, scaler5)
    # evaluationResult8 = evaluation(trainData, model8, scaler8)

    # evaluationResults = f"\nK-Means-3 Evaluation: {evaluationResult3}\nK-Means-4 Evaluation: {evaluationResult4}  \nK-Means-5 Evaluation: {evaluationResult5}\nK-Means-8 Evaluation: {evaluationResult8}"
    # print(evaluationResults)

    # # Save the results to a file
    # output_path = 'evaluation/summary.txt'
    # with open(output_path, 'w') as file:
    #     file.write(evaluationResults)