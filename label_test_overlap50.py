import csv
import pickle


def label(output_file):

	f = open(output_file, "r")
	lines = f.readlines()
	f.close()


	newdict = pickle.load(open("name100.pkl", "rb"))
   

	f = open("libsvm_350_overlap50.txt","w")
	for line in lines:
		if line.split()[0] in newdict:
			f.write(str(newdict[line.split()[0]])+" ") 
			f.write(' '.join(line.split()[1:])+"\n")


	f.close()


label("350_3.txt")
