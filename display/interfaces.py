from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QVBoxLayout, QPushButton, QMainWindow, QTableWidgetItem, QTableWidget, QHeaderView
class Window(QMainWindow): 
    def __init__(self): 
        super(Window, self).__init__()

        self.layout = QVBoxLayout()
        self.setGeometry(0, 0, 1200, 500)

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
        self.saveButton.move(120, 100)
        self.saveButton.setText('Сохранить в CSV')

        self.freqTable = QTableWidget(self)
        self.freqTable.setGeometry(700, 150, 480, 320) 
        self.freqTable.setColumnCount(5) 

        self.freqHeader = self.freqTable.horizontalHeader()    
        self.freqHeader.setSectionResizeMode(0, QHeaderView.Stretch)

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
        self.saveButton.clicked.connect(self.saveInFile)

        self.layout.addWidget(self.date)
        self.layout.addWidget(self.dateLabel)
        self.layout.addWidget(self.startButton)
        self.layout.addWidget(self.table)
        self.setLayout(self.layout)
    
    def fillTable(self, match): 
        self.currentRow = self.table.rowCount()
        self.createRowsWithMatchData(match, self.currentRow, 'Home')
        self.currentRow += 1
        self.createRowsWithMatchData(match, self.currentRow, 'Away') 

    def createRowsWithMatchData(self, match, indexCurrentRow, prefix):
        self.table.insertRow(indexCurrentRow)
        self.table.setItem(indexCurrentRow, 0, QTableWidgetItem(match['matchDate']))
        self.table.setItem(indexCurrentRow, 1, QTableWidgetItem(match[f'name{prefix}']))
        for period in range(4): 
            currentColumn = period + 2
            self.table.setItem(indexCurrentRow, currentColumn, QTableWidgetItem(str(match[f'point{prefix}'][period])))
        self.table.setItem(indexCurrentRow, 6, QTableWidgetItem(str(match['result'])))

    def fillFreqTable(self, match): 
        self.currentFreqRow = self.freqTable.rowCount()
        for item in match: 
            self.freqTable.insertRow(self.currentFreqRow)
            self.freqTable.setItem(self.currentFreqRow, 0, QTableWidgetItem(str(item)))
            self.freqTable.setItem(self.currentFreqRow, 1, QTableWidgetItem(str(match[item]['pass'])))
            self.freqTable.setItem(self.currentFreqRow, 2, QTableWidgetItem(str(match[item]['take'])))  
            self.freqTable.setItem(self.currentFreqRow, 3, QTableWidgetItem(str(match[item]['defeat'])))  
            self.freqTable.setItem(self.currentFreqRow, 4, QTableWidgetItem(str(match[item]['total'])))  
    
    def startProgram(self):
        # Абстрактная функция - надо реализовать у того, кто наследует 
        raise NotImplementedError
    
    def saveInFile(): 
        raise NotImplementedError

if __name__ == '__main__': 
    app = QApplication([])
        # Исп. как контейнер 
    window = Window()
    window.show()
    app.exec_()