import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QFormLayout, QLineEdit, QPushButton, QCheckBox
from PyQt6.QtGui import QIcon, QFont


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Set window title
        self.setWindowTitle("DynamicForm")

        # Set window icon
        self.setWindowIcon(QIcon('img/Qt_logo.png'))

        # Create the main form layout
        form_layout = QFormLayout()
        self.setLayout(form_layout)

        # Create and style the main label
        self.label_1 = QLabel("Please fill in the form so that we can contact you")
        self.label_1.setFont(QFont("Helvetica", 24))

        # Create input fields
        self.f_name = QLineEdit(self)
        self.l_name = QLineEdit(self)
        self.email = QLineEdit(self)
        self.phone_number = QLineEdit(self)

        # Create checkboxes for contact method
        self.ckBoxEmail = QCheckBox(self, text = "Email")
        self.ckBoxPhone = QCheckBox(self, text = "Phone")

        # Create a horizontal layout for the checkboxes
        self.h_widget = QWidget()
        layout_h = QHBoxLayout(self.h_widget)
        layout_h.addWidget(self.ckBoxEmail)
        layout_h.addWidget(self.ckBoxPhone)

        # Add widgets to the form layout
        form_layout.addRow(self.label_1)
        form_layout.addRow("First Name", self.f_name)
        form_layout.addRow("Last Name", self.l_name)
        form_layout.addRow("Email", self.email)
        form_layout.addRow("Phone Number", self.phone_number)
        form_layout.addRow("Please tell us your prefered contact method", self.h_widget)
        form_layout.addRow(QPushButton("Press me",
                                       clicked = self.button_pressed))

        # Show the window
        self.show()

    def button_pressed(self):
        # Determine preferred contact method
        contact = ""
        if self.ckBoxEmail.isChecked():
            contact = "Email"
        if self.ckBoxPhone.isChecked():
            contact = "Phone"
        
        # Update the label with a personalized message
        self.label_1.setText(f'Nice to meet you {self.f_name.text()} {self.l_name.text()} !, we will contact you ASAP, preferably on your {contact}.')

def main():
    # Create the application and main window
    app = QApplication([])
    mw = MainWindow()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()