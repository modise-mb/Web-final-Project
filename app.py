from flask import Flask, render_template, redirect, request

app = flask(__name__)

@app.route("/")
def index():
    return "hello, world"