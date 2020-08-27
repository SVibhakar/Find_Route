NAME   :  SEJAL VIBHAKAR
UTA ID :  1001765264
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Programming Language Used : Python

Code Structure :
	find_route.py reads the command line arguments. 
	It takes in three arguments namely,  input filename, source city and destination city. 
	It takes in four arguments namely,  input filename, source city, destination city and heuristic filename.
 > Both Uninformed and Informed search are done in a sinlge program file.
 > Prints out node expanded, generated and maximun node that were there in the fringe.
 > Prints out distance and route, if exists

How to run :
	The program takes arguments like this.
Example,
     (For Uninformed Search):	find_route input_filename source_city destination_city 
     (For Informed Search):	find_route input_filename source_city destination_city Heuristic_filename 

To run the program : 
	py/python find_route.py input1.txt Bremen Munich
	py/python find_route.py input1.txt Bremen Kassel h_kassel.txt
Provide the full path for input123.txt in case input file is not at the project location.
  
