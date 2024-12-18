class Family:
    def __init__(self,members,last_name):
        self.members = members
        self.last_name = last_name

    def born(self, **kwargs):
        self.members.append(**kwargs)
        print(f'{kwargs.get} {self.last_name} has been born.' )

    def is_18(self, name):
        for member in self.memebers:
            if member ['name'] == name:
                return member['age'] >= 18
        return None

    def family_presentation(self):
        print(f"Family Last Name: {self.last_name}")
        print("Family Members:")
        for member in self.members:
            print(f"  - Name: {member['name']}, Age: {member['age']}, Gender: {member['gender']}, Is Child: {member['is_child']}")

initial_members = [
    {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False},
    {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False}
]

cohen_family = Family(members=initial_members, last_name="Cohen")

# Add a new family member using the born method
cohen_family.born(name='ELiav', age=0, gender='Male', is_child=True)

# Check if a member is over 18
print(cohen_family.is_18('Michael'))  
print(cohen_family.is_18('Emma'))  

cohen_family.family_presentation()
