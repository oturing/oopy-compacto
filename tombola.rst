Tômbola
=======

Ao instanciar, passamos os itens::

    >>> from tombola import Tombola
    >>> t = Tombola([1, 2, 3])
    
Verificar se está carregada::

    >>> t.carregada()
    True
    
Misturar os itens da tombola::
    
    >>> def embaralhar_fake(l):
    ...     l[0], l[1] = l[1], l[0]

    >>> t.misturar(embaralhar_fake)
    

Sortear::
    
    >>> t.sortear()
    3
    >>> t.sortear()
    1
    >>> t.sortear()
    2

Verificar se está carregada::

    >>> t.carregada()
    False
    