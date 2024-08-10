import pandas as pd
from IPython.display import display, HTML

# Data sudah dibuat sebelumnya
data = {
    'No': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Kenaikan derajat keasaman (V1)': [3, 4, 4, 5, 5, 6, 7, 8, 7, 9],
    'Penyusutan volume (V2)': [2, 1, 3, 1, 4, 5, 6, 4, 2, 1],
    'Kategori': ['Baik', 'Baik', 'Baik', 'Baik', 'Baik', 'Buruk', 'Buruk', 'Buruk', 'Buruk', 'Buruk']
}
df = pd.DataFrame(data)

# Fungsi untuk menerapkan styling pada DataFrame
def colorize(val):
    color = 'green' if val == 'Baik' else 'red' if val == 'Buruk' else 'black'
    return f'color: {color}'

styled_df = df.style.applymap(colorize, subset=['Kategori']).hide(axis='index')
display(styled_df)