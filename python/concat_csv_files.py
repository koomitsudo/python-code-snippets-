import pandas as pd

# CSVファイルを読み込む
df1 = pd.read_csv('file1.csv')
df2 = pd.read_csv('file2.csv')

# データフレームを縦に結合
df_combined = pd.concat([df1, df2], ignore_index=True)

# 結果を新しいCSVファイルに保存
df_combined.to_csv('combined_file.csv', index=False)