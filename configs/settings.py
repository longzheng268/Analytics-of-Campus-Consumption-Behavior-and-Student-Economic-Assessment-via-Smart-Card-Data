import plotly.express as px

class Config:
    # 数据路径
    DATA_PATH = "./data"
    DATA1_NAME = "data1.csv"
    DATA2_NAME = "data2.csv"
    
    # 编码配置
    ENCODING = "gb18030"  # 处理中文编码
    
    # 特征工程参数
    CLUSTER_NUM = 3        # 聚类数量
    TIME_FEATURES = ["Hour", "Weekday", "IsWeekend"]
    
    # 可视化参数
    COLOR_SCHEME = px.colors.qualitative.Pastel