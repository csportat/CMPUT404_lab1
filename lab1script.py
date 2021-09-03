import requests
# For Question 2, 3 and 4 
print(requests.__version__)

# GET the Google homepage 
page = requests.get('http://www.google.com/')