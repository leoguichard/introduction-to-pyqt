import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QFormLayout, QLineEdit, QPushButton, QCheckBox
from PyQt6.QtGui import QIcon, QFont
import os

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("DynamicForm")

        self.setWindowIcon(QIcon('img/Qt_logo.png'))


        form_layout = QFormLayout()
        self.setLayout(form_layout)

        # widgets
        self.label_1 = QLabel("Please fill in the form so that we can contact you")
        self.label_1.setFont(QFont("Helvetica", 24))

        self.f_name = QLineEdit(self)
        self.l_name = QLineEdit(self)
        self.email = QLineEdit(self)
        self.phone_number = QLineEdit(self)


        self.ckBoxEmail = QCheckBox(self, text = "Email")
        self.ckBoxPhone = QCheckBox(self, text = "Phone")

        self.h_widget = QWidget()
        layout_h = QHBoxLayout(self.h_widget)
        layout_h.addWidget(self.ckBoxEmail)
        layout_h.addWidget(self.ckBoxPhone)


        # add rows to app
        form_layout.addRow(self.label_1)
        form_layout.addRow("First Name",self.f_name)
        form_layout.addRow("Last Name",self.l_name)
        form_layout.addRow("Email",self.email)
        form_layout.addRow("Phone Number",self.phone_number)
        form_layout.addRow("Please tell us your prefered contact method", self.h_widget)
        form_layout.addRow(QPushButton("Press me",
                                       clicked = self.button_pressed))


        self.show()


    def button_pressed(self):
        contact = ""
        if self.ckBoxEmail.isChecked():
            contact = "Email"
        if self.ckBoxPhone.isChecked():
            contact = "Phone"
        
        self.label_1.setText(f'Nice to meet you {self.f_name.text()} {self.l_name.text()} !, we will contact you ASAP, preferably on your {contact}.')


def main():
    app = QApplication([])
    mw = MainWindow()
    sys.exit(app.exec())
    # print(os.path.isfile(os.path.abspath(os.path.join(os.getcwd(),"img/Qt_logo.png"))))

if __name__ == "__main__":
    main()