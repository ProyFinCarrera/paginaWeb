#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created by: Jairo Gonzalez Lemus alu0100813272@ull.edu.es
# File test_myfirebase.py:
#			1. Class for upload and download of data in the firebase account.
# -*- coding: utf-8 -*-
import unittest
import myfirebase


class TestPythonSoftware(unittest.TestCase):

	def test_retorna_document_with_value_ecual(self):
		self.assertEqual('{}', myfirebase.searchEqual(3))

    def test_should_return_python_when_number_is_3(self):
        self.assertEqual('Python', python_diario.get_string(3))
 
    if __name__ == '__main__': 
        unittest.main()
