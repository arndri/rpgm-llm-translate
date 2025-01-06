import sys
from PyQt6.QtWidgets import (
    QApplication, 
    QMainWindow, 
    QPushButton, 
    QLabel, 
    QVBoxLayout, 
    QWidget,
    QFileDialog,
    QMessageBox
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

class RPGMTranslatorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.file_path = None

    def initUI(self):
        self.setWindowTitle('RPGM Translator')
        self.setFixedSize(500, 300)
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label = QLabel('RPGM Translator')
        title_label.setFont(QFont('Arial', 20, QFont.Weight.Bold))
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title_label)
        subtitle_label = QLabel('Japanese to English Translation Tool')
        subtitle_label.setFont(QFont('Arial', 12))
        subtitle_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(subtitle_label)
        layout.addSpacing(20)
        self.select_button = QPushButton('Select RPGM File')
        self.select_button.setFixedSize(200, 40)
        self.select_button.clicked.connect(self.select_file)
        layout.addWidget(self.select_button, alignment=Qt.AlignmentFlag.AlignCenter)

        self.file_label = QLabel('No file selected')
        self.file_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.file_label.setWordWrap(True)
        layout.addWidget(self.file_label)

        self.status_label = QLabel('')
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.status_label)

    def select_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select RPGM Executable",
            "",
            "Executable files (*.exe)"
        )
        
        if file_path:
            self.file_path = file_path
            filename = file_path.split('/')[-1]
            self.file_label.setText(f'Selected file: {filename}')
            self.status_label.setText('File loaded successfully!')
            self.status_label.setStyleSheet('color: green')
            

            QMessageBox.information(
                self,
                "File Path",
                f"Full path:\n{file_path}"
            )
        else:
            self.status_label.setText('No file selected')
            self.status_label.setStyleSheet('color: red')

def main():
    app = QApplication(sys.argv)
    window = RPGMTranslatorApp()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()