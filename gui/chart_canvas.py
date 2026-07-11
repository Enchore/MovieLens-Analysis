"""
Matplotlib 圖表畫布組件
將 Matplotlib 圖表嵌入 Tkinter 界面中。
"""
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class ChartCanvas(tk.Frame):
    """Matplotlib 圖表 Tkinter 畫布。"""

    def __init__(self, parent: tk.Widget, title: str = ""):
        """
        初始化圖表畫布。

        Args:
            parent: 父容器
            title: 圖表標題
        """
        super().__init__(parent)
        self._figure = Figure(figsize=(8, 6), dpi=100)
        self._canvas = FigureCanvasTkAgg(self._figure, master=self)
        self._canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def get_figure(self) -> Figure:
        """獲取 Matplotlib Figure 對象。"""
        return self._figure

    def refresh(self):
        """刷新畫布顯示。"""
        self._canvas.draw()

    def clear(self):
        """清除畫布。"""
        self._figure.clear()
        self._canvas.draw()
