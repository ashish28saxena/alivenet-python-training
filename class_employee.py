class Employee:
	empCount = 0
	
	def __init__(self, name, age,):
		self.name=name
		self.age=age
		Employee.empCount += 1
	
	def displaycount(self):
		print "Total Employee %d" % Employee.empCount
		
	def displayemployee(self):
		print "Name : ", self.name, ", salary",self.age	
	 
emp1= Employee("ashish saxena",200)	
emp2 = Employee("Manni", 5000)

emp2.displayemployee()

	  

	 


