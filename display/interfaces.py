from PyQt5.QtWidgets import QLabel, QLineEdit, QVBoxLayout, QPushButton, QMainWindow, QTableWidget, QTableWidgetItem, QHeaderView
class Window(QMainWindow): 
    def __init__(self): 
      super(Window, self).__init__()

      self.layout = QVBoxLayout()
      self.setGeometry(0, 0, 700, 500)

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

      self.table = QTableWidget(self)
      self.table.setGeometry(10, 150, 680, 320) 
      self.table.setColumnCount(7)  
      # Настройка ширины ячеек
      self.header = self.table.horizontalHeader()    
      self.header.setSectionResizeMode(1, QHeaderView.Stretch)
      self.header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
      self.header.setSectionResizeMode(3, QHeaderView.ResizeToContents)
      self.header.setSectionResizeMode(4, QHeaderView.ResizeToContents)
      self.header.setSectionResizeMode(5, QHeaderView.ResizeToContents)

      self.startButton.clicked.connect(self.startProgram)

      self.layout.addWidget(self.date)
      self.layout.addWidget(self.dateLabel)
      self.layout.addWidget(self.startButton)
      self.layout.addWidget(self.table)
      self.setLayout(self.layout)
    
    def startProgram():
      # Абстрактная функция - надо реализовать у того, кто наследует 
      raise NotImplementedError

    def fillTable():
      raise NotImplementedError
