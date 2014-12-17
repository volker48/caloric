import json
from flask import url_for
from caloric.tests.mixins import LoginMixin, RequestContextMixin, CaloricTest


__author__ = 'Marcus McCurdy'


class EntryCreation(LoginMixin, RequestContextMixin, CaloricTest):

    def get_user_entries_test(self):
        url = url_for('entry.entries')
        res = self.test_app.get(url, headers=self.headers)
        self.assertEqual(res.status_code, 200)
        loaded = json.loads(res.data)
        self.assertEqual(len(loaded['entries']), 2)

    def get_single_entry_test(self):
        url = url_for('entry.entry', entry_id=2)
        res = self.test_app.get(url, headers=self.headers)
        self.assertEqual(res.status_code, 200)
        entry = json.loads(res.data)['entry']
        self.assertEqual(entry['text'], 'Eggs and bacon')
        self.assertEqual(entry['calories'], 400)



