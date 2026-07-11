"""
數據加載器模塊
負責加載 MovieLens 數據集的各種文件格式。
"""
import pandas as pd
from typing import Optional, Tuple


class DataLoader:
    """MovieLens 數據加載器。"""

    def __init__(self, data_dir: str = "data"):
        """
        初始化數據加載器。

        Args:
            data_dir: 數據目錄路徑
        """
        self._data_dir = data_dir

    def load_ratings(self, filepath: Optional[str] = None) -> pd.DataFrame:
        """
        加載評分數據。

        Args:
            filepath: 評分文件路徑（可選）

        Returns:
            評分 DataFrame (user_id, movie_id, rating, timestamp)
        """
        path = filepath or f"{self._data_dir}/ml-1m/ratings.dat"
        df = pd.read_csv(
            path,
            sep="::",
            engine="python",
            names=["user_id", "movie_id", "rating", "timestamp"],
            encoding="latin-1"
        )
        return df

    def load_movies(self, filepath: Optional[str] = None) -> pd.DataFrame:
        """
        加載電影數據。

        Args:
            filepath: 電影文件路徑（可選）

        Returns:
            電影 DataFrame (movie_id, title, genres)
        """
        path = filepath or f"{self._data_dir}/ml-1m/movies.dat"
        df = pd.read_csv(
            path,
            sep="::",
            engine="python",
            names=["movie_id", "title", "genres"],
            encoding="latin-1"
        )
        return df

    def load_users(self, filepath: Optional[str] = None) -> pd.DataFrame:
        """
        加載用戶數據。

        Args:
            filepath: 用戶文件路徑（可選）

        Returns:
            用戶 DataFrame (user_id, gender, age, occupation, zip_code)
        """
        path = filepath or f"{self._data_dir}/ml-1m/users.dat"
        df = pd.read_csv(
            path,
            sep="::",
            engine="python",
            names=["user_id", "gender", "age", "occupation", "zip_code"],
            encoding="latin-1"
        )
        return df

    def load_all(self) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
        """
        一次性加載所有數據。

        Returns:
            (ratings, movies, users) 三個 DataFrame 的元組
        """
        ratings = self.load_ratings()
        movies = self.load_movies()
        users = self.load_users()
        return ratings, movies, users
