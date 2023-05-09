class NumericalMethods():
    def __init__(self) -> None:
        pass
    
    def Bissection(equation,a:float,b:float,interations:int,error:float)->tuple:
        samesign=lambda x,y: x*y>0
        assert not samesign(equation(a),equation(b))
        FA=equation(a)
        table={
            'a':[],
            'b':[],
            'm':[],
            'f(a)':[],
            'f(b)':[],
            'f(m)':[],
            'f(a)-f(b)':[],
            '(a-b)/2':[]
        }
        for i in range(interations):
            m=(a+b)/2.
            table['a'].append(a)
            table['b'].append(b)
            table['m'].append(m)
            table['f(a)'].append(FA)
            table['f(b)'].append(equation(b))
            table['f(m)'].append(equation(m))
            table['f(a)-f(b)'].append(FA-equation(b))
            table['(a-b)/2'].append((a-b)/2.)
            FM=equation(m)
            if error is not None and abs(a-b)<error or FM==0:
                break
            if samesign(equation(a),equation(m)):
                a=m
                FA=FM
            else:
                b=m
                FB=FM
        
        return m, table
    