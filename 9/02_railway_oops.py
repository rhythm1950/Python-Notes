import pandas as pd

pd.DataFrame()
class RailwayForm:
    formType = "RailwayForm"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")

rhythmsApplication = RailwayForm()
rhythmsApplication.name = "rhythm"
rhythmsApplication.train = "Rajdhani Express"
rhythmsApplication.printData()