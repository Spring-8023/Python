# -*- coding:utf-8 -*-
import os
import yaml



cur_path = os.path.dirname(__file__)
# print cur_path

filepath = os.path.split(os.path.realpath(__file__))

fileNamePath = os.path.split(os.path.realpath(__file__))[0]
# print filepath
# print fileNamePath
# print os.path.realpath(__file__)
# yamlPath = os.path.join(fileNamePath,'config.yaml')
# print(yamlPath)

# 读取文件路径
def file_name(file_dir):
    L = []
    for root, dirs, files in os.walk(file_dir):
        # print(root)  # 当前目录路径
        # print(dirs)  # 当前路径下所有子目录
        # print(files)  # 当前路径下所有非目录子文件
        for file in files:
            # print os.path.splitext(file)

            # if os.path.splitext(file)[1] == '.yaml' :
            #     L.append(os.path.join(root, file))
            #     print os.path.join(root, file)
            #     print L

            if os.path.splitext(file)[1] == '.yaml':
                if os.path.splitext(file)[0] == 'test':

                    return os.path.join(root, file)

# 其中os.path.splitext()函数将路径拆分为文件名+扩展名

# 读取文件路径
def file_name2(file_dir, file_name):
    L = []
    for root, dirs, files in os.walk(file_dir):
        # print(root)  # 当前目录路径
        # print(dirs)  # 当前路径下所有子目录
        # print(files)  # 当前路径下所有非目录子文件
        for file in files:
            # print os.path.splitext(file)

            # if os.path.splitext(file)[1] == '.yaml' :
            #     L.append(os.path.join(root, file))
            #     print os.path.join(root, file)
            #     print L

            if os.path.splitext(file)[1] == '.yaml':
                if os.path.splitext(file)[0] == file_name:

                    return os.path.join(root, file)

# 其中os.path.splitext()函数将路径拆分为文件名+扩展名

def listdir(path, list_name):   #  传入存储的list
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            print(listdir(file_path, list_name))
        else:
            list_name.append(file_path)
            print(list_name)

def read_yaml(cur_path):
    file_path = file_name(cur_path)
    f = open(file_path, 'r')
    # print f.read()
    d = yaml.load(f.read(), Loader=yaml.FullLoader)
    return d
    print(type(d))
    print(d['login_data']['url'])
    print(d['other_data']['name'])
    print(d.get('login_data').get('data'))


def read_yaml2(cur_path):
    # file_path = file_name(cur_path)
    f = open(cur_path, 'r')
    # print f.read()
    d = yaml.load(f.read(), Loader=yaml.FullLoader)
    return d
    print(type(d))
    print(d['login_data']['url'])
    print(d['other_data']['name'])
    print(d.get('login_data').get('data'))

if __name__ == '__main__':
    # file_path = file_name(cur_path)
    # listdir(cur_path)
    # f = []
    # listdir(cur_path, f)
    read_yaml(cur_path)