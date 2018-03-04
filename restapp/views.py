from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# import required modules written by Tsengunn
from restapp import diff, expand, factor, integration, simplify

# Create your views here.
class AllData(APIView):
    def get(self, request, format = None):
        qtype= request.GET['type']
        equation = request.GET['equation']
        equation = equation.replace("^", "**")
        answer = "default"

        #put up the functions here
        if qtype == 'diff':
            proc = diff.Diff(equation, request.GET['var'], request.GET['times'])
            answer = proc.latex_print()
        elif qtype == 'integ':
            proc = integration.Integrate(equation, request.GET['min'],request.GET['max'])
            answer = proc.latex_print()
        elif qtype == 'expand':
            proc = expand.Expand(equation)
            answer = proc.latex_print()
        elif qtype == 'factor':
            proc = factor.Factor(equation)
            answer = proc.latex_print()
        else:
            proc = simplify.Simplify(equation)
            answer = proc.latex_print()

        #might need to serialize the data to native python data types
        return Response({'answer' : answer, 'equation':equation})
