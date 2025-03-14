Input/Output
<img width="676" alt="Image" src="https://github.com/user-attachments/assets/646d1efa-6609-4cd3-bbcf-e5a44bc1489f" />

<img width="604" alt="Image" src="https://github.com/user-attachments/assets/4fdeb8cd-7b4b-4944-8f2a-a4b79248c4f3" />

<img width="604" alt="Image" src="https://github.com/user-attachments/assets/ab88236c-9497-4303-9dbd-3007201fe884" />

<img width="604" alt="Image" src="https://github.com/user-attachments/assets/8edb7d00-d575-4bba-b185-cfb7311a0b0e" />







---

# BMI Calculator (PyQt6)

This Python application is a **BMI (Body Mass Index) Calculator** built using the **PyQt6** library. It allows users to input their weight (in kilograms) and height (in centimeters), calculates their BMI, and displays the result in a user-friendly interface with color-coded categories. The app also features a dynamic button that changes its color based on the BMI value and provides a menu for additional options.

## Features

- **BMI Calculation**: The application takes the user's weight and height and calculates their BMI.
- **Dynamic Button Color**: The button changes color based on the calculated BMI:
  - **Red** for "Obese" (BMI ≥ 30)
  - **Green** for "Normal" (18.5 ≤ BMI < 25)
  - **Orange** for "Overweight" (25 ≤ BMI < 30)
  - **Red** for "Underweight" (BMI < 18.5)
- **Color-Coded BMI Categories**: Each BMI category (Underweight, Normal, Overweight, Obese) is displayed with a different color for better readability.
- **Help Section**: An informational menu is available to guide users on how to use the app.
- **Clear Option**: Clear the inputs and reset the button text and color.

## Requirements

- Python 3.x
- PyQt6 library

## Installation

To get started with the project, follow these steps:

1. **Clone the repository** (or download the code files):
   ```bash
   git clone https://github.com/yourusername/bmi-calculator.git
   ```

2. **Navigate to the project directory**:
   ```bash
   cd bmi-calculator
   ```

3. **Install the required dependencies**:
   ```bash
   pip install pyqt6
   ```

## Usage

1. **Run the application**:
   ```bash
   python main.py
   ```

2. **Enter your weight (kg) and height (cm)** in the respective input fields.

3. **Click the "Calculate BMI" button** to see your BMI. The button will change color based on the BMI value:
   - **Red** for "Obese" (BMI ≥ 30)
   - **Green** for "Normal" (18.5 ≤ BMI < 25)
   - **Orange** for "Overweight" (25 ≤ BMI < 30)
   - **Red** for "Underweight" (BMI < 18.5)

4. **Clear the inputs**: You can reset the inputs and button text by clicking the "Clear" option in the "File" menu.

5. **Help Option**: The "How to Use" option in the "Help" menu will show you instructions for using the app.

## BMI Categories

The following categories are used to classify the BMI value:

- **Underweight**: BMI < 18.5 (Red)
- **Normal**: BMI between 18.5 and 25 (Green)
- **Overweight**: BMI between 25 and 30 (Orange)
- **Obese**: BMI ≥ 30 (Dark Red)

## Code Description

### **1. Main Window**

The `BMICalculator` class inherits from `QMainWindow` and represents the main application window. It contains the UI layout and logic for the BMI calculation.

- **UI Elements**:
  - **Labels**: To prompt users to enter their weight and height.
  - **Line Edits**: To allow users to input their weight and height.
  - **Button**: To trigger the BMI calculation, with dynamic color changes based on the result.
  - **Status Label**: Displays the BMI category (e.g., Underweight, Normal, etc.) below the button.

### **2. Dynamic Button Color**

The color of the **Calculate BMI** button changes according to the calculated BMI:

- **Underweight (BMI < 18.5)**: Button turns **red**.
- **Normal (18.5 ≤ BMI < 25)**: Button turns **green**.
- **Overweight (25 ≤ BMI < 30)**: Button turns **orange**.
- **Obese (BMI ≥ 30)**: Button turns **dark red**.

This is handled in the `calculate_bmi()` method, where the BMI is computed, and the button’s color and text are updated accordingly.

### **3. Menu Bar**

The menu bar includes:
- **File Menu**:
  - **Exit**: Closes the application.
  - **Clear**: Resets all input fields and button text.
- **Help Menu**:
  - **How to Use**: Displays a message box with usage instructions.

### **4. Layouts**

- **QVBoxLayout**: The main vertical layout is used to stack the widgets in the window, such as the labels, input fields, and button.
- **QHBoxLayout**: A horizontal layout is used at the bottom of the window to display the BMI category cells (Underweight, Normal, Overweight, Obese), each with a different background color.

### **5. Functions**

- **`calculate_bmi`**: Calculates the BMI based on the input weight and height and updates the button's text and color based on the result.
- **`get_bmi_status`**: Determines the BMI category and assigns a color to the status and button.
- **`clear_inputs`**: Resets the input fields and the button to its default state.
- **`show_help`**: Displays a help message explaining how to use the application.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to update the repository link or any other details specific to your project!
