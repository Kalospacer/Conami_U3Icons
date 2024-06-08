import os
import re

def rename_files(path):
    # 确保路径字符串中的反斜杠被正确处理
    path = path.replace('\\', '/')  # 将反斜杠替换为正斜杠
    filenames = os.listdir(path)
    
    for i, filename in enumerate(filenames):
        if filename.endswith(".png"):
            # 修复正则表达式，确保正确提取文件名中的数字部分
            new_filename = re.sub(r'^.*?_(\d+)', r'\1', filename)
            
            # 如果新文件名与已有文件名重复，则删除该文件
            while new_filename in filenames:
                filenames.remove(new_filename)
                new_filename = f"{i}_{new_filename}"
                
            # 使用os.path.join确保跨平台兼容性
            os.rename(os.path.join(path, filename), os.path.join(path, new_filename))
            # 如果新文件名为0.png，则删除该文件
            if new_filename == '0.png':
                os.remove(os.path.join(path, new_filename))
            elif new_filename == '0_0.png':
                os.remove(os.path.join(path, new_filename))

if __name__ == "__main__":
    # 确保路径字符串中的反斜杠被正确处理
    path = "C:/Users/Kalo/Documents/Conami-U3Icons/items"
    rename_files(path)
