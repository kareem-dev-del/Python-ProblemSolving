def solve_linear(equation):
    
    #إزالة الفراغات
    equation = equation.replace(" ", "")

    #فصل طرفي المعادلة
    left, right = equation.split('=')
    #تحويل الطرف الثاني إلى رقم
    right = int(right)
    #إيجاد موقع x
    x_index = left.find('x')
    #ستخراج الرقم قبل x (a)
    a_str = left[:x_index]
    if a_str in ('', '+'):
        a = 1
    elif a_str == '-':
        a = -1
    else:
        a = int(a_str)
    #استخراج الباقي بعد x (b)
    b_str = left[x_index+1:]
    if b_str == '':
        b = 0
    else:
        b = int(b_str)

    x = (right - b) / a
    return x

equation = "2x - 10 = 0"
result = solve_linear(equation)
print(f"Equation: {equation}")
print(f"x = {result}")


