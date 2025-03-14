import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, \
    QPushButton, QMessageBox, QMenuBar, QMenu
from PyQt6.QtGui import QAction, QColor
from PyQt6.QtCore import Qt


class BMICalculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BMI Calculator")
        self.setGeometry(100, 100, 400, 400)  # Increased size to fit new elements

        self.init_ui()

    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Main layout
        layout = QVBoxLayout()

        # Weight input
        self.label_weight = QLabel("Enter your weight (kg):")
        self.label_weight.setStyleSheet("font-size: 16px; color: #333333;")
        self.input_weight = QLineEdit()
        self.input_weight.setPlaceholderText("e.g., 70")
        self.input_weight.setStyleSheet("font-size: 18px; padding: 10px;")

        # Height input
        self.label_height = QLabel("Enter your height (cm):")
        self.label_height.setStyleSheet("font-size: 16px; color: #333333;")
        self.input_height = QLineEdit()
        self.input_height.setPlaceholderText("e.g., 170")
        self.input_height.setStyleSheet("font-size: 18px; padding: 10px;")

        # Calculate button
        self.calculate_button = QPushButton("Calculate BMI")
        self.calculate_button.setStyleSheet("""
            background-color: #4CAF50;
            color: white;
            font-size: 18px;
            padding: 10px;
            border-radius: 5px;
        """)
        self.calculate_button.clicked.connect(self.calculate_bmi)

        # BMI status description
        self.status_label = QLabel("")
        self.status_label.setStyleSheet("font-size: 16px; color: #333333;")

        # Adding widgets to the layout
        layout.addWidget(self.label_weight)
        layout.addWidget(self.input_weight)
        layout.addWidget(self.label_height)
        layout.addWidget(self.input_height)
        layout.addWidget(self.calculate_button)
        layout.addWidget(self.status_label)

        # Create the BMI category cells
        self.create_bmi_categories(layout)

        central_widget.setLayout(layout)

        self.create_menu()

    def create_bmi_categories(self, layout):
        # Horizontal layout for the BMI category cells
        category_layout = QHBoxLayout()

        # Create each category cell with different color
        self.create_bmi_category_cell(category_layout, "Underweight <18.5", "#FF6347")  # Red
        self.create_bmi_category_cell(category_layout, "Normal 18.5-25", "#32CD32")  # Green
        self.create_bmi_category_cell(category_layout, "Overweight 25-30", "#FFA500")  # Orange
        self.create_bmi_category_cell(category_layout, "Obese >30", "#FF0000")  # Dark Red

        layout.addLayout(category_layout)

    def create_bmi_category_cell(self, layout, text, color):
        label = QLabel(text)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet(
            f"background-color: {color}; color: white; font-size: 14px; padding: 10px; margin: 5px; border-radius: 5px;")
        layout.addWidget(label)

    def create_menu(self):
        menu_bar = QMenuBar(self)
        self.setMenuBar(menu_bar)

        file_menu = QMenu("File", self)
        help_menu = QMenu("Help", self)

        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)

        clear_action = QAction("Clear", self)
        clear_action.triggered.connect(self.clear_inputs)

        help_action = QAction("How to Use", self)
        help_action.triggered.connect(self.show_help)

        file_menu.addAction(exit_action)
        file_menu.addAction(clear_action)
        help_menu.addAction(help_action)

        menu_bar.addMenu(file_menu)
        menu_bar.addMenu(help_menu)

    def calculate_bmi(self):
        try:
            weight = float(self.input_weight.text())
            height_cm = float(self.input_height.text())
            height_m = height_cm / 100  # Convert cm to meters
            bmi = weight / (height_m ** 2)

            status, color, button_color = self.get_bmi_status(bmi)
            self.calculate_button.setText(f"BMI: {bmi:.2f}")
            self.calculate_button.setStyleSheet(f"""
                background-color: {button_color};
                color: white;
                font-size: 18px;
                padding: 10px;
                border-radius: 5px;
            """)
            self.status_label.setText(f"{status}")
            self.status_label.setStyleSheet(f"font-size: 16px; color: {color};")
        except ValueError:
            QMessageBox.warning(self, "Input Error", "Please enter valid numeric values for weight and height.")

    def get_bmi_status(self, bmi):
        if bmi < 18.5:
            return "Underweight: less than 18.5", "#FF6347", "#FF6347"  # Red
        elif 18.5 <= bmi < 25:
            return "Normal: between 18.5 and 25", "#32CD32", "#32CD32"  # Green
        elif 25 <= bmi < 30:
            return "Overweight: between 25 and 30", "#FFA500", "#FFA500"  # Orange
        else:
            return "Obese: 30 or greater", "#FF0000", "#FF0000"  # Dark Red

    def clear_inputs(self):
        self.input_weight.clear()
        self.input_height.clear()
        self.calculate_button.setText("Calculate BMI")
        self.calculate_button.setStyleSheet("""
            background-color: #4CAF50;
            color: white;
            font-size: 18px;
            padding: 10px;
            border-radius: 5px;
        """)
        self.status_label.clear()

    def show_help(self):
        QMessageBox.information(self, "How to Use",
                                "Enter your weight in kilograms and height in centimeters, then click 'Calculate BMI' to see your result.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BMICalculator()
    window.show()
    sys.exit(app.exec())
