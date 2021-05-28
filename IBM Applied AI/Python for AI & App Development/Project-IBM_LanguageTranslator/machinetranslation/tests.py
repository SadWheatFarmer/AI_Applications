################################################################################
"""
Author: John Smutny
Date: 05/27/2021
Des: Unit Test for Language Translation module 'translator.py'.
        Google Translate was used to verify IBM operation. Unfortunately, there
        seems to be differences between the two services to translate
        words/phrases.
NOTE: Read the package's README.txt file for further examples.
"""
################################################################################

import unittest
from translator import english_to_french, english_to_german


class TestEnglishToFrench(unittest.TestCase):
    """
    Collection of tests for the translator/english_to_french() function.
    See README.txt for any differences between IBM and Google Translate.
    """
    def test_null(self):
        """
        Test to see if NULL values can be translated.
        Expected: IBM Watson will throw an exception if NULL is inputted.
                    This exception is avoided in the 'english_to_french()' fct.
        """
        en_text = ""
        fr_translated = english_to_french(en_text)
        correct_fr = "NULL"
        self.assertEqual(correct_fr, fr_translated)

    def test_hello(self):
        """
        Test to translate a single english word.
        """
        en_text = "Hello"
        fr_translated = english_to_french(en_text)
        correct_fr = "Bonjour"
        self.assertEqual(correct_fr, fr_translated)

    def test_multi_word(self):
        """
        Test to translate a single english statement.
        NOTE: Example of difference between IBM and Google Translate.
        """
        en_text = "Peace on Earth"
        fr_translated = english_to_french(en_text)
        correct_fr = "Paix sur Terre"
        self.assertEqual(correct_fr, fr_translated)

    def test_multi_line(self):
        """
        Test to translate two statements separated by a new line character.
        NOTE: See README.txt. IBM_Watson API will delete \n.
        NOTE: Example of difference between IBM and Google Translate.
        """
        en_text = "Blue square\nRed Circle"
        fr_translated = english_to_french(en_text)
        correct_fe = "Carré bleu\nCercle rouge"
        correct_fe_ibm_api = "Cercle rouge bleu carré"
        self.assertNotEqual(correct_fe, fr_translated)
        self.assertEqual(correct_fe_ibm_api, fr_translated)


class TestEnglishToGerman(unittest.TestCase):
    """
    Collection of tests for the translator/english_to_german() function
    See README.txt for any differences between IBM and Google Translate.
    """
    def test_null(self):
        """
        Test to see if NULL values can be translated.
        Expected: IBM Watson will throw an exception if NULL is inputted.
                    This exception is avoided in the 'english_to_german()' fct.
        """
        en_text = ""
        de_translated = english_to_german(en_text)
        correct_de = "NULL"
        self.assertEqual(correct_de, de_translated)

    def test_hello(self):
        """
        Test to translate a single english word.
        """
        en_text = "Hello"
        de_translated = english_to_german(en_text)
        correct_de = "Hallo"
        self.assertEqual(correct_de, de_translated)

    def test_multi_word(self):
        """
        Test to translate a single english statement.
        NOTE: Example of difference between IBM and Google Translate.
        """
        en_text = "Peace on Earth"
        de_translated = english_to_german(en_text)
        correct_de = "Frieden auf Erden"
        correct_de_ibm_api = "Frieden auf der Erde"
        self.assertNotEqual(correct_de, de_translated)
        self.assertEqual(correct_de_ibm_api, de_translated)

    def test_multi_line(self):
        """
        Test to translate two statements separated by a new line character.
        NOTE: See README.txt. IBM_Watson API will delete \n.
        NOTE: Example of difference between IBM and Google Translate.
        """
        en_text = "Blue square\nRed Circle"
        de_translated = english_to_german(en_text)
        correct_de = "blaues Quadrat\nroter Kreis"
        correct_de_ibm_api = "Blauer Quadrat Roter Kreis"
        self.assertNotEqual(correct_de, de_translated)
        self.assertEqual(correct_de_ibm_api, de_translated)


if __name__ == '__main__':
    unittest.main()
