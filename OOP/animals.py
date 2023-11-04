class Animals():
    def __init__(self, name:str, kind:str) -> None:
        self.name = name
        self.kind = kind
        print(self.name, self.kind)

Animals('pinki', 'labdador')