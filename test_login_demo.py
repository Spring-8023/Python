# -*- coding:utf-8 -*-
import os
import requests
import test_read_yaml

cur_path = os.path.dirname(__file__)
file_path = test_read_yaml.file_name2(cur_path, 'test')

def Login():
    login_data = test_read_yaml.read_yaml2(file_path)
    # print login_data
    url = login_data['login_data']['url']
    data = login_data['login_data']['data']
    # # print self.url
    s = requests.Session()
    res = s.post(url=url, data=data)
    print(res.content)
    # # print ('-----')
    return s


if __name__ == '__main__':
    Login()