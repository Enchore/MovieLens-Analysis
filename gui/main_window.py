"""
GUI 主窗口模塊
提供 Tkinter 圖形界面，整合三大分析模塊的可視化功能。
"""
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from typing import Optional


class MainWindow(tk.Tk):
    """MovieLens 分析工具主窗口。"""

    def __init__(self):
        super().__init__()
        self.title("MovieLens 影片評分數據分析系統")
        self.geometry("1200x800")
        self._setup_menu()
        self._setup_ui()

    def _setup_menu(self):
        """設置選單欄。"""
        menubar = tk.Menu(self)

        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="導入數據", command=self._import_data)
        file_menu.add_separator()
        file_menu.add_command(label="退出", command=self.quit)
        menubar.add_cascade(label="文件", menu=file_menu)

        analysis_menu = tk.Menu(menubar, tearoff=0)
        analysis_menu.add_command(label="時間序列分析", command=self._run_time_series)
        analysis_menu.add_command(label="關聯性分析", command=self._run_correlation)
        analysis_menu.add_command(label="分布分析", command=self._run_distribution)
        menubar.add_cascade(label="分析", menu=analysis_menu)

        self.config(menu=menubar)

    def _setup_ui(self):
        """設置主界面佈局。"""
        # 左側控制面板
        control_panel = ttk.LabelFrame(self, text="分析模塊選擇", padding=10)
        control_panel.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

        ttk.Button(
            control_panel, text="時間序列分析",
            command=self._run_time_series
        ).pack(fill=tk.X, pady=5)

        ttk.Button(
            control_panel, text="關聯性分析",
            command=self._run_correlation
        ).pack(fill=tk.X, pady=5)

        ttk.Button(
            control_panel, text="分布分析",
            command=self._run_distribution
        ).pack(fill=tk.X, pady=5)

        # 右側圖表展示區域
        chart_frame = ttk.LabelFrame(self, text="分析結果", padding=10)
        chart_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True,
                         padx=10, pady=10)

        # TODO: 嵌入 Matplotlib 圖表
        self._chart_placeholder = ttk.Label(
            chart_frame,
            text="請先導入數據，然後選擇分析模塊",
            font=("Microsoft YaHei", 14)
        )
        self._chart_placeholder.pack(expand=True)

        # 狀態欄
        self._status_var = tk.StringVar(value="就緒")
        status_bar = ttk.Label(self, textvariable=self._status_var, relief=tk.SUNKEN)
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    def _import_data(self):
        """導入 MovieLens 數據集。"""
        # TODO: 打開文件對話框，加載數據
        messagebox.showinfo("提示", "請選擇 MovieLens 數據集文件")

    def _run_time_series(self):
        """執行時間序列分析。"""
        # TODO: 調用 TrendAnalysis 並展示結果
        self._status_var.set("正在執行時間序列分析...")

    def _run_correlation(self):
        """執行關聯性分析。"""
        # TODO: 調用 CorrelationAnalysis 並展示結果
        self._status_var.set("正在執行關聯性分析...")

    def _run_distribution(self):
        """執行分布分析。"""
        # TODO: 調用 DistributionAnalysis 並展示結果
        self._status_var.set("正在執行分布分析...")


if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
