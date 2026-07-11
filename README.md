# MovieLens 影片評分數據分析系統

> MovieLens 影片評分數據分析系統 | Movie Rating Data Analysis System

## 項目簡介

基於百萬級 MovieLens 評分數據集，開發的三模塊數據分析工具，含自定義 Tkinter GUI 介面，支援多維度統計分析與豐富的數據視覺化。時間序列分析（評分趨勢）、關聯性分析（上映時間 vs 評分）、分布分析（高評分電影用戶評分分布）。

## 功能模塊

### 模塊一：時間序列分析
- 評分數量隨時間變化趨勢
- 評分均值隨年份變化
- 熱門電影評分時間序列

### 模塊二：關聯性分析
- 上映時間與評分的關聯性
- 電影類型與評分的關聯性
- 用戶活躍度與評分行為的關聯

### 模塊三：分布分析
- 高評分電影的用戶評分分布
- 評分等級分布統計
- 用戶評分習慣分布

## 技術棧

| 類別 | 技術 |
|------|------|
| 數據處理 | Python, Pandas, NumPy |
| 視覺化 | Matplotlib |
| GUI | Tkinter |
| 統計分析 | 自定義統計函數 |

## 項目結構

```
MovieLens-Analysis/
├── analysis/                  # 三大分析模塊
│   ├── time_series/          # 時間序列分析
│   │   ├── __init__.py
│   │   └── trend_analysis.py
│   ├── correlation/          # 關聯性分析
│   │   ├── __init__.py
│   │   └── correlation_analysis.py
│   └── distribution/         # 分布分析
│       ├── __init__.py
│       └── distribution_analysis.py
├── gui/                       # Tkinter GUI 介面
│   ├── __init__.py
│   ├── main_window.py
│   └── chart_canvas.py
├── data/                      # 數據目錄
│   └── README.md             # 數據集說明
├── utils/                     # 工具函數
│   ├── __init__.py
│   └── data_loader.py
├── requirements.txt
├── README.md
├── .gitignore
└── LICENSE
```

## 快速開始

```bash
# 克隆項目
git clone https://github.com/Enchore/MovieLens-Analysis.git
cd MovieLens-Analysis

# 安裝依賴
pip install -r requirements.txt

# 運行 GUI
python -m gui.main_window
```

## 數據集

本項目使用 [MovieLens](https://grouplens.org/datasets/movielens/) 數據集。
請從官方網站下載數據集並解壓到 `data/` 目錄。

## 貢獻

歡迎提交 Issue 和 Pull Request。

## 許可證

本項目基於 [MIT License](LICENSE) 開源。
