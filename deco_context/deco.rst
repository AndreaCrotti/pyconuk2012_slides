=================================
 Decorators and Context managers
=================================

.. general motivation: Showing two important constructs in Python that
.. even if they are just syntactic sugar they help a lot writing
.. better and less code.
.. You 

Decorator
=========

*A decorator is the name used for a software design pattern. Decorators
dynamically alter the functionality of a function, method, or class
without having to directly use subclasses or change the source code of
the function being decorated.*

Decorators have been introduced in Python 2.4, (see decorator-history_).


Background
==========

- every function in Python is a **first class object**

.. code-block:: python

    def func(arg1, arg2):
        var1 = 10
    
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


+-----+---------+--------------+---------+
| INP | fib     | fib_memoized | speedup |
+-----+---------+--------------+---------+
|   5 | 2.66 μs | 1.16 μs      | 2x      |
+-----+---------+--------------+---------+
|  20 | 3.78 ms | 1.21 μs      |3000x    |
+-----+---------+--------------+---------+

Hello decorator
===============

.. TODO: should I explain why (*args, **kwargs) is the generic way to
   call any function?

.. this is not what is supposed to do, should be in the right order

.. literalinclude:: ../code/deco/deco.py
   :pyobject: decorator


Which is simply syntactic sugar for:

.. code-block:: python

    def to_decorate(): pass
    to_decorate = decorator(to_decorate)


Memoization
===========

*memoize* caches the results of generic function calls.

.. literalinclude:: ../code/deco/deco.py
   :pyobject: memoize

.. explain step by step what happened there

Memoization explained I
=======================

.. code-block:: python

   @memoize
   def fib_memoized(n):

Is equivalent to:

.. code-block:: python

   fib_memoized = memoize(fib_memoized)

Which becomes:

.. code-block:: python
     
     memoize(fib_memoized, cache={})

**cache is mutable**, so it will be assigned to an object only the first call.

.. TODO: should I do a digression here??

Memoize explained II
====================

Define an inner function which will substitute the real function:

.. code-block:: python

    def _memoize(*args, **kwargs):

Define an immutable key based on the arguments given:

.. code-block:: python

        key = (args, str(kwargs))

Fill the cache and return the result of calling the function:

.. code-block:: python

        if not key in cache:
            cache[key] = func(*args, **kwargs)

        return cache[key]


Parametric decorator I
======================

Here is where things might get hairy, how do I add arguments to a
decorator?

.. code-block:: python

    @deco(arg1="value", arg2=100)
    def function..

*Triple* function

.. literalinclude:: ../code/deco/deco.py
    :pyobject: param_deco    


Parametric decorator II
=======================

Or alternatively overriding the __call__ method.

.. literalinclude:: ../code/deco/deco.py
    :pyobject: call_decorator


Class decorator
===============

Also a class is an object, and can be also decorator since python > 2.5.

.. literalinclude:: ../code/deco/deco.py
    :pyobject: class_decorator


.. code::

    @class_decorator
    class C1:
        pass


Patch classes
=============

.. use mock.patch to show how to patch entire classes

.. literalinclude:: ../code/deco/patch_class.py

Which applies the patch for all the methods found by *inspection*.

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

.. literalinclude:: ../code/deco/context.py
    :pyobject: TempFile

Add that there can be an exception handling in the with, equivalent to
the:

.. try:
.. except:
.. finally:

construct in some ways.


Using contextlib
================

Contextmanager runs the generator until yield, then stops and runs
until the end.

.. literalinclude:: ../code/deco/context.py
   :pyobject: with_context_manager


Thanks
======

.. figure:: ../images/questions.jpg

Slides generated with hieroglyph_, and can be found on github_.

.. notslides::

.. _decorator-history: http://wiki.python.org/moin/PythonDecorators
.. _hieroglyph: https://github.com/nyergler/hieroglyph
.. TODO: actually create the repo
.. _github: https://github.com/andreacrotti/pyconuk2012_slides
.. _with_statement: http://www.python.org/dev/peps/pep-0343/
