#import httpx
#from flask_caching import Cache
from flask import Flask, abort, redirect, request
import random

app = Flask(__name__)
@app.route('/<path:type>/<path:http_code>')
def index(type,http_code):
    if type == '' or http_code == '':
        abort(404)
    
    noun_cat=['cat']
    noun_suffix = ['dog','pizza','garden','fish']
    noun_main = ['ducks','cats','goats',]
    nouns = noun_suffix + noun_main + noun_cat

    if search_string(nouns,type) == False:
        abort(404)

    if type == 'random':
        host_name = request.host.split(":")[0]
        url_main = host_name + "/" + nouns[random.randint(0,len(nouns)-1)]
    if search_string(noun_suffix,type) or search_string(noun_cat,type):
        url_main = "http." + type
    if search_string(noun_main,type):
        url_main = "http" + type + ".com"

    if search_string(noun_cat,type) or type == "random":
        redirect_response = redirect("https://" + url_main +"/" + http_code)
        return redirect_response
    if search_string(nouns,type):
        redirect_response = redirect("https://" + url_main + "/" + http_code + ".jpg")
        #redirect_response.headers['Cache-Control'] = 'max-age=0, s-maxage=300'
        return redirect_response

def search_string(list,target_string):
    if target_string in list:
        #index = list.index(target_string)
        return True
    else:
        return False


if __name__ == '__main__':
    app.run()