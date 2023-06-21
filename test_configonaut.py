import unittest
import os
import json
from configonaut import Configonaut


class TestConfigonaut(unittest.TestCase):
    def setUp(self):
        self.filename = 'test_config.json'
        self.config = Configonaut(self.filename)
        self.config['database'] = {'host': 'localhost', 'port': 5432}
        self.config.save()

    def tearDown(self):
        os.remove(self.filename)

    def test_get_item(self):
        db_config = self.config['database']
        self.assertEqual(db_config.to_value(), {'host': 'localhost', 'port': 5432})

    def test_set_item(self):
        self.config['database']['host'] = '127.0.0.1'
        self.config.save()
        with open(self.filename, 'r') as file:
            data = json.load(file)
            self.assertEqual(data['database']['host'], '127.0.0.1')

    def test_delete_item(self):
        del self.config['database']['port']
        self.config.save()
        with open(self.filename, 'r') as file:
            data = json.load(file)
            self.assertNotIn('port', data['database'])


if __name__ == '__main__':
    unittest.main()
