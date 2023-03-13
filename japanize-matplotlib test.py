# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import matplotlib.pyplot as plt
import japanize_matplotlib

# モーターの周波数
hertz = [300, 200, 200, 500, 600, 2000, 1600, 1800, 1850, 1700, 1500, 1500, 1500, 1400, 5000, 6000, 2000, 3000, 3000]
# 箱ひげ図
plt.boxplot(hertz)
# 日本語でタイトルを設定する
plt.title('モーター音の周波数')
# 描画
plt.show()

