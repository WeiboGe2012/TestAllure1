import pytest, allure


class TestAbc:

    @allure.step(title="测试步骤001")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_abc(self):
        allure.attach('描述', '我是测试步骤001的描述～～～')
        assert 1

    @allure.severity(allure.severity_level.BLOCKER)
    def test_b(self):
        allure.attach('描述', '我是测试步骤002的描述～～～')
        assert 1


if __name__ == '__main__':
    pytest.main("-s --alluredir report taoge.py")