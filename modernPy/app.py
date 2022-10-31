from cmath import pi
from bottle import route, run, template
from random import gauss, seed, choice, choices, randint, shuffle, sample
from statistics import mean, stdev

x = lambda x, y, z : gauss(x,y)*z
y = lambda x, y, z : gauss(x,y)*z

populations = [
    [x(0, 1, 1), y(0, 1, 1)],
]
outcomes = [
    'win',
    'lose',
    'play again',
]
    
outcome_1 = choice(outcomes)
lottery = sorted(sample(range(0,64), k=8))
num = x(2,4,9)

print(outcome_1)

@route('/main/<number>')
def main(number):
    return template('main', number=number)

@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}your lucky number is {{num}}</b>!', name=name, num=lottery)

run(host='localhost', port=8080)
