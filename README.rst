===============================
Supervisor serialrestart
===============================

.. image:: https://badge.fury.io/py/supervisor-serialrestart.png
    :target: http://badge.fury.io/py/supervisor-serialrestart

.. image:: https://pypip.in/d/supervisor-serialrestart/badge.png
        :target: https://crate.io/packages/supervisor-serialrestart?version=latest


Adds ``serialrestart`` command to [Supervisor](http://supervisord.org/). This command works
simmilar to restart but if you have multiple services, it sometimes is
preferable to restart them one after another to minimize downtime.

It even supports wildcards.

* Free software: BSD license

.. * Documentation: http://supervisorserialrestart.rtfd.org.

Example
-------

::

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

    $supervisor> serialrestart baz:b*
    baz:bar: stopped
    baz:bar: started


