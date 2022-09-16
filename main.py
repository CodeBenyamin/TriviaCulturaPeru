BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

import random
import time

iniciar_trivia = True
intentos = 0


puntaje = random.randint(0,5)

iniciar_trivia = True
intentos = 0

while iniciar_trivia == True:
 puntaje = 0
 puntaje = random.randint(0,5)
 intentos += 1

 print(BLUE + "\n Bienvenido a mi trivia sobre cultura general de Perú." + RESET)
 time.sleep(1)

 print(GREEN + "Pondremos a prueba tus conocimientos \n" + RESET)
 time.sleep(1)
 print("Tu suerte decidio obsequiarte", puntaje, "puntos")
 time.sleep(1)

 print(GREEN+"\nIntento número:",intentos,""+RESET)
 input("Presiona Enter para continuar\n")

 nombre = input(RED + "Ingrese tu nombre: " + RESET)
 time.sleep(1)

 print(CYAN + "\n Hola", nombre,"responde las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Enter' para enviar tu respuesta:\n"+ RESET)

 time.sleep(1)
 print("Estas preparado?")
 time.sleep(3)
 print("\nComenzamos en...")
 for x in range(3, 0, -1):
   print(x)
   time.sleep(1)
   
#pregunta 01
 print(MAGENTA + "\n1) Quién extendio el Imperio de los Incas. \n")
 time.sleep(2)
 print("a) Manco Cápac")
 time.sleep(1)
 print("b) Sinchi Roca")
 time.sleep(1)
 print("c) Inca Roca")
 time.sleep(1)
 print("d) Pachacútec")
 time.sleep(1)

 respuesta_1 = input("\n Tu respuesta: "+RESET)
 time.sleep(2)

 while respuesta_1 not in ("a", "b", "c", "d"):
    respuesta_1 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")

 if respuesta_1 == "a":
   puntaje -= 10
   print("Incorrecto", nombre, ":Manco Cápac no fundó el Imperio de los Incas"+ RESET)
   time.sleep(1)
   print("Has perdido puntos. Tienes", puntaje, "puntos.")
   time.sleep(1)
 elif respuesta_1 == "b":
   puntaje -= 10
   print("Incorrecto", nombre, "Sinchi Roca no fundó el Imperio de los Incas" + RESET)
   time.sleep(1)
   print("Has perdido puntos. Tienes", puntaje, "puntos.")
   time.sleep(1)
 elif respuesta_1 == "c":
   puntaje -= 10
   print("Incorrecto", nombre, "Inca Roca no fundó el Imperio de los Incas" + RESET)
   time.sleep(1)
   print("Has perdido puntos. Tienes", puntaje, "puntos.")
   time.sleep(1)
 else:
   print(YELLOW+"Respuesta Correcta", nombre, "¡Muy bien!" + RESET)
   time.sleep(1)
   print(CYAN+"!Recibes puntos¡"+RESET)
   time.sleep(1)
   puntaje += random.randint(10,15)
   print(GREEN+"Tienes",puntaje,"puntos. "+RESET)

 time.sleep(3)
#pregunta 02
 print(MAGENTA+"\n2) Sitio arqueológico del Perú relacionado con el origen de la civilización.\n")
 time.sleep(2)
 print("a) Machu Picchu")
 time.sleep(1)
 print("b) Sipán")
 time.sleep(1)
 print("c) Caral")
 time.sleep(1)
 print("d) Tunanmarca")
 time.sleep(1)

 respuesta_2 = input("\n Tu respuesta: ")
 time.sleep(2)

 while respuesta_2 not in ("a", "b", "c", "d"):
    respuesta_2 = input(
        "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")

 if respuesta_2 == "a":
    puntaje = puntaje - 10
    print("Incorrecto", nombre, "no es Machu Picchu"+RESET)
    time.sleep(1)
    print("Has perdido puntos. Tienes", puntaje, "puntos.")
    time.sleep(1)
 elif respuesta_2 == "b":
    puntaje = puntaje - 10
    print("Incorrecto", nombre, "no es Sipán"+RESET)
    time.sleep(1)
    print("Has perdido puntos. Tienes", puntaje, "puntos.")
    time.sleep(1)
 elif respuesta_2 == "d":
    puntaje -= 10
    print("Incorrect", nombre, "no es Tunanmarca"+RESET)
    time.sleep(1)
    print("Has perdido puntos. Tienes", puntaje, "puntos.")
    time.sleep(1)
 else:
    puntaje = puntaje + 10
    print(YELLOW+"Respuesta Correcta", nombre, "¡Muy bien!"+RESET)
    time.sleep(1)
    print(CYAN+"Recibes puntos"+RESET)
    time.sleep(1)
    puntaje += random.randint(10,15)
    print(GREEN+"Tienes",puntaje,"puntos. "+RESET)
    
 time.sleep(3)
#pregunta 03
 print(MAGENTA+"\n 3) En la batalla de Ayacucho, el ejército patriota estuvo al mando de: \n")
 time.sleep(2)
 print("a) Simón Bolívar")
 time.sleep(1)
 print("b) Agustín Gamarra")
 time.sleep(1)
 print("c) Antonio José de Sucre")
 time.sleep(1)
 print("d) José de San Martín")
 time.sleep(1)

 respuesta_3 = input("\n Tu respuesta: ")

 while respuesta_3 not in ("a", "b", "c", "d"):
    respuesta_3 = input(
        "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")

 if respuesta_3 == "a":
   puntaje = puntaje - 10
   print("Incorrecto", nombre, "no es Simón Bolívar"+RESET)
   time.sleep(1)
   print("Has perdido puntos. Tienes", puntaje, "puntos.")
 elif respuesta_3 == "b":
   puntaje = puntaje - 10
   print("Incorrecto", nombre, "no es Agustín Gamarra"+RESET)
   time.sleep(1)
   print("Has perdido puntos. Tienes", puntaje, "puntos.")
 elif respuesta_3 == "d":
   puntaje -= 10
   print("Incorrecto", nombre, "no es José de San Martín"+RESET)
   time.sleep(1)
   print("Has perdido puntos. Tienes", puntaje, "puntos.")
 else:
   puntaje += random.randint(10,15)
   print(YELLOW+"Respuesta Correcta", nombre, "¡Muy bien!"+RESET)
   time.sleep(1)
   print(CYAN+"Recibes puntos"+RESET)
   time.sleep(1)
   puntaje += random.randint(10,15)
   print(GREEN+"Tienes",puntaje,"puntos. "+RESET)

 time.sleep(3)
