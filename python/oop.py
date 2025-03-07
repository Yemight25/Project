class person:
    def __init__(self):
       self. name= 'yemi'
       self.gender= ' Male'
       self.age= 22

    def talk(self):
        print(" Hi,I'm ", self.name)
    def vote(self):
        if self.age< 18:  
                 print(' You are not eligible to vote')
        else:
             print(" you are eligible to vote")  
obj = person()
person.talk(obj)
person.vote(obj)                    