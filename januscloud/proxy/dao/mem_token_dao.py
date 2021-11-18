# -*- coding: utf-8 -*-
import threading

from januscloud.proxy.dao.token_dao import TokenDao


class MemTokenDao(TokenDao):

    lock = threading.Lock()

    def __init__(self):
        self._tokens = {}

    def add(self, token):
        with self.lock:
            self._tokens[token] = token

    def remove(self, token):
        with self.lock:
            self._tokens.pop(token, None)

    def valid(self, token):
        with self.lock:
            return token is not None and token is not '' and self._tokens.get(token, None) is not None
