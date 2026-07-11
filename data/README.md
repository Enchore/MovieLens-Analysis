# MovieLens 數據集說明

本項目使用 MovieLens 數據集進行影片評分數據分析。

## 數據集獲取

請從 [GroupLens 官網](https://grouplens.org/datasets/movielens/) 下載數據集。

推薦使用 **MovieLens 1M** 或 **MovieLens 25M** 數據集。

## 數據集文件

下載後解壓到本目錄，文件結構如下：

```
data/
├── README.md           # 本文件
├── ml-1m/             # MovieLens 1M 數據集
│   ├── ratings.dat    # 用戶評分數據 (UserID::MovieID::Rating::Timestamp)
│   ├── movies.dat     # 電影信息 (MovieID::Title::Genres)
│   └── users.dat      # 用戶信息 (UserID::Gender::Age::Occupation::Zip-code)
```

## 數據格式

- **ratings.dat**: `UserID::MovieID::Rating::Timestamp`
- **movies.dat**: `MovieID::Title::Genres`
- **users.dat**: `UserID::Gender::Age::Occupation::Zip-code`

## 評分等級

評分範圍為 1-5 星（整數）。
