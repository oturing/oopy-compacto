# coding: utf-8

from random import shuffle

class Tombola(object):
    
    def __init__(self, itens):
        self.itens = itens
        
    def carregada(self):
        return len(self.itens) > 0
        
    def misturar(self, fn_embaralhar=shuffle):
        fn_embaralhar(self.itens)
        
    def sortear(self):
        return self.itens.pop()