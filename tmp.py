class Prova:
    _myClassVariable = 0

    def __init__(self, input):
        self.myInstanceVariable = input

    def standardMethod(self):
        print(self.myInstanceVariable)

    @staticmethod #si usano per il dao
    def staticMethod(): # vede solo quello che gli passo come argomento
        #non ho accesso ne ha self, ne a cls
        pass

    @classmethod #hanno accesso alle variabili di classe, si usano nel dbconnect
    def classMethod(cls):
        print(cls._myClassVariable)


newInstance = Prova("txt")
newInstance.standardMethod()
