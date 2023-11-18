A project that use clustering algorithms, including GMM and K-means to analyze word frequency.


document_clustering.py would load a dataset from BBC that contains word frequency vectors for thousands of documents on five different topics.


For K-means:
Run the document clustering script with K=a, norm_flag=b, diffuse=c, where a,b,c are parameters could be tuned.

For K-means++:
Run the document clustering script with center_init = "kmeans_pp".

For GMM:
Run the document clustering script with test_method='gmm'.

WordCloud is required to run mkWordClouds.py to visualize results.

(Some datasets are not uploaded because of size limitation)
