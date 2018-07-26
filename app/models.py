from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login_manager
from datetime import datetime
import datetime

from sqlalchemy import DateTime

class Cooperative(db.Model):
	"""
	Creating the cooperative database here.
	"""
	__tablename__ = 'cooperatives'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(300))
	description = db.Column(db.String(300))
	employees = db.relationship('Employee', backref='cooperative', lazy='dynamic')
	def __repr__(self):
		return '<Cooperative: {}>'.format(self.name)

subs = db.Table('subs',
	db.Column('employee_id', db.Integer, db.ForeignKey('employees.id')),
	db.Column('department_id', db.String(399), db.ForeignKey('departments.email'))
	)



class Employee(UserMixin, db.Model):
	"""
	Create an Employee table
	"""
	# Ensures table will be named in plural and not in singular
	# as is the name of the model
	__tablename__ = 'employees'
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(60), index=True, unique=False)
	username = db.Column(db.String(60), index=True)
	first_name = db.Column(db.String(60), index=True)
	last_name = db.Column(db.String(60), index=True)
	phone_number = db.Column(db.String(200), index=True)
	password_hash = db.Column(db.String(128))
	department_id = db.Column(db.String(400), db.ForeignKey('departments.email'))
	role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
	project_id = db.Column(db.Integer, db.ForeignKey('projects.id'))
	employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'))
	cooperative_id = db.Column(db.Integer, db.ForeignKey('cooperatives.id'))
	profile        = db.relationship('Profile', uselist=False, back_populates="employee")

	#user_id        = db.Column(db.Integer, db.ForeignKey('user.user_id'))
	#activity_id   = db.relationship('Activity', backref='employee', lazy='dynamic')
	#membership = db.relationship('Department', secondary=subs, backref=db.backref('members', lazy='dynamic'))
	is_admin = db.Column(db.Boolean, default=True)
	is_coop_admin = db.Column(db.Boolean, default=False)
	is_overall = db.Column(db.Boolean, default=False)
	is_invited = db.Column(db.Boolean, default=False)
	is_union   = db.Column(db.Boolean, default=False)
	is_ferwacotamo = db.Column(db.Boolean, default=False)
	is_confederation = db.Column(db.Boolean, default=False)
	is_rca = db.Column(db.Boolean, default=False)
	invited_by = db.Column(db.String(300))
	district   = db.Column(db.String(300))


	@property
	def password(self):
		"""
		Prevent pasword from being accessed
		"""
		raise AttributeError('password is not a readable attribute.')

	@password.setter
	def password(self, password):
		"""
		Set password to a hashed password
		"""
		self.password_hash = generate_password_hash(password)

	def verify_password(self, password):
		"""
		Check if hashed password matches actual password
		"""
		return check_password_hash(self.password_hash, password)

	def __repr__(self):
		return '<Employee: {}>'.format(self.username)


# Set up user_loader
@login_manager.user_loader
def load_user(user_id):
	return Employee.query.get(int(user_id))






#Models for inventories.
class Product(db.Model):
	__tablename__ = "products"
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(300))
	description = db.Column(db.String(400))
	quantity = db.Column(db.String(400))
	in_date = db.Column(db.String(400))
	status  = db.Column(db.String(400))
	department_id = db.Column(db.String(300), db.ForeignKey('departments.email'))


	def __repr__(self):
		return '<Product: {}>'.format(self.name)





#Models for inventories.
class Order(db.Model):
	__tablename__ = "ordes"
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(300))
	product = db.Column(db.String(300))
	description = db.Column(db.String(400))
	quantity = db.Column(db.String(400))
	in_date = db.Column(db.String(400))
	status  = db.Column(db.String(400))
	department_id = db.Column(db.String(300), db.ForeignKey('departments.email'))


	def __repr__(self):
		return '<Order: {}>'.format(self.name)





