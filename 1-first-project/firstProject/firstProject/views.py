import datetime
from django.http import HttpResponse


def saludo(request):
    webPage = """
    <html>
        <body>
            <h1>Hola mundo!</h1>
        </body>
    </html>
    """
    return HttpResponse(webPage)


def fecha(request):
    miFecha = datetime.datetime.now()
    texto2 = (
        """
    <html>
        <body>
        <h2>Fecha y hora actual: </h2>%s
        </body>
    </html>
"""
        % miFecha
    )
    return HttpResponse(texto2)


def calcEdad(request, edadActual, year):
    edadActual = 18
    periodo = year - 2025
    edadFutura = edadActual + periodo
    documento = "<html><body><h2>En el año %s tendrás %s años.</h2></body></html>" % (
        year,
        edadFutura,
    )
    return HttpResponse(documento)
