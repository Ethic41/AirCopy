# Author: Dahir Muhammad Dahir
# Date: 15-June-2019 11:01 PM
# About: I will tell you later

import hashlib


class AirAuth:
    def __init__(self, username, random_key, ip_address):
        self.username = username
        self.random_key = random_key
        self.ip_address = ip_address

    def hash_key(self, key):
        pass

    def encrypt_message(self, message, key):
        pass

    def request_auth(self):
        pass

    def decrypt_message(self, ciphertext):
        pass

    def confirm_auth(self):
        pass

    def finalize(self, response):
        pass