class Federation(db.Model):
	__tablename__ = 'federations'
	id = db.Column(db.Integer, primary_key=True)
	sno = db.Column(db.String(300))
	code = db.Column(db.String(300))
	name = db.Column(db.String(300))
	certificate = db.Column(db.String(300))
	reg_date	= db.Column(db.String(300))
	province 	= db.Column(db.String(300))
	district 	= db.Column(db.String(300))
	sector 		= db.Column(db.String(300))
	activity 	= db.Column(db.String(300))
	unions		= db.relationship('Union', backref="federation", lazy="dynamic")

	def __repr__(self):
		return '<Federation: {}>'.formt(self.name)


	""" We will always use this __init__ function to upload excel file  """
	def __init__(self, code):
		self.id = id
		self.code = code





class Union(db.Model):
	__tablename__ = 'unions'
	id = db.Column(db.Integer, primary_key=True)
	sno = db.Column(db.String(300))
	code = db.Column(db.String(300))
	name = db.Column(db.String(300))
	certificate = db.Column(db.String(300))
	reg_date	= db.Column(db.String(300))
	province 	= db.Column(db.String(300))
	district 	= db.Column(db.String(300))
	sector 		= db.Column(db.String(300))
	activity 	= db.Column(db.String(300))
	#cooperatives = db.relationship('Department', backref="union", lazy="dynamic")
	federation_id = db.Column(db.Integer, db.ForeignKey('federations.id'))

	def __repr__(self):
		return '<Union: {}>'.formt(self.name)


		""" We will always use this __init__ function to upload excel file  """
	def __init__(self, code):
		self.id = id
		self.code = code







class Department(db.Model):
	"""
	Create a Department table
	"""
	__tablename__ = 'departments'
	id = db.Column(db.Integer, autoincrement=True, nullable=True)
	# General information
	no = db.Column(db.Integer)
	code = db.Column(db.String(400))
	email = db.Column(db.String(300), primary_key=True, unique=True)
	name  = db.Column(db.String(600))
	regdate = db.Column(db.String(400))
	certificate = db.Column(db.String(400))
	description = db.Column(db.String(200))
	province    = db.Column(db.String(400))
	district    = db.Column(db.String(300))
	sector      = db.Column(db.String(300))
	cell      = db.Column(db.String(300))
	activity    = db.Column(db.String(400))
	coop_type   = db.Column(db.String(300))

	category   = db.Column(db.String(300))
	field   = db.Column(db.String(300))
	# federation_id = db.Column(db.Integer, db.ForeignKey('federations.id'))
	# union_id	   = db.Column(db.Integer, db.ForeignKey('unions.id'))
	# Professional information
	started_data = db.Column(db.String(300))
	starting_share = db.Column(db.Integer)
	#email       = db.Column(db.String(300))
	applications = db.relationship('Application', backref='department', lazy='dynamic')
	employees = db.relationship('Employee', backref='department',lazy='dynamic')
	products        = db.relationship('Product', backref='department', lazy='dynamic')
	orders          = db.relationship('Order', backref='department', lazy='dynamic')
	members         = db.relationship('Member', backref='department', lazy='dynamic')
	motos 			= db.relationship('Moto', backref='motos', lazy='dynamic')
	decisions       = db.relationship('Decision', backref='department', lazy='dynamic')
	communications  = db.relationship('Communication', backref='department', lazy='dynamic')

	contributions  = db.relationship('Contribution', backref='department', lazy='dynamic')
	reports         = db.relationship('Report', backref='department', lazy='dynamic')
	howtos      = db.relationship('Howto', backref='department', lazy='dynamic')
	links       = db.relationship('Link', backref='department', lazy='dynamic')
	trainings 	= db.relationship('Training', backref='department', lazy='dynamic')
	applytrainings = db.relationship('applyTraining', backref='department', lazy='dynamic')

	files       = db.relationship('File', backref='department', lazy='dynamic')
	BankAccounts        = db.relationship('BankAccount', backref='department', lazy='dynamic')
	loans       = db.relationship('Loan', backref='department', lazy='dynamic')    
	notifications       = db.relationship('Notification', backref='department', lazy='dynamic')
	intekoRusange       = db.relationship('intekoRusange', backref='department', lazy='dynamic')
	inamaUbuyobozi       = db.relationship('inamaUbuyobozi', backref='department', lazy='dynamic')
	ubugenzuzi       = db.relationship('Ubugenzuzi', backref='department', lazy='dynamic')
	isanduku       = db.relationship('Isanduku', backref='department', lazy='dynamic')
	is_active 	   = db.Column(db.Boolean, default=False)

	#Dealing with excel staff here.

	""" We will always use this __init__ function to upload excel file  """
	def __init__(self, email):
		self.id = id
		self.email = email

	""" That in btn """
		#self.description = description
		#self.employees   = employees


	def __repr__(self):
		return '<Department: {}>'.format(self.name)

