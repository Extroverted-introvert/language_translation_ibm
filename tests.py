import unittest

from translator import TranslatorService

class TranslateTest(unittest.TestCase): 
    
    def test1_english_to_french(self):
        translator_service = TranslatorService()
        translated_text = translator_service.english_to_french('Hello')
 
        self.assertEqual(translated_text, "Bonjour")

    def test2_english_to_french(self):
        translator_service = TranslatorService()
        translated_text = translator_service.english_to_french('')
 
        self.assertEqual(translated_text, "")  

    def test3_english_to_french(self):
        translator_service = TranslatorService()
        translated_text = translator_service.english_to_french('This is a translate test')
 
        self.assertEqual(translated_text, "Il s'agit d'un test de traduction") 

    def test1_english_to_german(self):
        translator_service = TranslatorService()
        translated_text = translator_service.english_to_german('Hello')
 
        self.assertEqual(translated_text, "Hallo")

    def test2_english_to_german(self):
        translator_service = TranslatorService()
        translated_text = translator_service.english_to_german('')
 
        self.assertEqual(translated_text, "")  

    def test3_english_to_german(self):
        translator_service = TranslatorService()
        translated_text = translator_service.english_to_german('This is a translate test')
 
        self.assertEqual(translated_text, "Dies ist ein Übersetzungstest")          

unittest.main()        