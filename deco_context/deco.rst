=================================
 Decorators and Context managers
=================================

Definition
==========

A decorator is the name used for a software design pattern. Decorators
dynamically alter the functionality of a function, method, or class
without having to directly use subclasses or change the source code of
the function being decorated.


What is it
----------

- every function in Python is a **first class object**

In [10]: def func(arg1, arg2):
   ....:     var1 = 10

*func* is now bound to an object, which for example encapsulates

For example func.func_code.co_varnames gives ('arg1', 'arg2', 'var1')
In [18]: func.func_code.co_code
Out[18]: 'd\x01\x00}\x02\x00d\x00\x00S'

Shocking example
================

.. literalinclude:: ../code/deco/deco.py
   :pyobject: fib

.. code-block:: python

    @memoize
    def fib_memoized(n):
        if n <= 1:
            return 1
        return fib_memoized(n-1) + fib_memoized(n-2)

- fib(5): 2.66 us  <=>   fib_memoized(5): 1.16 us
- fib(20): 3.78 ms <=>   fib_memoized(20): 1.21 us


Simplest decorator possible:
============================

.. TODO: should I explain why (*args, **kwargs) is the generic way to
   call any function?

.. this is not what is supposed to do, should be in the right order

.. literalinclude:: ../code/deco/deco.py
   :pyobject: decorator

Which can be used as:

.. code-block:: python

   @decorator
   def myfunc(): pass


And it's simply syntactic sugar for

.. code-block:: python

    to_decorate = decorator(to_decorate)


Parametric decorator
====================

Here is where things might get hairy, how do I add arguments to a
decorator?

.. code-block:: python

    @deco(arg1="value", arg2=100)
    def function..

Ideally we have to do the following, write a function that

.. code-block:: python
    
    def multi_deco(func):
        def _multi_deco(arg1, arg2):
             def __multi_deco(*args, **kwargs):

             return __multi_deco

        return _multi_deco


Using the __call__ class:
=========================

.. code-block:: python

    class call_decorator:
        def __init__(self, arg1, arg2):
            self.arg1 = arg1
            self.arg2 = arg2

        def __call__(self, func):
            def _decorator(*args, **kwargs):
                ret = func(*args, **kwargs)
                return ret

            return _decorator


Class decorator
===============

Also a class is an object, and can be also decorator since python > 2.5.

.. code-block:: python

    def class_decorator(cls):
        # here self is a free variable
        def new_meth(self):
            return 100

        cls.new_meth = new_meth
        return cls

    @class_decorator
    class C1:
        pass


Context manager
===============

Introduced in Python 2.5 with the with_statement_.

A context manager is useful whenever you can split the actions in:

- set up
- action
- teardown

Two ways to do it


Temporary file creation:
========================


.. code-block:: python

    class TempFile:
        """Create a temporary file with the given content and remove it on exit
        """
        def __init__(self, content=None):
            self.content = content or ""
            self.temp_file = mktemp()

        def __enter__(self):
            with open(self.temp_file, 'w') as wr:
                wr.write(self.content)

            return self.temp_file

        def __exit__(self, type, value, traceback):
            remove(self.temp_file)


Using contextlib
================

Contextmanager runs the generator until yield, then stops and runs
until the end.

.. code-block:: python

    from contextlib import contextmanager

    @contextmanager
    def tag(name):
        print "<%s>" % name
        yield
        print "</%s>" % name


Thanks
======

.. figure for possible questions

.. rst-class:: build

.. figure:: ../images/questions.jpg

Slides generated with hieroglyph_


.. notslides::

.. _decostory: http://wiki.python.org/moin/PythonDecorators
.. _hieroglyph: https://github.com/nyergler/hieroglyph
.. TODO: actually create the repo
.. _slides: https://github.com/andreacrotti/pyconuk2012_slides
.. _with_statement: http://www.python.org/dev/peps/pep-0343/
