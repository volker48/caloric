import json
from flask import url_for
from caloric.tests.mixins import CaloricTest, RequestContextMixin, LoginMixin

__author__ = 'marcusmccurdy'


class LoginTests(RequestContextMixin, CaloricTest):

    def setUp(self):
        super(LoginTests, self).setUp()
        self.url = url_for('jwt')

    def valid_login_test(self):
        res = self.json_post(self.url, {'username': 'john@gmail.com', 'password': 'abc123'})
        self.assertEqual(res.status_code, 200)
        payload = json.loads(res.data)
        self.assertTrue('token' in payload)

    def bad_password_test(self):
        res = self.json_post(self.url, {'username': 'john@gmail.com', 'password': 'badpassword'})
        self.assertEqual(res.status_code, 400)

    def non_existing_user_test(self):
        res = self.json_post(self.url, {'username': 'idontexist@gmail.com', 'password': 'password'})
        self.assertEqual(res.status_code, 400)


class UserApiTests(LoginMixin, RequestContextMixin, CaloricTest):

    def get_user_test(self):
        url = url_for('user.user', user_id=self.user.id)
        res = self.test_app.get(url, headers=self.headers)
        self.assertEqual(res.status_code, 200)
        loaded = json.loads(res.data)
        self.assertEqual(self.user.email, loaded['email'])
        self.assertEqual(self.user.daily_calories, 2000)


