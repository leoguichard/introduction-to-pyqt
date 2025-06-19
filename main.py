import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QTextEdit, QVBoxLayout
from PyQt6.QtGui import QIcon


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Hello App')
        self.setWindowIcon(QIcon('img/Qt_logo.png'))
        self.resize(800,600) #width, height

        layout = QVBoxLayout()
        self.setLayout(layout)

        # widgets
        self.inputField = QLineEdit()
        button = QPushButton('&Enter your name above and click me', clicked=self.sayHello)
        #button.clicked.connect(self.sayHello()) #another way to connect a method to a click
        self.outputField = QTextEdit()

        
        layout.addWidget(self.inputField)
        layout.addWidget(button)
        layout.addWidget(self.outputField)

    def sayHello(self):
        inputText = self.inputField.text()
        self.outputField.setText(f'Hello {inputText}')
        

#app = QApplication([])
app = QApplication(sys.argv) # used to run with in command args
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

app.exec()

