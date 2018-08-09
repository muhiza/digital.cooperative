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
    izina_ribanza =  StringField("Izina ribanza", validators=[DataRequired()], render_kw={"placeholder": "Injizamo Izina ribanza"})
    izina_rikurikira =  StringField("Izina rikurikira", validators=[DataRequired()], render_kw={"placeholder": "Injizamo Izina rikurikira"})
    ayandi =  StringField("Ayandi (Singombwa)", render_kw={"placeholder": "Ayandi (Singombwa)"})
    igitsina =  SelectField(
        'Igitsina',
        choices=[('Igitsina', 'Igitsina'), ('Gabo', 'Gabo'), ('Gole', 'Gole'), ('Ibindi', 'Ibindi')])
    indangamuntu =  StringField("Indangamuntu", validators=[DataRequired()], render_kw={"placeholder": "Injiza nomero y'indangamuntu"})
    code =  StringField("Code", validators=[DataRequired()], render_kw={"placeholder": "Shyiramo code y'umunyamuryango"})
    
    tariki_yavukiye =  DateField("Tariki y'amavuko", format='%Y-%m-%d', validators=[DataRequired()])
    intara =  StringField("Intara", validators=[DataRequired()], render_kw={"placeholder": "Injiza intara"})
    akarere =  StringField("Akarere", validators=[DataRequired()], render_kw={"placeholder": "Injiza akarere"})
    umurenge =  StringField("Umurenge", validators=[DataRequired()], render_kw={"placeholder": "Injiza umurenge"})
    akagari =  StringField("Akagari", validators=[DataRequired()], render_kw={"placeholder": "Injiza akagari"})
    
    umudugudu =  StringField("Umudugudu", validators=[DataRequired()], render_kw={"placeholder": "Injizamo Umudugudu"})
    tariki_yinjiriye =  StringField("Taliki y'injiriye", validators=[DataRequired()], render_kw={"placeholder": "Injizamo Itariki umunyamuryango yinjiriye"})
    umugabane = StringField("Umugabane", validators=[DataRequired()], render_kw={"placeholder": "Injizamo Umugabane w'umunyamuryango"})
    umukono     =  StringField("Umukono", validators=[DataRequired()], render_kw={"placeholder": "Injizamo Umukono w'umunyamuryango"})  
    nomero_ya_telephone = StringField("Nimero ya telephone", validators=[DataRequired()], render_kw={"placeholder": "Shyiramo numero ya telephone"})
    
    amashuri = SelectField(
        'Amashuri',
        choices=[('Amashuri', 'Amashuri'), ('Abatarize', 'Abatarize'), ('Abanza', 'Abanza'), ('Ayisumbuye', 'Ayisumbuye'), 
                 ('Kaminuza', 'Kaminuza'), ('Imyuga', 'Imyuga')])
    ubumuga = SelectField(
    'Ubumuga',
    choices=[('Ubumuga', 'Ubumuga'), ('Amaguru', 'Amaguru'), ('Amaboko', 'Amaboko'), ('Kutabona', 'Kutabona'), 
             ('Kutumva', 'Kutumva'), ('Mu mutwe', 'Mu mutwe'), ('Ibindi', 'Ibindi')])
    arubatse = SelectField(
    'Arubatse',
    choices=[('Arubatse', 'Arubatse'), ('Yego', 'Yego'), ('Oya', 'Oya')])
    umubare_wabana = StringField("Umubare w'abana", validators=[DataRequired()], render_kw={"placeholder": "Shyiramo Umubare w'abana"})
    icyiciro_cyubudehe = StringField("Icyiciro cy'ubudehe", validators=[DataRequired()], render_kw={"placeholder": "Icyiciro cy'ubudehe"})
    ubwishingizi = StringField("Ubwishingizi", validators=[DataRequired()], render_kw={"placeholder": "Shyiramo ubwishingizi bw'umunyamuryango"})    
    akazi_akora_muri_koperative = StringField("Akazi Akora Muri Koperative", validators=[DataRequired()], render_kw={"placeholder": "Shyiramo akazi umunyamuryango akora muri Koperative"})
    akandi_kazi_akora = StringField("Akandi kazi akora", validators=[DataRequired()], render_kw={"placeholder": "Shyiramo Akandi kazi akora"})
    ubuso_ahingaho  = StringField("Ubuso ahingaho icyayi", validators=[DataRequired()], render_kw={"placeholder": "Shyiramo Ubuso ahingaho icyayi"})
    
    ubwoko_bwigihingwa = StringField("Ubwoko bw'igihingwa (Icyayi)", validators=[DataRequired()], render_kw={"placeholder": "Shyiramo Ubwoko bw'igihingwa (Cy'icyayi)"})
    ubuso_ahingaho_ibindi  = StringField("Ubuso ahingaho ibindi", validators=[DataRequired()], render_kw={"placeholder": "Shyiramo Ubuso ahingaho ibindi"})
    ubwoko_bwigihingwa_kindi = StringField("Ubwoko bw'ikindi gihingwa", validators=[DataRequired()], render_kw={"placeholder": "Shyiramo Ubwoko bw'ikindi gihingwa ahinga"})
    ubuso_budakoreshwa  = StringField("Ubuso budakoreshwa", validators=[DataRequired()], render_kw={"placeholder": "Shyiramo Ubuso bundi budakoreshwa"})
    


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






