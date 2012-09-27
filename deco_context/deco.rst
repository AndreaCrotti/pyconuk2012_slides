=================================
 Decorators and Context managers
=================================

.. general motivation: Showing two important constructs in Python that
.. even if they are just syntactic sugar they help a lot writing
.. better and less code.

.. The reason why I decided to give this talk is to try to demistify
.. decorators and context managers, because they are not really so
.. hard and they are widely used patterns in Python.


Decorator
=========

A **decorator** is a function that takes a *function object* as
argument, and returns a function object with an alterated behaviour.

Decorators have been introduced in Python 2.4, (see decorator-history_).

.. TODO: remove the definition, and just show a nice example first


Background
==========

.. Before I show what a decorator is in Python, it should be clear to
.. everyone that in Python a function is a first class object.

.. Once a function func is defined the name 'func' will be bound in
.. the current namespace to a object, which type is function.

.. We can inspect the function and see for example its arguments,
.. or even see the compiled code with func.func_code.co_code.

.. TODO: add that this is not like this in Java, but similar to
.. function pointers in C

- every function in Python is a **first class object**

::

    def func(arg1, arg2):
        var1 = 10
    
*func* is now bound to an **object**, with type

::
    
    >>> type(func)
    >>> function

::

    >>> func.func_code.co_varnames
    >>> ('arg1', 'arg2', 'var1')
    >>> func.func_code.co_code
    >>> 'd\x01\x00}\x02\x00d\x00\x00S'

Shocking example
================

.. And here we see a very simple first example of where a decorator
.. might be useful.

.. literalinclude:: ../code/deco/deco.py
   :pyobject: fib

::

    @memoize
    def fib_memoized(n):
        if n <= 1:
            return 1
        return fib_memoized(n-1) + fib_memoized(n-2)


+-----+---------+--------------+---------+
|  n  | fib     | fib_memoized | speedup |
+-----+---------+--------------+---------+
|   5 | 2.66 μs | 1.16 μs      | 2x      |
+-----+---------+--------------+---------+
|  20 | 3780 μs | 1.21 μs      |3000x    |
+-----+---------+--------------+---------+

Hello decorator
===============

.. TODO: should I explain why (*args, **kwargs) is the generic way to
   call any function?

.. this is not what is supposed to do, should be in the right order

.. literalinclude:: ../code/deco/deco.py
   :pyobject: decorator


Which is simply syntactic sugar for:

::

    def my_function(): pass
    my_function = decorator(my_function)


Simple example
==============

.. literalinclude:: ../code/deco/deco.py
   :pyobject: verbose


::

    >>> def silly_func():
    >>>     print("Simple function")

    >>> silly_func = verbose(silly_func)

::

    Entering function silly_func
    Simple function
    Exiting function silly_func


Why the _decorator?
===================

.. One question which I previously received is why do we actually need the _decorator?
.. Why can't I just define it like this:

.. Can anyone see what's wrong with this?

.. literalinclude:: ../code/deco/deco.py
   :pyobject: naive_decorator

.. The problem is that once we don

::
   
   my_function = naive_decorator(my_function)

Here the function get **immediately executed!**, returning None


Back to memoization
===================

*memoize* caches the results of generic function calls.

.. literalinclude:: ../code/deco/deco.py
   :pyobject: memoize


.. explain step by step what happened there

**Completely generic, memoize any recursive function**

Memoization unfolded
====================

::

    fib(5)
    fib(4) + fib(3)
    (fib(3) + fib(2)) + (fib(2) + fib(1))
    ...
    
- *cache* is initially {}
- fib(2) should be computed twice, but it's cached after first run


Running in a forked process
===========================

.. literalinclude:: ../code/deco/deco.py
   :pyobject: on_forked_process

.. TODO: add about
.. - chaining decorators
.. - decorator nesting


Parametric decorator 1
======================

Here is where things might get hairy, how do I add arguments to a
decorator?

::

    @deco(arg1="value", arg2=100)
    def function..

*Triple* function

.. literalinclude:: ../code/deco/deco.py
    :pyobject: param_deco    


Parametric decorator 2
======================

Or alternatively overriding the __call__ method.

.. literalinclude:: ../code/deco/deco.py
    :pyobject: call_decorator


Parametric decorator 3
======================

.. literalinclude:: ../code/deco/deco.py
    :pyobject: retry_n_times


Class decorator
===============

Also a class is an object, and can be also decorator since python > 2.5.

.. literalinclude:: ../code/deco/deco.py
    :pyobject: class_decorator


.. code::

    @class_decorator
    class C1:
        pass


Patching classes
================

.. use mock.patch to show how to patch entire classes

.. literalinclude:: ../code/deco/patch_class.py

Which applies the patch for all the methods found by *inspection*.

Context manager
===============

.. TODO: Add an example about locks

.. main idea is to keep track of the context

Introduced in Python 2.5 with the with_statement_.

A context manager is useful whenever you can split the actions in:

- set up
- action
- teardown

**Very common pattern**:

- database connection
- perforce connection
- temporary environment


With statement
==============

The idea is to *not forget cleanup actions*.

::
    
    with open('file.txt') as source:
         text = source.read()

Is equivalent to:

::

    source = open('file.txt')
    text = source.read()
    source.close()


Implement __enter__ and __exit__
================================

.. literalinclude:: ../code/deco/context.py
    :pyobject: TempFile

Add that there can be an exception handling in the with.

.. try:
.. except:
.. finally:


Using contextlib
================

Contextmanager runs the generator until yield, then stops and runs
until the end.

::

    from contextlib import contextmanager

    @contextmanager
    def tag(name):
        print "<%s>" % name
        yield
        print "</%s>" % name

::
    
     >>> with tag('H1'):
     >>>      print('Title')
    
     '<H1>Title</H1>'


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
