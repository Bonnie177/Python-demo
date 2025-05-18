import subprocess
import os
import sys

class Hello:
    def __init__(self):
        self.name = 'nini'
        self.age = 3

    def introduce(self):
        print(f"{self.name},今年{self.age}岁")

    def is_adult(self):
        return self.age >= 18

    def main(self):
        self.introduce()
        if self.is_adult():
            print(f"{self.name} is an adult.")
        else:
            print(f"{self.name} is not an adult.")

if __name__ == "__main__":
    Hello().main()