"""
Dealing with excel staffs here.

	def __init__(self, no, code, name, certificate, regdate, province, district, sector, activity):
		self.no = no
		self.code = code
		self.name = name
		self.certificate = certificate
		self.regdate = regdate
		self.province = province
		self.district = district
		self.sector = sector
		self.activity = activity

	def __repr__(self):
		return '<Role %r>' % self.name

"""









class Role(db.Model):
	"""
	Create a Role table
	"""

	__tablename__ = 'roles'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(60), unique=True)
	description = db.Column(db.String(200))
	employees = db.relationship('Employee', backref='role',
								lazy='dynamic')

	members = db.relationship('Member', backref='role',
								lazy='dynamic')


	"""
	#Dealing with excel staff here.
	def __init__(self,name):
		self.id = id
		self.name = name
		#self.description = description
		#self.employees   = employees
	"""

	def __repr__(self):
		return '<Role: {}>'.format(self.name)




# Table for the projects in the cooperative are here.
class Project(db.Model):

	"""
	Renaming the table to prular form here.
	"""

	__tablename__  = "projects"

	"""
		All the fields that will be on the table are here.
	"""

	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(300))
	description = db.Column(db.String(300))
	starting_date = db.Column(db.String(300))
	ending_date = db.Column(db.String(300))
	
	description = db.Column(db.String(300))
	duration    = db.Column(db.String(300))
	employees   = db.relationship('Employee', backref='project', lazy='dynamic')

	def __repr__(self):
		return '<Project: {}>'.format(self.name)

"""

# Table for all products we are having in our cooperative are here.
class Product(db.Model):
		Renaming the table to be plural here
	__tablename__ = "products"
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(300))
	description = db.Column(db.String(300))
	image       = db.String(db.String(300))
	price       = db.Column(db.String(400))
	client_id   = db.Column(db.Integer, db.ForeignKey('clients.id'))

	def __repr__(self):
		return '<Product: {}>'.format(self.name)
"""


# Table for our clients internally in the cooperative comes here.

class Client(db.Model):

	"""
	Rename the table from singular to prular form here.
	"""

	__tablename__ = "clients"

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(300))
	location = db.Column(db.String(300))
	business = db.Column(db.String(300))
	#product  = db.relationship('Product', backref='client', lazy='dynamic')

	def __repr__(self):
		return '<Client: {}>'.format(self.name)


"""


"""

# Database for storing the information about member's applications
# To join cooperatives they want to join.


class Application(db.Model):

	__tablename__ = "applications"
	id = db.Column(db.Integer, primary_key=True, unique=True)
	emailaa = db.Column(db.String(300))
	firstNameaa = db.Column(db.String(300))
	secondNameaa = db.Column(db.String(300))
	othersaa = db.Column(db.String(300))
	Districtaa = db.Column(db.String(300))
	Sectoraa = db.Column(db.String(300))
	Cellaa = db.Column(db.String(300))
	nIdaa = db.Column(db.String(300))
	entryDateaa = db.Column(db.String(300))
	shareaa = db.Column(db.String(300))
	exitDateaa = db.Column(db.String(300))
	umuzunguraaa = db.Column(db.String(300))
	umukonoaa = db.Column(db.String(300))
	genderaa  = db.Column(db.String(300))
	dobaa     = db.Column(db.String(300))
	phoneaa = db.Column(db.String(300))
	Amashuriaa = db.Column(db.String(300))
	Ubumugaaa = db.Column(db.String(300))
	department_id = db.Column(db.String(300), db.ForeignKey('departments.email'))


	def __repr__(self):
		return '<Application: {}>'.format(self.emailaa)


