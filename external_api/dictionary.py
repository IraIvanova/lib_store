import requests


class DictionaryAPI:
    def __init__(self, base_url):
        self.base_url = base_url

    def send_request(self, url):
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code}")
            return None

    def search_word(self, word, language):
        return self.send_request(f"{self.base_url}/words?search={word}&language={language}")

    def search_translations(self, word, language):
        return self.send_request(f"{self.base_url}/translations?search={word}&language={language}")

    def add_word(self, word_data):
        return self.send_request(f"{self.base_url}/words/")

    def get_word_by_id(self, word_id, language):
        return self.send_request(f"{self.base_url}/translations?id={word_id}&language={language}")

    def get_additional_info_for_word(self, word_id, language):
        return self.send_request(f"{self.base_url}/words?id={word_id}&language={language}")

    def get_book_list(self, search, language):
        return self.send_request(f"{self.base_url}?search={search}&language={language}")

    def get_book_by_id(self, book_id):
        return self.send_request(f"{self.base_url}/text/{book_id}")
