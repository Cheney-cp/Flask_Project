# -*- coding: utf-8 -*-


from flask import Flask, redirect, url_for, render_template, request, session

app = Flask(__name__)


@app.route('/login')
def login():
    return render_template('/login.html')
