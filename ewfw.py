class school:
    def __init__(self,name,location,student,teachers,ranking):
        self.n=name
        self.address=location
        self.snumbers=student
        self.tnumbers=teachers
        self.position=ranking
    def output(self):
        print(self.n,self.address,self.snumbers,self.tnumbers,self.position)
    def ratio(self):
        print(self.snumbers/self.tnumbers)
    def changestudents(self,drop):
        self.snumbers=self.snumbers-drop
    def addstudents(self,add):
        self.snumbers=self.snumbers+add
    def firestaff(self,fire):
        self.tnumbers=self.tnumbers-fire
cgs=school("chittagong grammar school","chawkbazar",400,100,1)
cgs.output()
cgs.ratio()
cgs.changestudents(20)
cgs.addstudents(1)
cgs.firestaff(1)
class section(school):
    def __init__(self,name,boys,girls):
        self.name=name
        self.boys=boys
        self.girls=girls
    def bg(self):
        print(self.boys/self.girls)
g=section("G",20,20)
g.bg()
