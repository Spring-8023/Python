# -*- coding:utf-8 -*-
import unittest
import requests
import json
import sys
import test_read_yaml
import os
cur_path = os.path.dirname(__file__)


class TestFridayDemo(unittest.TestCase):

    @classmethod
    def setUpClass(scl):
        d = test_read_yaml.read_yaml(cur_path)
        globals()['url'] = d['login_data']['url']
        TestFridayDemo.url = d['login_data']['url']
        TestFridayDemo.s = requests.session()
        TestFridayDemo.d = test_read_yaml.read_yaml(cur_path)

    def login_by_account(self):
        self.host = 'http://192.168.0.8:80'
        self.url = self.host + '/V2/StudentSkip/loginCheckV4.action'
        self.data = {
            'password': '54d87d745c5c90aeeff78b08b26d2ee6',
            # 'account': '4ab073e23f051f50fbc7107cb550400f',
            # password    54d87d745c5c90aeeff78b08b26d2ee6
            'account': '7e657c97967e7f66255a9c93d84c63bd',
            # 'registrationId': '',
            # 'ifa': 'FA743629-436F-4EFA-B493-2A883B1D83CF',
            # 'ifv': '349305A8-D830-4D7C-B125-B2847BB2AC50',
            'versionNumber': '9.5.5',
            'platform': '2',
            # 'channel': 'AppStore',
            # 'phoneVersion': '12.2',
            # 'phoneModel': 'iPhone X',
            # 'phoneBrand': 'Apple'
        }
        res = requests.request('POST', self.url, data=self.data)
        # result = res.json()
        print(res.content)

        # print json.dumps(result, ensure_ascii=False, indent=2)

    def test_01_login(self):
        # file_path = test_read_yaml.file_name(cur_path)
        # d = test_read_yaml.read_yaml(cur_path)
        self.url = TestFridayDemo.d['login_data']['url']
        self.data = TestFridayDemo.d['login_data']['data']
        # print self.url, self.data
        # print globals()['url']
        print(TestFridayDemo.url)
        res = TestFridayDemo.s.request('POST', url=self.url, data=self.data)
        # return TestFridayDemo.s
        print(res.content)


    def test_02_getList_By_Type(self):
        self.url = TestFridayDemo.d['treehole_data']['url']
        self.data = TestFridayDemo.d['treehole_data']['data']
        print(self.url)
        res = TestFridayDemo.s.request('POST', url=self.url, data=self.data)
        print(res.content)





if __name__ == '__main__':

    unittest.main()
