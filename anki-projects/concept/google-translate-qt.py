import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QTextEdit, QPushButton, QLabel
from googletrans import Translator

class TranslationApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Text Translation')
        self.setGeometry(100, 100, 400, 300)

        # Widgets
        self.text_input = QTextEdit()
        self.result_label = QLabel()

        self.translate_button = QPushButton('Translate', self)
        self.translate_button.clicked.connect(self.translate_text)

        self.copy_button = QPushButton('Copy', self)
        self.copy_button.clicked.connect(self.copy_text)

        self.paste_button = QPushButton('Paste', self)
        self.paste_button.clicked.connect(self.paste_text)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.text_input)
        layout.addWidget(self.result_label)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.translate_button)
        button_layout.addWidget(self.copy_button)
        button_layout.addWidget(self.paste_button)

        layout.addLayout(button_layout)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def translate_text(self):
        text_to_translate = self.text_input.toPlainText()
        translator = Translator()
        translated_text = translator.translate(text_to_translate, src='auto', dest='en')
        translated_text_with_line_breaks = self.add_line_breaks(translated_text.text)
        self.result_label.setText(translated_text_with_line_breaks)

    def add_line_breaks(self, text, max_line_length=40):
        words = text.split()
        lines = []
        current_line = ""
        for word in words:
            if len(current_line) + len(word) + 1 <= max_line_length:
                current_line += word + " "
            else:
                lines.append(current_line)
                current_line = word + " "
        if current_line:
            lines.append(current_line)
        return "\n".join(lines)

    def copy_text(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.text_input.toPlainText())

    def paste_text(self):
        clipboard = QApplication.clipboard()
        self.text_input.setPlainText(clipboard.text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TranslationApp()
    window.show()
    sys.exit(app.exec_())
