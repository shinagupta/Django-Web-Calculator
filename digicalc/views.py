from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def digicalc(request):
	template = loader.get_template('template1.html')
	return HttpResponse(template.render())

def calculator_view(request):
    result = None

    if 'number1' in request.GET and 'number2' in request.GET and 'operation' in request.GET:
        number1 = float(request.GET['number1'])
        number2 = float(request.GET['number2'])
        operation = request.GET['operation']

        if operation == 'add':
            result = number1 + number2
        elif operation == 'subtract':
            result = number1 - number2
        elif operation == 'multiply':
            result = number1 * number2
        elif operation == 'divide' and number2 != 0:
            result = number1 / number2

    context = {'result': result}
    return render(request, 'template1.html', context)
