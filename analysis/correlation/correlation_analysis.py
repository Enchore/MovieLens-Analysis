"""
關聯性分析模塊
分析影片上映時間、類型與評分之間的關聯性。

包含：
- 上映年份與評分的相關性
- 電影類型與評分的關聯性
- 用戶活躍度與評分行為的關聯
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from typing import Optional


plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei']
plt.rcParams['axes.unicode_minus'] = False


class CorrelationAnalysis:
    """關聯性分析類。"""

    def __init__(self, ratings_df: pd.DataFrame, movies_df: pd.DataFrame):
        """
        初始化關聯性分析。

        Args:
            ratings_df: 評分數據 DataFrame
            movies_df: 電影數據 DataFrame
        """
        self._ratings = ratings_df.copy()
        self._movies = movies_df.copy()
        self._merged = pd.merge(ratings_df, movies_df, on='movie_id')

    def year_rating_correlation(self) -> float:
        """
        計算上映年份與評分的 Pearson 相關係數。

        Returns:
            相關係數
        """
        if 'year' not in self._merged.columns:
            # 從標題提取年份
            self._merged['year'] = self._merged['title'].str.extract(
                r'\((\d{4})\)'
            ).astype(float)

        corr = self._merged[['year', 'rating']].corr().iloc[0, 1]
        return corr

    def genre_rating_stats(self) -> pd.DataFrame:
        """
        計算各電影類型的評分統計。

        Returns:
            各類型的評分統計 DataFrame
        """
        if 'genres' not in self._merged.columns:
            return pd.DataFrame()

        # 展開多標籤類型
        genres_expanded = self._merged.assign(
            genre=self._merged['genres'].str.split('|')
        ).explode('genre')

        stats = genres_expanded.groupby('genre')['rating'].agg(
            ['mean', 'median', 'count', 'std']
        ).sort_values('mean', ascending=False)

        return stats

    def user_activity_correlation(self) -> pd.DataFrame:
        """
        分析用戶活躍度與評分行為的關聯。

        Returns:
            用戶活躍度統計 DataFrame
        """
        user_stats = self._ratings.groupby('user_id').agg(
            rating_count=('rating', 'count'),
            avg_rating=('rating', 'mean'),
            rating_std=('rating', 'std')
        ).reset_index()

        # 計算相關性
        corr = user_stats[['rating_count', 'avg_rating']].corr()
        return corr

    def plot_year_rating_scatter(self, save_path: Optional[str] = None):
        """
        繪製上映年份與評分的散點圖。

        Args:
            save_path: 圖片保存路徑
        """
        if 'year' not in self._merged.columns:
            self._merged['year'] = self._merged['title'].str.extract(
                r'\((\d{4})\)'
            ).astype(float)

        fig, ax = plt.subplots(figsize=(10, 6))
        # 採樣以避免過密
        sample = self._merged.sample(min(5000, len(self._merged)))
        ax.scatter(sample['year'], sample['rating'], alpha=0.1, s=5)
        ax.set_title('上映年份與評分的關聯性', fontsize=14)
        ax.set_xlabel('上映年份', fontsize=12)
        ax.set_ylabel('評分', fontsize=12)
        ax.grid(True, alpha=0.3)

        if save_path:
            plt.savefig(save_path, dpi=150, bbox_inches='tight')
        else:
            plt.show()

    def plot_genre_rating_bar(self, save_path: Optional[str] = None):
        """
        繪製各類型平均評分柱狀圖。

        Args:
            save_path: 圖片保存路徑
        """
        stats = self.genre_rating_stats()
        fig, ax = plt.subplots(figsize=(14, 6))
        stats['mean'].plot(kind='bar', ax=ax, color='#722ed1')
        ax.set_title('各電影類型平均評分', fontsize=14)
        ax.set_xlabel('電影類型', fontsize=12)
        ax.set_ylabel('平均評分', fontsize=12)
        ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
        ax.grid(True, alpha=0.3, axis='y')

        if save_path:
            plt.savefig(save_path, dpi=150, bbox_inches='tight')
        else:
            plt.show()
