import os
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
from apps.liquidacion.models import Liquidacion  # Importa el modelo correcto
from django.utils import timezone

def link_callback(uri, rel):
    """
    Convert HTML URIs to absolute system paths so xhtml2pdf can access those resources
    """
    result = finders.find(uri)
    if result:
        if not isinstance(result, (list, tuple)):
            result = [result]
        result = list(os.path.realpath(path) for path in result)
        path = result[0]
    else:
        sUrl = settings.STATIC_URL  # Typicalmente /static/
        sRoot = settings.STATIC_ROOT  # Typicalmente /home/userX/project_static/
        mUrl = settings.MEDIA_URL  # Typicalmente /media/
        mRoot = settings.MEDIA_ROOT  # Typicalmente /home/userX/project_static/media/

        if uri.startswith(mUrl):
            path = os.path.join(mRoot, uri.replace(mUrl, ""))
        elif uri.startswith(sUrl):
            path = os.path.join(sRoot, uri.replace(sUrl, ""))
        else:
            return uri

    # Asegúrate de que el archivo exista
    if not os.path.isfile(path):
        raise Exception(
            'Las URI de medios deben comenzar con %s o %s' % (sUrl, mUrl)
        )
    return path

def reporte_liquidaciones(request):
    template_path = 'liquidacion/liquidacion_print_all.html'
    today = timezone.now()
    liquidaciones = Liquidacion.objects.all()  # Obtén las liquidaciones en lugar de compras
    context = {
        'obj': liquidaciones,
        'today': today,
        'request': request
    }
    response = HttpResponse(content_type='application/pdf')
    response['content-Disposition'] = 'inline; filename="todas_liquidaciones.pdf"'  # Corrige el nombre del archivo
    template = get_template(template_path)
    html = template.render(context)
    # Crea un PDF
    pisa_status = pisa.CreatePDF(html, dest=response, link_callback=link_callback)
    # Si hay errores, muestra una vista con el mensaje de error
    if pisa_status.err:
        return HttpResponse('Se produjeron errores al generar el informe PDF.')
    return response
