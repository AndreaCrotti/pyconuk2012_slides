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

- every function in

In [10]: def func(arg1, arg2):
   ....:     var1 = 10

func.func_code.co_argcount     func.func_code.co_consts       func.func_code.co_flags        func.func_code.co_name         func.func_code.co_stacksize
func.func_code.co_cellvars     func.func_code.co_filename     func.func_code.co_freevars     func.func_code.co_names        func.func_code.co_varnames
func.func_code.co_code         func.func_code.co_firstlineno  func.func_code.co_lnotab       func.func_code.co_nlocals

For example func.func_code.co_varnames gives ('arg1', 'arg2', 'var1')
In [18]: func.func_code.co_code
Out[18]: 'd\x01\x00}\x02\x00d\x00\x00S'

Shocking example
================

.. code:: python

  def memoize(f, cache={}, *args, **kwargs):

      def _memoize(*args, **kwargs):
          key = (args, str(kwargs))
          if not key in cache:
              cache[key] = f(*args, **kwargs)
          return cache[key]

      return _memoize

  def fib(n):
       if n <= 1:
           return 1
       return fib(n-1) + fib(n-2)

  @memoize
  def fib_memoized(n):
       if n <= 1:
           return 1
       return fib_memoized(n-1) + fib_memoized(n-2)


Simplest decorator possible:
============================

.. TODO: should I explain why (*args, **kwargs) is the generic way to
   call any function?

.. this is not what is supposed to do, should be in the right order

.. rst-class:: build

.. code:: python

    def decorator(func):
        def _decorator(*args, **kwargs):
            # something before the function is run
            ret = func(*args, **kwargs)
            # something after the function is run
            return ret

        return _decorator


Which can be used as:

.. code:: python

   @decorator
   def myfunc(): pass


Parametric decorator
====================

Here is where things might get hairy, how do I add arguments to a
decorator?

.. code:: python

    @deco(arg1="value", arg2=100)
    def function..

Ideally we have to do the following, write a function that

.. code:: python
    
    def multi_deco(func):
        def _multi_deco(arg1, arg2):
             def __multi_deco(*args, **kwargs):

             return __multi_deco

        return _multi_deco


Using the __call__ class:
=========================

.. code:: python

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

.. code:: python

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


.. code:: python

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

.. code:: python

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
