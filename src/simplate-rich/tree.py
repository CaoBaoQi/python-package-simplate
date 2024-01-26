import os


def print_tree(directory, ignored_dirs=None, prefix=''):
    """递归打印目录树，忽略特定目录

    :param directory: 要遍历的目录路径
    :param ignored_dirs: 忽略的目录列表
    :param prefix: 当前递归层的前缀，用于格式化输出
    """
    if ignored_dirs is None:
        ignored_dirs = []

    files = os.listdir(directory)
    filtered_files = [file for file in files if file not in ignored_dirs]

    for i, file in enumerate(filtered_files):
        path = os.path.join(directory, file)
        is_last = i == len(filtered_files) - 1  # 检查是否为当前目录下的最后一个文件/目录

        # 打印当前文件/目录名称
        print(prefix + '└── ' if is_last else prefix + '├── ', file)

        # 如果是目录，则递归调用此函数
        if os.path.isdir(path):
            # 更新前缀，用于下一层递归的格式化输出
            new_prefix = prefix + ('    ' if is_last else '│   ')
            print_tree(path, ignored_dirs, new_prefix)


# 使用示例
current_file_path = os.path.abspath(__file__)
# 使用 os.path.split() 分割路径
path_parts = current_file_path.split(os.sep)
# 找到 'src' 并获取其前面的部分
src_index = path_parts.index('src')
path_until_src = os.sep.join(path_parts[:src_index + 1])

directory_path = path_until_src  # 可以更换为任意目录路径
ignored_dirs = ['__pycache__', '.git', '.idea']  # 替换为你想忽略的目录名称
print_tree(directory_path, ignored_dirs)
