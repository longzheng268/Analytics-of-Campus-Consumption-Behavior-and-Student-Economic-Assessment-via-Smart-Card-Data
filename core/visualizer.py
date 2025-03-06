import plotly.express as px
from configs.settings import Config

class Visualizer:
    @staticmethod
    def plot_time_analysis(df):
        """时间分布分析"""
        fig = px.histogram(df, x="Hour", nbins=24,
                          color_discrete_sequence=Config.COLOR_SCHEME,
                          title="<b>消费时段分布</b>")
        fig.update_layout(bargap=0.1)
        return fig

    @staticmethod
    def plot_spatial_analysis(df):
        """空间分布分析"""
        canteen_data = df["Dept"].value_counts().nlargest(5)
        fig = px.pie(canteen_data, values=canteen_data.values, 
                    names=canteen_data.index,
                    hole=0.3,
                    title="<b>食堂消费占比TOP5</b>")
        return fig

    @staticmethod
    def plot_cluster_3d(features, clusters):
        """三维聚类可视化"""
        fig = px.scatter_3d(
            features,
            x='总消费',
            y='消费次数',
            z='周末消费比',
            color=clusters.astype(str),
            color_discrete_sequence=Config.COLOR_SCHEME,
            title="<b>学生消费特征三维聚类</b>"
        )
        fig.update_traces(marker_size=5)
        return fig