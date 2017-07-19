from django.shortcuts import render
from django.db import connection
import json
# Create your views here.


def panel1(request):

    sql = """Select Agente,Referencia, DATEPART(WEEK,  FechaRequerida) as SemanaDelYear,
    DATEPART(WEEK,  FechaRequerida) +7 as SemanaMasSiete,  MovID from Compra
     where Estatus='PENDIENTE' and Mov='PEDIDO' and FechaEmision > DATEADD(WEEK, -7, GETDATE()) ORDER BY Agente, SemanaDelYear"""
    cursor = connection.cursor()
    cursor.execute(sql)
    fechas = cursor.fetchall()

    sql = """Select DISTINCT DATEPART(WEEK,  FechaRequerida) as SemanaDelYear,DATEPART(WEEK,  FechaRequerida) +7 as SemanaMasSiete from Compra  where Estatus='PENDIENTE' and FechaEmision > DATEADD(mm, -1, GETDATE()) ORDER BY SemanaDelYear"""
    cursor = connection.cursor()
    cursor.execute(sql)
    barrasemanas = cursor.fetchall()



    #agentee
    sql = """Select Agente,Referencia, DATEPART(MONTH,FechaRequerida) AS Mes,DATEPART(WEEK,  FechaRequerida) as SemanaDelYear,
    DATEPART(WEEK,  FechaRequerida) +7 as SemanaMasSiete,  MovID from Compra
     where Estatus='PENDIENTE' and Mov='PEDIDO'  and FechaEmision > DATEADD(WEEK, -7, GETDATE()) AND Agente='C01' ORDER BY  SemanaDelYear"""
    cursor = connection.cursor()
    cursor.execute(sql)
    C01 = cursor.fetchall()

    sql = """Select Agente,Referencia, DATEPART(MONTH,FechaRequerida) AS Mes, DATEPART(WEEK,  FechaRequerida) as SemanaDelYear,
    DATEPART(WEEK,  FechaRequerida) +7 as SemanaMasSiete,  MovID from Compra
     where Estatus='PENDIENTE' and Mov='PEDIDO'  and FechaEmision > DATEADD(WEEK, -7, GETDATE()) AND Agente='C02' ORDER BY  SemanaDelYear"""
    cursor = connection.cursor()
    cursor.execute(sql)
    C02 = cursor.fetchall()

    sql = """Select Agente,Referencia, DATEPART(MONTH,FechaRequerida) AS Mes, DATEPART(WEEK,  FechaRequerida) as SemanaDelYear,
    DATEPART(WEEK,  FechaRequerida) +7 as SemanaMasSiete,  MovID from Compra
     where Estatus='PENDIENTE' and Mov='PEDIDO'  and FechaEmision > DATEADD(WEEK, -7, GETDATE()) AND Agente='C03' ORDER BY  SemanaDelYear"""
    cursor = connection.cursor()
    cursor.execute(sql)
    C03 = cursor.fetchall()
    context = {
        'fechas': fechas,
        'barrasemanas':barrasemanas,
        'C03':C03,
        'C02':C02,
        'C01':C01
    }

    return render(request, 'panel1.html', context)