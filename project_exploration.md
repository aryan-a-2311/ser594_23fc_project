#### SER594: Exploratory Data Munging and Visualization
#### Title: Analyzing the Changing Nature of the Mobile Phone Market
#### Author: Aryan Arvind Agarwal
#### Date: 10/18/2023

## Basic Questions
**Dataset Author(s):** Aryan Arvind Agarwal

**Dataset Construction Date:** 10/12/2023

**Dataset Record Count:** 520

**Dataset Field Meanings:** 

Brand: Manufacturer of the mobile phone.

Model: The particular model of the mobile device.

RAM: The mobile device's available Random Access Memory, denoted in gigabytes or megabytes.

Memory: The mobile phone's available internal storage space, denoted in gigabytes or megabytes.

Battery Capacity: The energy storage capacity of the battery in a mobile phone. Commonly denoted in milliampere-hours (mAh).

Item Weight: The mobile phone's physical weight, typically denoted in pounds, ounces, or grams.

Price: The mobile phone's retail price, expressed in US dollars.

Screen Size: Refers to the diagonal dimension of the display of a mobile phone, typically denoted in inches.

Sales based on Ratings: Approximate sales figures derived on the basis of the number of user ratings.

**Dataset File Hash(es):** 2a5d6c4c43c0e5c34db00c8f60877ca6

## Note: 
Please refrain from running "wf_datagen.py" unless it is completely necessary. This will result in the generation of a new dataset, which will overwrite the existing dataset. This will result in the loss of the existing dataset and the need to re-run the data transformation and visualization scripts. This might also result in the current .md files about the project exploration and cluster exploration to become outdated.

Also the complete running of the file takes about 2.5-3 hrs to complete. Hence, please don't run it.

## Interpretable Records
### Record 1
**Raw Data:** 
Brand: Motorola
Model: PAN00015US
RAM: 4 GB
Memory: 4 GB
Battery Capacity: 5000
Item Weight: 4.99 Grams
Price: $145.10
Screen Size: 6.8 Inches
Sales based on Ratings: 1308

**Interpretation:** This record shows a Motorola mobile device bearing the model name PAN00015US. The phone possesses internal storage and RAM capacities of 4 GB each. It features a 6.8-inch display and a 5000mAh battery. The phone is available for $145.10 and has a sales figures of 1308 units based on the number of ratings it has. Additionally, the phone has a weight of only 4.99 grams.

### Record 2
**Raw Data:** 
Brand: Samsung
Model: A14
RAM: 4 GB
Memory: 128 GB
Battery Capacity: 5000 Milliamp Hours
Item Weight: 7.1 ounces
Price: $151.99
Screen Size: 6.6 Inches
Sales based on Ratings: 103

**Interpretation:** This record shows a Samsung mobile device bearing the model name A14. The phone possesses internal storage and RAM capacities of 128 GB and 4 GB respectively. It features a 6.6-inch display and a 5000mAh battery. The phone is available for $151.99 and has a sales figures of 103 units based on the number of ratings it has. Additionally, the phone has a weight of 7.1 ounces.

## Background Domain Knowledge
In the past few decades, the mobile phone industry has experienced profound transformations, progressing from rudimentary communication devices to advanced multifunctional electronics. Including sophisticated features like health monitoring, productivity, and communication in addition to entertainment, mobile phones are now indispensable components of contemporary life. In a fiercely competitive market, producers strive to provide superior attributes, enhanced operational capabilities, and reduced price points.

There has been a shift in consumer preferences towards smartphones that possess superior cameras, extended battery life, and increased processing capacity (Higher RAM). Consumers exhibit considerable interest in the technical attributes of smartphones, specifically those powered by the iOS and Android operating systems, according to a study conducted by Ozcalıcı and Soysal Bilmiş (2023). Mehta (2023) conducts an additional study that identifies significant trends in consumer technology, with a particular focus on the evolving mobile technology landscape.

The pricing aspect significantly impacts consumer decision-making. Price determination is frequently influenced by data, with manufacturers and retailers frequently utilizing a variety of technical specifications. A study conducted by Kiran and Jebakumar (2022) employed machine learning methods to forecast mobile phone pricing classes, thereby showcasing the industry's growing reliance on data-driven approaches [3].

Gaining an understanding of the connections among these different factors can provide manufacturers and consumers with invaluable information, enabling them to make more informed product development and purchasing decisions.

**References:**
[1] Özçalıcı, M., & Soysal Bilmiş, A. N., (2023). SMART PHONE MARKETS ANALYSIS WITH A-PRIORI ALGORITHM: THE CASE OF TURKEY. Uluslararası Yönetim İktisat ve İşletme Dergisi , vol.19, no.2, 328-347.
[2] Mehta, S. (2023, May 26). 8 of the Most Substantial Consumer Technology Trends in 2023. ABI Research.
[3] Kiran, V. A., & Jebakumar, R. (2022, January). Prediction of Mobile Phone Price Class using Supervised Machine Learning Techniques. International Journal of Innovative Science and Research Technology, 7(1).


## Data Transformation
### Transformation 1
**Description:** Imputation of Missing Values in the Brand and Model columns.

**Soundness Justification:** The values that are absent from these columns are substituted with the label 'Unknown'. This ensures the preservation of the data's integrity by explicitly recognizing the absence of the information. There are no errors or outliers introduced.

### Transformation 2
**Description:** Normalization of Brand names.

**Soundness Justification:** Every possible form of the identical brand name is assigned to a singular standardized name. This guarantees uniformity while preserving the data's semantics and preventing the introduction of errors.


### Transformation 3
**Description:** Memory and RAM conversion from different units to gigabytes.

**Soundness Justification:** This facilitates analysis by standardizing the units utilized to represent these characteristics. There is no discarding of usable data, and the semantics of the data remain unchanged.


### Transformation 4
**Description:** Imputation for missing values in Battery Capacity, Item Weight, and Screen Size using median value.

**Soundness Justification:** Median imputation is a method that exhibits robustness as it remains error-free and devoid of outliers. This maintains the distribution of the data as a whole.

### Transformation 5
**Description:** An algorithm for calculating and transforming prices using RAM and memory groups.

**Soundness Justification:** The missing values for Price are imputed using the mean price of comparable RAM and memory categories as a filler. This method effectively manages absent data while preventing the introduction of errors.



## Visualization
### Visual 1 (Histogram for Brand)
**Analysis:** The histogram for the Brand column depicts the distribution of the data across the various brands. The most popular brands are Samsung, Apple, and Motorola, with the majority of the data points belonging to these three brands. The least popular brands are Google, OnePlus, and Xiaomi, with the fewest data points belonging to these three brands.

### Visual 2 (Scatter Matrix of Item Weight, Memory, Price, and Battery Capacity)
**Analysis:** The scatter matrix offers valuable insights into the interconnections among battery capacity, memory, price, and item weight. While no significant linear correlation appears to exist between any two characteristics, a marginal trend indicates that products with greater memory capacity may command a higher price. Furthermore, the distribution of item weight seems to lack any discernible pattern in comparison to the remaining attributes.