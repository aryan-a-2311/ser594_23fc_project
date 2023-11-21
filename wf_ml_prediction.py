import pandas as pd
import pickle

def loadKMeans3():
    # Load the trained K-Means model and the scaler using pickle
    with open('models/kmeans_model_k_3.pkl', 'rb') as model_file:
        model = pickle.load(model_file)
    with open('models/scaler_k_3.pkl', 'rb') as scaler_file:
        scaler = pickle.load(scaler_file)
    return model, scaler

def loadKMeans4():
    # Load the trained K-Means model and the scaler using pickle
    with open('models/kmeans_model_k_4.pkl', 'rb') as model_file:
        model = pickle.load(model_file)
    with open('models/scaler_k_4.pkl', 'rb') as scaler_file:
        scaler = pickle.load(scaler_file)
    return model, scaler

def loadKMeans5():
    # Load the trained K-Means model and the scaler using pickle
    with open('models/kmeans_model_k_5.pkl', 'rb') as model_file:
        model = pickle.load(model_file)
    with open('models/scaler_k_5.pkl', 'rb') as scaler_file:
        scaler = pickle.load(scaler_file)
    return model, scaler

def loadKMeans8():
    # Load the trained K-Means model and the scaler using pickle
    with open('models/kmeans_model_k_8.pkl', 'rb') as model_file:
        model = pickle.load(model_file)
    with open('models/scaler_k_8.pkl', 'rb') as scaler_file:
        scaler = pickle.load(scaler_file)
    return model, scaler

def kMeansPrediction(model, scaler, input_data):
    # Scale the input data using the loaded scaler
    scaledInput = scaler.transform(input_data)

    # Predict the cluster for the input data
    cluster = model.predict(scaledInput)
    return cluster

