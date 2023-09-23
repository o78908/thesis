import os
import pandas as pd

# 指定要处理的文件夹路径
folder_path = 'C:\\Users\\Modern 14\\Desktop\\test'

# 获取文件夹内所有的CSV文件
csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]

# 遍历每个CSV文件并添加time列
for csv_file in csv_files:
    file_path = os.path.join(folder_path, csv_file)
    
    # 从文件名中提取最后8位数字（不包括.csv）
    time_value = csv_file[:-4][-8:]
    
    # 将时间值转换为yyyy-mm-dd格式
    formatted_time = f"{time_value[:4]}-{time_value[4:6]}-{time_value[6:8]}"
    
    # 读取CSV文件
    df = pd.read_csv(file_path)
    
    # 添加名为"time"的列，设置值为格式化后的时间值
    df['time'] = formatted_time
    
    # 保存修改后的CSV文件
    df.to_csv(file_path, index=False)

print("处理完成")
