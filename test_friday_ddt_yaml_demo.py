# -*- coding:utf-8 -*-
import unittest
import requests
from ddt import ddt, file_data, unpack
import test_read_yaml
import os
import json
import test_login_demo
import HTMLTestRunner
import sys
reload(sys)
sys.setdefaultencoding('utf8')

# res = requests.session()
cur_path = os.path.dirname(__file__)
print(cur_path)
file_path = cur_path + '/Data/config.yaml'
# print file_path

@ddt
class FridayDdtYamlDemo(unittest.TestCase):

    @classmethod
    def setUpClass(scl):
        FridayDdtYamlDemo.res = requests.session()
        cur_path = os.path.dirname(__file__)

        # FridayDdtYamlDemo.file_path = test_read_yaml.file_name(cur_path)

        FridayDdtYamlDemo.d = test_read_yaml.read_yaml(cur_path)
        # print FridayDdtYamlDemo.d
        # print(FridayDdtYamlDemo.file_path)
        # FridayDdtYamlDemo.res = test_login_demo.Login()



    def setUp(self):
        self.url = FridayDdtYamlDemo.d['login_data']['url']
        self.data = FridayDdtYamlDemo.d['login_data']['data']
        # print self.url
        res = FridayDdtYamlDemo.res .post(url=self.url, data=self.data)
        self.assertEqual(200, res.status_code, msg='状态码为200，表示通过')
        print res.content
        print ('-----')
        # FridayDdtYamlDemo.res = test_login_demo.Login()

    @file_data(file_path)
    def test_login(self, **data):

        self.url = data['url']
        self.data = data['data']
        self.method = data['method']
        if self.method == 'POST':

            res = FridayDdtYamlDemo.res.post(url=self.url, data=self.data)
            # print('post')
            print(json.dumps(res.json(), ensure_ascii=False))
            self.assertEqual(200, res.status_code, msg='状态码为200，表示通过')

        elif self.method == 'GET':
            res = FridayDdtYamlDemo.res.get(url=self.url, data=self.data)
            print(json.dumps(res.json(), ensure_ascii=False))
        # print self.url
        # print(FridayDdtYamlDemo.file_path)



if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(FridayDdtYamlDemo))
    with open('test.html', 'w') as f:
        runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='单元测试报告', description='单元测试报告')
        runner.run(suite)
    f.close()

