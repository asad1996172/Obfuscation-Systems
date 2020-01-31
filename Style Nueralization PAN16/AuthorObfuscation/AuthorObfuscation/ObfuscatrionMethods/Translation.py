from mstranslator import Translator
from enum import Enum

class Translation:
    """Translation"""

    def translate(self, textToTranslate, languageList):
        if type(textToTranslate) is not str:
            raise ValueError("The argument textToTranslate must be string")
        #to save our translation limit the api calls are commented. uncoment to enable translation
        translator = Translator('GeorgiKaradjov', 'Y2c414NBMQlVgVPZK7vmFT7WZ/DJ4sKRYsTxG9NAXlQ=')
        tempTranslation = textToTranslate
        languageFrom = Language.English
        for language in languageList:
            if issubclass(type(language), Language):
                tempTranslation = translator.translate(tempTranslation, lang_from = languageFrom.value, lang_to = language.value)
                languageFrom = language
            else:
                raise ValueError("You must pass only valid values from Languages enum")

        tempTranslation = translator.translate(tempTranslation, lang_from = languageFrom.value, lang_to = Language.English.value)
        return tempTranslation

class Language(Enum):
    English = 'en'
    Bulgarian = 'bg'
    Croatian = 'hr'
    Czech = 'cs'
    Danish = 'da'
    Dutch = 'nl'
    Estonian = 'et'
    Finnish = 'fi'
    German = 'de'
    Greek = 'el'
    Russian = 'ru'
    Hindi = 'hi'
    Hungarian = 'hu'
    Indonesian = 'id'
    Italian = 'it'
    Japanese = 'ja'
    Swahili = 'sw'
    Klingon = 'twh' #live long and prosper
    Korean = 'ko'
    Latvian = 'lv'
    Norwegian = 'no'
    Polish = 'pl'
    Spanish = 'es'
    Swedish = 'sv'
    Turkish = 'tr'
    Ukrainian = 'uk'