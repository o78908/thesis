import os
import pandas as pd

# 指定要处理的文件夹路径
folder_path = 'C:\\Users\\Modern 14\\Desktop\\test2'

# 获取文件夹内所有的CSV文件
csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]

# 创建一个字典，用于存储文件名前12个字符和对应的DataFrame
dataframes_dict = {}

# 遍历每个CSV文件并合并数据
for csv_file in csv_files:
    file_path = os.path.join(folder_path, csv_file)
    
    # 获取文件名前12个字符作为标识符
    identifier = csv_file[:-4][:-8]
    
    # 如果标识符已经存在于字典中，就将数据追加到对应的DataFrame中
    if identifier in dataframes_dict:
        df = pd.read_csv(file_path)
        dataframes_dict[identifier] = pd.concat([dataframes_dict[identifier], df], ignore_index=True)
    else:
        # 如果标识符不在字典中，创建一个新的DataFrame，并添加到字典中
        dataframes_dict[identifier] = pd.read_csv(file_path)

# 将合并后的数据保存到一个新的CSV文件中，并以标识符作为文件名的一部分
output_folder = 'C:\\Users\\Modern 14\\Desktop\\test2\\output'  # 指定输出文件夹
os.makedirs(output_folder, exist_ok=True)  # 创建输出文件夹（如果不存在）
for identifier, df in dataframes_dict.items():
    output_file = os.path.join(output_folder, f'{identifier}_merged.csv')
    df.to_csv(output_file, index=False)

print("处理完成")
