#!/usr/bin/python

from bottle import Bottle, run, template, static_file
from dircache import listdir
from os import sep

prism = Bottle()

# Testing ...
@prism.route('/')
@prism.route('/hello')
@prism.route('/hello/<name>')
def hello(name='Stranger'):
    return template('Hello {{name}}, how are you today?', name=name)

# Testing ...
@prism.route('/Photographs')
@prism.route('/Photographs/')
def send_dir(directory=''):
    path = photos_base_dir + sep + directory
    #return template('I will send you path: {{path}}', path=path)
    return listdir(path)

# Display a photo
@prism.route('/Photographs/<image:path>')
def send_image(image):
    if image[-1] == '/': # directory
        return send_dir(image)
    else:
        return static_file(image, root='/home/djh/Dropbox/Photographs')

# Display a set
@prism.route('/sets')
@prism.route('/sets/')
@prism.route('/sets/<setid:re:[a-z0-9]*>')
def view_set(setid='Stranger'):
    return template('Hello {{setid}}, how are you today?', setid=setid)

# Display a collection of sets and collections
@prism.route('/collections')
@prism.route('/collections/<collectionid>')
def view_set(collectionid='Stranger'):
    return template('Hello {{collectionid}}, how are you today?',
            collectionid=collectionid)

run(prism, host='localhost', port=8080, debug=True)
