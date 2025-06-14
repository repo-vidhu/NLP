from translate import Translator

def translate_text(text, dest_language):
    translator = Translator(to_lang=dest_language)
    translated = translator.translate(text)
    return translated


if __name__ == "__main__":
    text = input("Enter text to translate: ")
    dest_language = input("Enter destination language (e.g., 'es' for Spanish, 'fr' for French): ")
    translated_text = translate_text(text, dest_language)
    print(f"Translated Text: {translated_text}")

