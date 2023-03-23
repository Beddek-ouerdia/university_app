import tkinter
import os
import random

import sys
os.system('cls')

class University_App():

    #variable classe
    app_version=2.5
    app_name="university App"


  #constructor
    def __init__(self,full_screen_arg,bool=False) :
        
        #instance variable
        self.full_screen=full_screen_arg
class student:
    def __init__(self,name,age,identifiant):
        self.name=name
        self.age=age
        self.identifiant=identifiant 
    def afficher_age (self):
        return self.age


class Licence_student(student):
    def __init__(self,level,speciality):
        self.level=level
        self.speciality=speciality


class professor:
    def __init__(self,courses:list=[],autre_univ=[]):

        #INSTANCE ATTRIBUT
        self.courses=courses

        #instance attribut(unused by constructor)
        self.giving_course=False


    def set_giving_course(self,is_giving_course:bool):
        if(is_giving_course):
            self.giving_course=True
    def get_giving_course(self):
        return self.giving_course
    
class user:
    pass
class University_App:
    pass
professor_001=professor(autre_univ=["sorbonne"])
student001 = student("wardi",15,2025)

print(student001.afficher_age())