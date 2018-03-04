from sympy import *
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_application


class Diff:
    var = ''
    equation = ''
    times = 1

    def __init__(self, equation, var, times='1'):
        self.equation = equation
        self.var = var
        self.times = int(times)

    def latex_print(self):
        x = Symbol(self.var)
        transformations = standard_transformations + (implicit_application,)
        parse_expr(self.equation, transformations=transformations)
        return latex(diff(self.equation, x, self.times))



a = Diff('x^2 +x + 1', 'x')
b = Diff('x^2+x+1', 'x', '2')
print(a.latex_print())
print(b.latex_print())











