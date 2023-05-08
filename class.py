class Employee:
    def __init__(self, name, company):
        self.name = name
        self.company = company

    def introduction(self):
        print(f"Hello, my name is {self.name} and I am working in {self.company}.")


python = Employee("Alice", 'Factentry')
java = Employee("Bob", 'Amazon')
php = Employee("Charlie", "Microsoft")

python.introduction() 
java.introduction()  
php.introduction()  
