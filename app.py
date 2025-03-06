import streamlit as st
import pandas as pd  # Add this import
from core.data_loader import DataLoader
from core.preprocessor import DataPreprocessor
from core.visualizer import Visualizer
from core.model import ConsumptionModel
from configs.settings import Config

# 初始化模块
loader = DataLoader()
preprocessor = DataPreprocessor()
viz = Visualizer()
model = ConsumptionModel()

# 页面配置
st.set_page_config(page_title="校园消费分析系统", layout="wide")

# 数据加载
@st.cache_data
def load_dataset():
    data1, data2 = loader.load_raw_data()
    merged = loader.merge_datasets(data1, data2)
    return preprocessor.clean_data(merged)

df = load_dataset()

# 侧边栏控制
analysis_type = st.sidebar.radio(
    "选择分析模式",
    ["📊 实时消费分析", "🏫 食堂运营看板", "📈 经济状况评估"]
)

# 主界面
st.title("🎓 智慧校园消费分析平台")
st.markdown("---")

if analysis_type == "📊 实时消费分析":
    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(viz.plot_time_analysis(df), use_container_width=True)
    with col2:
        st.plotly_chart(viz.plot_spatial_analysis(df), use_container_width=True)

elif analysis_type == "🏫 食堂运营看板":
    # 添加时间筛选器
    selected_hours = st.slider("选择营业时段", 6, 22, (11, 13))
    filtered_df = df[df["Hour"].between(*selected_hours)]
    
    col1, col2 = st.columns([3, 2])
    with col1:
        st.plotly_chart(viz.plot_spatial_analysis(filtered_df), 
                       use_container_width=True)
    with col2:
        st.dataframe(filtered_df.groupby('Dept')['Money']
                    .agg(['sum', 'count', 'mean']).style.format("{:.2f}"))

elif analysis_type == "📈 经济状况评估":
    features = preprocessor.build_features(df)
    labels = model.train(features)
    
    tab1, tab2 = st.tabs(["三维可视化", "群体画像"])
    
    with tab1:
        st.plotly_chart(viz.plot_cluster_3d(features, labels),
                       use_container_width=True)
    
    with tab2:
        profile = model.profile_clusters(features, labels)
        
        # 数据验证
        total_users = len(features)
        st.markdown("**数据验证：**")
        st.markdown(f"- 总用户数：{total_users}")
        
        # 转换labels为Series
        labels_series = pd.Series(labels)  # 添加这行
        # 计算群体百分比
        cluster_dist = labels_series.value_counts(normalize=True).sort_index() * 100
        dist_text = "\n".join([f"• 群体 {i}: {pct:.1f}%" for i, pct in cluster_dist.items()])
        st.markdown(f"- 群体分布：\n{dist_text}")
        
        # 显示群体画像
        st.markdown("**群体画像说明：**")
        st.markdown("- 群体编号：0（低消费）、1（中等）、2（高消费）")
        st.markdown("- 消费次数：表示该群体人均刷卡次数")
        st.markdown("- 数值经过反标准化处理，保留两位小数")
        
        # 优化数据显示
        # 反标准化处理
        original_values = preprocessor.scaler.inverse_transform(features[preprocessor.scaler.feature_names_in_])
        original_df = pd.DataFrame(original_values, 
                                 columns=preprocessor.scaler.feature_names_in_, 
                                 index=features.index)
        original_df['Cluster'] = labels
        
        # 重新计算群体画像
        profile = original_df.groupby('Cluster').agg({
            '总消费': ['mean', 'median', 'std'],
            '消费次数': ['mean', 'median', 'std'],
            '周末消费比': ['mean', 'median', 'std']
        })
        
        # 格式化显示
        numeric_cols = [col for col in profile.columns if col != '群体描述']
        st.dataframe(profile.style.format({
            '总消费_mean': "¥{:,.0f}",
            '消费次数_mean': "{:,.0f}次",
            '周末消费比_mean': "{:.1%}"
        }, subset=numeric_cols).background_gradient(cmap='Blues'))