import csv
import pickle

with open('profile_database_100.csv', mode='r') as infile:
	reader = csv.reader(infile)
	mydict = dict((rows[0], (reader.line_num-1)/100) for rows in reader)

f = open("name100.pkl", "wb")
pickle.dump(mydict, f)
f.close()



newdict = pickle.load(open("name100.pkl", "rb"))
print newdict

