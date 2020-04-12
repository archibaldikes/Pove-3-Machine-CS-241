
class machine:
    
    def __init__(self):
        self.fuel = 100
        self.xcord = 10
        self.ycord = 10
        
        
    def status(self):
        print()
        print("({},{}) - Fuel: {}".format(self.xcord, self.ycord, self.fuel))
        print()

    def left(self):
        if self.fuel <= 0:
            print()
            print("Insufficient fuel to perform action")
            print()
        else:
            self.fuel -= 5
            self.xcord -= 1


    def right(self):
        if self.fuel <= 0:
            print()
            print("Insufficient fuel to perform action")
            print()
        else:
            self.fuel -= 5
            self.xcord += 1
            

    def up(self):
        if self.fuel <= 0:
            print()
            print("Insufficient fuel to perform action")
            print()
        else:
            self.fuel -= 5
            self.ycord += 1
            

    def down(self):
        if self.fuel <= 0:
            print()
            print("Insufficient fuel to perform action")
            print()
        else:
            self.fuel -= 5
            self.ycord -= 1


    def fire(self):
        if self.fuel <= 15:
            print()
            print("Insufficient fuel to perform action")
            print()
        else:
            print()
            print('Pew! Pew!')
            print()
            self.fuel -= 15

    

def main():
    robot = machine()
    choice = None
    while choice != "quit":
        choice = input("Enter command from list below: ")
        if choice == "right":
            robot.right()
        elif choice == "left":
            robot.left()
        elif choice == "up":
            robot.up()
        elif choice == "down":
            robot.down()
        elif choice == "status":
            robot.status()
        elif choice == "fire":
            robot.fire()
    print()
    print('Goodbye')
        


if __name__ == "__main__":
    main()



