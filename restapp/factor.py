from sympy import *
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_application


class Factor:
    equation = ''

    def __init__(self, equation):
        self.equation = equation

    def latex_print(self):
        transformations = standard_transformations + (implicit_application,)
        parse_expr(self.equation, transformations=transformations)
        return latex(factor(self.equation))


a = Factor('(x+1)**3')
b = Factor('x^2+x + x+1')
print(a.latex_print())
print(b.latex_print())











