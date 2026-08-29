class Account:
    def __init__(self, id, name):
        self.ID = id
        self.name = name


class StudentAccount(Account):
    def __init__(self, id, name):
        super().__init__(id, name)
        self.classes = []
        self.is_enlistment_locked = False
        self.is_enlisted = False

    def add_class(self, class_name):
        self.classes.append(class_name)

    def lock_enlistment(self):
        self.is_enlistment_locked = True
        print(f"{self.name} has locked enlistment.")


class AdviserAccount(Account):
    def __init__(self, id, name):
        super().__init__(id, name)
        self.advisees = []
        self.enlisted_advisees = []

    def add_advisee(self, student):
        self.advisees.append(student)
        print(f"{self.name} has added {student.name} as an advisee.")

    def print_advisees(self):
        print("Advisees:")
        for student in self.advisees:
            classes = ", ".join(student.classes)
            status = "Enlisted" if student.is_enlisted else "Not Enlisted"
            print(f"{student.ID} {student.name}: {classes} ({status})")

    def lock_enlistment_for(self, student):
        if student not in self.advisees:
            print(f"Error: {student.name} is not an advisee of {self.name}.")
            return

        if not student.is_enlistment_locked:
            print(f"Error: {student.name}'s enlistment is not locked yet.")
            return

        student.is_enlisted = True
        if student not in self.enlisted_advisees:
            self.enlisted_advisees.append(student)
        print(f"{student.name} is now enlisted.")


student1 = StudentAccount("05524", "Ross")
student1.add_class("Class 1")
student1.add_class("Class 2")
student1.add_class("Class 4")
student1.lock_enlistment()
adviser = AdviserAccount("01341", "Rachel")
adviser.add_advisee(student1)
adviser.lock_enlistment_for(student1)
student2 = StudentAccount("12345", "Chandler")
student2.add_class("Class 1")
student2.add_class("Class 3")
adviser.add_advisee(student2)
adviser.lock_enlistment_for(student2)
student3 = StudentAccount("01353", "Joey")
student3.add_class("Class 5")
student3.add_class("Class 9")

adviser.lock_enlistment_for(student3)
