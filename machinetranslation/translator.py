"""IBM Translation Service"""
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from constants import API_URL, API_KEY

class TranslatorService:
    """Translator Service Class"""

    def __init__(self):
        authenticator = IAMAuthenticator(API_KEY)
        self.language_translator = LanguageTranslatorV3(
            version='2018-05-01',
            authenticator=authenticator)

        self.language_translator.set_service_url(API_URL)

    def english_to_french(self,text):
        """English to French Translation Function"""
        if len(text) == 0:
            return text
        translation = self.language_translator.translate(text, model_id='en-fr').get_result()
        print(translation)
        translated_text = translation['translations'][0]['translation']
        return translated_text

    def english_to_german(self,text):
        """English to German Translation Function"""
        translation = dict()
        if len(text) == 0:
            return text
        translation = self.language_translator.translate(text, model_id='en-de').get_result()
        translated_text = translation['translations'][0]['translation']
        return translated_text