class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(80))
	body = db.Column(db.Text)
	pub_date = db.Column(db.DateTime)

	category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
	category = db.relationship('Category',
							   backref=db.backref('posts',
												  lazy='dynamic'))

	def __repr__(self):
		return '<Post %r>' % self.title

	def __init__(self, title, body, category, pub_date=None):
		self.title = title
		self.body = body
		if pub_date is None:
			pub_date = datetime.utcnow()
		self.pub_date = pub_date
		self.category = category

	def __repr__(self):
		return '<Post %r>' % self.title


class Category(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50))

	def __repr__(self):
		return '<Category %r>' % self.name

	def __init__(self, name):
		self.name = name



# Models for the profiles of the users, in the system.
class Profile(db.Model):

	__tablename__ = 'profiles'

	id = db.Column(db.Integer, primary_key=True)
	# Education columns.
	primary_school = db.Column(db.String(300))
	secondary_school = db.Column(db.String(300))
	university_school = db.Column(db.String(300))
	vocational_school = db.Column(db.String(300))

	# Eperiances.
	exp1  = db.Column(db.String(300))
	exp2  = db.Column(db.String(300))
	exp3  = db.Column(db.String(300))

	# Strengths.
	strn1 = db.Column(db.String(300))
	strn2 = db.Column(db.String(300))
	strn3 = db.Column(db.String(300))

	# Careers.
	car1 = db.Column(db.String(300))
	car2 = db.Column(db.String(300))
	car3 = db.Column(db.String(300))

	# Interest.
	inter1 = db.Column(db.String(300))
	inter2 = db.Column(db.String(300))
	inter3 = db.Column(db.String(300))

	# Location
	district = db.Column(db.String(300))
	employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'))
	employee = db.relationship('Employee', back_populates="profile")


	def __repr__(self):
		return '<Profile: {}>'.format(self.id)

#Class to create the table of members who located in all coperatives which found in ferwacotamo.
"""


Email
Rejected or not? = 1 or 0
Martuel status
Province
Insurance_type
Ubudehe
Children
Language
nationality (Discuss)
rular_or_urban
member_source
job
occupation

"""
class Member(db.Model):
	__tablename__ = "members"
	id = db.Column(db.Integer, primary_key=True, unique=True)
	firstName = db.Column(db.String(300))
	secondName = db.Column(db.String(300))
	others = db.Column(db.String(300))
	Province = db.Column(db.String(300))
	District = db.Column(db.String(300))
	Sector = db.Column(db.String(300))
	Cell = db.Column(db.String(300))
	nId = db.Column(db.String(300))
	entryDate = db.Column(db.String(300))
	share = db.Column(db.String(300))
	exitDate = db.Column(db.String(300))
	umuzungura = db.Column(db.String(300))
	umukono = db.Column(db.String(300))
	gender  = db.Column(db.String(300))
	dob     = db.Column(db.String(300))
	age     = db.Column(db.String(300))
	phone = db.Column(db.String(300))
	Amashuri = db.Column(db.String(300))
	Ubumuga = db.Column(db.String(300))
	marital_status = db.Column(db.String(300))
	ubudehe 	   = db.Column(db.String(300))
	insurance      = db.Column(db.String(300))
	Language	   = db.Column(db.String(300))
	member_source =  db.Column(db.String(300))
	job			  =  db.Column(db.String(300))
	has_children       = db.Column(db.String(300))
	rular_or_urban       = db.Column(db.String(300))
	is_active      = db.Column(db.Boolean, default=True)
	role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
	department_id = db.Column(db.String(300), db.ForeignKey('departments.email'))




	""" We will always use this __init__ function to upload excel file """
	def __init__(self, nId):
		self.id = id
		self.nId = nId
	

	"""
	Importing data using this views.
	================================
	
	def __init__(self, firstName, secondName, others, District, Sector, Cell, nId, entryDate, share,
						exitDate, umuzungura, umukono, gender, dob, phone, Amashuri, Ubumuga,
						dl, plate, owner, ownerPhone,
						department_id):
		#self.id = id
		self.firstName = firstName
		self.secondName = secondName
		self.others = others
		#if pub_date is None:
			#pub_date = datetime.utcnow()
		#self.pub_date = pub_date
		self.District = District
		self.Sector = Sector
		self.Cell = Cell
		self.nId = nId
		#self.cooperative = cooperative
		self.entryDate = entryDate
		self.share = share
		self.exitDate = exitDate
		self.umuzungura = umuzungura
		self.umukono = umukono
		self.gender = gender
		self.dob = dob
		self.phone = phone
		self.Amashuri = Amashuri
		self.Ubumuga = Ubumuga
		self.dl = dl
		self.plate = plate
		self.owner = owner
		self.ownerPhone = ownerPhone
		self.department_id = department_id


	def __repr__(self):
		return '<Member: {}>'.format(self.secondName)
	"""

