import requests


class DictionaryAPI:
    def __init__(self, base_url):
        self.base_url = base_url

    def search_word(self, word, language):
        url = f"{self.base_url}/words?search={word}&language={language}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code}")
            return None

    def search_translations(self, word, language):
        url = f"{self.base_url}/translations?search={word}&language={language}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code}")
            return None

    def add_word(self, word_data):
        url = f"{self.base_url}/words/"
        response = requests.post(url, json=word_data)
        if response.status_code == 201:
            return response.json()
        else:
            print(f"Error: {response.status_code}")
            return None

    def get_word_by_id(self, word_id, language):
        url = f"{self.base_url}/translations?id={word_id}&language={language}"
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code}")
            return None
