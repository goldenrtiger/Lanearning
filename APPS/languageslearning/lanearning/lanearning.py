# coding:utf-8

# all the imports
import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('layout.html')

@app.route('/play')
def play():
	return render_template('play.html')