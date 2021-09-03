import requests
# For Question 2, 3 and 4 
print(requests.__version__)

# GET the Google homepage 
page = requests.get('http://www.google.com/')
#print('\n', page.text)

# "Modify your Python script so that it downloads itself from GitHub and prints out its own source code from GitHub." 
rawPg = requests.get('https://raw.githubusercontent.com/csportat/CMPUT404_lab1/main/lab1script.py')
print('\n', rawPg.text)
