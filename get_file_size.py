#import OS module
import os

#retrieve current directory path
dirpath =  os.getcwd()

#list that'll hold the file's directory path and size
results=[]

#will retrieve only the file in the current directory
onlyfiles = [file for file in os.listdir(dirpath) if os.path.isfile(file) ] 

#loops through the onlyfiles variable and retreive the filepath and size of the files
for filesname in onlyfiles:
    #fullpathnew2 = fullpathnew.replace('\\', '\')
    results_dict = {'Path': os.path.abspath(filesname), 'Size': os.path.getsize(filesname)}
    results.append(results_dict) # appends the results to the results[] variable
  
print(*results, sep="\n") #print results to the screen