import numpy as np
from sklearn.cluster import KMeans
from scipy.spatial import distance

class EngagementScorer:
    def __init__(self, data_frame, coordinates_columns=['X_column', 'Y_column', 'Z_column']):
        self.df = data_frame.copy()
        self.coordinates_columns = coordinates_columns
        self.clusters_column = 'clusters'
        self.score_column = 'engagement_score'
        self.cluster_centroids = None

    def fit_clusters(self, n_clusters=3):
        kmeans = KMeans(n_clusters=n_clusters, random_state=42)
        self.df[self.clusters_column] = kmeans.fit_predict(self.df[self.coordinates_columns])
        self.cluster_centroids = self.df.groupby(self.clusters_column)[self.coordinates_columns].mean()

    def calculate_engagement_score(self):
        if self.cluster_centroids is None:
            raise ValueError("Clusters are not fitted. Call 'fit_clusters' first.")
        
        def euclidean_distance(x, y):
            return distance.euclidean(x, y)

        least_engaged_cluster = self.cluster_centroids.idxmin()['X_column']
        self.df[self.score_column] = self.df.apply(
          lambda row: euclidean_distance(row[self.coordinates_columns], self.cluster_centroids.loc[least_engaged_cluster]),
            axis=1
        )

    def get_engagement_scores(self):
        if self.score_column not in self.df.columns:
            raise ValueError("Engagement scores are not calculated. Call 'calculate_engagement_score' first.")
        return self.df[['User_ID', self.score_column]]

