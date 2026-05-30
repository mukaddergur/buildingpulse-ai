import pandas as pd
import os

data_path = 'data'
files = ['datatraining.txt', 'datatest.txt', 'datatest2.txt']

for file in files:
    file_path = os.path.join(data_path, file)

    df = pd.read_csv(file_path)
    new_filename = file.replace('.txt', '.csv')
    save_path = os.path.join(data_path, new_filename)
    df.to_csv(save_path, index=False)
    print(f"Dönüştürüldü: {save_path}")