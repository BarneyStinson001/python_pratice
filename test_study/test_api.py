import pytest,time


class TestApi:
    @pytest.mark.smoke
    def test_01(self):
        print('test ok')
        time.sleep(1)

    @pytest.mark.count_management
    def test_02(self):
        time.sleep(1)
        # raise Exception('抛出异常')

    def test_03(self):
        time.sleep(1)


if __name__=='__main__':
    pytest.main()