class Moto(db.Model):

	__tablename__ = 'motos'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(300))
	plate = db.Column(db.String(300))
	owner = db.Column(db.String(300))
	owner_tel = db.Column(db.String(300))
	member_id = db.Column(db.Integer, db.ForeignKey('members.id'))
	department_id = db.Column(db.String(300), db.ForeignKey('departments.email'))

	def __repr__(self):
		return '<Moto: {}>'.format(self.name)




# Class / Table for notifications to all changes in the database
class Notification(db.Model):

	__tablename__ = "notifications"

	id = db.Column(db.Integer, primary_key=True, unique=True)
	action = db.Column(db.String(400))
	done_by = db.Column(db.String(400))
	done_from = db.Column(db.String(400))
	done_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)

	done_time = db.Column(db.String(400))
	done_to   = db.Column(db.String(400))
	effect = db.Column(db.String(400))
	department_id = db.Column(db.String(300), db.ForeignKey('departments.email'))


	def __repr__(self):
		return '<Notification: {}>'.format(self.name)
	




# All the tables (models) for the coop admin's activities.
# Table for the decisions

class Decision(db.Model):

	__tablename__ = "decisions"
	
	id = db.Column(db.Integer, primary_key=True, unique=True)
	status = db.Column(db.String(300))
	decision = db.Column(db.String(300))
	owner    = db.Column(db.String(300))
	stakeholders = db.Column(db.String(300))
	due_date     = db.Column(db.String(300))
	background   = db.Column(db.String(300))
	department_id = db.Column(db.String(300), db.ForeignKey('departments.email'))

	def __repr__(self):
		return '<Decision: {}>'.format(self.status)


	def __repr__(self):
		return '<Decision: {}>'.format(self.owner)








class Report(db.Model):

	__tablename__ = "reports"
	
	id = db.Column(db.Integer, primary_key=True, unique=True)
	status = db.Column(db.String(200))
	project = db.Column(db.String(200))
	task = db.Column(db.String(200))
	description      = db.Column(db.String(300))
	notes = db.Column(db.String(200))
	date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
	department_id = db.Column(db.String(300), db.ForeignKey('departments.email'))

	def __repr__(self):
		return '<Report: {}>'.format(self.name)












class Howto(db.Model):

	__tablename__ = "howtos"
	
	id = db.Column(db.Integer, primary_key=True, unique=True)
	name = db.Column(db.String(300))
	labels = db.Column(db.String(300))
	description    = db.Column(db.String(300))
	steps = db.Column(db.String(300))
	file     = db.Column(db.String(300))
	#background      = db.Column(db.String(300))
	department_id = db.Column(db.String(300), db.ForeignKey('departments.email'))

	def __repr__(self):
		return '<Howto: {}>'.format(self.name)





class Link(db.Model):

	__tablename__ = "links"
	
	id = db.Column(db.Integer, primary_key=True, unique=True)
	link = db.Column(db.String(300))
	title = db.Column(db.String(300))
	labels = db.Column(db.String(300))
	sharewith = db.Column(db.String(300))
	comment      = db.Column(db.String(300))
	#background      = db.Column(db.String(300))
	department_id = db.Column(db.String(300), db.ForeignKey('departments.email'))

	def __repr__(self):
		return '<Link: {}>'.format(self.title)



class File(db.Model):

	__tablename__ = "files"
	
	id = db.Column(db.Integer, primary_key=True, unique=True)

	name = db.Column(db.String(300))
	description      = db.Column(db.String(300))
	#background      = db.Column(db.String(300))
	image_filename = db.Column(db.String(300), default=None, nullable=True)
	image_url = db.Column(db.String(300), default=None, nullable=True)
	department_id = db.Column(db.String(300), db.ForeignKey('departments.email'))

	def __repr__(self):
		return '<Link: {}>'.format(self.title)





