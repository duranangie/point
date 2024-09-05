# Chat entre Clientes con Flask

Este proyecto proporciona una simple aplicación de chat basada en Flask que permite a dos clientes intercambiar mensajes automáticamente. El servidor gestiona la comunicación y envía mensajes del primer cliente al siguiente en la lista de clientes registrados.

## Requisitos

- Python 3.x
- `virtualenv` 

## Instalación

1. Clona este repositorio a tu máquina local:

   `git clone <URL_DEL_REPOSITORIO>`

   `cd <NOMBRE_DEL_REPOSITORIO>`

2. Crea un entorno virtual para evitar conflictos con otras instalaciones de paquetes:

   `python3 -m venv myenv`

   `source myenv/bin/activate`

3. Instala las dependencias necesarias:

   `pip install flask requests`

## Uso

Inicia el servidor Flask:

   `python servidor.py`

   El servidor se ejecutará en [http://127.0.0.0:5000](http://127.0.0.0:5000).

Inicia dos instancias del cliente en terminales separadas. Ejecuta el cliente en cada terminal:

   `python cliente.py`

   Cuando se te solicite, ingresa un ID único para cada cliente.

Intercambia mensajes:

   - En el Cliente 1, envía un mensaje. El Cliente 2 debería recibirlo automáticamente.
   - En el Cliente 2, puedes enviar un mensaje que el Cliente 1 recibirá automáticamente.

## Notas

- **Ngrok**: Si deseas exponer tu servidor Flask a la red pública usando Ngrok, asegúrate de tener Ngrok instalado y ejecuta el siguiente comando en una nueva terminal:

   `ngrok http 5000`

   Ngrok te proporcionará una URL pública que puedes usar para que los clientes se conecten a tu servidor Flask.

- **Código**: El código del servidor y del cliente se encuentra en los archivos `servidor.py` y `cliente.py`, respectivamente. Asegúrate de ajustar las configuraciones según sea necesario.

## Uso de virtualenv

Es recomendable usar un entorno virtual para evitar conflictos con otras instalaciones de paquetes. Para crear y activar un entorno virtual, usa los siguientes comandos:

   `python3 -m venv myenv`

   `source myenv/bin/activate`

Para desactivar el entorno virtual, simplemente ejecuta:

   `deactivate`

## Autor

Este proyecto fue creado por Angie Duran. Si tienes alguna pregunta o sugerencia, no dudes en contactarme.
