"""
時間序列分析模塊
分析評分數據隨時間的變化趨勢。

包含：
- 評分數量隨時間變化趨勢
- 評分均值隨年份變化
- 熱門電影評分時間序列
"""
import pandas as pd
import matplotlib.pyplot as plt
from typing import Optional


plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei']
plt.rcParams['axes.unicode_minus'] = False


class TrendAnalysis:
    """時間序列趨勢分析類。"""

    def __init__(self, ratings_df: pd.DataFrame):
        """
        初始化時間序列分析。

        Args:
            ratings_df: 評分數據 DataFrame，需包含 timestamp 列
        """
        self._df = ratings_df.copy()
        self._df['datetime'] = pd.to_datetime(
            self._df['timestamp'], unit='s'
        )
        self._df['year'] = self._df['datetime'].dt.year
        self._df['month'] = self._df['datetime'].dt.to_period('M')

    def rating_count_trend(self) -> pd.Series:
        """
        計算每月評分數量趨勢。

        Returns:
            按月統計的評分數量 Series
        """
        monthly = self._df.groupby('month').size()
        return monthly

    def average_rating_by_year(self) -> pd.Series:
        """
        計算每年平均評分。

        Returns:
            按年統計的平均評分 Series
        """
        yearly_avg = self._df.groupby('year')['rating'].mean()
        return yearly_avg

    def plot_rating_trend(self, save_path: Optional[str] = None):
        """
        繪製評分數量趨勢圖。

        Args:
            save_path: 圖片保存路徑（可選）
        """
        monthly = self.rating_count_trend()
        fig, ax = plt.subplots(figsize=(14, 6))
        monthly.plot(ax=ax, color='#1890ff', linewidth=1.5)
        ax.set_title('評分數量月度變化趨勢', fontsize=14)
        ax.set_xlabel('月份', fontsize=12)
        ax.set_ylabel('評分數量', fontsize=12)
        ax.grid(True, alpha=0.3)

        if save_path:
            plt.savefig(save_path, dpi=150, bbox_inches='tight')
        else:
            plt.show()

    def plot_yearly_avg_rating(self, save_path: Optional[str] = None):
        """
        繪製年度平均評分折線圖。

        Args:
            save_path: 圖片保存路徑（可選）
        """
        yearly = self.average_rating_by_year()
        fig, ax = plt.subplots(figsize=(10, 6))
        yearly.plot(ax=ax, marker='o', color='#52c41a', linewidth=2)
        ax.set_title('年度平均評分變化', fontsize=14)
        ax.set_xlabel('年份', fontsize=12)
        ax.set_ylabel('平均評分', fontsize=12)
        ax.grid(True, alpha=0.3)

        if save_path:
            plt.savefig(save_path, dpi=150, bbox_inches='tight')
        else:
            plt.show()
