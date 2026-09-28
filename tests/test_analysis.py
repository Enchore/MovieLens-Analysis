"""分析与数据加载模块的单元测试。

数据用代码里现造的小 DataFrame / 临时文件，不依赖仓库里没提交的
MovieLens 数据集（data/ 目录只有说明文件）。
绘图函数只做 Matplotlib 调用，不在测试范围内。
"""
import os
import sys

import pandas as pd
import pytest

sys.path.insert(
    0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

from analysis.correlation.correlation_analysis import CorrelationAnalysis
from analysis.distribution.distribution_analysis import DistributionAnalysis
from analysis.time_series.trend_analysis import TrendAnalysis
from utils.data_loader import DataLoader


@pytest.fixture
def ratings_df():
    # 3 个用户 × 4 部电影，跨两个年份，评分含 1 / 3 / 5 三档
    return pd.DataFrame(
        {
            "user_id": [1, 1, 2, 2, 3, 3, 3],
            "movie_id": [10, 11, 10, 12, 11, 12, 13],
            "rating": [5, 3, 5, 1, 4, 1, 5],
            "timestamp": [
                1577836800,  # 2020-01-01
                1593561600,  # 2020-07-01
                1609459200,  # 2021-01-01
                1609459200,  # 2021-01-01
                1625097600,  # 2021-07-01
                1625097600,  # 2021-07-01
                1625097600,  # 2021-07-01
            ],
        }
    )


@pytest.fixture
def movies_df():
    return pd.DataFrame(
        {
            "movie_id": [10, 11, 12, 13],
            "title": ["A", "B", "C", "D"],
            "genres": ["Action", "Drama", "Action|Comedy", "Drama"],
        }
    )


def test_data_loader_parses_double_colon_format(tmp_path):
    raw = tmp_path / "ratings.dat"
    raw.write_text(
        "1::10::5::978300760\n2::11::3::978302109\n", encoding="utf-8"
    )

    df = DataLoader(data_dir=str(tmp_path)).load_ratings(filepath=str(raw))

    assert list(df.columns) == ["user_id", "movie_id", "rating", "timestamp"]
    assert len(df) == 2
    assert list(df["rating"]) == [5, 3]
    assert df["user_id"].tolist() == [1, 2]


def test_rating_level_distribution_counts_each_level(ratings_df, movies_df):
    analysis = DistributionAnalysis(ratings_df, movies_df)
    dist = analysis.rating_level_distribution()

    assert dist.to_dict() == {1: 2, 3: 1, 4: 1, 5: 3}
    assert dist.sum() == len(ratings_df)


def test_user_rating_distribution_aggregates_per_user(ratings_df, movies_df):
    stats = DistributionAnalysis(ratings_df, movies_df).user_rating_distribution()

    assert set(stats.columns) == {"total_ratings", "mean_rating"}
    assert stats.loc[3, "total_ratings"] == 3
    assert stats.loc[3, "mean_rating"] == pytest.approx((4 + 1 + 5) / 3)
    assert stats["total_ratings"].sum() == len(ratings_df)


def test_high_rated_movies_filter_by_threshold(ratings_df, movies_df):
    # 电影 10 平均分 5.0、13 为 5.0；阈值 5.0 时应只剩这两部的评分且全为 5
    dist = DistributionAnalysis(ratings_df, movies_df).high_rated_movies_user_dist(
        threshold=5.0
    )

    assert dist.to_dict() == {5: 3}


def test_rating_count_trend_groups_by_month(ratings_df):
    trend = TrendAnalysis(ratings_df).rating_count_trend()

    assert trend.sum() == len(ratings_df)
    # 2020-01、2020-07、2021-01、2021-07 共 4 个月份
    assert len(trend) == 4
    assert trend.iloc[-1] == 3  # 2021-07 有 3 条评分


def test_average_rating_by_year(ratings_df):
    yearly = TrendAnalysis(ratings_df).average_rating_by_year()

    assert set(yearly.index) == {2020, 2021}
    assert yearly.loc[2020] == pytest.approx((5 + 3) / 2)
    assert yearly.loc[2021] == pytest.approx((5 + 1 + 4 + 1 + 5) / 5)


def test_correlation_analysis_needs_year_and_genre_columns(ratings_df, movies_df):
    movies = movies_df.copy()
    movies["year"] = [2000, 2001, 2002, 2003]

    corr = CorrelationAnalysis(ratings_df, movies).year_rating_correlation()

    assert isinstance(corr, float)
    assert -1.0 <= corr <= 1.0
