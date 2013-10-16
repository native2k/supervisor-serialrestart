Supervisor serialrestart
========================

Description
-----------

Adds ``serialrestart`` command to [Supervisor](http://supervisord.org/). This command works
simmilar to restart but if you have multiple services, it sometimes is
preferable to restart them one after another to minimize downtime.

It even  suppoorts wildcards.

Example
-------

    supervisor> status
    baz:bar                          RUNNING
    baz:foo                          RUNNING
    one                              RUNNING

    supervisor> serialrestart all
    baz:bar: stopped
    baz:bar: started
    baz:foo: stopped
    baz:foo: started
    one: stopped
    one: started

    supervisor> serialrestart baz:*
    baz:bar: stopped
    baz:bar: started
    baz:foo: stopped
    baz:foo: started

    supervisor> serialrestart baz:b*
    baz:bar: stopped
    baz:bar: started



Installation
------------


    sudo python setup.py install


And then add into your supervisor.conf:


    [ctlplugin:serialrestart]
    supervisor.ctl_factory = supervisorserialrestart.controllerplugin:make_serialrestart_controllerplugin


Changelog
---------

 * 0.1.0
    * Simple support for ``serialrestart``


