========================
Supervisor serialrestart
========================

Description
===========

Adds ``serialrestart`` command to Supervisor_. This command works simmilar to restart but if you have multiple services, it sometimes is preferable to restart them one after another to minimize downtime.

Example
=======

::
    supervisorctl serialrestart all
    foo: stopped
    foo: started
    bar: stopped
    bar: started



Installation
============


::
    sudo python setup.py install


And then add into your supervisor.conf:

::
  
  [ctlplugin:serialrestart]
    supervisor.ctl_factory = supervisorserialrestart.controllerplugin:make_serialrestart_controllerplugin


      
      
Configuration
=============

Changelog
=========
 * 0.1.0
    * Simple support for ``serialrestart``

.. _Supervisor: http://supervisord.org/

