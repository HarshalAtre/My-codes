from msilib.schema import Class


class railform:
    formtype="railwayform"
    def printData(self):
        print(f' the name is {self.name}')
        print(f' the train is {self.train}')

me=railform()
me.name="HARSHAL"
me.train="shatabdi"
me.printData()
    








