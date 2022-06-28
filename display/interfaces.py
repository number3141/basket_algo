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
    
    def fillTable(self, names, pointList, result, matchData): 
      countRow = self.table.rowCount()
      isSecondTeam = 0
      for indexRow in range(countRow, countRow + 2): 
        self.table.insertRow(indexRow)
        self.table.setItem(indexRow, 0, QTableWidgetItem(matchData))
        self.table.setItem(indexRow, 1, QTableWidgetItem(names[isSecondTeam]))
        for period in range(4): 
          self.table.setItem(indexRow, period + 2, QTableWidgetItem(str(pointList[isSecondTeam][period])))
        self.table.setItem(indexRow, 6, QTableWidgetItem(str(result)))
        isSecondTeam = 1
    
    def startProgram(self):
      # Абстрактная функция - надо реализовать у того, кто наследует 
      raise NotImplementedError
    
    def saveInExcel(): 
      raise NotImplementedError