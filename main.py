import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import (
    QApplication, QWidget, QHBoxLayout, QPushButton, QLabel, QVBoxLayout, QGridLayout
)


class CalculatorButton(QPushButton):
    def __init__(self, value, action=None) -> None:
        super().__init__(text=value)
        # self.setFont(QFont("Arial", 15))

        if action is not None:
            self.clicked.connect(action)


class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        self.result = "0"

        self.setup_UI()

    def setup_UI(self):
        main_layout = QVBoxLayout(self)

        screen_layout = QHBoxLayout()
        self.result_screen = QLabel(self.result)
        self.result_screen.setFont(QFont("Helvetica", 20))
        screen_layout.addWidget(
            self.result_screen, alignment=Qt.AlignmentFlag.AlignRight)

        button_layout = QGridLayout()

        b_clear = CalculatorButton("CLEAR", self.clear)
        b_decimal = CalculatorButton(
            ".", lambda: self.update_result_screen("."))
        b_0 = CalculatorButton("0", lambda: self.update_result_screen("0"))
        b_1 = CalculatorButton("1", lambda: self.update_result_screen("1"))
        b_2 = CalculatorButton("2", lambda: self.update_result_screen("2"))
        b_3 = CalculatorButton("3", lambda: self.update_result_screen("3"))
        b_4 = CalculatorButton("4", lambda: self.update_result_screen("4"))
        b_5 = CalculatorButton("5", lambda: self.update_result_screen("5"))
        b_6 = CalculatorButton("6", lambda: self.update_result_screen("6"))
        b_7 = CalculatorButton("7", lambda: self.update_result_screen("7"))
        b_8 = CalculatorButton("8", lambda: self.update_result_screen("8"))
        b_9 = CalculatorButton("9", lambda: self.update_result_screen("9"))
        b_plus = CalculatorButton("+", lambda: self.update_result_screen("+"))
        b_minus = CalculatorButton("-", lambda: self.update_result_screen("-"))
        b_multiply = CalculatorButton(
            "*", lambda: self.update_result_screen("*"))
        b_divide = CalculatorButton(
            "/", lambda: self.update_result_screen("/"))
        b_result = CalculatorButton("=", self.calculate)

        button_layout.addWidget(b_clear, 0, 0, 1, 3)
        button_layout.addWidget(b_divide, 0, 3)
        button_layout.addWidget(b_1, 1, 0)
        button_layout.addWidget(b_2, 1, 1)
        button_layout.addWidget(b_3, 1, 2)
        button_layout.addWidget(b_multiply, 1, 3)
        button_layout.addWidget(b_4, 2, 0)
        button_layout.addWidget(b_5, 2, 1)
        button_layout.addWidget(b_6, 2, 2)
        button_layout.addWidget(b_plus, 2, 3)
        button_layout.addWidget(b_7, 3, 0)
        button_layout.addWidget(b_8, 3, 1)
        button_layout.addWidget(b_9, 3, 2)
        button_layout.addWidget(b_minus, 3, 3)
        button_layout.addWidget(b_0, 4, 0, 1, 2)
        button_layout.addWidget(b_decimal, 4, 2)
        button_layout.addWidget(b_result, 4, 3)

        main_layout.addLayout(screen_layout)
        main_layout.addLayout(button_layout, stretch=2)

    def update_result_screen(self, value):
        if self.result == "0":
            self.result = value
        else:
            self.result += value
        self.result_screen.setText(self.result)

    def calculate(self):
        self.result = str(eval(self.result))
        self.result_screen.setText(self.result)

    def clear(self):
        self.result = "0"
        self.result_screen.setText(self.result)


def main():
    app = QApplication(sys.argv)

    win = Calculator()
    win.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
