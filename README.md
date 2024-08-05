# Mi Movistar

Sistema Integral de registro y seguimiento para una empresa telefónica.

# Índice

1. [Estado del Proyecto](#id1)
2. [Descripción del Proyecto](#id2)
3. [Tecnologías Utilizadas](#id3)
4. [Estructura del proyecto](#id4)
5. [Características](#id5)
6. [Diseño](#id6)
7. [Instrucciones](#id7)
8. [Personas Desarrolladoras del Proyecto](#id8)

# Estado del proyecto<a name="id1"></a>

Finalizado

# Descripción del Proyecto<a name="id2"></a>

* Este sistema permite realizar operaciones CRUD para crear, leer, actualizar y eliminar perfiles de usuarios.

* Permite el seguimiento del historial de usuarios

* Personalización de Servicios: Análisis de patrones de comportamiento de los usuarios para adaptar la oferta de servicios a las necesidades individuales.

- **Gestión de la Fidelización de Clientes** : 

-Identificación y seguimiento de clientes leales basados en la duración de su relación con la empresa.

-Integración con el módulo de bonificaciones para ofrecer recompensas especiales a los clientes más fieles.

# Tecnologías utilizadas<a name="id3"></a>

* Python

# Estructura del proyecto<a name="id4"></a>

![alt text](image.png)

# Características<a name="id5"></a>

Archivos Fundamentales:

**movistar.py**: Este archivo es el corazón del sistema. Contiene el código que maneja la parte lógica del programa, es fundamental para que funcione el sistema.

**categoriasUsuarios.json**: Aquí se guarda la información de los clientes de acuerdo a su categoría, que pueden ser nuevos clientes, clientes regulares o clientes leales.

**registro.json**: Aquí se guarda la información de cada cliente, dada por ellos mismos al momento del registro a la plataforma.

**servicios.json**: Aquí se guarda la información de cada servicio (características y precio) que ofrece la empresa. Además, cada servicio ofrece la información de los clientes que lo han adquirido.

# Diseño<a name="id6"></a>

* Solo puede ser visto y usado en consola

# Instrucciones<a name="id7"></a>

1. Clonar el repositorio
~~~
https://github.com/JesusBustamante/Filtro_python_BustamanteJesus.git
~~~

2. Si es clonado en Visual Studio Code, descargue la extensión de Python.

3. También descargue python desde un navegador web o la microsoft store.

3. Ejecuta el programa en la terminal de GitBash de la siguiente forma: 
~~~ 
python movistar.py 
~~~

# Personas Desarrolladoras del Proyecto<a name="id8"></a>
