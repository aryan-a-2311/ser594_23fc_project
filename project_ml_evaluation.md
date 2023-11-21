#### SER594: Machine Learning Evaluation
#### Title: Analyzing the Changing Nature and Identifying Gaps in the Mobile Phone Market
#### Author: Aryan Arvind Agarwal
#### Date: 11/20/2023

## Evaluation Metrics
### Metric 1
**Name:** Silhouette Score

**Choice Justification:** 
The selection of the Silhouette Score is based on its effectiveness in quantifying the degree of similarity between an object and its own cluster, as opposed to other clusters. The metric offers an easy and transparent means of assessing the suitability of the clustering by taking into account both separation (the degree of separateness between objects within the same cluster) and cohesion (the closeness of objects within the same cluster). This score functions especially well in situations where the true identifiers of the data are unknown, allowing for an assessment to be made on the basis of the structure revealed within the data.

**Interpretation:** 
When the Silhouette Score approaches +1, it signifies that the samples are sufficiently distant from adjacent clusters, implying that the clusters are highly pure and clearly defined. A value in close proximity of 0 signifies clusters that overlap, whereas a value near -1 signifies incorrect clustering. Therefore, in general, clusters that are more clearly defined and distinct are denoted by higher values.


### Metric 2
**Name:** Davies-Bouldin Score

**Choice Justification:** 
The Davies-Bouldin Score is chosen as a clustering metric due to its capacity to assess both the similarities and differences between clusters. The metric calculates the mean "similarity" between individual clusters and the cluster that most closely resembles them, with this similarity being determined by the distance between cluster centres and the clusters' individual sizes. This score is advantageous in identifying compact and well-separated cluster sets, which are critical for achieving efficient clustering.

**Interpretation:** 
An improved clustering arrangement is denoted by a lower Davies-Bouldin Score, which signifies that each cluster is situated at a greater distance from its most similar cluster and exhibits reduced dispersion among its members. Hence, the objective is to reduce this score to its minimum, where a score of "0" signifies the optimal situation in which clusters are spatially distant and contain negligible variability among themselves.



## Alternative Models
### Alternative 1
**Construction:** 
This model employs K-Means clustering with k=4 clusters. The selection of four clusters was determined by an initial hypothesis regarding the data structure, with the intention of categorising the data into four discrete segments.

**Evaluation:** 
The Davies-Bouldin Score is 0.7467, while the Silhouette Score is 0.2869. The Silhouette Score indicates a moderate degree of cluster cohesion and separation, despite being positive. A score approaching 1 would signify clusters that are more clear and distinct. The Davies-Bouldin Score suggests that clusters lack significant distinctiveness, as evidenced by the presence of overlap or internal variance, when it approaches 1 from 0. Although the model performs satisfactorily overall, cluster definition could be enhanced.


### Alternative 2
**Construction:** 
This model employs K-Means clustering with k=5 clusters. The decision to utilise five clusters was an effort to capture a greater level of detail in the data in comparison to the four-cluster model, which could potentially accommodate a wider range of data patterns.

**Evaluation:** 
Based on its higher Silhouette Score of 0.3238 and Davies-Bouldin Score of 0.8007, this model exhibits marginally enhanced cluster separation and cohesion in comparison to the four-cluster model. Conversely, the observed rise in the Davies-Bouldin Score implies that the clusters potentially lack sufficient separation or exhibit heightened internal dispersion. Although this model appears to strike a balance between granularity and cluster quality, the clusters may contain some redundancy or inconsistency.


### Alternative 3
**Construction:** 
This model employs K-Means clustering with k=8 clusters. This was done as an endeavour to capture a more intricate and diverse structure inherent in the data. A varied and unique clusterings within the dataset was anticipated.

**Evaluation:** 
The model attains a Davies-Bouldin Score of 0.6609 and a Silhouette Score of 0.4267. Among the three alternatives, these scores indicate the clustering quality that is most favourable. A higher Silhouette Score signifies clusters that are more precisely defined and exhibit greater separation; conversely, a lower Davies-Bouldin Score implies that these clusters are more compact and well-separated from one another. It appears that this model clusters the data in the most distinct and well-separated manner.


### Alternative 4
**Construction:** 
This model employs K-Means clustering with k=4 clusters. The selection of three clusters uses a methodology that seeks to encompass a comprehensive, universal framework within the dataset. This arrangement has been determined through prior knowledge of the data, which indicated that three distinct groups adequately represent the underlying patterns.

**Evaluation:** 
The model shows a Silhouette Score of 0.8358 and a Davies-Bouldin Score of 0.1018. The obtained scores demonstrate an outstanding level of clustering quality. A Silhouette Score approaching 1 indicates that the data points within each cluster are densely packed and that the clusters are effectively separated, thereby signifying distinct and unambiguous cluster boundaries. This is further supported by the extremely low Davies-Bouldin Score, which indicates not only that the clusters are distinct but also that their variance is minimal, implying that members of the same cluster are extremely homogeneous.



## Best Model

**Model:** The Model with k=3 clusters is the best model.