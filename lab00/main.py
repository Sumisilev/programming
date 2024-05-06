import sys
from PySide6.Qtwidgets import QApplication, QMainWindow, QPushButton
def calculate_postage():
    pass
def generate_report():
    pass
app = QApplication(sys.argv)

window = QMainWindow
window.setWindowTitle ("Почтовые отправления")

calculate_button = QPushButton ("Рассчитать цену")
calculate_button.clicked.connect(generate_report)

window.setCentralWidget(calculate_button)
window.snow()

sys.exit(app.exec())

from postage_calculator import calculate_postage
from report_generator import generate_word_report, generate_excel_report

data =[]

def calculate_postage_handler():
    weight = 2 # Пример веса
    distance = 10 # Пример расстояния

    cost = calculate_postage(weight, distance)

    data.append({'weight': weight, 'distance': distance, 'cost': cost}) 

def generate_report_handler():
    generate_word_report(data)
    generate_excel_report(data)
    
app =QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("Почтовые отправления")

calculate_button = QPushButton ("Рассчитать цену")
calculate_button.clicked.connect(calculate_postage_handler)

report_button = QPushButton("Создать отчет")
report_button.clicked.connect(generate_report_handler)

window.setCentralWidget(calculate_button)
window.show()

sys.exit(app.exec())