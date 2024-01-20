class Computer:
    # Attributes ->(Variables), 
    # And Behavior -> Methods (Function)

    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram


    def config(self): # this is called a METHOD not FUNCTION
        print("config is", self.cpu, self.ram) 


comp1 = Computer("i5", "8gb")
comp2 = Computer("Ryzen3", "16gb")

comp1.config()
comp2.config()