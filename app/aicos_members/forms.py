from flask_wtf import FlaskForm
from flask_login import login_required, current_user
from wtforms import StringField, TextAreaField, FileField, DateTimeField, SelectField, SubmitField, IntegerField
from wtforms.fields.html5 import DateField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Email


#from ..models import Department, Role, Employee, Product
from ..models import *


from flask_wtf.file import FileField, FileAllowed, FileRequired
from .. import images



class RoleForm(FlaskForm):
    """
    Form for admin to add or edit a role
    """
    name = StringField('Name', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit')








class ReportForm(FlaskForm):
    """
    Form for admin to add or edit a role
    """
    status = SelectField(
        'Status',
        choices=[('Uko bihagaze', 'Uko bihagaze'), ('Byararangiye', 'Byararangiye'), ('Biracyakomeje', 'Biracyakomeje'), 
                ('Ntibiratangira gukorwaho', 'Ntibiratangira gukorwaho')])
    project = StringField('Izina ry umushinga', validators=[DataRequired()], render_kw={"placeholder": "Andika Izina ry'umushinga"})
    task = StringField('Izina ry igikorwa', validators=[DataRequired()], render_kw={"placeholder": "Andika izina ry'igikorwa"})
    description = TextAreaField('Ubusobanuro', validators=[DataRequired()], render_kw={"placeholder": "Andika Ubusobanuro"})
    notes = TextAreaField('Andika ibindi (Ntago ari ngombwa)', validators=[DataRequired()], render_kw={"placeholder": "Andika ibindi (Ntago ari ngombwa)"})
    submit = SubmitField('Ohereza')






class DecForm(FlaskForm):
    #status = SelectField(
        #'status',
        #choices=[('nt', 'Not Started'), ('ip', 'In progress'), ('dc', 'Decided')])
    status = SelectField(
        'Status',
        choices=[('Not Started', 'Not Started'), ('In Progress', 'In progress'), ('Decided', 'Decided')])
    decision =  StringField("Decision", validators=[DataRequired()])
    #owner    =  StringField("Owner", validators=[DataRequired()])
    owner = QuerySelectField(query_factory=lambda: Employee.query.filter_by(first_name=current_user.first_name), get_label="first_name")
    stakeholders = StringField("Stakeholders", validators=[DataRequired()])
    due_date    =  DateField("Due date",format='%Y-%m-%d', validators=[DataRequired()])
    background  =  StringField("Background", validators=[DataRequired()])
    #department_id  =  StringField("Department Id", validators=[DataRequired()])

    submit      =  SubmitField('Create')









class MemberForm(FlaskForm):
    firstNamex =  StringField("Izina ribanza", validators=[DataRequired()], render_kw={"placeholder": "Injizamo Izina ribanza"})
    secondNamex =  StringField("Izina rikurikira", validators=[DataRequired()], render_kw={"placeholder": "Injizamo Izina rikurikira"})
    othersx =  StringField("Ayandi (Singombwa)", render_kw={"placeholder": "Ayandi (Singombwa)"})
    Districtx =  StringField("Akarere", validators=[DataRequired()], render_kw={"placeholder": "Injizamo Akarere"})
    Sectorx =  StringField("Umurenge", validators=[DataRequired()], render_kw={"placeholder": "Injizamo Umurenge"})
    Cellx =  StringField("Akagari", validators=[DataRequired()], render_kw={"placeholder": "Injizamo akagari"})
    nIdx =  IntegerField("Nimero ndangamuntu", validators=[DataRequired()], render_kw={"placeholder": "Injiza Nimero y'indangamuntu"})
    entryDatex =  DateField("Tariki yinjiriyemo",format='%Y-%m-%d', validators=[DataRequired()])
    sharex =  IntegerField("Umugabane", validators=[DataRequired()], render_kw={"placeholder": "Injizamo Umugabane"})
    exitDatex =  DateField("Tariki yasohokeyemo",format='%Y-%m-%d', validators=[DataRequired()])
    umuzungurax =  StringField("Umuzungura", validators=[DataRequired()], render_kw={"placeholder": "Injizamo Umuzungura"})
    umukonox =  StringField("Umukono", validators=[DataRequired()], render_kw={"placeholder": "Injizamo Umukono"})
    genderx = SelectField(
        'Igitsina',
        choices=[('Igitsina', 'Igitsina'), ('Gabo', 'Gabo'), ('Gole', 'Gole'), ('Ibindi', 'Ibindi')])
    dobx     =  DateField("Tariki y'amavuko", format='%Y-%m-%d', validators=[DataRequired()])  
    phonex = StringField("Nimero ya telephone", validators=[DataRequired()], render_kw={"placeholder": "Shyiramo numero ya telephone"})
    amashurix = SelectField(
        'Amashuri',
        choices=[('Amashuri', 'Amashuri'), ('Abatarize', 'Abatarize'), ('Abanza', 'Abanza'), ('Ayisumbuye', 'Ayisumbuye'), 
                 ('Kaminuza', 'Kaminuza'), ('Imyuga', 'Imyuga')])
    ubumugax = SelectField(
    'Ubumuga',
    choices=[('Ubumuga', 'Ubumuga'), ('Amaguru', 'Amaguru'), ('Amaboko', 'Amaboko'), ('Kutabona', 'Kutabona'), 
             ('Kutumva', 'Kutumva'), ('Mu mutwe', 'Mu mutwe'), ('Ibindi', 'Ibindi')])
    """
    Current Comment
    ==========================
    #owner    =  StringField("Owner", validators=[DataRequired()])
    #owner    =  StringField("Owner", validators=[DataRequired()])
    #owner    =  StringField("Owner", validators=[DataRequired()])
    #owner    =  StringField("Owner", validators=[DataRequired()])
    """
    submit      =  SubmitField('Injiza Umunyamuryango')



class EmployeeAssignForm(FlaskForm):
    """
    Form for admin to assign departments and roles to employees
    """
    cooperative = QuerySelectField(query_factory=lambda: Department.query.filter_by(email='justin@gmail.com'),
                                  get_label="name")
    role = QuerySelectField(query_factory=lambda: Role.query.filter_by(name='President'),
                            get_label="name")
    submit = SubmitField('Submit')





class PaymentForm(FlaskForm):
    #status = SelectField(
        #'status',
        #choices=[('nt', 'Not Started'), ('ip', 'In progress'), ('dc', 'Decided')])
    reason = SelectField(
        'Status',
        choices=[('Reason', 'none'), ('Umusanzu', 'Umusanzu'), ('Umugabane', 'Umugabane'),
        ('Amande', 'Amande')])
    amount =  StringField("Decision", validators=[DataRequired()])
    #owner    =  StringField("Owner", validators=[DataRequired()])
    date    =  DateField("Due date", format='%Y-%m-%d', validators=[DataRequired()])
    #department_id  =  StringField("Department Id", validators=[DataRequired()])
    submit      =  SubmitField('Save')


class communicationForm(FlaskForm):
    #status = SelectField(
        #'status',
        #choices=[('nt', 'Not Started'), ('ip', 'In progress'), ('dc', 'Decided')])
    ms_from = StringField("Message From", validators=[DataRequired()], render_kw={"placeholder": "Enter Subject"})
    to = SelectField(
        'Message To',
        choices=[('All members', 'All members'), ('All female member', 'All female member'),
         ('All male member', 'All male member'), ('Non members', 'Non members')])
    message =  TextAreaField("Message", validators=[DataRequired()], render_kw={"placeholder": "Enter Message content"})
    #owner    =  StringField("Owner", validators=[DataRequired()])
    comment = TextAreaField("Comment", validators=[DataRequired()], render_kw={"placeholder": "Enter Comment (Optional)"})
    #department_id  =  StringField("Department Id", validators=[DataRequired()])
    submit      =  SubmitField('Send')





class GoalForm(FlaskForm):

    #status = SelectField(
        #'status',
        #choices=[('nt', 'Not Started'), ('ip', 'In progress'), ('dc', 'Decided')])

    name =  StringField("Izina ry'igikorwa", validators=[DataRequired()], render_kw={"placeholder": "Andika izina ry'igikorwa"})
    description =  TextAreaField("Ubusobanuro", validators=[DataRequired()], render_kw={"placeholder": "Andika ubusobanuro bw'igikorwa"})
    amount =  StringField("Amafaranga agomba gutangwa", validators=[DataRequired()], render_kw={"placeholder": "Andika amafaranga akenewe"})
    startingDate     =  DateField("Tariki igikorwa gitangiriye", format='%Y-%m-%d', validators=[DataRequired()],)  
    endingDate     =  DateField("Tariki igikorwa kizarangirira", format='%Y-%m-%d', validators=[DataRequired()])  

    submit      =  SubmitField('Emeza')






