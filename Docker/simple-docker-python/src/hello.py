class MyClass:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return "MyClass class"

    def print_name(self):
        print(f'Hello, {self.name}')
