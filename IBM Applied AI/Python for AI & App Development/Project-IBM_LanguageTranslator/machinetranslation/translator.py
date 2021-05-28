"""
Be sure to install the 'ibm_watson' python package.
From Terminal: pip install ibm_watson
"""

# IBM imports to use Language Translator IBM
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import LanguageTranslatorV3

# Modules for language conversion
from pandas import json_normalize

# IBM API information
languageAPI_Key = "CzyI_s7p_YCQXJFjTFkOWiOLzfziH-t1HyzScVh41fcN"
languageAPI_URL = "https://api.us-south.language-translator.watson.cloud.ibm" \
                  ".com/instances/5f48ed0d-4238-4607-bdfe-307366425776 "
version_lt = '2018-05-01'


def english_to_french(en_text):
    """

    See this URL for IBM LanguageTranslator version information
    - https://cloud.ibm.com/apidocs/language-translator?code=python
    :return: 
    """
    authenticator = IAMAuthenticator(languageAPI_Key)
    language_translator = LanguageTranslatorV3(version=version_lt,
                                               authenticator=authenticator)
    language_translator.set_service_url(languageAPI_URL)

    # Prevent user from trying to translate null values.
    if en_text != None:
        translator_response = language_translator.translate(text=en_text,
                                                            model_id='en-fr')
        fr_translation = translator_response.get_result()['translations'][0][
            'translation']
    else:
        print("[ERROR] translator/english_to_french() - Cannot translate a "
              "NULL string.")
        fr_translation = "NULL"

    return fr_translation
