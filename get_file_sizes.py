import os

dirpath =  os.getcwd()
results=[]

onlyfiles = [file for file in os.listdir(dirpath) if os.path.isfile(file) ] 

for filesname in onlyfiles:
    #fullpathnew2 = fullpathnew.replace('\\', '\')
    results_dict = {'Path': os.path.abspath(filesname), 'Size': os.path.getsize(filesname)}
    results.append(results_dict)
  
print(*results, sep="\n")