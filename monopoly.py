from bottle import route, run, template, static_file, get
import json

@get('/')
def index():
    return template('index.html')

@get('/css/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root='css')

@get('/js/<filename:re:.*\.js>')
def javascripts(filename):
    return static_file(filename, root='js')

@get('/sounds/<filename:re:.*\.wav>')
def javascripts(filename):
    return static_file(filename, root='sounds')

@get('/images/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
    return static_file(filename, root='images')

def main():
    run(host='0.0.0.0', port=argv[1])

if __name__ == '__main__':
    main()