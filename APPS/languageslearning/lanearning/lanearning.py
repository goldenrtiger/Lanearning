# coding:utf-8

# all the imports
import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/play')
def play():
	return render_template('play.html')

@app.route('/Phonetics')
def Phonetics():
	return render_template('Phonetics.html')

@app.route('/Lexique')
def lexique():
	return render_template('lexique.html')

@app.route('/leason1')
def leason1():
	return render_template('leason1.html')

@app.route('/leason2')
def leason2():
	return render_template('leason2.html')

@app.route('/lesson3')
def leason3():
	return render_template('lesson3.html')