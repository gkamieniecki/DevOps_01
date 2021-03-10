# import statements
from flask import Flask, jsonify
from bs4 import BeautifulSoup
import requests
app = Flask(__name__)
app.debug = True

@app.route("/")
def returnjokes():
    jokes_list = []
    
    for x in range(1, 8):

        # variable which holds our GET request and converts it into plain text
        source =  requests.get(f"http://bash.org.pl/latest/?page={x}").text
        
        # variable which let us navigate and search through the HTML for data we want
        soup = BeautifulSoup(source, 'html.parser')

        # variable which finds every div with class "quote"
        jokes_divs = soup.find_all("div", class_="quote")
        
        for tag in jokes_divs:
            remove_tags = tag.get_text() # removes HTML tags
            jokes_list.append(remove_tags)
    
    # new list with first 100 objects in "jokes_list" list
    jokes_list2 = []
    for n in range(100):
        jokes_list2.append(jokes_list[n])

    return jsonify({"jokes": jokes_list2}) #returns the list in JSON format

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)