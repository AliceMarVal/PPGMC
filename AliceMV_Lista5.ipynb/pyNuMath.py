import math

# Bisseção
def bissecao (f,a,b,TOL,N0):
    inter = ""
    casas = abs(int(math.floor(math.log10(TOL)))) 
    for i in range(N0):
        c = (a + b)/2
        inter += f"Iteração {i + 1}: c = {c} -> f(c) = {f(c):.{casas}f}\n"
        if f(c) == 0 or (b - a)/2 < TOL:
            return c, inter, i + 1
        if f(a)*f(c) < 0:
            b = c
        else:
            a = c            
    return c, inter, N0

# Ponto Fixo 
def ponto_fixo(g, p0, TOL, N0):
    inter = ""
    casas = abs(int(f"{TOL:e}".split('e')[1])) 
    p = p0 
    for i in range(N0):
        p = g(p0)
        inter += f"Iteração {i + 1} -> ponto = {p:.{casas}f}\n"
        if abs(p - p0) < TOL:
            return p, inter, i + 1
        p0 = p
        
    return p, inter, N0

# Newton
def newton(f, df, p0, TOL, N0):
    inter = ""
    for i in range(N0):
        p = p0 - (f(p0) / df(p0))
        inter += f"Iteração {i+1}: p = {p:.6f}, f(p) = {f(p):.2e}\n"
        if abs(p - p0) < TOL:
            return p, inter, i + 1
        p0 = p
    return p, inter, N0

# Secante
def secante(f, p0, p1, TOL, N0):
    inter = ""
    q0 = f(p0)
    q1 = f(p1)
    for i in range(1, N0 + 1):
        p = p1 - q1 * (p1 - p0) / (q1 - q0)
        inter += f"Iteração {i}: p = {p:.6f}, f(p) = {f(p):.2e}\n"
        if abs(p - p1) < TOL:
            return p, inter, i 
        p0 = p1
        p1 = p
        q0 = q1
        q1 = f(p1)
    return p1, inter, N0

# Bisseção - Critérios de Parada
def bissecao_ex4 (f,a,b,TOL,N0, criterio):
    inter = ""
    casas = abs(int(math.floor(math.log10(TOL)))) 
    c_1 = 0
    for i in range(N0):
        c = (a + b)/2
        inter += f"Iteração {i + 1}: c = {c} -> f(c) = {f(c):.{casas}f}\n"
        if criterio == 1 and abs(c - c_1) < TOL:
            return c, inter, i +1
        elif criterio == 2 and (abs(c - c_1)) / abs(c) < TOL:
            return c, inter, i + 1
        elif criterio == 3 and abs(f(c)) < TOL:
            return c, inter, i + 1
        if f(a)*f(c) < 0:
            b = c
        else:
            a = c
        c_1 = c            
    return c, inter, N0

# Newton com Histórico de Aproximações
def newton_hist(f, df, p0, TOL, N0):
    aprox = []
    for i in range(N0):
        p = p0 - (f(p0) / df(p0))
        aprox.append(p)
        if abs(p - p0) < TOL:
            return p, aprox
        p0 = p
    return p, aprox

# Bisseção com Histórico de Aproximações
def bissecao_hist (f,a,b,TOL,N0):
    aprox = [] 
    for i in range(N0):
        c = (a + b)/2
        aprox.append(c)
        if f(c) == 0 or (b - a)/2 < TOL:
            return c, aprox
        if f(a)*f(c) < 0:
            b = c
        else:
            a = c            
    return c, aprox  

# Secante com Histórico de Aproximações
def secante_hist(f, p0, p1, TOL, N0):
    hist = []
    for i in range(1, N0 + 1):
        hist.append(p1)
        q0 = f(p0)
        q1 = f(p1)
        p = p1 - q1 * (p1 - p0) / (q1 - q0)
        if abs(p - p1) < TOL:
            return p, hist
        p0 = p1
        p1 = p
        q0 = q1
        q1 = f(p1)
    return p1, hist

# Newton com Critérios de Parada
def newton_ex13(f, df, p0, TOL, N0, criterio):
    inter = ""
    for i in range(N0):
        p = p0 - (f(p0) / df(p0))
        inter += f"Iteração {i+1}: p = {p:.6f}, f(p) = {f(p):.2e}\n"
        if criterio == 1 and abs(p - p0) < TOL:
            return p, inter, i + 1
        elif criterio == 2 and (abs(p - p0) / abs(p)) < TOL:
            return p, inter, i + 1
        elif criterio == 3 and abs(f(p)) < TOL:
            return p, inter, i + 1
        p0 = p
    return p, inter, N0

# Secante com Critérios de Parada
def secante_ex13(f, p0, p1, TOL, N0, criterio):
    inter = ""
    q0 = f(p0)
    q1 = f(p1)
    for i in range(1, N0 + 1):
        p = p1 - q1 * (p1 - p0) / (q1 - q0)
        inter += f"Iteração {i}: p = {p:.6f}, f(p) = {f(p):.2e}\n"
        if criterio == 1 and abs(p - p1) < TOL:
            return p, inter, i 
        elif criterio == 2 and (abs(p - p1) / abs(p)) < TOL:
            return p, inter, i 
        elif criterio == 3 and abs(f(p)) < TOL:
             return p, inter, i 
        p0 = p1
        p1 = p
        q0 = q1
        q1 = f(p1)
    return p1, inter, N0

