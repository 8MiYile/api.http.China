import random
def index(type,http_code):
    if type == '' or http_code == '':
        return False
    
    noun_cat=['cat']
    noun_suffix = ['dog','pizza','garden','fish']
    noun_main = ['ducks','cats','goats',]
    nouns = noun_suffix + noun_main + noun_cat

    if type == 'random':
        url_main = "api.http.中国/" + nouns[random.randint(0,len(nouns)-1)]
    if search_string(noun_suffix,type) or search_string(noun_cat,type):
        url_main = "http." + type
    if search_string(noun_main,type):
        url_main = "http" + type + ".com"

    if search_string(noun_cat,type) or type == "random":
        print("https://" + url_main +"/" + http_code)

    if search_string(nouns,type):
        print("https://" + url_main + "/" + http_code + ".jpg")

def search_string(list,target_string):
    if target_string in list:
        #index = list.index(target_string)
        return True
    else:
        return False


if __name__ == '__main__':
    index("random","302")
    