from django.shortcuts import render,HttpResponse
from django.core.urlresolvers import reverse,reverse_lazy
from django.views.generic import CreateView, TemplateView
import matplotlib
matplotlib.use('Agg')
#import matplotlib.pyplot as plt
#from matplotlib.patches import Polygon


# Create your views here.
class index(TemplateView):
    template_name = 'index.html'
class herramienta(TemplateView):
    template_name = 'prueba.html'

def graphic(request):
    
    import matplotlib.pyplot as plt, mpld3
    import matplotlib
    import numpy as np
    import mpld3
    from mpld3 import plugins, utils

    fig, ax = plt.subplots()
    x = np.linspace(0, 10, 1000)
    for offset in np.linspace(0, 3, 7):
        ax.plot(x, 0.9 * np.sin(x - offset), lw=5, alpha=0.4)
    ax.set_ylim(-1.2, 1.0)
    ax.text(5, -1.1, "Here are some curves", size=18)
    ax.grid(color='lightgray', alpha=0.7)

   
    
    g = mpld3.fig_to_html(fig)
    return HttpResponse(g)