from PyQt5.QtWidgets import QFileDialog, QMessageBox, QLabel, QLineEdit, QVBoxLayout, QPushButton, QMainWindow, QTableWidgetItem, QTableWidget, QHeaderView, QApplication
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

      self.saveButton = QPushButton(self)
      self.saveButton.move(590, 100)
      self.saveButton.setText('Сохранить Excel')

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
      self.saveButton.clicked.connect(self.saveInExcel)

      self.layout.addWidget(self.date)
      self.layout.addWidget(self.dateLabel)
      self.layout.addWidget(self.startButton)
      self.layout.addWidget(self.table)
      self.setLayout(self.layout)
    
    def fillTable(self, match): 
      countRow = self.table.rowCount()
      self.createRowsWithMatchData(match, countRow, 'Home')
      countRow += 1
      self.createRowsWithMatchData(match, countRow, 'Away') 

    def createRowsWithMatchData(self, match, indexCurrentRow, prefix):
      self.table.insertRow(indexCurrentRow)
      self.table.setItem(indexCurrentRow, 0, QTableWidgetItem(match['matchDate']))
      self.table.setItem(indexCurrentRow, 1, QTableWidgetItem(match[f'name{prefix}']))
      for period in range(4): 
        currentColumn = period + 2
        self.table.setItem(indexCurrentRow, currentColumn, QTableWidgetItem(str(match[f'point{prefix}'][period])))
      self.table.setItem(indexCurrentRow, 6, QTableWidgetItem(str(match['result'])))
      
    
    def startProgram(self):
      # Абстрактная функция - надо реализовать у того, кто наследует 
      raise NotImplementedError
    
    def saveInExcel(): 
      raise NotImplementedError