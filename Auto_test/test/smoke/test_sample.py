import unittest
import json
from lib.utils import create_driver
class TestSample(unittest.TestCase):
    def setUp(self):
        self.driver=create_driver.get_driver_instance()
    def tearDown(self):
        self.driver.close()
    def test_sample_title(self):
        #get current title and verify
        test_data=json.load(open("./test/smoke/sample_data.json"))
        expected_title=test_data['sample_test']['expected_title']
        actual_title=self.driver.title
        assert actual_title == expected_title