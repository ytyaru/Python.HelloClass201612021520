class Human:
    def __init__(self):
        # __init__ is Constructor.
        self.name = "Python"
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def introduce(self):
        print("My name is {0}".format(self.name))
