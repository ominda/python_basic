class Animals():
    def __init__(self, name:str, bread:str) -> None:
        self.name = name
        self.bread = bread
        print(self.name, self.bread)

Animals('pinki', 'labdador')