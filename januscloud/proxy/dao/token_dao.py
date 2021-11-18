# -*- coding: utf-8 -*-

class TokenDao(object):

    def add(self, token):
        """
        Adds the specified token as a valid token. After addition, valid must return true for this token.
        :param token: The token to add
        :return: None
        """
        pass

    def remove(self, token):
        """
        Removes the specified token from the valid tokens. After removal, valid must return false for this token.
        :param token: the token to remove
        :return: None
        """
        pass

    def valid(self, token):
        """
        Checks if the token is valid, and returns true if so.
        :param token: The token to check
        :return: true iff the token has been added before and is valid, else false
        """
        pass
