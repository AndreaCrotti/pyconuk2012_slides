=====================
 ZeroMQ from scratch
=====================

.. As a premise I'm not really a ZeroMQ expert, I only started to use
.. it a few months ago.  I decided to give a talk about it because in
.. the past I saw a couple of talks and still didn't get what it was
.. actually useful or good for.

.. So this talk will be more pragmatic and hands on.

What is ZeroMQ
==============

.. So what is zeromq?  It's basically sockets on steroids, a message
.. passing library with a socket-like API.  It has bindings with more
.. than 30 languages (even javascript or PHP), it's asynchronous,
.. really fast and provides great advanced communication patterns.

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

.. Whenever we have a complex application that needs to be run in
.. parallel the standard solution would be using multiple threads.
.. There are many problems with multi-threading applications with
.. explicit locks, they are hard to understand, even worse to debug
.. and they really don't scale very well.

.. The biggest problem is the shared state between threads, and a
.. better solution is not share state at all, but use a message
.. passing architecture.


.. TODO: add a slide to show what is wrong with sockets
.. So what was wrong with the standard sockets?


Multi-threaded application are usually:

- hard to understand
- a nightmare to debug
- very hard to scale

               **Don't share state!!**

**Message passing**:

Sending network messages between processes, but sockets are *hard*.


Basic concepts
==============

- **socket**:

  API is compatible with the standard sockets, but *much more magic*

- **context**

  + one and only for every process
  + container for all the sockets of a process

::

    import zmq

    context = zmq.Context()
    socket = context.socket(zmq.REQ)

.. go in IPython and show the various things in zmq

Connection
==========

- inproc (in local process)
- ipc (interprocess, no Windows)
- tcp (tcp sockets)

Many clients can *connect* to the same port

::

    socket.connect('tcp://localhost:8888')

Only one process can *bind*

::

    socket.bind('tcp://localhost:8888')


Patterns
========

Builtin network patterns:

- Request-Reply
- Publish-Subscribe
- Push-Pull

.. TODO: add something about router / dealer?? Probably not necessary

Extra devices:

- QUEUE (for req-rep)
- STREAMER (push-pull)
- FORWARDER (pub-sub)


Request/Reply
=============

.. the great thing about ZeroMQ is that it builts all the network
.. patterns that you might need, and allows to compose them very easily



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


Push/Pull sample
================

.. literalinclude:: ../code/zmq/push_pull/push.py
   :pyobject: push


.. literalinclude:: ../code/zmq/push_pull/pull.py
   :pyobject: pull


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

.. literalinclude:: ../code/zmq/pub_sub/pub.py
    :pyobject: pub


Subscriber
==========

.. literalinclude:: ../code/zmq/pub_sub/sub.py
    :pyobject: sub


Pub logger
==========

.. literalinclude:: ../code/zmq/pub_logger/pub_log.py
    :pyobject: add_zmq_handler



Complete application
====================

.. ditaa::

                   +-------------+
                   |             |
                   |   Manager   |
                   |             |
                   +-------------+
                   |    PUSH     |
                   \------+------/
                          |
                        array
                          |
          +---------------+---------------+
          |               |               |
        subarray        subarray        subarray
          |               |               |
          v               v               v
    /------------\  /------------\  /------------\
    |    PULL    |  |    PULL    |  |    PULL    |
    +------------+  +------------+  +------------+
    |            |  |            |  |            |
    |   Worker   |  |   Worker   |  |   Worker   |
    |            |  |            |  |            |
    +------------+  +------------+  +------------+
    |    PUB     |  |    PUB     |  |    PUB     |
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
                   |    SUB      |
                   +-------------+
                   |             |
                   |    Sink     |
                   |             |
                   +-------------+


Protocol
========

.. literalinclude:: ../code/zmq/dist_adder/proto.py
    :pyobject: Task

 
Serialising
===========

Dump result on the network

::

    result = Result(1, 1000)
    res_sender = context.socket(zmq.PUB)
    res_sender.connect(RESULT_CHANNEL)
    res_sender.send(result.dump())

The sink can reconstruct easily

::

    res_recv = context.socket(zmq.SUB)
    res_recv.connect(RESULT_CHANNEL)
    res_recv.setsockopt(zmq.SUBSCRIBE, '')
    res_msg = res_recv.recv()
    res = Result.load(res_msg)


.. Sink
.. ====

.. .. literalinclude:: ../code/zmq/dist_adder/sink.py
..     :pyobject: start_sink


.. Worker
.. ======

.. .. literalinclude:: ../code/zmq/dist_adder/worker.py
..     :pyobject: start_worker


.. Manager
.. =======

.. .. literalinclude:: ../code/zmq/dist_adder/manager.py
..     :pyobject: start_manager


On multithreading
=================

(from zeromq_guide_)

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