# All the tables (models) for the coop admin's activities.
# Table for the decisions

class Communication(db.Model):

	__tablename__ = "communications"
	
	id = db.Column(db.Integer, primary_key=True, unique=True)
	message = db.Column(db.String(300))
	ms_from = db.Column(db.String(300))
	comment = db.Column(db.String(300))
	to = db.Column(db.String(300))
	date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
	department_id = db.Column(db.String(300), db.ForeignKey('departments.email'))

	def __repr__(self):
		return '<Communication: {}>'.format(self.message)



class Contribution(db.Model):

	__tablename__ = "contributions"
	
	id = db.Column(db.Integer, primary_key=True, unique=True)
	owner = db.Column(db.String(300))
	contributionFor = db.Column(db.String(300))
	amount = db.Column(db.String(300))
	date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
	comment     = db.Column(db.String(300))
	member_id = db.Column(db.Integer, db.ForeignKey('members.id'))

	department_id = db.Column(db.String(300), db.ForeignKey('departments.email'))

	def __repr__(self):
		return '<Contribution: {}>'.format(self.owner)








class BankAccount(db.Model):

	__tablename__ = "bankaccounts"
	
	id = db.Column(db.Integer, primary_key=True, unique=True)
	memberId = db.Column(db.String(300))
	memberName = db.Column(db.String(300))
	bankAccountNumber = db.Column(db.String(300))
	accountType = db.Column(db.String(300))
	amount = db.Column(db.String(300))
	date     = db.Column(db.String(300))
	#background      = db.Column(db.String(300))
	department_id = db.Column(db.String(300), db.ForeignKey('departments.email'))

	def __repr__(self):
		return '<BankAccount: {}>'.format(self.memberName)



#Class to create the table of members who located in all coperatives which found in ferwacotamo.
class Loan(db.Model):

	__tablename__ = "loans"
	
	id = db.Column(db.Integer, primary_key=True, unique=True)
	memberId = db.Column(db.String(300))
	memberName = db.Column(db.String(300))
	introducer1Id = db.Column(db.String(300))
	introducer1Name = db.Column(db.String(300))
	introducer1BankAccountBalance = db.Column(db.String(300))
	introducer1Share = db.Column(db.String(300))

	introducer2Id = db.Column(db.String(300))
	introducer2Name = db.Column(db.String(300))
	introducer2BankAccountBalance = db.Column(db.String(300))
	introducer2Share = db.Column(db.String(300))

	loanAmount = db.Column(db.String(300))
	interestRate = db.Column(db.String(300))
	durationInDay = db.Column(db.String(300))
	remarksIfAny = db.Column(db.String(300))

	loanType = db.Column(db.String(300))
	totalLoanWithInterest = db.Column(db.String(300))
	activedBy = db.Column(db.String(300))
	loanIssueDate = db.Column(db.String(300))
	department_id = db.Column(db.String(300), db.ForeignKey('departments.email'))


	def __repr__(self):
		return '<Loan: {}>'.format(self.memberName)








#Class to create the table of members who located in all coperatives which found in ferwacotamo.
class fixedDepositAccount(db.Model):

	__tablename__ = "fixeddepositaccounts"
	
	id = db.Column(db.Integer, primary_key=True, unique=True)
	memberId = db.Column(db.String(300))
	memberName = db.Column(db.String(300))
	fixedDepositAmount = db.Column(db.String(300))
	durationInDay = db.Column(db.String(300))
	fixedDepositInterest = db.Column(db.String(300))
	maturityDate = db.Column(db.String(300))
	matureAmount = db.Column(db.String(300))
	createdBy = db.Column(db.String(300))
	date = db.Column(db.String(300))


	#department_id = db.Column(db.String(300), db.ForeignKey('departments.email'))

	def __repr__(self):
		return '<fixedDepositAccount: {}>'.format(self.memberName)






