"""Neste exercício, você deve criar uma classe abstrata chamada Animal que possui um método abstrato sound(). 
Em seguida, você deve criar classes concretas que herdam da classe abstrata Animal e implementam o método sound(). 
No exemplo acima, temos as classes Cat e Dog que herdam de Animal e implementam o método sound().
 Depois, criamos instâncias dessas classes e imprimimos o som que cada animal faz.

Sua tarefa é executar o código e verificar se ele funciona corretamente, imprimindo os sons corretos para cada animal.
"""

from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name
    @abstractmethod
    def sound(self):
        ...
        

class Cat(Animal):
    def sound(self):
        return 'Meow'

class Dog(Animal):
    def sound(self):
        return 'AuAu'

cat = Cat('Tom')
dog = Dog('Marley')
print(f'The dog does: ', dog.sound())
print(f'The cat does: ', cat.sound())