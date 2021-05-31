from googletrans import Translator
import googletrans

translator = Translator()

translated = translator.translate('xin chào', src='vi', dest='en')
 
print(translated)