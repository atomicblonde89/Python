class duck:
    def swim(self):
        print("Duck Swimming")
    
    def fly(self):
        print("Duck Flying")

class whale:
     def swim(self):
         print("Whale Swimming")

for animal in [duck(), whale()]:
    animal.swim()
    animal.fly()
    