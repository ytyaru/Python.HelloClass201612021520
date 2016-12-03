#import hello.human.Human
from hello.human import Human

a = Human()
b = Human()

a.set_name('Taro')
b.set_name('Jiro')

a.introduce()
b.introduce()
