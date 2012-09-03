=================================
 Decorators and Context managers
=================================

Definition
==========

A decorator is the name used for a software design pattern. Decorators
dynamically alter the functionality of a function, method, or class
without having to directly use subclasses or change the source code of
the function being decorated.

Simplest decorator possible:
============================

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
    


Context manager
===============

A context manager is useful whenever you can split the actions in:

- set up
- action
- teardown

Two ways to do it

.. rst-class:: build



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


Links
=====

.. _decostory: http://wiki.python.org/moin/PythonDecorators
.. _hieroglyph: https://github.com/nyergler/hieroglyph
.. TODO: actually create the repo
.. _slides: https://github.com/andreacrotti/pyconuk2012_slides
