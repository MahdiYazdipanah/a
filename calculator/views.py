from django.shortcuts import render
import math

def calculator(request):
    result = None
    operation_icon = None
    num1 = None
    num2 = None
    show_num2 = True

    if request.method == 'POST':
        num1 = request.POST.get('num1')
        num2 = request.POST.get('num2')
        operation = request.POST.get('operation')


        num1 = float(num1) if num1 else None
        num2 = float(num2) if num2 else None


        if operation == 'add' and num1 is not None and num2 is not None:
            result = num1 + num2
            operation_icon = '+'
            show_num2 = True
        elif operation == 'subtract' and num1 is not None and num2 is not None:
            result = num1 - num2
            operation_icon = '-'
            show_num2 = True
        elif operation == 'multiply' and num1 is not None and num2 is not None:
            result = num1 * num2
            operation_icon = '×'
            show_num2 = True
        elif operation == 'divide' and num1 is not None and num2 is not None:
            result = num1 / num2 if num2 != 0 else "خطا: عدد دوم اصلاح شود"
            operation_icon = '/'
            show_num2 = True
        elif operation == 'power' and num1 is not None and num2 is not None:
            result = math.pow(num1, num2)
            operation_icon = 'xⁿ'
            show_num2 = True
        elif operation == 'sqrt' and num1 is not None:
            result = math.sqrt(num1) if num1 >= 0 else "خطا: عدد را اصلاح کن"
            operation_icon = '√'
            show_num2 = False
        elif operation == 'abs' and num1 is not None:
            result = abs(num1)
            operation_icon = f'|{num1}|'
            show_num2 = False
        elif operation == 'log' and num1 is not None:
            result = math.log10(num1) if num1 > 0 else "خطا: عدد باید بزرگتر از صفر باشد"
            operation_icon = 'log₁₀'
            show_num2 = False
        elif operation == 'factorial' and num1 is not None:
            result = math.factorial(int(num1)) if num1 >= 0 and num1.is_integer() else "خطا: عدد باید بزرگتر از صفر باشد"
            operation_icon = f'{num1}!'
            show_num2 = False
        elif operation == 'sin' and num1 is not None:
            result = round(math.sin(math.radians(num1)), 4)
            operation_icon = 'sin'
            show_num2 = False
        elif operation == 'cos' and num1 is not None:
            result = round(math.cos(math.radians(num1)), 4)
            operation_icon = 'cos'
            show_num2 = False
        elif operation == 'tan' and num1 is not None:
            cos_value = math.cos(math.radians(num1))
            result = round(math.tan(math.radians(num1)), 4) if cos_value != 0 else "خطا: تانژانت نا معلوم"
            operation_icon = 'tan'
            show_num2 = False

    return render(request, 'calculator.html', {
        'result': result,
        'operation_icon': operation_icon,
        'num1': num1,
        'num2': num2,
        'show_num2': show_num2
    })