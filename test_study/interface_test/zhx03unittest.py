# codine =utf-8
import requests
import zhx01config
import unittest


class Testcase(unittest.TestCase):
    def test_register(self):
        r = requests.post(zhx01config.url_register['注册接口'], zhx01config.url_register['params'])
        status = r.status_code
        self.assertEqual(200, status)
        print(status)
        print(r.content)
        print(r.text)

    def test_login(self):
        r = requests.get(zhx01config.url_login)
        status = r.status_code
        self.assertEqual(200, status)
        print(status)

        print(r.json())
        expected = '裤子男'
        j = r.json()
        print(j)
        self.assertEqual(expected, j['result'][1][0])
        print(r.text)


if __name__ == 'main':
    unittest.main()
