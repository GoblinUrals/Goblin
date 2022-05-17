class SoftwareEngineer:
    alias = "Keyboard Magician"

    @classmethod
    def class_code(cls, language):
        print (f" class method , {cls.alias}  codes in {language}")

    @staticmethod
    def static_code(language):
        print (f" static method, codes in {language}")

def global_code(language):
    print(f" global function , codes in {language} ")

SoftwareEngineer.class_code('Python')
SoftwareEngineer.static_code('Python')

global_code('Python')


