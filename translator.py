from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

class TranslatorService:

    def __init__(self):
        authenticator = IAMAuthenticator('wN9TDs4ZktlY0kfnA5C-OiaDn1yY1ZgqXtIvhxqkDqwX')
        self.language_translator = LanguageTranslatorV3(
            version='2018-05-01',
            authenticator=authenticator)

        self.language_translator.set_service_url('https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/70dc9916-894d-4cc7-9df1-7887613a468f')
        

    def english_to_french(self,text):
        if len(text) == 0:
            return text
        translation = self.language_translator.translate(
            text, model_id='en-fr').get_result()
        translated_text = translation['translations'][0]['translation']    
        return translated_text        


    def english_to_german(self,text):
        if len(text) == 0:
            return text
        translation = self.language_translator.translate(
            text, model_id='en-de').get_result()
        translated_text = translation['translations'][0]['translation']    
        return translated_text        