#Class to create the table of members who located in all coperatives which found in ferwacotamo.
class Transaction(db.Model):

	__tablename__ = "transactions"
	
	id = db.Column(db.Integer, primary_key=True, unique=True)
	bankAccountNumber = db.Column(db.String(300))
	memberName = db.Column(db.String(300))
	accountType = db.Column(db.String(300))
	depositOrWithdraw = db.Column(db.String(300))
	cashOrCheque = db.Column(db.String(300))
	amount = db.Column(db.String(300))
	balance = db.Column(db.String(300))
	date = db.Column(db.String(300))


	#department_id = db.Column(db.String(300), db.ForeignKey('departments.email'))

	def __repr__(self):
		return '<Transaction: {}>'.format(self.memberName)






# Model for Share Account Transaction
class Share(db.Model):

	__tablename__ = "shares"
	
	id = db.Column(db.Integer, primary_key=True, unique=True)
	memberId = db.Column(db.String(300))
	shareAccNo = db.Column(db.String(300))
	memberName = db.Column(db.String(300))
	depositOrWithdraw = db.Column(db.String(300))
	shareAmount = db.Column(db.String(300))
	balanceShare = db.Column(db.String(300))
	date = db.Column(db.String(300))


	#department_id = db.Column(db.String(300), db.ForeignKey('departments.email'))


	def __repr__(self):
		return '<Share: {}>'.format(self.memberName)




# Model for Share Account Transaction
class Installment(db.Model):

	__tablename__ = "installments"
	
	id = db.Column(db.Integer, primary_key=True, unique=True)
	memberId = db.Column(db.String(300))
	loanId = db.Column(db.String(300))
	memberName = db.Column(db.String(300))
	lastInstallmentPay = db.Column(db.String(300))
	lastInstallmentPayDate = db.Column(db.String(300))
	cashOrCheque    =   db.Column(db.String(300))
	payLoanInstallment = db.Column(db.String(300))
	balance = db.Column(db.String(300))
	date = db.Column(db.String(300))
	remarksIfAny = db.Column(db.String(300))

	#department_id = db.Column(db.String(300), db.ForeignKey('departments.email'))

	def __repr__(self):
		return '<Installment: {}>'.format(self.memberName)



class Payment(db.Model):

	__tablename__ = 'payments'

	id = db.Column(db.Integer, primary_key=True, unique=True)
	reason = db.Column(db.String(300))
	amount = db.Column(db.String(300))
	date   = db.Column(db.String(300))

	def __repr__(self):
		return '<Payment: {}>'.format(self.reason)







# Governance Book Models.

class intekoRusange(db.Model):

	__tablename__ = "intekorusange"
	
	id = db.Column(db.Integer, primary_key=True, unique=True)
	status1 = db.Column(db.String(300))
	decision1 = db.Column(db.String(300))
	owner1    = db.Column(db.String(300))
	stakeholders1 = db.Column(db.String(300))
	due_date1     = db.Column(db.String(300))
	background1   = db.Column(db.String(300))
	department_id = db.Column(db.String(300), db.ForeignKey('departments.email'))

	def __repr__(self):
		return '<intekoRusange: {}>'.format(self.status)


	def __repr__(self):
		return '<intekoRusange: {}>'.format(self.owner)




class inamaUbuyobozi(db.Model):

	__tablename__ = "inamaubuyobozi"
	
	id = db.Column(db.Integer, primary_key=True, unique=True)
	status = db.Column(db.String(300))
	decision = db.Column(db.String(300))
	owner    = db.Column(db.String(300))
	stakeholders = db.Column(db.String(300))
	due_date     = db.Column(db.String(300))
	background   = db.Column(db.String(300))
	department_id = db.Column(db.String(300), db.ForeignKey('departments.email'))

	def __repr__(self):
		return '<inamaUbuyobozi: {}>'.format(self.status)


	def __repr__(self):
		return '<inamaUbuyobozi: {}>'.format(self.owner)


class Ubugenzuzi(db.Model):

	__tablename__ = "ubugenzuzi"
	
	id = db.Column(db.Integer, primary_key=True, unique=True)
	status = db.Column(db.String(300))
	decision = db.Column(db.String(300))
	owner    = db.Column(db.String(300))
	stakeholders = db.Column(db.String(300))
	due_date     = db.Column(db.String(300))
	background   = db.Column(db.String(300))
	department_id = db.Column(db.String(300), db.ForeignKey('departments.email'))

	def __repr__(self):
		return '<Ubugenzuzi: {}>'.format(self.status)


	def __repr__(self):
		return '<Ubugenzuzi: {}>'.format(self.owner)



