from email.message import MIMEPart
from abc import ABCMeta


""" class Person:

    def __init__(self,fname,lname) :
        self.fname = fname
        self.lname = lname

    def show_fullname(self):
        print('name is {} and lname is {}'.format(self.fname , self.lname))

    def __str__(self) -> str:
        return 'name is {} and lname is {}'.format(self.fname , self.lname)

class Student(Person):
    students = []
    def __init__(self, fname, lname,sid):
        super().__init__(fname, lname)
        self.studentid = sid
        self.students.append(self)

    def __str__(self) :
        return 'studet : {} and id is {}'.format(super().__str__(),self.studentid)


class Teacher(Person):

    def __init__(self, fname, lname,tid):
        super().__init__(fname, lname)
        self.teacherid = tid

class StudentList(list):

    def __init__(self,*args,**kwargs) :
        self.name = kwargs['name']
        super().__init__(*args,**kwargs)
        

    def search(self,name):
        pass
    
# s1 = Student('siavash', 'rad',232)
# s2 = Student('Mahan', 'Mahtabi',2544)
# s3 = Student('Raeza', 'Mohammadi',955)
# print(s1)
# s1.show_fullname() """



class BaseUser: 
    """ hello """
    def __init__(self,F_name,L_name,age,*args,**kwargs) :
        self.fname = F_name
        self.lname = L_name
        self.age = age
   
    @staticmethod
    def Fullname(self):
        return self.fname + self.lname
    
    def __repr__(self) -> str:
        return ': (\'{}\')'.format(  self.fname )

    def __str__(self) -> str:
        return 

    def __add__(self,other):
        return self.fname + other.fname

    def __len__(self):
        return len(self.Fullname()) 

class BaseDevice:
    def __init__(self,model,os_version,os_name,*args,**kwargs):
        self.model1 = model
        self.os_version = os_version
        self.os_name = os_name
        super().__init__(*args, **kwargs)

    def title(self):
        return f' Device_Model :{self.model1}'

class MobileUser(BaseUser,BaseDevice):

    user_list = []


  
    def __init__(self,phone_number,F_name,uuid,*args,**kwargs):
        self.phone_number = phone_number
        self.uuid =uuid
        self.fname= F_name
        super().__init__(F_name,*args,**kwargs)
        MobileUser.user_list.append(self.uuid)

    @classmethod
    def create(cls, uuid,*args,**kwargs):
        exist = False
        if uuid  in cls.user_list:
            exist = True
            return None
        else:
            ## call the initial function
            return cls(uuid=uuid,**kwargs)

    # def __eq__(self,other) -> bool:
    #     return self.phone_number == other.phone_number

    
    
    

    def __str__(self) -> str:
        return self.fname

class Web_User(BaseUser):
    def __init__(self,email,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.email = email

    



if __name__ =='__main__':
    user = MobileUser.create( phone_number='09360581929',F_name= 'siavash',L_name = 'rad',age = 21, 
                        model = 'note 8 pro' ,os_version=10, os_name = 'OREO' ,uuid = 123  )

    user2 = MobileUser.create( phone_number='09360581929',F_name= 'MAhan',L_name = 'shamsi',age = 31, 
                        model = 'note 8 pro' ,os_version=11, os_name = 'ORE33O' ,uuid=123  )

    user2 = MobileUser.create( phone_number='09360581929',F_name= 'MAhan',L_name = 'shamsi',age = 31, 
    model = 'note 8 pro' ,os_version=11, os_name = 'ORE33O' ,uuid=1823  )
    user2 = MobileUser.create( phone_number='09360581929',F_name= 'MAhan',L_name = 'shamsi',age = 31, 
    model = 'note 8 pro' ,os_version=11, os_name = 'ORE33O' ,uuid=1283  )

    # dev1 = BaseUser('siavash','MEehrad',21)
    # dev2 = BaseUser('setayesh','Rad',13)

    # print(setattr(user, 'model1','xiaomi')) 


    def __add__(self,other):
        return self.fname + other.fname

    print(user == user2)
    print(id(user))

    print((user.Fullname()))
     