from wf_dataprocessing import processingMain
from wf_visualization import visualizationMain

def mainCore():
    print("Starting data processing...")
    processingMain()
    
    print("Starting data visualization...")
    visualizationMain()

if __name__ == "__main__":
    mainCore()