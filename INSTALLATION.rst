============
Installation
============

At the command line::

    $ easy_install supervisor-serialrestart

Or::

    $ pip install supervisor-serialrestart


And then add into your supervisor.conf::

    [ctlplugin:serialrestart]
    supervisor.ctl_factory = supervisorserialrestart.controllerplugin:make_serialrestart_controllerplugin

