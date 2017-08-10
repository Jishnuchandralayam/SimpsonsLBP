'''
	Implement the LBP algorithm seen in the classroom using any programming language.
	The algorithm should receive as input any image and return the LBP image and also the 
	256-position histogram with the distribution of the LBP codes.
'''
import argparse
import os.path
import LBP

def main():	
	ap = argparse.ArgumentParser(description='Run the local binary patterns algorithm using a basic 3x3.')
	ap.add_argument('-i', '--input', dest='input', type=str, required=True, help='file name with path of the input image')    		
	arguments = ap.parse_args()
	

	#Change to generic	
	input_file = arguments.input #'data/base/bart.jpg'

	if os.path.isfile(input_file):        
		run = LBP.LBP(input_file)
		print("RUNNING algorithm developed")
		run.execute()	
		#print("RUNNING scikit-image")
		#run.compare()	
	else:
	    print("File '{}' does not exist.".format(input_file))	    

if __name__ == "__main__":
    main()