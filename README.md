# 🎓 校园消费行为分析与学生经济评估项目
*Analytics of Campus Consumption Behavior and Student Economic Assessment via Smart Card Data*

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-red.svg)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## 📖 项目概述

本项目是一个基于**智能卡数据**的校园消费行为分析与学生经济状况评估系统。通过对学生餐卡刷卡数据的深度挖掘，项目实现了消费模式识别、消费行为分析和学生群体分类，为高校学生事务管理和食堂运营优化提供数据支持。

### 🎯 项目特色
- **实时数据分析**：基于真实的校园一卡通数据进行分析
- **多维度分析**：时间维度、空间维度、消费模式多角度分析
- **智能聚类**：使用K-Means算法对学生进行消费群体分类
- **交互式可视化**：基于Streamlit的Web应用，支持实时交互
- **模块化设计**：清晰的代码架构，易于扩展和维护

### 🖼️ 系统截图

**实时消费分析模块**
![实时消费分析](https://github.com/user-attachments/assets/084bbcc2-d943-443b-a0f3-e435127e4d3d)

**食堂运营看板模块** 
![食堂运营看板](https://github.com/user-attachments/assets/f20fec72-8d58-4fce-bf96-619f2d4ee837)

**经济状况评估模块**
![经济状况评估](https://github.com/user-attachments/assets/55f0f32c-c54b-4a36-9c05-80e03acc16cf)

## 🏗️ 项目架构

```
Analytics-of-Campus-Consumption-Behavior/
├── 📁 configs/           # 配置文件
│   └── settings.py       # 项目配置参数
├── 📁 core/              # 核心功能模块
│   ├── data_loader.py    # 数据加载器
│   ├── preprocessor.py   # 数据预处理器
│   ├── model.py          # 机器学习模型
│   └── visualizer.py     # 数据可视化
├── 📁 data/              # 数据文件
│   ├── data1.csv         # 学生基本信息数据
│   └── data2.csv         # 消费交易记录数据
├── 📁 doc/               # 项目文档
│   ├── 学生校园消费行为分析项目说明报告.pdf
│   └── 学生校园消费行为分析项目说明报告.docx
├── app.py                # Streamlit主应用
├── requirements.txt      # 依赖包列表
└── README.md            # 项目说明文档
```

## 📊 数据结构

### 学生信息数据 (data1.csv)
| 字段 | 类型 | 说明 |
|------|------|------|
| CardNo | string | 学生卡号（主键）|
| Sex | string | 性别 |
| Major | string | 专业信息 |
| AccessCardNo | string | 门禁卡号 |

### 消费记录数据 (data2.csv)
| 字段 | 类型 | 说明 |
|------|------|------|
| CardNo | string | 学生卡号（外键）|
| Date | datetime | 消费时间 |
| Money | float | 消费金额 |
| Dept | string | 消费地点（食堂名称）|
| Type | string | 交易类型 |

## 🔧 环境要求

### 系统要求
- **Python**: 3.8 或更高版本
- **操作系统**: Windows 10/11, macOS 10.14+, Ubuntu 18.04+
- **内存**: 建议 4GB 以上
- **存储**: 至少 1GB 可用空间

### 依赖库
项目所需的Python包及其版本要求：

```
pandas>=2.0.0          # 数据处理和分析
numpy>=1.24.0          # 数值计算
matplotlib>=3.7.0      # 基础绘图库
seaborn>=0.12.0        # 统计可视化
scikit-learn>=1.3.0    # 机器学习库
streamlit>=1.28.0      # Web应用框架
plotly>=5.15.0         # 交互式可视化
```

## 🚀 安装和运行

### 1. 克隆项目
```bash
git clone https://github.com/longzheng268/Analytics-of-Campus-Consumption-Behavior-and-Student-Economic-Assessment-via-Smart-Card-Data.git
cd Analytics-of-Campus-Consumption-Behavior-and-Student-Economic-Assessment-via-Smart-Card-Data
```

### 2. 安装依赖
```bash
# 使用pip安装（推荐）
pip install -r requirements.txt

# 或者单独安装
pip install pandas numpy matplotlib seaborn scikit-learn streamlit plotly
```

### 3. 运行项目
```bash
streamlit run app.py
```

### 4. 访问应用
在浏览器中打开 `http://localhost:8501` 即可访问系统

## 📱 功能模块详解

### 1. 📊 实时消费分析
- **消费时段分布**：分析学生在不同时间段的消费频次
- **食堂消费占比**：展示各食堂的消费比例分布
- **实时数据更新**：支持数据的实时刷新和展示

**技术实现**：
```python
# 时间分布分析
def plot_time_analysis(df):
    fig = px.histogram(df, x="Hour", nbins=24)
    return fig
```

### 2. 🏫 食堂运营看板  
- **营业时段筛选**：可通过滑块选择特定营业时段
- **食堂消费分析**：展示不同食堂的消费统计数据
- **运营数据统计**：包含总消费、消费次数、平均消费等指标

**技术特色**：
- 支持时间范围动态筛选
- 实时更新统计数据
- 多维度数据展示

### 3. 📈 经济状况评估
- **三维聚类可视化**：基于总消费、消费次数、周末消费比进行3D展示
- **群体画像分析**：将学生分为低消费、中等消费、高消费三个群体
- **详细数据统计**：提供各群体的均值、中位数、标准差等统计指标

**机器学习算法**：
```python
# K-Means聚类
def train(self, features):
    self.model = KMeans(n_clusters=3, random_state=42)
    self.model.fit(features)
    return self.model.labels_
```

## 🔬 技术栈

### 数据处理
- **Pandas**: 数据加载、清洗、转换
- **NumPy**: 数值计算和数组操作
- **Scikit-learn**: 机器学习和数据标准化

### 数据可视化
- **Plotly**: 交互式图表和3D可视化
- **Matplotlib**: 基础图表绘制
- **Seaborn**: 统计图表美化

### Web应用
- **Streamlit**: 快速构建数据科学Web应用
- **Python**: 后端逻辑和数据处理

### 机器学习
- **K-Means聚类**: 学生消费群体分类
- **StandardScaler**: 数据标准化处理
- **特征工程**: 消费行为特征提取

## 📈 核心算法

### 1. 数据预处理
```python
def clean_data(df):
    # 处理金额异常值（0.1-100元范围）
    df = df[df['Money'].between(0.1, 100)]
    
    # 时间特征工程
    df['Hour'] = df['Date'].dt.hour
    df['Weekday'] = df['Date'].dt.weekday  
    df['IsWeekend'] = df['Weekday'].isin([5,6]).astype(int)
    
    return df.dropna(subset=['Dept', 'Sex'])
```

### 2. 特征构建
```python
def build_features(self, df):
    features = df.groupby("CardNo").agg({
        "Money": ["sum", "mean", "count"],    # 总消费、均消、消费次数
        "Hour": ["std"],                      # 消费时间波动
        "Weekday": ["nunique"],               # 活跃天数
        "IsWeekend": ["mean"]                 # 周末消费比
    })
    
    # 特征标准化
    scaler = StandardScaler()
    return scaler.fit_transform(features)
```

### 3. 聚类分析
- **算法**: K-Means (k=3)
- **特征**: 总消费、消费次数、周末消费比
- **标准化**: StandardScaler标准化处理
- **评估**: 基于聚类中心的群体排序

## 🎯 应用场景

### 高校管理方面
- **学生资助识别**: 通过消费模式识别经济困难学生
- **生活习惯分析**: 了解学生作息和消费习惯
- **异常行为检测**: 识别异常消费模式

### 食堂运营方面  
- **营业时段优化**: 根据消费时段分布调整营业时间
- **菜品配置**: 基于消费偏好优化菜品供应
- **人员配置**: 根据客流分析合理安排人员

### 数据科学研究
- **消费行为建模**: 构建学生消费行为预测模型
- **群体特征分析**: 深入分析不同群体的消费特征
- **时序分析**: 消费模式的时间变化趋势

## 🤝 贡献指南

### 开发环境设置
1. Fork 项目到你的GitHub账户
2. 克隆你的Fork到本地
3. 创建新的功能分支
4. 进行开发和测试
5. 提交Pull Request

### 代码规范
- 使用Python PEP 8编码规范
- 添加适当的注释和文档字符串
- 确保代码的可读性和维护性
- 提交前进行充分测试

### 问题反馈
如果你发现bug或有功能建议，请：
1. 在GitHub Issues中创建新问题
2. 详细描述问题或需求
3. 提供相关的错误信息或截图
4. 建议解决方案（如果有的话）

## 📄 许可证

本项目采用 MIT 许可证。详细信息请查看 [LICENSE](LICENSE) 文件。

## 👥 项目团队

- **项目负责人**: [longzheng268](https://github.com/longzheng268)
- **技术栈**: Python, Streamlit, Machine Learning, Data Visualization

## 🔗 相关链接

- [项目详细文档](./doc/)
- [Streamlit官方文档](https://docs.streamlit.io/)
- [Plotly可视化文档](https://plotly.com/python/)
- [Scikit-learn机器学习文档](https://scikit-learn.org/stable/)

## 📊 项目统计

- **数据规模**: 3244名学生的消费记录
- **时间跨度**: 覆盖完整学期的消费数据
- **分析维度**: 时间、空间、消费金额、消费频次
- **群体分类**: 低消费(3.3%)、中等消费(45.2%)、高消费(51.5%)

---

*如果本项目对你有帮助，请给它一个⭐️！*
