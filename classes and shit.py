class team():
    def __init__(self,*argv):
        self.array=[]
        for arg in argv:
            self.array.append(arg)
    def output(self):
        print(self.array)
startup=team('Hamza','Patrix','Sani','Ishmam')
print(startup.array[1])
startup.output()
