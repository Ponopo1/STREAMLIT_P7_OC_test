import unittest
from unittest.mock import patch
import os

# Obtenir le répertoire du fichier actuel 
current_file_directory = os.path.dirname(__file__)

class TestApi(unittest.TestCase):
    API_URL = "https://api-projet7-open-bd8c05735794.herokuapp.com"

    # Test pour vérifier que la liste client est bien chargée
    @patch('requests.get') 
    def test_liste_client(self, mock_get):
        from Streamlit import liste_client  
        
        # Simuler une réponse avec statut 200
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = []  
        
        result = liste_client()  
        
        # Assertions to check if the behavior is correct
        self.assertTrue(result)  
        print("Liste de client correctement implémentée")

if __name__ == '__main__':
    unittest.main()
    

