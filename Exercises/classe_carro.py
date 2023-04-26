"""Suponha que você queira criar uma classe para representar um carro. Essa classe deve permitir a criação de carros com uma marca,
 um modelo e um ano de fabricação. Também deve ser possível ligar e desligar o carro, além de consultar se o carro está ligado ou desligado.
Escreva o código para implementar essa classe e crie algumas instâncias da classe para testar seus métodos."""

class Car:
    def __init__(self, brand, model, age, connected=False):
        self.brand = brand
        self.model = model
        self.age = age
        self.connected = connected
    
    def turn_on(self):
        if self.connected:
            print(f'{self.brand} is already on.')
            return
        print(f'{self.brand} is on...')
        self.connected = True
    
    def turn_off(self):
        if self.connected is False:
            print( f'{self.brand} is alredy off...')
            return
        print(f'{self.brand} is off.')
        self.connected = False
    
 # Criando as instâncias para classe car.

car_1 = Car('Volvo', 'XC60', 2020)
car_1.turn_on()
car_1.turn_on()
car_1.turn_off()
car_1.turn_off()
car_1.request_user()
print('Age:', car_1.age,'Model: ', car_1.model)    
        

    