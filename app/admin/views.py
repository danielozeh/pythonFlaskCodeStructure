from . import admin_blueprint

from flask import Flask, render_template, url_for, session, redirect, flash, request


#### NOTE ONLY IMPORT THESE CLASSES WHEN THEY WILL BE USED 
from app.classes.SelectQueryClass import SelectQueryClass
from app.classes.InsertQueryClass import InsertQueryClass
from app.classes.UpdateQueryClass import UpdateQueryClass
from app.classes.DeleteQueryClass import DeleteQueryClass
from app.classes.ImageUploadClass import ImageUploadClass

SelectQueryClass = SelectQueryClass()
InsertQueryClass = InsertQueryClass()
UpdateQueryClass = UpdateQueryClass()
DeleteQueryClass = DeleteQueryClass()
ImageUploadClass = ImageUploadClass()

@admin_blueprint.route('/dashboard/')
def index():

	all_users = SelectQueryClass._getAllusers()

	return render_template('admin/dashboard.html', all_users = all_users)


@admin_blueprint.route('/another-page')
def another_page():

	return render_template('admin/another-page.html')