from django.shortcuts import render,HttpResponse
from django.core.urlresolvers import reverse,reverse_lazy
from django.views.generic import CreateView, TemplateView
import matplotlib
matplotlib.use('Agg')


# Create your views here.
class index(TemplateView):
    template_name = 'index.html'
class herramienta(TemplateView):
    template_name = 'prueba.html'
class help(TemplateView):
    template_name = 'help.html'
class theory(TemplateView):
    template_name = 'theory.html'
class tool(TemplateView):
    template_name ='tool.html'


def graphic(request, funcion, iteraciones, lower_bound, upper_bound):
    
    import matplotlib.pyplot as plt, mpld3
    import matplotlib.figure as fg
    import matplotlib
    import numpy as np
    import mpld3
    from mpld3 import plugins, utils
    from matplotlib.patches import Polygon
    
    from pprint import pprint
    fig=fg.Figure(fig)
    
    fig, ax = plt.subplots(figsize=(11,6.5))
    # pprint(vars(fig))
    # print ('#########################################3')
    x = np.linspace(-10, 10, 1000)
    #fig.subplots_adjust(right=2,top=1.1)
    #fig.adjustable='box'
    #fig.figsize=(5,2)
    # print(type(fig))
    # fig.fg.Figure()
    # Ver atributos de un objeto
    # pprint(vars(fig))
    # ax.legend_ = 'Raffo'
    # fig.figurePatch.set_width(3)
    # fig.figurePatch.set_height(3)
    # fig._animated=True
    # print(fig._animated)
    #paso de la funcion a graficar
    y='x**3
    #iteraciones
    n=0
    #limite inferior
    a=-10.0
    #limite superior
    b=10.0
    
    #fig.Figure(figsize=1000)

    """rect=[1,1,1,1]
    fig.add_axes(rect)
    fig.add_axes(rect, frameon=False, facecolor='g')
    fig.add_axes(rect, polar=True)
    fig.add_axes(rect, projection='polar')
    fig.add_axes(ax)"""
    # Propiedades de la linea que es definida por la funcion
    ax.plot(x,y, lw=5, alpha=0.7)
    # Add grid to figure
    ax.grid(True, alpha=0.3)
    
    #ax.set_ylim(-1.2, 1.0)
    #ax.text(5, -1.1, "Here are some curves", size=18)
    
    # Dibujar area bajo la curva
    ix = np.linspace(a, b)
    iy = ix
    verts = [(a, 0)] + list(zip(x, y)) + [(b, 0)]
    poly = Polygon(verts, facecolor='0.9', edgecolor='0.5')
    ax.add_patch(poly)

    


    # For transform it to HTML
    g = mpld3.fig_to_html(fig)
    return HttpResponse(g)
    
    
#Definimos la funcion trapecio
#@ n: numero de x
#@ a y b los intervalos de la integral
#@ f: La funcion a integrar
def trapecio(n, a, b, f):
    #calculamos h
    h = (b - a) / n
    #Inicializamos nuestra varible donde se almacenara las sumas
    x=a
    rest=0.0
    #hacemos un ciclo para ir sumando las areas
    for i in range(0, n):
        suma = 0.0
        suma = f(x)
        x+=h
        suma += f(x)
        rest += (suma / 2)* h
           
    #Retornamos el resultado
    return (rest)

#Definimos la funcion simpson
#@ n: numero de x
#@ a y b los intervalos de la integral
#@ f: La funcion a integrar
def simpson(n, a, b, f):
    #calculamos h
    h = (b - a) / n
    #Inicializamos nuestra varible donde se almacenara las sumas
    x=a
    rest=0.0
    #hacemos un ciclo para ir sumando las areas
    for i in range(0, n):
        suma = 0.0
        if(i % 2 == 0):
            suma = f(x)
            x+=h
            suma += 4 * f(x)
            x+=h
            suma += f(x)
            rest += (suma / 3)* h
        #en caso contrario no calculamos
        else:
            True    
    #Retornamos el resultado
    return (rest)

#Definimos la funcion romberg
#@ a y b los intervalos de la integral
#@ f: La funcion a integrar
def romberg(f, a, b, eps = 1E-8):
    """Approximate the definite integral of f from a to b by Romberg's method.
    eps is the desired accuracy."""
    R = [[0.5 * (b - a) * (f(a) + f(b))]]  # R[0][0]
    n = 1
    while True:
        h = float(b-a)/2**n
        R.append((n+1)*[None])  # Add an empty row.
        R[n][0] = 0.5*R[n-1][0] + h*sum(f(a+(2*k-1)*h) for k in range(1, 2**(n-1)+1)) # for proper limits
        for m in range(1, n+1):
            R[n][m] = R[n][m-1] + (R[n][m-1] - R[n-1][m-1]) / (4**m - 1)
        if abs(R[n][n-1] - R[n][n]) < eps:
            #print(R)
            return R[n][n]
        n += 1