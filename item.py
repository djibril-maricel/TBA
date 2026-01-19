from debug import DEBUG

class Item():
    """
    docstring à faire
    """

    # define the constructor
    def __init__(self, name:str, description:str, weight):
        self.name = name
        self.description = description
        self.weight = weight

    def __str__(self):
        return f""+ self.name +" : "+ self.description +" ("+ str(self.weight) +" kg)"
    
    def get_weight(self):
        return self.weight