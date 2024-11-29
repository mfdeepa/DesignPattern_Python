class InvalidArgumentException(Exception):
    pass


class Gender:
    Male = "Male"
    Female = "Female"
    Other = "Other"


class Student:
    def __init__(self, builder):
        self.name = builder.name
        self.age = builder.age
        self.university_name = builder.university_name
        self.gender = builder.gender
        self.phone_number = builder.phone_number
        self.psp = builder.psp

    @staticmethod
    def create_builder():
        return Student.Builder()

    def __str__(self):
        return (
            f"Student(name={self.name}, age={self.age}, "
            f"university_name={self.university_name}, gender={self.gender}, "
            f"phone_number={self.phone_number}, psp={self.psp})"
        )

    class Builder:
        def __init__(self):
            self.name = None
            self.age = None
            self.university_name = None
            self.gender = None
            self.phone_number = None
            self.psp = None

        def set_name(self, name):
            self.name = name
            return self

        def set_age(self, age):
            self.age = age
            return self

        def set_university_name(self, university_name):
            self.university_name = university_name
            return self

        def set_gender(self, gender):
            self.gender = gender
            return self

        def set_phone_number(self, phone_number):
            self.phone_number = phone_number
            return self

        def set_psp(self, psp):
            self.psp = psp
            return self

        def validate(self):
            if len(self.phone_number) != 10:
                raise InvalidArgumentException("Phone number must be 10 digits long.")

        def build(self):
            self.validate()
            return Student(self)
