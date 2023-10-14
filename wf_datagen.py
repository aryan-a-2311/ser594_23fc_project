import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup

def amazonLinkScraper():
    HEADERS = ({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.60', 'Accept-Language': 'en-US, en;q=0.5'})
    for pgNo in range(1, 21):
        print("Link Scraping Page: ", pgNo, " of 20")
        basePageBegin = "https://www.amazon.com/s?k=mobile+phones&page="
        pageNo = pgNo
        basePageEnd = "&crid=1TB5U7ULJNNJF&qid=1697249334&sprefix=mobile+phone%2Caps%2C172&ref=sr_pg_"
        url = basePageBegin + str(pageNo) + basePageEnd + str(pageNo)

        try:
            response = requests.get(url, headers=HEADERS)
            soup = BeautifulSoup(response.content, 'html.parser')
        except Exception as e:
            # print("Error in URL: ", url, "\nError: ", e)
            return None


        links = soup.findAll("a", attrs = {"class": "a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"})

        for link in links:
            finalLink = "https://www.amazon.com" + link.get('href')
            amazonURLs.append(finalLink)


def amazonScraper(url):
    print("Scraping from URL: ", url)
    HEADERS = ({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.60', 'Accept-Language': 'en-US, en;q=0.5'})
    # testUrl = "https://www.amazon.com/SAMSUNG-Factory-Unlocked-Smartphone-Adaptive/dp/B0BLP2PY6N/ref=sr_1_5?crid=1TB5U7ULJNNJF&keywords=mobile+phones&qid=1697169003&sprefix=mobile+phone%2Caps%2C172&sr=8-5"
    # response = requests.get(testUrl, headers=HEADERS)
    try:
        response = requests.get(url, headers=HEADERS)
        soup = BeautifulSoup(response.content, 'html.parser')
    except Exception as e:
        print("Error in URL: ", url, "\nError: ", e)
        return None

    data = {
        "Brand": "",
        "Model": "",
        "RAM": "",
        "Memory": "",
        "Battery Capacity": "",
        "Item Weight": "",
        "Price": "",
        "Screen Size": "",
        "Sales based on Ratings": ""
    }
    
    try:
        technicalSpecTable = soup.find("table", attrs={"id": "productDetails_detailBullets_sections1"})
        for brandData in technicalSpecTable:
            if "Manufacturer" in brandData.text:
                data["Brand"] = brandData.text
            
            if "Item model number" in brandData.text:
                data["Model"] = brandData.text

            if "Ram Memory Installed Size" in brandData.text:
                data["RAM"] = brandData.text
            
            if "Memory Storage Capacity" in brandData.text:
                data["Memory"] = brandData.text
            
            if "Battery Capacity" in brandData.text:
                data["Battery Capacity"] = brandData.text
            
            if "Item Weight" in brandData.text:
                data["Item Weight"] = brandData.text

            if "Standing screen display size" in brandData.text:
                data["Screen Size"] = brandData.text
    except:
        pass

    try:
        data["Brand"] = data["Brand"].split("Manufacturer")[1].strip()
    except:
        pass
    
    try:
        data["Model"] = data["Model"].split("Item model number")[1].strip()
    except:
        pass
    
    try:    
        data["RAM"] = data["RAM"].split("Ram Memory Installed Size")[1].strip()
    except:
        pass
    
    try:    
        data["Memory"] = data["Memory"].split("Memory Storage Capacity")[1].strip()
    except:
        pass
    
    try:    
        data["Battery Capacity"] = data["Battery Capacity"].split("Battery Capacity")[1].strip()
    except:
        pass
    
    try:    
        data["Item Weight"] = data["Item Weight"].split("Item Weight")[1].strip()
    except:
        pass
    
    try:
        data["Screen Size"] = data["Screen Size"].split("Standing screen display size")[1].strip()
    except:
        pass
    
    try:
        priceDiv = soup.find("div", attrs={"class": "a-section a-spacing-none aok-align-center"})
        priceSpan = priceDiv.find("span", attrs={"class": "a-price aok-align-center reinventPricePriceToPayMargin priceToPay"})
        data["Price"] = priceSpan.find("span", attrs={"class": "a-offscreen"}).text
    except:
        pass
    
    try:
        # Find the number of ratings from a span tag with id acrCustomerReviewText
        ratingSpan = soup.find("span", attrs={"id": "acrCustomerReviewText"})
        # Get the text from the span tag
        ratingText = ratingSpan.text
        # Split the text to get the number of ratings
        ratingText = ratingText.split(" ")[0]
        # Convert the number of ratings to int
        data["Sales based on Ratings"] = int(ratingText.replace(",", ""))
        print(data["Sales based on Ratings"])
    except:
        pass
    return data

amazonURLs = []
amazonData = []

def saveToCSV(dataList):
    df = pd.DataFrame([item for item in dataList if item is not None])

    # Save the DataFrame to a CSV file
    csv_file_path = 'data_original/originalData.csv'
    df.to_csv(csv_file_path, index=False)

if __name__ == '__main__':
    amazonLinkScraper()
    dataList = [amazonScraper(url) for url in amazonURLs]
    print(dataList)
    saveToCSV(dataList)
    # amazonScraper("TestUrl")