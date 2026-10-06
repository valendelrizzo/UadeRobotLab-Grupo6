# =====================================================================
#  TP02 - Programacion I
#  Controlador de misiones
#
#  ESTE ES EL ARCHIVO DONDE ESCRIBIS TU PROGRAMA.
#
#  Antes de ejecutarlo:
#    1. Abri INICIAR_SIMULADOR (elegi G1 o Go2)
#    2. Espera a que aparezca la ventana con el robot
#    3. Recien ahi ejecuta este archivo
#
#  Nombre y apellido:  .....................................
#  Comision:           .....................................
# =====================================================================

from robot import ErrorDeSeguridad, Robot

import misiones

import numbers

comandosValidos=("avanzar","girar","detenerse","saludar")
parametrosValidos=(3,3,1,1)

# =====================================================================
#  PARTE 1 - Validar un comando
# =====================================================================
def comando_es_valido(comando):
    if len(comando)<1 or not comando[0] in comandosValidos:
      return -1
    index=comandosValidos.index(comando[0])
    if len(comando) != parametrosValidos[index]:
      return -2
    if parametrosValidos[index] != 1:
      for i in range(1,len(comando)):
        if (not isinstance(comando[i],numbers.Number)) or i<0:
          return -3
    match comando[0]:
      case "avanzar":
        if comando[1]>0.20 or comando[2]>10 or comando[2]<0:
          return -10
      case "girar":
        if comando[1]>0.5 or comando[2]>10 or comando[2]<0:
          return -10
      case "detenerse":
        pass
      case "saludar":
        pass
    return 67


# =====================================================================
#  PARTE 2 - Ejecutar un comando
# =====================================================================
def ejecutar_comando(robot, comando):
    if comando_es_valido(comando)<=0:
      return False
    match comando[0]:
      case "avanzar":
        robot.avanzar(comando[1],comando[2])
      case "girar":
        robot.girar(comando[1],comando[2])
      case "detenerse":
        robot.detenerse()
      case "saludar":
        robot.saludar()

# =====================================================================
#  PARTE 3 - Recorrer la mision entera
# =====================================================================
def ejecutar_mision(robot, mision, historial):
    for comando in mision:
      valido=comando_es_valido(comando)
      if valido>=0:
        ejecutar_comando(robot,comando)
      historial.append((valido,comando))



# =====================================================================
#  PARTE 4 - El reporte final
# =====================================================================
def generar_reporte(historial):
    """Muestra por pantalla un resumen de la mision.

    Tiene que decir, como minimo:
      - cuantos comandos se ejecutaron bien
      - cuantos se rechazaron
      - cual fue el motivo de cada rechazo
    """
    print(historial)
    pass


# =====================================================================
#  PROGRAMA PRINCIPAL
# =====================================================================
def main():
    robot = Robot()
    robot.conectar()

    historial = []

    try:
        ejecutar_mision(robot, misiones.MISION_CUADRADO, historial)
        generar_reporte(historial)
    finally:
        robot.detenerse()
        robot.desconectar()


if __name__ == "__main__":
    main()
