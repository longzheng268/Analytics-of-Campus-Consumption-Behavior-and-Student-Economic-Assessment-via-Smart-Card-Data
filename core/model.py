from sklearn.cluster import KMeans
import numpy as np
from configs.settings import Config

class ConsumptionModel:
    def __init__(self):
        self.model = KMeans(n_clusters=Config.CLUSTER_NUM,
                           random_state=42)

    def train(self, features):
        self.model.fit(features)
        
        # 根据聚类中心对标签重新排序
        cluster_centers = self.model.cluster_centers_
        sorted_indices = cluster_centers[:,0].argsort()  # 按总消费特征排序
        self.model.labels_ = np.searchsorted(sorted_indices, self.model.labels_)
        
        return self.model.labels_

    def profile_clusters(self, features, labels):
        features['Cluster'] = labels
        
        profile = features.groupby('Cluster').agg({
            '总消费': ['mean', 'median', 'std'],
            '消费次数': ['mean', 'median', 'std'],
            '周末消费比': ['mean', 'median', 'std']
        })
        
        profile.columns = ['_'.join(col).strip() for col in profile.columns.values]
        
        # 动态生成群体描述
        cluster_stats = features.groupby('Cluster')['总消费'].mean().sort_values()
        profile['群体描述'] = [
            f"低消费群体：总消费均值¥{cluster_stats[0]:.0f}，消费频次较低",
            f"中等消费群体：总消费均值¥{cluster_stats[1]:.0f}，消费模式均衡", 
            f"高消费群体：总消费均值¥{cluster_stats[2]:.0f}，消费频繁"
        ]
        
        return profile.round(2)