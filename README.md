# Proyecto1VisionArtificial
 En este repositorio se trabajara el primer proyecto de visión Artificial.
 
 
 
# Proceso 
==========
 
**Proyecto Base:**


La primera propuesta para el proyecto fue hacer un programa en el que pudiera calibrar sobre que objeto trackear, y usar el centroide de este para la posición del mouse. Se planteo de igual manera trabajar una interfaz gráfica con pyqt5 y Qt Designer.

Una vez terminado el proyecto base se testeo sobre el juego planteado "Getting Over It" pero nos dimos cuenta que los inputs del juego no funcionaban como esperamos, aqui decidimos pivotear a juegos propuestos anteriormente, ya para la implementación propia.


**Implementaciones:**


- ***2048***
 Se usa la posición del objeto con respecto a la camara para gestionar los inputs, Arriba,Abajo,Izquierda,Derecha.
 Branch: Implementación Felipe


- ***Friday Night Funkin***
 Se usa la posición del objeto con respecto a la camara para gestionar los inputs, Arriba,Abajo,Izquierda,Derecha. A diferencia del anterior la "zona muerta" es diferente y la manera que trata los inputs. 
 *Branch: FelipeV2*


- ***Jump King*** *Implementación Juan*
 Se usa la posición del rostro para presionar las techas (flecha izquierda, flecha derecha, flecha inferior), los tres movimientos básicos del juego son: moverse a la izquierda, moverse a la derecha y saltar hacia una de las dos direcciones.

 Al saltar hay que presionar una de las flechas para saltar hacia un lado, sino salta hacia arriba pero no avanza, por lo que se guarda la última posición en la que estuvo el rostro para que al saltar salte hacia esa dirección.

 Las zonas de dirección están bastante cerca del centro de la pantalla par que al jugador no le toque desplazarse demasiado para que el personaje se mueva, por lo que solo debe inclinarse hacia un lado. Y para el salto la persona debe agacharse para que su rostro esté en la parte inferior, y cuando suba su rostro el personaje salta, depende del tiempo que el jugador tiene su rostro en la parte inferior el personaje salta más o menos.

 Este tipo de control busca que el jugador se sienta como el propio personaje, ya que el personaje imita al jugador, si quiero que se desplace a un lado, el jugador debe de hacer lo mismo y si quiero que salte, el jugador debe agacharse y saltar. 
