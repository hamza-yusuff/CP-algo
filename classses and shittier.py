class startup():
    def __init__(self,n1,n2,n3,n4,n5):
        self.m1=n1
        self.m2=n2
        self.m3=n3
        self.m4=n4
        self.m5=n5
    def boardoutput(self):
        print('The board members are:',self.m1,self.m2,self.m3,self.m4,self.m5)
    def market(self,*argv):
        self.new=[]
        for arg in argv:
            self.new.append(arg)
    def marketoutput(self):
        print(self.new)
    def calculation(self,cost,earning):
        print('The profit obtained:',earning-cost)
mudirdokan=startup('hamza','pratik','awsaf','ishmam','yasir')
mudirdokan.boardoutput()
mudirdokan.market('imtiaz','arhaam','sani','ayman','arnab')
mudirdokan.marketoutput()
mudirdokan.calculation(1200,3000)
