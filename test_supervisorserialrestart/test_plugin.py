import re
from nose import tools
from os.path import dirname, join
from subprocess import PIPE, Popen
from unittest import TestCase

CONFIG_FILE = join(dirname(__file__), 'supervisord.conf')

class TestPlugin(TestCase):

    def setUp(self):
        self._supervisorctl('start all')

    def _supervisorctl(self, cmd, config_file=CONFIG_FILE):
        out = Popen('supervisorctl --configuration="%s" %s' % (config_file, cmd), shell=True, stdout=PIPE).stdout.read()
        print out
        return out

    def test_serialrestart_empty(self):
        result = self._supervisorctl('serialrestart')
        lines = result.split('\n')
        self.assertEqual(lines[0],
                         'Error: serialrestart requires a process name')
        assert(len(lines) == 10)


    def test_serialrestart_fail(self):
        result = self._supervisorctl('serialrestart blub')
        self.assertEqual(result,
                         'No such process blub\n')

    def test_serialrestart_one(self):
        result = self._supervisorctl('serialrestart one')
        self.assertEqual(result,
                         'one: stopped\none: started\n')

    def test_serialrestart_multi(self):
        result = self._supervisorctl('serialrestart one baz:foo')
        self.assertEqual(result,
                         'baz:foo: stopped\nbaz:foo: started\n'
                         'one: stopped\none: started\n')

    def test_serialrestart_all(self):
        result = self._supervisorctl('serialrestart all')
        self.assertEqual(result,
                         'baz:bar: stopped\nbaz:bar: started\n'
                         'baz:foo: stopped\nbaz:foo: started\n'
                         'one: stopped\none: started\n')

    def test_serialrestart_wildcard(self):
        result = self._supervisorctl('serialrestart baz:*')
        self.assertEqual(result,
                         'baz:bar: stopped\nbaz:bar: started\n'
                         'baz:foo: stopped\nbaz:foo: started\n')

    def test_serialrestart_wildcard_one(self):
        result = self._supervisorctl('serialrestart baz:b*')
        self.assertEqual(result,
                         'baz:bar: stopped\nbaz:bar: started\n')















