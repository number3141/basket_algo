from PyQt5.QtWidgets import QLabel, QLineEdit, QVBoxLayout, QPushButton, QMainWindow

class Window(QMainWindow): 
    def __init__(self): 
      super(Window, self).__init__()

      self.layout = QVBoxLayout()
      self.setGeometry(0, 0, 500, 500)

      self.setWindowTitle('Basket Parse')
      
      self.dateLabel = QLabel(self)
      self.dateLabel.move(10, 10)
      self.dateLabel.setText('Введите дату')

      self.date = QLineEdit(self)
      self.date.move(10, 50)
      self.date.setInputMask('99.99')

      self.startButton = QPushButton(self)
      self.startButton.move(10, 100)
      self.startButton.setText('Рассчитать')

      self.startButton.clicked.connect(self.startProgram)

      self.layout.addWidget(self.date)
      self.layout.addWidget(self.dateLabel)
      self.layout.addWidget(self.startButton)
      self.setLayout(self.layout)
    
    def startProgram():
      # Абстрактная функция - надо реализовать у того, кто наследует 
      raise NotImplementedError