#### SER594: Experimentation
#### Title: Analyzing the Changing Nature and Identifying Gaps in the Mobile Phone Market
#### Author: Aryan Arvind Agarwal
#### Date: 11/20/2023


## Explainable Records
### Record 1
**Raw Data:** 
- Brand: Serounder
- Model: sero81wccei6bh-12
- RAM: 8 GB
- Memory: 128 GB
- Battery Capacity: 6800 Milliamp Hours
- Item Weight: 195.61 Grams
- Price: $71.48
- Screen Size: 6.52 Inches
- Sales based on Ratings: 140

**Prediction Explanation:** 
- RAM and Memory: Cluster 0 has moderate to high RAM and average memory storage, therefore 8 GB and 128 GB fit nicely. A device with these specs can meet mainstream consumer needs.
- Battery Capacity: Although the battery capacity is bigger than Cluster 0, it still fits inside smartphones that promote extended usage, which is desirable in mainstream devices.
- Item Weight: It weighs less than the Cluster 0 average but is still within a common smartphone build's range.
- Screen Size: This matches the Cluster 0 average, showing a preference for popular screen sizes.
- Sales based on Ratings: Lower than Cluster 0 average, but still indicative of market approval. Serounder may have lesser sales due to brand familiarity than other brands.

This record's balance of RAM, memory, screen size and high battery capacity, make it a good Cluster 0 forecast.

### Record 2
**Raw Data:** 
- Brand: Samsung
- Model: a54
- RAM: 8 GB
- Memory: 256 GB
- Battery Capacity: 5000 Milliamp Hours
- Item Weight: 301 Grams
- Price: $367.45
- Screen Size: 6.4 Inches
- Sales based on Ratings: 22

**Prediction Explanation:** 
- RAM and Memory: Cluster 0 devices have high RAM and memory to meet mainstream users' processing and storage needs.
- Battery Capacity: The 5000 mAh battery capacity is ideal for Cluster 0, indicating a concentration on daily power.
- Weight: The weight is near to the Cluster 0 average, indicating mainstream smartphone build quality.
- Screen Size: The screen size is close to Cluster 0, meeting the needs of many people.
- Sales based on Ratings: Despite being a well-known brand, this model may target a niche market due to its higher price point.

The balanced combination of high RAM and memory, standard battery capacity, and screen size makes Record 2 a good candidate for Cluster 0.


## Interesting Features
### Feature A
**Feature:** Battery Capacity

**Justification:** 
The battery capacity of a smartphone, which is measured in milliamp-hours (mAh), is an essential factor in assessing its efficacy and attractiveness. Extended battery life generally results in more time between charges, which has a substantial influence on user satisfaction and experience. In today's world, where smartphones play a pivotal role in various daily activities such as communication, entertainment, and navigation, this characteristic assumes particular significance. In addition, devices featuring greater battery capacities are frequently positioned for extensive usage, including multimedia consumption or gaming, thereby catering to particular user demographics. Nonetheless, consumers may place significant value on the trade-offs associated with the weight or dimension of the device when opting for a more substantial battery. As a result, battery capacity is a crucial characteristic that can segment the market and substantially impact consumer preference.

### Feature B
**Feature:** Screen Size

**Justification:** 
The screen size of smartphones, which is usually measured in diagonal inches, is a distinguishing characteristic that significantly impacts consumer preference. It governs the entire user experience of diverse applications, gaming, and content consumption. In addition to enhancing the immersion of gaming and media, larger displays are frequently favored for productive activities such as document editing and reading. Conversely, users who prioritize portability will find smaller screens more practical due to their compact size and uncomplicated one-handed operation. Additionally, the screen size affects the phone's physical dimensions, which in turn affect its ergonomics and pocket-ability. Therefore, screen size is a critical factor in classifying smartphones into distinct categories such as phablets, standard, and compact, which cater to various user preferences and functional requirements.

## Experiments 
### Varying A
**Prediction Trend Seen:** 
The model appears to establish a correlation between exceptionally large battery capacities and high-end or specialized devices that possess exceptionally high specifications in general (similar to Cluster 2). These devices may have been developed with heavy-duty operation or specific applications in mind that require an extended battery life.

