from sympy import *
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_application


class Integrate:
    minn = ''
    maxx = ''
    var = ''
    equation = ''

    def __init__(self, equation, var, minn='', maxx=''):
        self.equation = equation
        self.var = var
        self.minn = minn
        self.maxx = maxx

    def latex_print(self):
        x = Symbol(self.var)
        transformations = standard_transformations + (implicit_application,)
        parse_expr(self.equation, transformations=transformations)
        if self.minn == '' and self.maxx == '':
            return latex(integrate(self.equation, x))
        else:
            return latex(integrate(self.equation, (x, self.minn, self.maxx)))


a = Integrate('x^2 +x + 1', 'x')
b = Integrate('x^2+x+1', 'x', '2/3', '5/4')
print(a.latex_print())
print(b.latex_print())











