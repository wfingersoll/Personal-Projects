
class agent1():

    def __init__(self):
        self.name = "Social Media Bot"
        self.env = "Social Media Website"
        self.act = ["Text Posting Service", "Image Posting Service"]
        self.sense = ["Text Processing", "Image Processing", "Audio Processing"]
        self.metrics = ["Views/post", "Likes/post", "Followers gained/post"]

    def print_info(self):
        print("\nName: " + self.name + "\nEnvironment: " + self.env + "\n\nActuators: ")
        for act in self.act:
            print(act)
        print("\nSensors: ")
        for sense in self.sense:
            print(sense)
        print("\nPerfomance Metrics: ")
        for metric in self.metrics:
            print(metric)
        print("----------------------------------------------------------------------------------------------------")

class agent2():

    def __init__(self):
        self.name = "Drone Pilot"
        self.env = "Earth"
        self.act = ["Rotors", "Camera"]
        self.sense = ["Camera", "Altimeter", "Gryoscope"]
        self.metrics = ["Time/destination", "Battery Charge/destination"]

    def print_info(self):
        print("\nName: " + self.name + "\nEnvironment: " + self.env + "\n\nActuators: ")
        for act in self.act:
            print(act)
        print("\nSensors: ")
        for sense in self.sense:
            print(sense)
        print("\nPerfomance Metrics: ")
        for metric in self.metrics:
            print(metric)
        print("----------------------------------------------------------------------------------------------------")

class agent3():

    def __init__(self):
        self.name = "Automated Warehouse"
        self.env = "A singular warehouse"
        self.act = ["Item retrivial device"]
        self.sense = ["QR Scanner", "Customer interface"]
        self.metrics = ["Item retrivial time", "User indicated success rate"]

    def print_info(self):
        print("\nName: " + self.name + "\nEnvironment: " + self.env + "\n\nActuators: ")
        for act in self.act:
            print(act)
        print("\nSensors: ")
        for sense in self.sense:
            print(sense)
        print("\nPerfomance Metrics: ")
        for metric in self.metrics:
            print(metric)
        print("----------------------------------------------------------------------------------------------------")

class agent4():

    def __init__(self):
        self.name = "Image manipulation bot"
        self.env = "A singular website"
        self.act = ["Image manipulation software"]
        self.sense = ["Web scrapper", "Internal database", "User interface"]
        self.metrics = ["User indicated success rate", "Time to manipulate image", "Time to search database/web"]

    def print_info(self):
        print("\nName: " + self.name + "\nEnvironment: " + self.env + "\n\nActuators: ")
        for act in self.act:
            print(act)
        print("\nSensors: ")
        for sense in self.sense:
            print(sense)
        print("\nPerfomance Metrics: ")
        for metric in self.metrics:
            print(metric)
        print("----------------------------------------------------------------------------------------------------")

class agent5():

    def __init__(self):
        self.name = "Weather Prediction bot"
        self.env = "Earth"
        self.act = ["Output (I.E a website, or a simple terminal, etc)"]
        self.sense = ["Probe (I.E a weather balloon, a sattelite, etc)", "Radar", "Other weather stations"]
        self.metrics = ["Rate of succsesful prediction", "Level of discrepencay between prediction and reality"]

    def print_info(self):
        print("\nName: " + self.name + "\nEnvironment: " + self.env + "\n\nActuators: ")
        for act in self.act:
            print(act)
        print("\nSensors: ")
        for sense in self.sense:
            print(sense)
        print("\nPerfomance Metrics: ")
        for metric in self.metrics:
            print(metric)
        print("----------------------------------------------------------------------------------------------------")







a1 = agent1()
a2 = agent2()
a3 = agent3()
a4 = agent4()
a5 = agent5()

a1.print_info()
a2.print_info()
a3.print_info()
a4.print_info()
a5.print_info()

