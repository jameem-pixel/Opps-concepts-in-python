from abc import ABC,abstractmethod

class Download(ABC):
    @abstractmethod
    def response(self,url):
        pass

class Nrwbank(Download):
    def response(self,url):
        print("nrw data")
    def clean_data(self):
        print("final data of Nrwbank")  
    
class Bourse(Download):
    def response(self,url):
        print("bourse data")

    def clean_data(self):
        print("final data of Bourse")  

data_nrwbank = Nrwbank()
data_bourse = Bourse()

data_nrwbank.response("www.nrw.com") 
data_nrwbank.clean_data()
data_bourse.response("www.bourse.com") 
data_bourse.clean_data()