The model's classification of smartphones with moderate battery capacities as mainstream is consistent with the utilization patterns and expectations of the average consumer (similar to Cluster 0). This signifies an acknowledgment of conventional market products featuring battery capacities that are adequate for routine activities without being overly large.

27,000 mAh appears to be the threshold for distinguishing between standard and non-standard battery capacities, as indicated by the model's predictions. This is consistent with the notion that smartphones with battery capacities greater than 10,000 mAh are considered specialized devices that are not typical consumer products.

The predictions of the model suggest that battery capacity plays a crucial role in distinguishing specialized, high-end devices (potentially designed for niche applications) from consumer smartphones that are widely used. The devices are classified into a cluster with generally higher specifications due to their exceptionally high battery capacities, whereas moderate capacities are consistent with those found in conventional market offerings.

### Varying B
**Prediction Trend Seen:** 
The model seems to identify standard screen sizes that are prevalent on mainstream smartphones, which are generally engineered to strike a balance between portability and visual quality. The categorization of these devices in Cluster 0 implies that they are regarded as conventional consumer handsets, complete with dimensions and functionalities that accommodate everyday tasks.

The observed screen sizes appear to be correlated by the model with an unorthodox device category (such as Cluster 1). This may suggest the presence of non-conventional smartphone designs or devices that integrate tablet and smartphone functionalities. This demonstrates an awareness that smartphones with such enormous displays are not typical and are instead regarded as specialized or niche products.

24 inches seems to be the threshold for distinguishing between standard and non-standard screen sizes, as indicated by the model's predictions. This is consistent with the notion that smartphones with displays larger than 6 inches are considered phablets or tablets, which are not typical consumer devices.

Screen size appears to be a significant differentiating factor between standard smartphones and more specialized, large-screen devices, according to the model's predictions. Cluster 0 corresponds to the classification of standard screen sizes, which is consistent with mainstream smartphones. However, Cluster 1 comprises devices with extraordinarily large screen sizes, which may represent large, non-standard devices such as tablets or hybrid devices.

### Varying A and B together
**Prediction Trend Seen:** 
A discernible pattern arises from the experiment involving correlated changes in 'Battery Capacity' and 'Screen Size'; this demonstrates the model's sophisticated understanding of feature interactions. Both features with moderate values are categorized into Cluster 0, which represents smartphones that are widely used. Cluster 1 devices are characterized by their exceptionally large screens, irrespective of the battery capacity, which is typical of tablet-like devices. In contrast, devices classified under Cluster 2 exhibit exceptionally high battery capacities, which underscore their emphasis on specialized or high-end applications. This phenomenon stands in opposition to variations of independent features, in which the model's determination seems more direct, as it is predominantly predicated on the feature surpassing a designated threshold.

The classification of the model appeared to be more straightforward when A and B were varied independently; it was predominantly determined by which feature surpassed a specific threshold. Nevertheless, by accounting for the combined impact of these features, the model demonstrates a nuanced approach due to the correlated changes in both of them. This suggests that the model does not merely respond to changes in individual features independently; rather, it assesses the interplay between these features and determines the device's category as a whole.

### Varying A and B inversely
**Prediction Trend Seen:** 
Experiments involving variations of 'Battery Capacity' and 'Screen Size' that are inversely correlated reveal that, regardless of screen size, classification in Cluster 2 is consistently induced by exceedingly high battery capacities. This is apparent from some of the experiments, where the model's decision is more significantly impacted by high battery capacities rather than reduced screen sizes. Nevertheless, in the case where the battery capacity is average and the screen size is exceptionally large, the model redesignates itself to Cluster 1, which exhibits a greater sensitivity to screen size.

These results stand in contrast to those obtained from variations of A and B that are independent. When modified individually, each feature predominantly impacts the classification in its own way, in accordance with a distinct pattern driven by thresholds. Conversely, when confronted with the inverse correlation scenario, the model consistently categorises these combinations into Cluster 2, evidently placing an emphasis on exceedingly large battery capacities rather than screen sizes. The model exhibits a hierarchical decision-making process, wherein particular attributes, such as an exceptionally large battery capacity, may exert a preponderant impact in comparison to others in distinct circumstances.