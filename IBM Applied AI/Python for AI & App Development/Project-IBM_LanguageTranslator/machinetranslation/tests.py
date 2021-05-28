"""

"""

import unittest
from translator import english_to_french


class Test_en_to_fr(unittest.TestCase):
    def test_null(self):
        en_text = ""
        fr_translated = english_to_french(en_text)
        correct_fr = "NULL"
        self.assertEqual(correct_fr, fr_translated)

    def test_Hello(self):
        en_text = "Hello"
        fr_translated = english_to_french(en_text)
        correct_fr = "Bonjour"
        self.assertEqual(correct_fr, fr_translated)

    def test_MutliWord(self):
        en_text = "Peace on Earth"
        fr_translated = english_to_french(en_text)
        correct_fr_Google = "Paix sur la terre"
        correct_fr_IBM_API = "Paix sur terre"
        self.assertNotEqual(correct_fr_Google, fr_translated)
        self.assertEqual(correct_fr_IBM_API, fr_translated)

    def test_MutliLine(self):
        en_text = "Blue square\nRed Circle"
        fr_translated = english_to_french(en_text)
        correct_fr = "Carré bleu\nCercle rouge"
        correct_fr_Google = "Carré bleu Cercle rouge"
        correct_fr_IBM_API = "Cercle rouge Carré bleu"
        self.assertNotEqual(correct_fr, fr_translated)
        self.assertNotEqual(correct_fr_Google, fr_translated)
        self.assertEqual(correct_fr_IBM_API, fr_translated)


if __name__ == '__main__':
    unittest.main()
