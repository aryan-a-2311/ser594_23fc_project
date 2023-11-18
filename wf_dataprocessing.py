import pandas as pd

def weightPreprocess(weight):
    if pd.isna(weight):
        return weight
    weight = weight.lower()
    value = ''.join(c for c in weight if c.isdigit() or c == '.')
    value = float(value)

    if "ounce" in weight:
        value *= 28.3495
    elif "pound" in weight:
        value *= 453.592
    elif "kilogram" in weight:
        value *= 1000
    
    return round(value, 2)

def batteryPreprocess(capacity):
    if pd.isna(capacity):
        return capacity
    capacity = str(capacity).lower()
    value = ''.join(c for c in capacity if c.isdigit())
    value = float(value)
    
    if "amp hours" in capacity and "milliamp" not in capacity:
        value *= 1000
    
    return int(value)

def screenSizePreprocess(size):
    if pd.isna(size):
        return size
    size = size.lower()
    value = ''.join(c for c in size if c.isdigit() or c == '.')
    value = float(value)
    
    if "centimeters" in size:
        value /= 2.54 
    
    return round(value, 2)

def pricePreprocess(price):
    if pd.isna(price):
        return price
    
    # Remove the dollar sign and commas, and convert to float
    return round(float(price.replace('$', '').replace(',', '')), 2)

def ramMemoryPreprocess(ramMem):
    if pd.isna(ramMem):
        return ramMem
    strRamMem = str(ramMem).lower()
    digRamMem = ''.join(c for c in strRamMem if c.isdigit() or c == '.')
    digRamMem = float(digRamMem) if digRamMem else None
    
    if "mb" in strRamMem:
        digRamMem /= 1024  
    elif "kb" in strRamMem:
        digRamMem /= (1024 * 1024) 
    elif "tb" in strRamMem:
        digRamMem *= 1024

    return round(digRamMem, 2) if digRamMem else None

def brandPreprocess(brand):
    if pd.isna(brand):
        return 'Unknown'
    brand = brand.strip().lower()
    
    # Handle variations of the same brand
    variations = {
        'samsung': ['samsung', 'samsung electronincs', 'samsung electronics'],
        'apple': ['apple', 'apple computer'],
        'motorola': ['motorola', 'motorola inc'],
        'alcatel': ['alcatel', 'alcaltel'],
        'oneplus': ['oneplus', 'one plus'],
        'google': ['google', 'google llc'],
        'cat': ['cat', 'cat phones'],
    }
    for standardName, variedName in variations.items():
        if brand in variedName:
            return standardName
    return brand

def processingMain():
    originalData = pd.read_csv("data_original/originalData.csv")
    processedData = originalData.copy()

    # For Brand and Model - Fill the Empty values with Unknown
    processedData['Brand'].fillna('Unknown', inplace=True)
    processedData['Model'].fillna('Unknown', inplace=True)

    # For Brand - Convert to lowercase and handle variations of the same brand
    processedData['Brand'] = processedData['Brand'].apply(brandPreprocess)
    
    # For Model - Convert to lowercase and strip the leading and trailing spaces
    processedData['Model'] = processedData['Model'].str.lower().str.strip()

    # For RAM and Memory - Fill the Empty values with a default value (8GB and 128GB respectively)
    processedData['RAM'].fillna('8 GB', inplace=True)
    processedData['Memory'].fillna('128 GB', inplace=True)

    # Converting RAM and Memory to numeric values
    processedData['RAM'] = processedData['RAM'].apply(ramMemoryPreprocess)
    processedData['Memory'] = processedData['Memory'].apply(ramMemoryPreprocess)

    # For Battery Capacity, Item Weight and Screen Size - Fill the Empty values with the median value
    
    # For Battery Capacity, Item Weight and Screen Size convert the values to numerics (mAh, grams and inches respectively)
    processedData['Battery Capacity'] = processedData['Battery Capacity'].apply(batteryPreprocess)

    processedData['Item Weight'] = processedData['Item Weight'].apply(weightPreprocess)

    processedData['Screen Size'] = processedData['Screen Size'].apply(screenSizePreprocess)

    # Fill the missing values with the median value
    processedData['Battery Capacity'].fillna(processedData['Battery Capacity'].median(), inplace=True)
    processedData['Item Weight'].fillna(processedData['Item Weight'].median(), inplace=True)
    processedData['Screen Size'].fillna(processedData['Screen Size'].median(), inplace=True)

    # For Sales based on Ratings - Using the median value
    processedData['Sales based on Ratings'].fillna(processedData['Sales based on Ratings'].median(), inplace=True)

    # Making the Price column numeric
    processedData['Price'] = processedData['Price'].apply(pricePreprocess)
    
    # For Price - using group-based mean based on RAM and Memory
    processedData['Price'] = processedData.groupby(['RAM', 'Memory'])['Price'].transform(lambda x: x.fillna(x.mean()))

    # Handling remaining missing values in Price using the overall mean since there might not be enough information in some groups by RAM and Memory
    remainingPrice = processedData['Price'].mean()
    processedData['Price'].fillna(remainingPrice, inplace=True)
    
    # Handling Outliers
    processedData['RAM'] = processedData['RAM'].apply(lambda x: '17' if x > 16 else ('0' if x < 1 else x))

    # For the 'Battery Capacity' column, correct the 4,200,000 values to 4200 and scale up values less than 100
    processedData['Battery Capacity'] = processedData['Battery Capacity'].apply(lambda x: 4200 if x == 4200000 else (x * 100 if x < 100 else x))

    # For the 'Item Weight' column, scale up weights less than 100
    processedData['Item Weight'] = processedData['Item Weight'].apply(lambda x: x * 10 if x < 100 and x >= 10 else (x * 100 if x < 10 else x))

    # Save the processed data to a new CSV file
    processedData.to_csv('data_processing/processedData.csv', index=False)

if __name__ == "__main__":
    processingMain()