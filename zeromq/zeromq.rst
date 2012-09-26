=====================
 ZeroMQ from scratch
=====================

.. motivation: we want to be able to exploit parallelism, using
.. message-passing instead of threads Not an expert but saw a couple
.. of talks about ZeroMQ and still no idea of what it was going on.

What
====

**sockets on steroids**.

.. ditaa::
     +------------+        +------------+
     |            |        |            | Zap!
     | TCP socket +------->| 0MQ socket |
     |            | BOOM!  |     cC00   |  POW!!
     +------------+        +------------+
       ^    ^    ^
       |    |    |
       |    |    +---------+
       |    |              |
       |    +----------+   |
      Illegal          |   |
      radioisotopes    |   |
      from secret      |   |
      Soviet atomic    | Spandex
      city             |
                   Cosmic rays


- bindings for 30+ languages
- asynchronous
- fast
- advanced patterns (fan-out, pipeline, req-rep)

Why
===

**Multi-threaded applications will eventually kill you!**

*It's like two drunkards trying to share a beer. It doesn't matter if they're good buddies. Sooner or later they're going to get into a fight. And the more drunkards you add to the pavement, the more they fight each other over the beer. The tragic majority of MT applications look like drunken bar fights.*

(zeromq_guide_ on multithread applications)


.. demo time

Patterns
========

Some examples of the various patterns.

Request/Reply
=============

.. ditaa::
    +------------+
    |            |
    |   Client   |
    |            |
    +------------+
    |    REQ     |
    \---+--------/
        |    ^
        |    |
   "Hello"  "World"
        |    |
        v    |
    /--------+---\
    |    REP     |
    +------------+
    |            |
    |   Server   |
    |            |
    +------------+

Publish/Subscribe
=================

.. ditaa::
                 +-------------+
                 |             |
                 |  Publisher  |
                 |             |
                 +-------------+
                 |     PUB     |
                 \-------------/
                      bind
                        |
                        |
                     updates
                        |
        +---------------+---------------+
        |               |               |
     updates         updates         updates
        |               |               |
        |               |               |
        v               v               v
     connect         connect         connect
  /------------\  /------------\  /------------\
  |    SUB     |  |    SUB     |  |    SUB     |
  +------------+  +------------+  +------------+
  |            |  |            |  |            |
  | Subscriber |  | Subscriber |  | Subscriber |
  |            |  |            |  |            |
  +------------+  +------------+  +------------+


Push/Pull
=========

.. ditaa::
                 +-------------+
                 |             |
                 |  Ventilator |
                 |             |
                 +-------------+
                 |    PUSH     |
                 \------+------/
                        |
                      tasks
                        |
        +---------------+---------------+
        |               |               |
      task            task             task
        |               |               |
        v               v               v
  /------------\  /------------\  /------------\
  |    PULL    |  |    PULL    |  |    PULL    |
  +------------+  +------------+  +------------+
  |            |  |            |  |            |
  |   Worker   |  |   Worker   |  |   Worker   |
  |            |  |            |  |            |
  +------------+  +------------+  +------------+
  |    PUSH    |  |    PUSH    |  |    PUSH    |
  \-----+------/  \-----+------/  \-----+------/
        |               |               |
      result          result          result
        |               |               |
        +---------------+---------------+
                        |
                     results
                        |
                        v
                 /-------------\
                 |    PULL     |
                 +-------------+
                 |             |
                 |    Sink     |
                 |             |
                 +-------------+
  
  

Hello world
===========

.. literalinclude:: ../code/zmq/hello.py
   :pyobject: start_client

.. literalinclude:: ../code/zmq/hello.py
   :pyobject: start_server


Sink
====

.. literalinclude:: ../code/zmq/simple/sink.py
    :pyobject: start_sink


Worker
======

.. literalinclude:: ../code/zmq/simple/worker.py
    :pyobject: start_worker


Manager
=======

.. literalinclude:: ../code/zmq/simple/manager.py
    :pyobject: start_manager


Thanks
======

.. figure:: ../images/questions.jpg

Slides generated with hieroglyph_, and can be found on github_.


Links
=====

.. _hieroglyph: https://github.com/nyergler/hieroglyph
.. _zeromq_guide: http://zguide.zeromq.org/
.. _github: https://github.com/andreacrotti/pyconuk2012_slides
