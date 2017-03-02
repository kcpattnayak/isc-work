def calc_hypo(a, b):
    hypo = (a**2 + b**2)**0.5
    return hypo

def calc_hypo(a,b):
    if type(a) not in (int,float) or type(b) not in (int,float):
    print 'Bad argument'
    return False
    if a<=0 or b <=0:
       print 'Bad argument'
       return False
    hypo = (a**2+b**2)**0.5
    return hypo
