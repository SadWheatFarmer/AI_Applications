################################################################################
"""
Author: John Smutny
Date: 05/27/2021
Des: Module that uses an IBM Watson Language Translator service to translate
        text from English to French or German.

NOTE: Be sure to install the 'ibm_watson' python package.
        From Terminal: pip install ibm_watson
"""
################################################################################


# IBM imports to use Language Translator IBM
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import LanguageTranslatorV3

# IBM API information
LANGUAGE_API_KEY = "--Login to IBM Watson for Key--"
LANGUAGE_API_URL1 = "https://api.us-south.language-translator.watson.cloud.ibm"
LANGUAGE_API_URL2 = ".com/instances/5f48ed0d-4238-4607-bdfe-307366425776"
LANGUAGE_API_URL = LANGUAGE_API_URL1 + LANGUAGE_API_URL2
VERSION_LT = '2018-05-01'


def english_to_french(en_text):
    """
    Translate text from English to French using IBM Watson API.
    :param en_text: English string to translate.
    :return: String of text in French.
    """

    # Initialize the IBM Watson API
    if LANGUAGE_API_KEY == "--Login to IBM Watson for Key--":
        print("[ERROR] Please fill in the IBM Watson API Key.")
    else:
        authenticator = IAMAuthenticator(LANGUAGE_API_KEY)
        language_translator = LanguageTranslatorV3(version=VERSION_LT,
                                                   authenticator=authenticator)
        language_translator.set_service_url(LANGUAGE_API_URL)

    # Prevent user from trying to translate null values.
    if en_text != "":
        # Translate text and output a formatted string
        translator_response = language_translator.translate(text=en_text,
                                                            model_id='en-fr')
        fr_translation = translator_response.get_result()['translations'][0][
            'translation']
    else:
        print("[ERROR] translator/english_to_french() - Cannot translate a "
              "NULL string.\n")
        fr_translation = "NULL"

    return fr_translation


def english_to_german(en_text):
    """
    Translate text from English to German using IBM Watson API.
    :param en_text: English string to translate.
    :return: String of text in German.
    """

    # Initialize the IBM Watson API
    if LANGUAGE_API_KEY == "--Login to IBM Watson for Key--":
        print("[ERROR] Please fill in the IBM Watson API Key.")
    else:
        authenticator = IAMAuthenticator(LANGUAGE_API_KEY)
        language_translator = LanguageTranslatorV3(version=VERSION_LT,
                                                   authenticator=authenticator)
        language_translator.set_service_url(LANGUAGE_API_URL)

    # Prevent user from trying to translate null values.
    if en_text != "":
        # Translate text and output a formatted string
        translator_response = language_translator.translate(text=en_text,
                                                            model_id='en-de')
        de_translation = translator_response.get_result()['translations'][0][
            'translation']
    else:
        print("[ERROR] translator/english_to_german() - Cannot translate a "
              "NULL string.")
        de_translation = "NULL"

    return de_translation
