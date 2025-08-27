# URL Malware Scanner
Un sencillo analizador de URLs de escritorio con una interfaz gráfica de usuario (GUI) construida en Python. Esta herramienta utiliza la API de Google Safe Browsing para verificar si un sitio web está marcado como malicioso o contiene amenazas de seguridad como malware o phishing.

✨ Características Principales
Interfaz Gráfica Sencilla: Un diseño limpio y fácil de usar, ideal para usuarios no técnicos.

Verificación en Tiempo Real: Utiliza la API de Google Safe Browsing v4 para obtener información actualizada sobre amenazas.

Resultados Claros: Muestra si un sitio es seguro o peligroso, especificando el tipo de amenaza encontrada.

Código Modular: El proyecto está estructurado en clases y archivos separados (main.py, gui.py, url_scanner.py) para una mejor legibilidad y mantenimiento.

🛠️ Requisitos Previos
Para poder ejecutar este proyecto, necesitarás:

Python 3: Asegúrate de tener Python instalado. Puedes descargarlo desde python.org.

Biblioteca pysafebrowsing: La dependencia principal para interactuar con la API de Google.

Clave de API de Google Safe Browsing: Necesitarás credenciales para realizar consultas a la API.

🚀 Instalación y Configuración
Sigue estos pasos para poner en marcha la aplicación.

1. Clona el Repositorio
Bash

git clone https://github.com/SERGMxL/URL_Scanner_python.git
cd URL_Scanner_python
2. Instala las Dependencias
Instala la biblioteca pysafebrowsing usando pip.

Bash

pip install pysafebrowsing
3. Obtén tu Clave de API
Ve a la Consola de Google Cloud.

Crea un nuevo proyecto o selecciona uno existente.

Busca y habilita la "Web Risk API" (la sucesora de Safe Browsing API).

Ve a "Credenciales", haz clic en "Crear credenciales" y selecciona "Clave de API".

Copia tu clave de API generada.

4. Configura la Clave de API en el Proyecto
Abre el archivo main.py y busca la siguiente línea:

Python

API_KEY = "TU_API_KEY"
Reemplaza "TU_API_KEY" con la clave que obtuviste en el paso anterior.

▶️ Cómo Usar la Aplicación
Una vez que hayas configurado tu clave de API, ejecuta la aplicación desde tu terminal:

Bash

python main.py
Se abrirá una ventana donde podrás:

Pegar la URL que deseas verificar en el campo de texto.

Hacer clic en el botón "Verificar Sitio".

El resultado aparecerá debajo del botón, indicando si el sitio es seguro o si se encontraron amenazas.
