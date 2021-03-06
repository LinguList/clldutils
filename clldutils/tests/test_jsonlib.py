# coding: utf8
from __future__ import unicode_literals
from datetime import date

from clldutils.testing import WithTempDir


class Tests(WithTempDir):
    def test_parse_json_with_datetime(self):
        from clldutils.jsonlib import parse

        assert parse(dict(d='2012-12-12T20:12:12.12'))['d'].year

    def test_json(self):
        from clldutils.jsonlib import dump, load

        d = {'a': 234, 'ä': 'öäüß'}
        p = self.tmp_path('test')
        dump(d, p)
        for k, v in load(p).items():
            assert d[k] == v

    def test_format_json(self):
        from clldutils.jsonlib import format

        format(date.today())
        self.assertEquals(format(5), 5)
