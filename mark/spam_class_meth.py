class Spam:
    numInstance = 0
    def __init__(self):
        Spam.numInstance += 1
    def prinNumInstances(cls):
        print("Number of instances: %s %s" % (cls.numInstances, cls))
    printNumInstances = classmethod(prinNumInstances)


class Sub(Spam):
    def printNumInstances(cls):
        print("Extra stuff...", cls)
        Spam.prinNumInstances()
    printNumInstances = classmethod(printNumInstances)
class Other(Spam): pass





