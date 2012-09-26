=====================
 ZeroMQ from scratch
=====================

.. motivation: we want to be able to exploit parallelism, using
.. message-passing instead of threads.

.. As a premise I'm not really a ZeroMQ expert, I only started to use
.. it a few months ago.  I decided to give a talk about it because in
.. the past I saw a couple of talks and still didn't get what it was
.. actually useful or good for.

.. So this talk will be more pragmatic and hands on.

What is ZeroMQ
==============

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

.. Suppose we have a complicated program that runs for a long time.
.. The standard solution would be to spawn many threads and pray.
.. Nightmare to debug

**Multi-threaded applications will eventually kill you!**


Basic concepts
==============

- **socket**:

  API is compatible with the standard sockets, but *much more magic*

- **context**

  + one and only for every process
  + container for all the sockets of a process

.. code-block:: python
   
    import zmq
    
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    

Connection
==========

- inproc (in local process)
- ipc (interprocess, no Windows)
- tcp (tcp sockets)

Many clients can *connect* to the same port

.. code-block:: python

    socket.connect('tcp://localhost:8888')

Only one process can *bind*

.. code-block:: python

    socket.bind('tcp://localhost:8888')


Patterns
========

Builtin network patterns:

- Request-Reply
- Publish-Subscribe
- Push-Pull

Extra devices:

- QUEUE
- FORWARDER
- STREAMER


Request/Reply
=============

.. the great thing about ZeroMQ is that it builts all the network
.. patterns that you might need, and allows to compose them very easily

Standard *reply-request pattern*

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


Hello world client
==================

.. literalinclude:: ../code/zmq/req_rep/client.py
   :pyobject: start_client


Hello world server
==================

.. literalinclude:: ../code/zmq/req_rep/server.py
   :pyobject: start_server


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


Publisher
=========




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


On multithreading
=================

(zeromq_guide_ on multithread applications)

*It's like two drunkards trying to share a beer. It doesn't matter if they're good buddies.*

*Sooner or later they're going to get into a fight. And the more drunkards you add to the pavement, the more they fight each other over the beer.*

*The tragic majority of MT applications look like drunken bar fights.*

Thanks
======

.. figure:: ../images/questions.jpg

Slides generated with hieroglyph_, and can be found on github_.



Links
=====

.. _hieroglyph: https://github.com/nyergler/hieroglyph
.. _zeromq_guide: http://zguide.zeromq.org/
.. _github: https://github.com/andreacrotti/pyconuk2012_slides
