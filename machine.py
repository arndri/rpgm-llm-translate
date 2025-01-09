from transformers import pipeline
from bs4 import BeautifulSoup
import os

class TranslationMachine:
    def __init__(self):
        self.translator = pipeline('translation', model='Mitsua/elan-mt-bt-ja-en')

    def translate_text(self, text):
        translation = self.translator(text)
        return translation[0]['translation_text']

    def process_html_file(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            soup = BeautifulSoup(file.read(), 'html.parser')
        
        original_texts = []
        for row in soup.find_all('tr')[1:]:
            text = row.find('td').text.strip()
            if text:
                original_texts.append(text)
        
        translations = [self.translate_text(text) for text in original_texts]
        
        rows = soup.find_all('tr')[1:]
        for row, translation in zip(rows, translations):
            cells = row.find_all('td')
            if len(cells) > 1:
                cells[1].string = translation
        
        output_path = os.path.splitext(file_path)[0] + '_translated.html'
        with open(output_path, 'w', encoding='utf-8') as file:
            file.write(str(soup))
        
        return output_path

def connect_to_ui(ui_instance):
    translator = TranslationMachine()
    
    def handle_translation():
        if ui_instance.file_path:
            try:
                output_path = translator.process_html_file(ui_instance.file_path)
                ui_instance.status_label.setText(f'Translation completed! Saved to: {output_path}')
                ui_instance.status_label.setStyleSheet('color: green')
            except Exception as e:
                ui_instance.status_label.setText(f'Error during translation: {str(e)}')
                ui_instance.status_label.setStyleSheet('color: red')
    
    # Connect translation handler to the translate button
    ui_instance.translate_button.clicked.connect(handle_translation)