# Isanduku models.
class Isanduku(db.Model):

	__tablename__ = "isanduku"
	
	id = db.Column(db.Integer, primary_key=True, unique=True)
	no = db.Column(db.String(300))
	done_date = db.Column(db.String(300))
	action    = db.Column(db.String(300))
	income = db.Column(db.String(300))
	expense     = db.Column(db.String(300))
	remain   = db.Column(db.String(300))
	done_by   = db.Column(db.String(300))
	done_to   = db.Column(db.String(300))
	department_id = db.Column(db.String(300), db.ForeignKey('departments.email'))

	def __repr__(self):
		return '<Isanduku: {}>'.format(self.action)


	def __repr__(self):
		return '<Isanduku: {}>'.format(self.action)


# Umusaruro models.
class Umusaruro(db.Model):

	__tablename__ = "umusaruro"
	
	id = db.Column(db.Integer, primary_key=True, unique=True)
	Amazina = db.Column(db.String(300))
	Taliki = db.Column(db.String(300))
	Uwagemuye = db.Column(db.String(300))
	Ibiro    = db.Column(db.String(300))
	Igiciro = db.Column(db.String(300))
	IkiguziCyose = db.Column(db.String(300))
	amafarangaYishyuweKuKiro   = db.Column(db.String(300))
	done_by   = db.Column(db.String(300))
	done_to   = db.Column(db.String(300))
	on_market = db.Column(db.Boolean, default=False)
	department_id = db.Column(db.String(300), db.ForeignKey('departments.email'))

	def __repr__(self):
		return '<Umusaruro: {}>'.format(self.Amazina)





# Goals models.
class Goal(db.Model):

	__tablename__ = "goals"
	
	id = db.Column(db.Integer, primary_key=True, unique=True)
	name = db.Column(db.String(300))
	Description = db.Column(db.String(300))
	Amount = db.Column(db.String(300))
	startingDate    = db.Column(db.String(300))
	endingDate = db.Column(db.String(300))
	paidMembers = db.Column(db.String(300))
	department_id = db.Column(db.String(300), db.ForeignKey('departments.email'))

	def __repr__(self):
		return '<Goal: {}>'.format(self.name)




# Umusaruro models.
class ibitaboByaBank(db.Model):

	__tablename__ = "ibitabobyabanks"
	
	id = db.Column(db.Integer, primary_key=True, unique=True)
	no = db.Column(db.String(300))
	date = db.Column(db.String(300))
	igikorwa = db.Column(db.String(300))
	debit    = db.Column(db.String(300))
	credit = db.Column(db.String(300))
	solde = db.Column(db.String(300))
	department_id = db.Column(db.String(300), db.ForeignKey('departments.email'))

	def __repr__(self):
		return '<ibitaboBank: {}>'.format(self.igikorwa)



class Training(db.Model):

	__tablename__ = "trainings"

	id 	 = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(300))
	trainer = db.Column(db.String(300))
	about = db.Column(db.String(300))
	description = db.Column(db.String(300))
	date 		= db.Column(db.String(300))
	is_active 	= db.Column(db.Boolean, default=False)
	department_id = db.Column(db.String(300), db.ForeignKey('departments.email'))

	def __repr__():
		return '<Training: {}>'.format(self.name)





class applyTraining(db.Model):

	__tablename__ = "applytrainings"

	id 	 = db.Column(db.Integer, primary_key=True)
	namea = db.Column(db.String(300))
	abouta = db.Column(db.String(300))
	descriptiona = db.Column(db.String(300))
	datea 		= db.Column(db.String(300))
	is_activea 	= db.Column(db.Boolean, default=False)
	department_id = db.Column(db.String(300), db.ForeignKey('departments.email'))

	def __repr__():
		return '<applyTraining: {}>'.format(self.name)




class userInfo(db.Model):

	__tablename__ = "userinfo"
	id = db.Column(db.Integer, primary_key=True)
	firstname = db.Column(db.String(300))
	secondname = db.Column(db.String(300))

	def __repr__(self):
		return '<userInfo: {}>'.format(self.firstname)

