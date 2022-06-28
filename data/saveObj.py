class Save(): 
  def __init__(self, data) -> None:
    self.data = data
  def convertDataObjectToString(self): 
    """Data - iterable"""
    for key in self.data: 
      