import pandas


class saveData(): 
    """Создаём объект для сохранения листов"""
    def __init__(self): 
        self.frameList = []
    
    def addFrame(self, data, columns, nameList = 'Zero'): 
        """Добавляем новый элемент в сохраняемый фрейм"""
        self.frameList.append({
            'data': pandas.DataFrame(data, columns=columns), 
            'nameList': nameList,
        })
    
    def saveInExcel(self, path):
        """Сохраняем все элементы на отдельные листы"""
        with pandas.ExcelWriter(path) as writer:
            for frame in self.frameList: 
                frame['data'].to_excel(writer, index=False, sheet_name=frame['nameList'])  