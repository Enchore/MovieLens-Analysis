"""
分布分析模塊
分析評分數據的分布特徵。

包含：
- 高評分電影的用戶評分分布
- 評分等級分布統計
- 用戶評分習慣分布
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from typing import Optional


plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei']
plt.rcParams['axes.unicode_minus'] = False


class DistributionAnalysis:
    """分布分析類。"""

    def __init__(self, ratings_df: pd.DataFrame, movies_df: pd.DataFrame):
        """
        初始化分布分析。

        Args:
            ratings_df: 評分數據 DataFrame
            movies_df: 電影數據 DataFrame
        """
        self._ratings = ratings_df.copy()
        self._movies = movies_df.copy()
        self._merged = pd.merge(ratings_df, movies_df, on='movie_id')

    def rating_level_distribution(self) -> pd.Series:
        """
        計算各評分等級的分布。

        Returns:
            評分等級分布 Series
        """
        return self._ratings['rating'].value_counts().sort_index()

    def high_rated_movies_user_dist(self, threshold: float = 4.0) -> pd.DataFrame:
        """
        分析高評分電影的用戶評分分布。

        Args:
            threshold: 高評分門檻

        Returns:
            高評分電影的用戶評分分布 DataFrame
        """
        # 找出高評分電影（平均評分 >= threshold）
        movie_avg = self._ratings.groupby('movie_id')['rating'].mean()
        high_rated_ids = movie_avg[movie_avg >= threshold].index

        high_rated_ratings = self._ratings[
            self._ratings['movie_id'].isin(high_rated_ids)
        ]
        return high_rated_ratings['rating'].value_counts().sort_index()

    def user_rating_distribution(self) -> pd.DataFrame:
        """
        分析用戶評分習慣分布。

        Returns:
            用戶評分統計 DataFrame
        """
        user_stats = self._ratings.groupby('user_id').agg(
            total_ratings=('rating', 'count'),
            mean_rating=('rating', 'mean')
        )

        return user_stats

    def plot_rating_distribution(self, save_path: Optional[str] = None):
        """
        繪製評分等級分布柱狀圖。

        Args:
            save_path: 圖片保存路徑
        """
        dist = self.rating_level_distribution()
        fig, ax = plt.subplots(figsize=(8, 6))
        dist.plot(kind='bar', ax=ax, color='#fa8c16')
        ax.set_title('評分等級分布', fontsize=14)
        ax.set_xlabel('評分', fontsize=12)
        ax.set_ylabel('數量', fontsize=12)
        ax.grid(True, alpha=0.3, axis='y')

        if save_path:
            plt.savefig(save_path, dpi=150, bbox_inches='tight')
        else:
            plt.show()

    def plot_high_rated_distribution(self, save_path: Optional[str] = None):
        """
        繪製高評分電影用戶評分分布圖。

        Args:
            save_path: 圖片保存路徑
        """
        dist = self.high_rated_movies_user_dist()
        fig, ax = plt.subplots(figsize=(8, 6))
        dist.plot(kind='bar', ax=ax, color='#eb2f96')
        ax.set_title('高評分電影 (>=4.0) 的用戶評分分布', fontsize=14)
        ax.set_xlabel('評分', fontsize=12)
        ax.set_ylabel('數量', fontsize=12)
        ax.grid(True, alpha=0.3, axis='y')

        if save_path:
            plt.savefig(save_path, dpi=150, bbox_inches='tight')
        else:
            plt.show()
