import pandas as pd
from configs.settings import Config

class DataLoader:
    @staticmethod
    def load_raw_data():
        """加载原始数据集"""
        data1 = pd.read_csv(
            f"{Config.DATA_PATH}/{Config.DATA1_NAME}",
            encoding=Config.ENCODING
        )
        data2 = pd.read_csv(
            f"{Config.DATA_PATH}/{Config.DATA2_NAME}",
            encoding=Config.ENCODING,
            parse_dates=['Date']
        )
        return data1, data2

    @staticmethod
    def merge_datasets(data1, data2):
        """合并数据集"""
        return pd.merge(data2, data1, on="CardNo", how="left")