if __name__ == "__main__":
    # K-Means Clustering Prediction
    # Input data for prediction
    inputData1 = pd.DataFrame([[8, 128, 6800, 195.61, 6.52, 140]],
                              columns=['RAM', 'Memory', 'Battery Capacity', 'Item Weight', 'Screen Size', 'Sales based on Ratings'])
    
    inputData2 = pd.DataFrame([[8, 256, 5000, 301, 6.4, 22]],
                              columns=['RAM', 'Memory', 'Battery Capacity', 'Item Weight', 'Screen Size', 'Sales based on Ratings'])
    
    
    inputDataExperimentA1 = pd.DataFrame([[10, 256, 40000, 200, 6.1, 60]],
                                        columns=['RAM', 'Memory', 'Battery Capacity', 'Item Weight', 'Screen Size', 'Sales based on Ratings'])
    
    inputDataExperimentA2 = pd.DataFrame([[10, 256, 32000, 200, 6.1, 60]],
                                        columns=['RAM', 'Memory', 'Battery Capacity', 'Item Weight', 'Screen Size', 'Sales based on Ratings'])
    
    inputDataExperimentA3 = pd.DataFrame([[10, 256, 27000, 200, 6.1, 60]],
                                        columns=['RAM', 'Memory', 'Battery Capacity', 'Item Weight', 'Screen Size', 'Sales based on Ratings'])
    
    inputDataExperimentA4 = pd.DataFrame([[10, 256, 27500, 200, 6.1, 60]],
                                        columns=['RAM', 'Memory', 'Battery Capacity', 'Item Weight', 'Screen Size', 'Sales based on Ratings'])
    
    inputDataExperimentA5 = pd.DataFrame([[10, 256, 6000, 200, 6.1, 60]],
                                        columns=['RAM', 'Memory', 'Battery Capacity', 'Item Weight', 'Screen Size', 'Sales based on Ratings'])

    
    inputDataExperimentB1 = pd.DataFrame([[10, 256, 6805, 200, 9.1, 60]],
                                        columns=['RAM', 'Memory', 'Battery Capacity', 'Item Weight', 'Screen Size', 'Sales based on Ratings'])
    
    inputDataExperimentB2 = pd.DataFrame([[10, 256, 6805, 200, 24.7, 60]],
                                        columns=['RAM', 'Memory', 'Battery Capacity', 'Item Weight', 'Screen Size', 'Sales based on Ratings'])
    
    inputDataExperimentB3 = pd.DataFrame([[10, 256, 6805, 200, 23.0, 60]],
                                        columns=['RAM', 'Memory', 'Battery Capacity', 'Item Weight', 'Screen Size', 'Sales based on Ratings'])
    
    inputDataExperimentB4 = pd.DataFrame([[10, 256, 6805, 200, 4.8, 60]],
                                        columns=['RAM', 'Memory', 'Battery Capacity', 'Item Weight', 'Screen Size', 'Sales based on Ratings'])
    
    inputDataExperimentB5 = pd.DataFrame([[10, 256, 6805, 200, 37.2, 60]],
                                        columns=['RAM', 'Memory', 'Battery Capacity', 'Item Weight', 'Screen Size', 'Sales based on Ratings'])
    
    
    inputDataExperimentABCorr1 = pd.DataFrame([[8, 128, 5000, 300, 6, 380]],
                                        columns=['RAM', 'Memory', 'Battery Capacity', 'Item Weight', 'Screen Size', 'Sales based on Ratings'])
    
    inputDataExperimentABCorr2 = pd.DataFrame([[8, 128, 8000, 300, 26, 380]],
                                        columns=['RAM', 'Memory', 'Battery Capacity', 'Item Weight', 'Screen Size', 'Sales based on Ratings'])
    
    inputDataExperimentABCorr3 = pd.DataFrame([[8, 128, 32000, 300, 7, 380]],
                                        columns=['RAM', 'Memory', 'Battery Capacity', 'Item Weight', 'Screen Size', 'Sales based on Ratings'])
    
    inputDataExperimentABCorr4 = pd.DataFrame([[8, 128, 26000, 300, 23, 380]],
                                        columns=['RAM', 'Memory', 'Battery Capacity', 'Item Weight', 'Screen Size', 'Sales based on Ratings'])
    
    inputDataExperimentABCorr5 = pd.DataFrame([[8, 128, 31000, 300, 9, 380]],
                                        columns=['RAM', 'Memory', 'Battery Capacity', 'Item Weight', 'Screen Size', 'Sales based on Ratings']) 
    

    inputDataExperimentABInv1 = pd.DataFrame([[8, 128, 28000, 300, 5, 380]],
                                        columns=['RAM', 'Memory', 'Battery Capacity', 'Item Weight', 'Screen Size', 'Sales based on Ratings'])
    
    inputDataExperimentABInv2 = pd.DataFrame([[8, 128, 31000, 300, 3.5, 380]],
                                        columns=['RAM', 'Memory', 'Battery Capacity', 'Item Weight', 'Screen Size', 'Sales based on Ratings'])
    
    inputDataExperimentABInv3 = pd.DataFrame([[8, 128, 28000, 300, 23, 380]],
                                        columns=['RAM', 'Memory', 'Battery Capacity', 'Item Weight', 'Screen Size', 'Sales based on Ratings'])
    
    inputDataExperimentABInv4 = pd.DataFrame([[8, 128, 5000, 300, 25, 380]],
                                        columns=['RAM', 'Memory', 'Battery Capacity', 'Item Weight', 'Screen Size', 'Sales based on Ratings'])
    
    inputDataExperimentABInv5 = pd.DataFrame([[8, 128, 29000, 300, 4.5, 380]],
                                        columns=['RAM', 'Memory', 'Battery Capacity', 'Item Weight', 'Screen Size', 'Sales based on Ratings'])
    
    # Load the models and scalers
    model3, scaler3 = loadKMeans3()
    # model4, scaler4 = loadKMeans4()
    # model5, scaler5 = loadKMeans5()
    # model8, scaler8 = loadKMeans8()

    # Predict K-Means Cluster
    predictedCluster_3_1 = kMeansPrediction(model3, scaler3, inputData1)
    # predictCluster_4_1 = kMeansPrediction(model4, scaler4, inputData1)
    # predictedCluster_5_1 = kMeansPrediction(model5, scaler5, inputData1)
    # predictedCluster_8_1 = kMeansPrediction(model8, scaler8, inputData1)
    
    predictedCluster3_2 = kMeansPrediction(model3, scaler3, inputData2)
    # predictCluster4_2 = kMeansPrediction(model4, scaler4, inputData2)
    # predictedCluster_5_2 = kMeansPrediction(model5, scaler5, inputData2)
    # predictedCluster_8_2 = kMeansPrediction(model8, scaler8, inputData2)

    predictedClusterExperimentA1 = kMeansPrediction(model3, scaler3, inputDataExperimentA1)
    predictedClusterExperimentA2 = kMeansPrediction(model3, scaler3, inputDataExperimentA2)
    predictedClusterExperimentA3 = kMeansPrediction(model3, scaler3, inputDataExperimentA3)
    predictedClusterExperimentA4 = kMeansPrediction(model3, scaler3, inputDataExperimentA4)
    predictedClusterExperimentA5 = kMeansPrediction(model3, scaler3, inputDataExperimentA5)

    predictedClusterExperimentB1 = kMeansPrediction(model3, scaler3, inputDataExperimentB1)
    predictedClusterExperimentB2 = kMeansPrediction(model3, scaler3, inputDataExperimentB2)
    predictedClusterExperimentB3 = kMeansPrediction(model3, scaler3, inputDataExperimentB3)
    predictedClusterExperimentB4 = kMeansPrediction(model3, scaler3, inputDataExperimentB4)
    predictedClusterExperimentB5 = kMeansPrediction(model3, scaler3, inputDataExperimentB5)

    predictedClusterExperimentABCorr1 = kMeansPrediction(model3, scaler3, inputDataExperimentABCorr1)
    predictedClusterExperimentABCorr2 = kMeansPrediction(model3, scaler3, inputDataExperimentABCorr2)
    predictedClusterExperimentABCorr3 = kMeansPrediction(model3, scaler3, inputDataExperimentABCorr3)
    predictedClusterExperimentABCorr4 = kMeansPrediction(model3, scaler3, inputDataExperimentABCorr4)   
    predictedClusterExperimentABCorr5 = kMeansPrediction(model3, scaler3, inputDataExperimentABCorr5)

    predictedClusterABInv1 = kMeansPrediction(model3, scaler3, inputDataExperimentABInv1)
    predictedClusterABInv2 = kMeansPrediction(model3, scaler3, inputDataExperimentABInv2)
    predictedClusterABInv3 = kMeansPrediction(model3, scaler3, inputDataExperimentABInv3)
    predictedClusterABInv4 = kMeansPrediction(model3, scaler3, inputDataExperimentABInv4)
    predictedClusterABInv5 = kMeansPrediction(model3, scaler3, inputDataExperimentABInv5)

    # Print the predicted clusters
    print("The predicted cluster using k = 3 for the input 1 is:", predictedCluster_3_1[0])
    # print("The predicted cluster using k = 4 for the input 1 is:", predictCluster_4_1[0])
    # print("The predicted cluster using k = 5 for the input 1 is:", print("The predicted cluster using k = 3 for the input 1 is:", predictedCluster_5_1[0])
    # print("The predicted cluster using k = 8 for the input 1 is:", predictedCluster_8_1[0])

    print("The predicted cluster using k = 3 for the input 2 is:", predictedCluster3_2[0])
    # print("The predicted cluster using k = 4 for the input 2 is:", predictCluster4_2[0])
    # print("The predicted cluster using k = 5 for the input 2 is:", predictedCluster_5_2[0])
    # print("The predicted cluster using k = 8 for the input 2 is:", predictedCluster_8_2[0])
    
    print("\nThe predicted cluster using k = 3 for the experiment A input 1 is:", predictedClusterExperimentA1[0])
    print("The predicted cluster using k = 3 for the experiment A input 2 is:", predictedClusterExperimentA2[0])
    print("The predicted cluster using k = 3 for the experiment A input 3 is:", predictedClusterExperimentA3[0])
    print("The predicted cluster using k = 3 for the experiment A input 4 is:", predictedClusterExperimentA4[0])
    print("The predicted cluster using k = 3 for the experiment A input 5 is:", predictedClusterExperimentA5[0])

    print("\nThe predicted cluster using k = 3 for the experiment B input 1 is:", predictedClusterExperimentB1[0])
    print("The predicted cluster using k = 3 for the experiment B input 2 is:", predictedClusterExperimentB2[0])
    print("The predicted cluster using k = 3 for the experiment B input 3 is:", predictedClusterExperimentB3[0])
    print("The predicted cluster using k = 3 for the experiment B input 4 is:", predictedClusterExperimentB4[0])
    print("The predicted cluster using k = 3 for the experiment B input 5 is:", predictedClusterExperimentB5[0])

    print("\nThe predicted cluster using k = 3 for the experiment A and B correlation input 1 is:", predictedClusterExperimentABCorr1[0])
    print("The predicted cluster using k = 3 for the experiment A and B correlation input 2 is:", predictedClusterExperimentABCorr2[0])
    print("The predicted cluster using k = 3 for the experiment A and B correlation input 3 is:", predictedClusterExperimentABCorr3[0])
    print("The predicted cluster using k = 3 for the experiment A and B correlation input 4 is:", predictedClusterExperimentABCorr4[0])
    print("The predicted cluster using k = 3 for the experiment A and B correlation input 5 is:", predictedClusterExperimentABCorr5[0])

    print("\nThe predicted cluster using k = 3 for the experiment A and B inverse correlation input 1 is:", predictedClusterABInv1[0])
    print("The predicted cluster using k = 3 for the experiment A and B inverse correlation input 2 is:", predictedClusterABInv2[0])
    print("The predicted cluster using k = 3 for the experiment A and B inverse correlation input 3 is:", predictedClusterABInv3[0])
    print("The predicted cluster using k = 3 for the experiment A and B inverse correlation input 4 is:", predictedClusterABInv4[0])
    print("The predicted cluster using k = 3 for the experiment A and B inverse correlation input 5 is:", predictedClusterABInv5[0])

    print("\nTo understand more about the clusters, please refer to the 'project_ml_clustering_exploration.md' file.")