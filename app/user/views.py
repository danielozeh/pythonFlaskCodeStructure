from . import user_blueprint

from flask import Flask, render_template, url_for, session, redirect, flash, request



@user_blueprint.route('/')
def index():

	return render_template('user/index.html')


@user_blueprint.route('/about-us/')
def about():

	return render_template('user/about.html')


@user_blueprint.route('/contact-us/')
def contact():

	return render_template('user/contact.html')