class student:
    name=None
    mark1=0
    mark2=0
    def total(self):
        print(self.mark1+self.mark2)
s = student()
s.name="john"
s.mark1=60
s.mark2=50
s.total()