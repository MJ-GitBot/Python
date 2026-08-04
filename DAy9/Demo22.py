from abc import ABC , abstractmethod
class A(ABC) :
    @abstractmethod 
    def withdraw(self,msg):
	// logic 

class B(A) :
	def withdraw(self,msg):
		 balace =amount - userneterdAmount;