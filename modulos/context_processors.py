from .models import Venta

def ventas_recientes(request):
    # Devuelve las 5 ventas más recientes de tipo 'virtual'
    ventas_recientes = Venta.objects.filter(modalidadventa='virtual').order_by('-fechaventa')[:5]
    return {'ventas_recientes': ventas_recientes}




from .models import Venta
from datetime import datetime

def daily_frase_motivadora(request):
    frases = [
        "Cada día es una nueva oportunidad.",
        "El éxito está en tu constancia.",
        "La disciplina vence al talento.",
        "Hoy es el día para dar lo mejor de ti."
    ]
    dia_actual = datetime.now().timetuple().tm_yday
    frase_del_dia = frases[dia_actual % len(frases)]
    
    # Obtener las ventas recientes
    ventas_recientes = Venta.objects.filter(modalidadventa='virtual').order_by('-fechaventa')[:5]
    
    return {
        'frase_del_dia': frase_del_dia,
        'ventas_recientes': ventas_recientes,
    }



from django.contrib.auth.models import Group

def groups_context_processor(request):
    if request.user.is_authenticated:
        return {
            'is_cliente': request.user.groups.filter(name="Clientes").exists(),
            'is_jefe_produccion': request.user.groups.filter(name="Jefe de Producción").exists(),
        }
    return {}
