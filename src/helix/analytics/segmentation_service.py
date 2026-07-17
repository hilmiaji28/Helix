from sklearn.cluster import KMeans

from .base import AnalyticsService


class SegmentationService(AnalyticsService):
    def fit(
        self,
        X,
        n_clusters=4,
    ):
        model = KMeans(
            n_clusters=n_clusters,
            random_state=42,
        )

        cluster = model.fit_predict(X)

        return cluster, model
