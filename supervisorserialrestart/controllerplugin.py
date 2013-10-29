# -*- coding: utf-8 -*-
from supervisor.supervisorctl import ControllerPluginBase
import fnmatch


class SerialRestartControllerPlugin(ControllerPluginBase):
    name = 'serialrestart'

    def __init__(self, controller, **config):
        self.ctl = controller
        self.match_group = bool(int(config.get('match_group', '0')))

    def _procrepr(self, process):
        template = '%(group)s:%(name)s'
        if process['group'] == process['name']:
            return process['name']
        else:
            return template % process

    def do_serialrestart(self, arg):
        if not self.ctl.upcheck():
            return

        names = arg.strip().split()
        supervisor = self.ctl.get_supervisor()

        if not names:
            self.ctl.output('Error: serialrestart requires a process name')
            self.help_serialrestart()
            return

        # first get all process to handle
        processes = set()

        allprocesses = [self._procrepr(p) for p in supervisor.getAllProcessInfo()]
        if 'all' in names:
            processes = allprocesses
        else:
            for name in names:
                match = [p for p in allprocesses if fnmatch.fnmatch(p, name)]
                if match:
                    processes = processes.union(match)
                else:
                    self.ctl.output('No such process %s' % (name, ))

        # do restart for each of them
        for process in processes:
            self.ctl.onecmd('restart %s' % process)

    def help_serialrestart(self):
        self.ctl.output("serialrestart <name>\t\tRestart a process")
        self.ctl.output("serialrestart <gname>:*\tRestart all processes in a group")
        self.ctl.output("serialrestart <name> <name>\tRestart multiple processes or "
                        "groups")
        self.ctl.output("serialrestart all\t\tRestart all processes")
        self.ctl.output("Note: serialrestart does restart one process after another, "
                        "instead of restart, which stops all process and then starts them.")
        self.ctl.output("Note: serialrestart does not reread config files. For that,"
                        " see reread and update.")
        self.ctl.output("Note: serialrestart also accepts wildcard expressions to match the process name")
        self.ctl.output("serialrestart a* restarts all processes begining with \"a\"")


def make_serialrestart_controllerplugin(controller, **config):
    return SerialRestartControllerPlugin(controller, **config)
