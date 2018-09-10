from flask import Flask
from flask import render_template, abort, flash, redirect, url_for, request
from . import aicos_union
from flask_login import current_user, login_required
from ..models import * 
from .forms import *
import flask_excel
import flask_excel as excel
from flask import abort,  request, flash, redirect, render_template, url_for, jsonify
from flask_login import current_user, login_required

def check_admin():
	if not current_user.is_admin:
		abort(403)

def check_union():
	if not current_user.is_union:
		abort(403)


@aicos_union.route('/')
@login_required
def indexUnion():
	return render_template('dashboard_union.html')

@aicos_union.route('/union/dashboard/')
@login_required
def union_dashboard():
	departments = Departments.query.all()
	employees = Member.query.all()
	all_deps = Departments.query.count()
	all_mbs = Member.query.count()