#pregunta 04
 print(MAGENTA+"\n 4) La Ciudad Sagrada de Caral se ubica cerca de la ciudad de ..., en la región Lima.\n ")
 time.sleep(2)
 print("a) Supe")
 time.sleep(1)
 print("b) Cañete")
 time.sleep(1)
 print("c) Chancay")
 time.sleep(1)
 print("d) Huarochirí")
 time.sleep(1)

 respuesta_4 = input("\n Tu respuesta: ")

 while respuesta_4 not in ("a","b","c","d"):
    respuesta_4 = input("Debes ingresar a, b, c o d. Ingresa nuevamente tu respuesta: ")

 if respuesta_4 == "b":
    puntaje -= random.randint(10,15)
    print("Incorrecto", nombre, "no es Cañete"+RESET)
    time.sleep(1)
    print("Has perdido puntos. Tienes", puntaje,"puntos." )
 elif respuesta_4 == "c":
    puntaje -= random.randint(10,15)
    print("Incorrecto", nombre, "no es Chancay"+RESET)
    time.sleep(1)
    print("Has perdido puntos. Tienes", puntaje,"puntos")
 elif respuesta_4 == "d":
    puntaje -= random.randint(10,15)
    print("Incorrecto", nombre, "no es Huarochirí")
    time.sleep(1)
    print("Has perdido puntos. Tienes", puntaje,"puntos"+RESET)
 else:
    puntaje += random.randint(10,15)
    print(YELLOW+"Respuesta Correcta", nombre, "¡Muy bien!"+RESET)
    time.sleep(1)
    print(CYAN+"Recibes puntos"+RESET)
    time.sleep(1)
    puntaje += random.randint(10,15)
    print(GREEN+"Tienes",puntaje,"puntos. "+RESET)
   
 time.sleep(3)
   #Pregunta 05
 print(MAGENTA+"\n5) Son culturas que se desarrollaron en la región La Libertad.\n")
 time.sleep(2)
 print("a) Chavín y Vicus")
 time.sleep(1)
 print("b) Mochica y Chimú")
 time.sleep(1)
 print("c) Chimú y Nasca")
 time.sleep(1)
 print("d) Mochica y Vicus")
 time.sleep(1)

 respuesta_5 = input("\n Tu respuesta: ")

 while respuesta_5 not in ("a","b","c","d"):
    respuesta_5 = input("Debes ingresar a, b, c o d. Ingresa nuevamente tu respuesta: ")

 if respuesta_5 == "a":
    puntaje -= random.randint(10,15)
    print("Incorrecto", nombre, ": no es Chavín y Vicus"+RESET)
    time.sleep(1)
    print("Has perdido puntos. Tienes", puntaje,"puntos." )
 elif respuesta_5 == "c":
    puntaje -= random.randint(10,15)
    print("Incorrecto", nombre, "no es Chimú y Nasca"+RESET)
    time.sleep(1)
    print("Has perdido puntos. Tienes", puntaje,"puntos")
 elif respuesta_5 == "d":
    puntaje /= 2
    print("Lo siento, ", nombre, "pero has elegido la respuesta incorrecta, Esto perjudica tus puntos ya que se dividira a la mitad tus puntos."+RESET)
    time.sleep(1)
    print("Has perdido puntos. Tienes", puntaje,"puntos"+RESET)
 else:
    puntaje *= 2
    print(YELLOW+"Respuesta Correcta", nombre, "¡Wow, me sorprendes!... ¡duplicare tu resultado!"+RESET)
    time.sleep(1)
    print(CYAN+"Recibes puntos"+RESET)
    time.sleep(1)
    puntaje += random.randint(10,15)
    print(GREEN+"Tienes",puntaje,"puntos. "+RESET)
  
 #pregunta 06
 print(MAGENTA+"\n 6) Año que se proclamo la independencia de Perú en la Plaza de Armas de Lima."+RESET)
 fechaindependencia = input("\n Tu respuesta es: ")
 time.sleep(2)
 if fechaindependencia == "1821":
   print(YELLOW+"¡Has acertado!"+RESET)
   puntaje +=20
 else:
   print(RED+"Lo siento, pero no acertaste, suerte para la proxima."+RESET)

 time.sleep(2)
  
#final de trivia
 print(BLUE+"\nGracias", nombre, "por jugar mi trivia"+RESET)
 time.sleep(3)

 print("\nCalculando...")
 for x in range(5, 0, -1):
   print(x)
   time.sleep(1)

 time.sleep(2)
 print(YELLOW+"\n¡Has logrado conseguir", puntaje, "puntos!."+RESET)

 print("\n¿Deseas intentar la trivia nuevamente?")
 repetir_trivia = input("Ingresa 'si' para repetir, o cualquier tecla para finalizar: ").lower()

 if repetir_trivia != "si":

   print("\nEspero" ,nombre, "que lo hayas pasado bien, hasta pronto!")
   iniciar_trivia = False
   puntaje = 0

 if iniciar_trivia == False:
   input("Gracias")
