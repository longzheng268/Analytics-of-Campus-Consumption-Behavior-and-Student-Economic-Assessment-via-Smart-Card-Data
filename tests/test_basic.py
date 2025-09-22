"""
基础测试文件
用于验证项目核心功能的基本测试用例
"""

import sys
import os
import pytest

# 添加项目根目录到Python路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def test_imports():
    """测试核心模块是否可以正常导入"""
    try:
        from core.data_loader import DataLoader
        from core.preprocessor import DataPreprocessor
        from core.visualizer import Visualizer
        from core.model import ConsumptionModel
        from configs.settings import Config
        assert True, "所有核心模块导入成功"
    except ImportError as e:
        pytest.fail(f"模块导入失败: {e}")


def test_config_values():
    """测试配置文件的基本值"""
    from configs.settings import Config
    
    # 检查基本配置项
    assert hasattr(Config, 'DATA_PATH'), "配置中应包含 DATA_PATH"
    assert hasattr(Config, 'CLUSTER_NUM'), "配置中应包含 CLUSTER_NUM"
    assert hasattr(Config, 'ENCODING'), "配置中应包含 ENCODING"
    
    # 检查聚类数量合理性
    assert Config.CLUSTER_NUM > 0, "聚类数量应大于0"
    assert Config.CLUSTER_NUM <= 10, "聚类数量应合理 (<=10)"


def test_data_loader_class():
    """测试DataLoader类是否可以实例化"""
    from core.data_loader import DataLoader
    
    loader = DataLoader()
    assert loader is not None, "DataLoader 应该可以正常实例化"
    
    # 检查关键方法是否存在
    assert hasattr(loader, 'load_raw_data'), "应包含 load_raw_data 方法"
    assert hasattr(loader, 'merge_datasets'), "应包含 merge_datasets 方法"


def test_preprocessor_class():
    """测试DataPreprocessor类是否可以实例化"""
    from core.preprocessor import DataPreprocessor
    
    preprocessor = DataPreprocessor()
    assert preprocessor is not None, "DataPreprocessor 应该可以正常实例化"
    
    # 检查关键方法是否存在
    assert hasattr(preprocessor, 'clean_data'), "应包含 clean_data 方法"
    assert hasattr(preprocessor, 'build_features'), "应包含 build_features 方法"


def test_model_class():
    """测试ConsumptionModel类是否可以实例化"""
    from core.model import ConsumptionModel
    
    model = ConsumptionModel()
    assert model is not None, "ConsumptionModel 应该可以正常实例化"
    
    # 检查关键方法是否存在
    assert hasattr(model, 'train'), "应包含 train 方法"
    assert hasattr(model, 'profile_clusters'), "应包含 profile_clusters 方法"


def test_visualizer_class():
    """测试Visualizer类是否可以实例化"""
    from core.visualizer import Visualizer
    
    viz = Visualizer()
    assert viz is not None, "Visualizer 应该可以正常实例化"
    
    # 检查关键方法是否存在
    assert hasattr(viz, 'plot_time_analysis'), "应包含 plot_time_analysis 方法"
    assert hasattr(viz, 'plot_spatial_analysis'), "应包含 plot_spatial_analysis 方法"
    assert hasattr(viz, 'plot_cluster_3d'), "应包含 plot_cluster_3d 方法"


def test_required_packages():
    """测试必需的包是否已安装"""
    required_packages = [
        'pandas', 'numpy', 'matplotlib', 'seaborn', 
        'sklearn', 'streamlit', 'plotly'
    ]
    
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            pytest.fail(f"必需的包 {package} 未安装")


if __name__ == "__main__":
    # 允许直接运行此文件进行测试
    pytest.main([__file__, "-v"])