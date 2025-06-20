import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QTextEdit, QVBoxLayout
from PyQt6.QtGui import QIcon


class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        # Set window properties
        self.setWindowTitle('Hello App')
        self.setWindowIcon(QIcon('img/Qt_logo.png'))
        self.resize(800,600) #width, height

        # Create layout
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Create widgets
        self.inputField = QLineEdit()
        # Adding a returnPressed event
        self.inputField.returnPressed.connect(self.sayHello)
        self.button = QPushButton('Enter your name above and click me or press enter')
        # Connect the button to the method
        self.button.clicked.connect(self.sayHello)
        self.outputField = QTextEdit("")
        self.outputField.setReadOnly(True)

        # Add widgets to the layout
        layout.addWidget(self.inputField)
        layout.addWidget(self.button)
        layout.addWidget(self.outputField)

    def sayHello(self):
        inputText = self.inputField.text()
        self.outputField.setText(f'Hello {inputText}')


def main():
    #app = QApplication([])
    app = QApplication(sys.argv) # used to run with in command args
    
    # adding some css
    app.setStyleSheet('''
        QWidget {
            font-size: 25px             
        }
                    
        QPushButton{
            font-size: 20px
        }
    ''')

    window = MyApp()
    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()