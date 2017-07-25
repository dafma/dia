from django.shortcuts import render
from django.db import connection

# Create your views here.


def cabecera(request):
    sql = """Select ID, Agente,Referencia, DATEPART(MONTH,FechaRequerida) AS Mes, DATEPART(WEEK,  FechaRequerida) as SemanaDelYear,
       DATEPART(WEEK,  FechaRequerida) +7 as SemanaMasSiete,  MovID from Compra
        where Estatus='PENDIENTE' and Mov='PEDIDO'  and FechaEmision > DATEADD(WEEK, -7, GETDATE()) ORDER BY  SemanaDelYear ,Agente"""
    cursor = connection.cursor()
    cursor.execute(sql)
    todo = cursor.fetchall()

    sql = """ Select ID, Agente,Referencia,convert(VARCHAR(10),FechaRequerida +49, 102) as FechaEnqueDebiaLlegar, DATEPART(MONTH,FechaRequerida) AS Mes, DATEPART(WEEK,  FechaRequerida) as SemanaDelYear,
       DATEPART(WEEK,  FechaRequerida) +7 as SemanaMasSiete,  MovID from Compra
        where Estatus='PENDIENTE' and Mov='PEDIDO'  and FechaEmision < DATEADD(WEEK, -7, GETDATE()) ORDER BY  SemanaDelYear ,Agente"""
    cursor = connection.cursor()
    cursor.execute(sql)
    retrasos = cursor.fetchall()
    context={
        "todo":todo,
        "retrasos":retrasos,
    }
    return render(request, 'cabecerapanel1.html', context)

def detallecabecera(request, ID):
    sql = ("""Select Agente,Referencia,MovID, Moneda,Proveedor,Vencimiento,Importe, DATEPART(MONTH,FechaRequerida) AS Mes, DATEPART(WEEK,  FechaRequerida) as SemanaDelYear,
           DATEPART(WEEK,  FechaRequerida) +7 as SemanaMasSiete,  MovID from Compra where Mov='PEDIDO' and ID=' %s '""" % (ID))
    cursor = connection.cursor()
    cursor.execute(sql)
    referencia = cursor.fetchall()
    context = {
            'data':referencia,
        }
    return render(request, 'detalle_pedido.html', context)