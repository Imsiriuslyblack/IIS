class Add:
    def do_work(self, x, y):
        return f'Sum: {x + y}'


class Sub:
    def do_work(self, x, y):
        return f'Sub: {x - y}'


class Multi:
    def do_work(self, x, y):
        return f'Multi: {x * y}'


class Divide:
    def do_work(self, x, y):
        return f'Divide: {x / y}'


class Calculator:
    def set_strategy(self, strategy):
        self.strategy = strategy
    def calculate(self, x, y):
        print('Strategy', self.strategy.do_work(x, y))


calc = Calculator()

x = int(input('Введите число X: '))
y = int(input('Введите число Y: '))

strategy = input('Введите действие:')

if strategy == '+':
    calc.set_strategy(Add())
elif strategy == '-':
    calc.set_strategy(Sub())
elif strategy == '*':
    calc.set_strategy(Multi())
elif strategy == '/':
    calc.set_strategy(Divide())

calc.calculate(x, y)
