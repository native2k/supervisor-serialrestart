Usage
-----

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


