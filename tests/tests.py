# -*- coding: utf-8 -*-

import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from flask.ext.cors import CORSMiddleware

class CORSMiddlewareTest(unittest.TestCase):
	def test_is_valid_origin(self):
		cors = CORSMiddleware(None)
		self.assertTrue(cors.is_valid_origin('http://www.w3.org'))

	def test_is_valid_origin_crlf(self):
		cors = CORSMiddleware(None)
		self.assertFalse(cors.is_valid_origin('http://www.w3.org\r\n'))

	def test_is_valid_origin_encoded_crlf1(self):
		cors = CORSMiddleware(None)
		self.assertFalse(cors.is_valid_origin('http://www.w3.org%0d%0a'))

	def test_is_valid_origin_encoded_crlf2(self):
		cors = CORSMiddleware(None)
		self.assertFalse(cors.is_valid_origin('http://www.w3.org%0D%0A'))

	def test_is_valid_origin_encoded_crlf3(self):
		cors = CORSMiddleware(None)
		self.assertFalse(cors.is_valid_origin('http://www.w3.org%0%0d%0ad%0%0d%0aa'))

if __name__ == '__main__':
    unittest.main()