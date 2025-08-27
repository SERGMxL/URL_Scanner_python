# url_scanner.py

from pysafebrowsing import SafeBrowsing

class UrlScanner:
    """
    Clase para escanear URLs utilizando la API de Google Safe Browsing.
    """
    def __init__(self, api_key):
        """
        Inicializa el escáner con la clave de la API.
        
        Args:
            api_key (str): Tu clave de la API de Google Safe Browsing.
        """
        if not api_key or api_key == "TU_API_KEY":
            raise ValueError("La clave de la API de Google Safe Browsing no es válida o no ha sido proporcionada.")
        self.sb = SafeBrowsing(api_key)

    def check_url(self, url):
        """
        Verifica una URL en busca de amenazas.
        
        Args:
            url (str): La URL que se va a verificar.
            
        Returns:
            str: Un mensaje indicando si el sitio es seguro o las amenazas encontradas.
        """
        try:
            response = self.sb.lookup_urls([url])
            if url in response and response[url].get('malicious'):
                threats = ', '.join(response[url].get('threats', []))
                return f"¡Peligro! Se encontraron las siguientes amenazas: {threats}"
            else:
                return "El sitio parece ser seguro."
        except Exception as e:
            return f"Ocurrió un error al contactar la API: {e}"