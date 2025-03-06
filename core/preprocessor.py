from sklearn.preprocessing import StandardScaler
from configs.settings import Config
import pandas as pd

class DataPreprocessor:
    @staticmethod
    def clean_data(df):
        """数据清洗"""
        # 处理金额异常值
        df = df[df['Money'].between(0.1, 100)]
        
        # 时间特征工程
        df['Hour'] = df['Date'].dt.hour
        df['Weekday'] = df['Date'].dt.weekday
        df['IsWeekend'] = df['Weekday'].isin([5,6]).astype(int)
        
        return df.dropna(subset=['Dept', 'Sex'])

    def build_features(self, df):  # 保留self参数，去掉@staticmethod
        """构建特征矩阵"""
        features = df.groupby("CardNo").agg({
            "Money": ["sum", "mean", "count"],
            "Hour": ["std"],
            "Weekday": ["nunique"],
            "IsWeekend": ["mean"]
        })
        features.columns = ["总消费", "均消", "消费次数", 
                          "消费时间波动", "活跃天数", "周末消费比"]
        
        # 处理NaN值
        features = features.fillna(0)  # 将NaN值替换为0
        
        # 标准化处理
        self.scaler = StandardScaler()
        scaled_features = self.scaler.fit_transform(features)
        return pd.DataFrame(
            scaled_features,
            index=features.index,
            columns=features.columns
        )