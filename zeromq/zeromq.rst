=====================
 ZeroMQ from scratch
=====================

*It's like two drunkards trying to share a beer. It doesn't matter if they're good buddies. Sooner or later they're going to get into a fight. And the more drunkards you add to the pavement, the more they fight each other over the beer. The tragic majority of MT applications look like drunken bar fights.*


    REQ is a mama socket, doesn't listen but always expects an answer. Mamas are strictly synchronous and if you use them they are always the 'request' end of a chain.
    REP is a papa socket, always answers, but never starts a conversation. Papas are strictly synchronous and if you use them, they are always the 'reply' end of a chain.
