import requests


class DictionaryAPI:
    def __init__(self, base_url):
        self.base_url = base_url

    def search_word(self, word):
        url = f"{self.base_url}/words?search={word}"
        response = requests.get(url)
        print(response, url, 5995)
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

    def get_word_by_id(self, word_id):
        url = f"{self.base_url}/words?id={word_id}"
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code}")
            return None
