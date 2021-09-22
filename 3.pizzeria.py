#Totalizar las ventas en una pizzeria
#entrada:ventas de cada sede de la pizzeria, por cada  mes del año 2020
#salida: venta total en el año,promedio mensual de ventas, la sede  con la venta mas alta,
#su valor y mes

total=0.0
sedeAlta=0
ventaMasAlta=0.0
mesAlto=0
for mes in range(1,13):
  for sede in range(1,4):
             venta=float(input("Ingrese la venta en la sede " + str(sede)+
                               " en el mes  " + str(mes)+ ": "))
             total=total+venta
             if (venta>ventaMasAlta):
               ventaMasAlta=venta
               sedeAlta=sede
               mesAlto=mes
  print("\n")
print("El total de ventas en el año fue " , total)

print("La venta promedio  mensual es $" , total/12)
print("la sede que tuvo la mayor venta fue la " + str(sedeAlta) +
      " con una venta total de $" , str(ventaMasAlta)+ " en el mes "+ str(mesAlto))
