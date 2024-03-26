#parent class

class Animal:

    def __init__(self):
        pass
    def speak(self):
        pass

    #child class 1
    class Dog(Animal):
        def __init__(self):
            pass
        def speak(self):
            print("I am a dog and i bark")

    #child class 2
    class Cat(Animal):
        def __init__(self):
            pass
        def speak(self):
            print("i am a cat and i purr")

#creatin instances
Dog1=Dog()
Dog1.speak()

Cat1=Cat()
Cat1.speak()