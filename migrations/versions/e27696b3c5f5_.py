"""empty message

Revision ID: e27696b3c5f5
Revises: 
Create Date: 2018-08-09 07:50:15.801997

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e27696b3c5f5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('clients',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=True),
    sa.Column('location', sa.String(length=200), nullable=True),
    sa.Column('business', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('cooperatives',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=True),
    sa.Column('description', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('departments',
    sa.Column('id', sa.Integer(), nullable=True),
    sa.Column('no', sa.Integer(), nullable=True),
    sa.Column('code', sa.String(length=200), nullable=True),
    sa.Column('email', sa.String(length=200), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=True),
    sa.Column('regdate', sa.String(length=200), nullable=True),
    sa.Column('certificate', sa.String(length=200), nullable=True),
    sa.Column('description', sa.String(length=200), nullable=True),
    sa.Column('province', sa.String(length=200), nullable=True),
    sa.Column('district', sa.String(length=200), nullable=True),
    sa.Column('sector', sa.String(length=200), nullable=True),
    sa.Column('cell', sa.String(length=200), nullable=True),
    sa.Column('activity', sa.String(length=200), nullable=True),
    sa.Column('coop_type', sa.String(length=200), nullable=True),
    sa.Column('category', sa.String(length=200), nullable=True),
    sa.Column('field', sa.String(length=200), nullable=True),
    sa.Column('started_data', sa.String(length=200), nullable=True),
    sa.Column('starting_share', sa.Integer(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('email'),
    sa.UniqueConstraint('email')
    )
    op.create_table('federations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sno', sa.String(length=200), nullable=True),
    sa.Column('code', sa.String(length=200), nullable=True),
    sa.Column('name', sa.String(length=200), nullable=True),
    sa.Column('certificate', sa.String(length=200), nullable=True),
    sa.Column('reg_date', sa.String(length=200), nullable=True),
    sa.Column('province', sa.String(length=200), nullable=True),
    sa.Column('district', sa.String(length=200), nullable=True),
    sa.Column('sector', sa.String(length=200), nullable=True),
    sa.Column('activity', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('fixeddepositaccounts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('memberId', sa.String(length=200), nullable=True),
    sa.Column('memberName', sa.String(length=200), nullable=True),
    sa.Column('fixedDepositAmount', sa.String(length=200), nullable=True),
    sa.Column('durationInDay', sa.String(length=200), nullable=True),
    sa.Column('fixedDepositInterest', sa.String(length=200), nullable=True),
    sa.Column('maturityDate', sa.String(length=200), nullable=True),
    sa.Column('matureAmount', sa.String(length=200), nullable=True),
    sa.Column('createdBy', sa.String(length=200), nullable=True),
    sa.Column('date', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('installments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('memberId', sa.String(length=200), nullable=True),
    sa.Column('loanId', sa.String(length=200), nullable=True),
    sa.Column('memberName', sa.String(length=200), nullable=True),
    sa.Column('lastInstallmentPay', sa.String(length=200), nullable=True),
    sa.Column('lastInstallmentPayDate', sa.String(length=200), nullable=True),
    sa.Column('cashOrCheque', sa.String(length=200), nullable=True),
    sa.Column('payLoanInstallment', sa.String(length=200), nullable=True),
    sa.Column('balance', sa.String(length=200), nullable=True),
    sa.Column('date', sa.String(length=200), nullable=True),
    sa.Column('remarksIfAny', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('payments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('reason', sa.String(length=200), nullable=True),
    sa.Column('amount', sa.String(length=200), nullable=True),
    sa.Column('date', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('projects',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=True),
    sa.Column('starting_date', sa.String(length=200), nullable=True),
    sa.Column('ending_date', sa.String(length=200), nullable=True),
    sa.Column('description', sa.String(length=200), nullable=True),
    sa.Column('duration', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('roles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=60), nullable=True),
    sa.Column('description', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('shares',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('memberId', sa.String(length=200), nullable=True),
    sa.Column('shareAccNo', sa.String(length=200), nullable=True),
    sa.Column('memberName', sa.String(length=200), nullable=True),
    sa.Column('depositOrWithdraw', sa.String(length=200), nullable=True),
    sa.Column('shareAmount', sa.String(length=200), nullable=True),
    sa.Column('balanceShare', sa.String(length=200), nullable=True),
    sa.Column('date', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('transactions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('bankAccountNumber', sa.String(length=200), nullable=True),
    sa.Column('memberName', sa.String(length=200), nullable=True),
    sa.Column('accountType', sa.String(length=200), nullable=True),
    sa.Column('depositOrWithdraw', sa.String(length=200), nullable=True),
    sa.Column('cashOrCheque', sa.String(length=200), nullable=True),
    sa.Column('amount', sa.String(length=200), nullable=True),
    sa.Column('balance', sa.String(length=200), nullable=True),
    sa.Column('date', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('userinfo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('firstname', sa.String(length=200), nullable=True),
    sa.Column('secondname', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('applications',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('emailaa', sa.String(length=200), nullable=True),
    sa.Column('firstNameaa', sa.String(length=200), nullable=True),
    sa.Column('secondNameaa', sa.String(length=200), nullable=True),
    sa.Column('othersaa', sa.String(length=200), nullable=True),
    sa.Column('Districtaa', sa.String(length=200), nullable=True),
    sa.Column('Sectoraa', sa.String(length=200), nullable=True),
    sa.Column('Cellaa', sa.String(length=200), nullable=True),
    sa.Column('nIdaa', sa.String(length=200), nullable=True),
    sa.Column('entryDateaa', sa.String(length=200), nullable=True),
    sa.Column('shareaa', sa.String(length=200), nullable=True),
    sa.Column('exitDateaa', sa.String(length=200), nullable=True),
    sa.Column('umuzunguraaa', sa.String(length=200), nullable=True),
    sa.Column('umukonoaa', sa.String(length=200), nullable=True),
    sa.Column('genderaa', sa.String(length=200), nullable=True),
    sa.Column('dobaa', sa.String(length=200), nullable=True),
    sa.Column('phoneaa', sa.String(length=200), nullable=True),
    sa.Column('Amashuriaa', sa.String(length=200), nullable=True),
    sa.Column('Ubumugaaa', sa.String(length=200), nullable=True),
    sa.Column('department_id', sa.String(length=200), nullable=True),
    sa.ForeignKeyConstraint(['department_id'], ['departments.email'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('applytrainings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('namea', sa.String(length=200), nullable=True),
    sa.Column('abouta', sa.String(length=200), nullable=True),
    sa.Column('descriptiona', sa.String(length=200), nullable=True),
    sa.Column('datea', sa.String(length=200), nullable=True),
    sa.Column('is_activea', sa.Boolean(), nullable=True),
    sa.Column('department_id', sa.String(length=200), nullable=True),
    sa.ForeignKeyConstraint(['department_id'], ['departments.email'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('bankaccounts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('memberId', sa.String(length=200), nullable=True),
    sa.Column('memberName', sa.String(length=200), nullable=True),
    sa.Column('bankAccountNumber', sa.String(length=200), nullable=True),
    sa.Column('accountType', sa.String(length=200), nullable=True),
    sa.Column('amount', sa.String(length=200), nullable=True),
    sa.Column('date', sa.String(length=200), nullable=True),
    sa.Column('department_id', sa.String(length=200), nullable=True),
    sa.ForeignKeyConstraint(['department_id'], ['departments.email'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('communications',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('message', sa.String(length=200), nullable=True),
    sa.Column('ms_from', sa.String(length=200), nullable=True),
    sa.Column('comment', sa.String(length=200), nullable=True),
    sa.Column('to', sa.String(length=200), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('department_id', sa.String(length=200), nullable=True),
    sa.ForeignKeyConstraint(['department_id'], ['departments.email'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('decisions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('status', sa.String(length=200), nullable=True),
    sa.Column('decision', sa.String(length=200), nullable=True),
    sa.Column('owner', sa.String(length=200), nullable=True),
    sa.Column('stakeholders', sa.String(length=200), nullable=True),
    sa.Column('due_date', sa.String(length=200), nullable=True),
    sa.Column('background', sa.String(length=200), nullable=True),
    sa.Column('department_id', sa.String(length=200), nullable=True),
    sa.ForeignKeyConstraint(['department_id'], ['departments.email'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('employees',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=60), nullable=True),
    sa.Column('username', sa.String(length=60), nullable=True),
    sa.Column('first_name', sa.String(length=60), nullable=True),
    sa.Column('last_name', sa.String(length=60), nullable=True),
    sa.Column('phone_number', sa.String(length=200), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('department_id', sa.String(length=200), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.Column('project_id', sa.Integer(), nullable=True),
    sa.Column('employee_id', sa.Integer(), nullable=True),
    sa.Column('cooperative_id', sa.Integer(), nullable=True),
    sa.Column('is_admin', sa.Boolean(), nullable=True),
    sa.Column('is_coop_admin', sa.Boolean(), nullable=True),
    sa.Column('is_overall', sa.Boolean(), nullable=True),
    sa.Column('is_invited', sa.Boolean(), nullable=True),
    sa.Column('is_union', sa.Boolean(), nullable=True),
    sa.Column('is_ferwacotamo', sa.Boolean(), nullable=True),
    sa.Column('is_confederation', sa.Boolean(), nullable=True),
    sa.Column('is_rca', sa.Boolean(), nullable=True),
    sa.Column('invited_by', sa.String(length=200), nullable=True),
    sa.Column('district', sa.String(length=200), nullable=True),
    sa.ForeignKeyConstraint(['cooperative_id'], ['cooperatives.id'], ),
    sa.ForeignKeyConstraint(['department_id'], ['departments.email'], ),
    sa.ForeignKeyConstraint(['employee_id'], ['employees.id'], ),
    sa.ForeignKeyConstraint(['project_id'], ['projects.id'], ),
    sa.ForeignKeyConstraint(['role_id'], ['roles.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_employees_email'), 'employees', ['email'], unique=False)
    op.create_index(op.f('ix_employees_first_name'), 'employees', ['first_name'], unique=False)
    op.create_index(op.f('ix_employees_last_name'), 'employees', ['last_name'], unique=False)
    op.create_index(op.f('ix_employees_phone_number'), 'employees', ['phone_number'], unique=False)
    op.create_index(op.f('ix_employees_username'), 'employees', ['username'], unique=False)
    op.create_table('files',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=True),
    sa.Column('description', sa.String(length=200), nullable=True),
    sa.Column('image_filename', sa.String(length=200), nullable=True),
    sa.Column('image_url', sa.String(length=200), nullable=True),
    sa.Column('department_id', sa.String(length=200), nullable=True),
    sa.ForeignKeyConstraint(['department_id'], ['departments.email'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('goals',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=True),
    sa.Column('Description', sa.String(length=200), nullable=True),
    sa.Column('Amount', sa.String(length=200), nullable=True),
    sa.Column('startingDate', sa.String(length=200), nullable=True),
    sa.Column('endingDate', sa.String(length=200), nullable=True),
    sa.Column('paidMembers', sa.String(length=200), nullable=True),
    sa.Column('department_id', sa.String(length=200), nullable=True),
    sa.ForeignKeyConstraint(['department_id'], ['departments.email'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('howtos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=True),
    sa.Column('labels', sa.String(length=200), nullable=True),
    sa.Column('description', sa.String(length=200), nullable=True),
    sa.Column('steps', sa.String(length=200), nullable=True),
    sa.Column('file', sa.String(length=200), nullable=True),
    sa.Column('department_id', sa.String(length=200), nullable=True),
    sa.ForeignKeyConstraint(['department_id'], ['departments.email'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('ibitabobyabanks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('no', sa.String(length=200), nullable=True),
    sa.Column('date', sa.String(length=200), nullable=True),
    sa.Column('igikorwa', sa.String(length=200), nullable=True),
    sa.Column('debit', sa.String(length=200), nullable=True),
    sa.Column('credit', sa.String(length=200), nullable=True),
    sa.Column('solde', sa.String(length=200), nullable=True),
    sa.Column('department_id', sa.String(length=200), nullable=True),
    sa.ForeignKeyConstraint(['department_id'], ['departments.email'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('inamaubuyobozi',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('status', sa.String(length=200), nullable=True),
    sa.Column('decision', sa.String(length=200), nullable=True),
    sa.Column('owner', sa.String(length=200), nullable=True),
    sa.Column('stakeholders', sa.String(length=200), nullable=True),
    sa.Column('due_date', sa.String(length=200), nullable=True),
    sa.Column('background', sa.String(length=200), nullable=True),
    sa.Column('department_id', sa.String(length=200), nullable=True),
    sa.ForeignKeyConstraint(['department_id'], ['departments.email'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('intekorusange',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('status1', sa.String(length=200), nullable=True),
    sa.Column('decision1', sa.String(length=200), nullable=True),
    sa.Column('owner1', sa.String(length=200), nullable=True),
    sa.Column('stakeholders1', sa.String(length=200), nullable=True),
    sa.Column('due_date1', sa.String(length=200), nullable=True),
    sa.Column('background1', sa.String(length=200), nullable=True),
    sa.Column('department_id', sa.String(length=200), nullable=True),
    sa.ForeignKeyConstraint(['department_id'], ['departments.email'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('isanduku',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('no', sa.String(length=200), nullable=True),
    sa.Column('done_date', sa.String(length=200), nullable=True),
    sa.Column('action', sa.String(length=200), nullable=True),
    sa.Column('income', sa.String(length=200), nullable=True),
    sa.Column('expense', sa.String(length=200), nullable=True),
    sa.Column('remain', sa.String(length=200), nullable=True),
    sa.Column('done_by', sa.String(length=200), nullable=True),
    sa.Column('done_to', sa.String(length=200), nullable=True),
    sa.Column('department_id', sa.String(length=200), nullable=True),
    sa.ForeignKeyConstraint(['department_id'], ['departments.email'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('links',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('link', sa.String(length=200), nullable=True),
    sa.Column('title', sa.String(length=200), nullable=True),
    sa.Column('labels', sa.String(length=200), nullable=True),
    sa.Column('sharewith', sa.String(length=200), nullable=True),
    sa.Column('comment', sa.String(length=200), nullable=True),
    sa.Column('department_id', sa.String(length=200), nullable=True),
    sa.ForeignKeyConstraint(['department_id'], ['departments.email'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('loans',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('memberId', sa.String(length=200), nullable=True),
    sa.Column('memberName', sa.String(length=200), nullable=True),
    sa.Column('introducer1Id', sa.String(length=200), nullable=True),
    sa.Column('introducer1Name', sa.String(length=200), nullable=True),
    sa.Column('introducer1BankAccountBalance', sa.String(length=200), nullable=True),
    sa.Column('introducer1Share', sa.String(length=200), nullable=True),
    sa.Column('introducer2Id', sa.String(length=200), nullable=True),
    sa.Column('introducer2Name', sa.String(length=200), nullable=True),
    sa.Column('introducer2BankAccountBalance', sa.String(length=200), nullable=True),
    sa.Column('introducer2Share', sa.String(length=200), nullable=True),
    sa.Column('loanAmount', sa.String(length=200), nullable=True),
    sa.Column('interestRate', sa.String(length=200), nullable=True),
    sa.Column('durationInDay', sa.String(length=200), nullable=True),
    sa.Column('remarksIfAny', sa.String(length=200), nullable=True),
    sa.Column('loanType', sa.String(length=200), nullable=True),
    sa.Column('totalLoanWithInterest', sa.String(length=200), nullable=True),
    sa.Column('activedBy', sa.String(length=200), nullable=True),
    sa.Column('loanIssueDate', sa.String(length=200), nullable=True),
    sa.Column('department_id', sa.String(length=200), nullable=True),
    sa.ForeignKeyConstraint(['department_id'], ['departments.email'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('members',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sno', sa.String(length=200), nullable=True),
    sa.Column('izinaRibanza', sa.String(length=200), nullable=True),
    sa.Column('izinaRikurikira', sa.String(length=200), nullable=True),
    sa.Column('Ayandi', sa.String(length=200), nullable=True),
    sa.Column('Igitsina', sa.String(length=200), nullable=True),
    sa.Column('indangamuntu', sa.String(length=200), nullable=True),
    sa.Column('tarikiYamavuko', sa.String(length=200), nullable=True),
    sa.Column('Intara', sa.String(length=200), nullable=True),
    sa.Column('Akarere', sa.String(length=200), nullable=True),
    sa.Column('Umurenge', sa.String(length=200), nullable=True),
    sa.Column('Akagari', sa.String(length=200), nullable=True),
    sa.Column('Umudugudu', sa.String(length=200), nullable=True),
    sa.Column('tarikiYinjiriye', sa.String(length=200), nullable=True),
    sa.Column('Umugabane', sa.String(length=200), nullable=True),
    sa.Column('Umukono', sa.String(length=200), nullable=True),
    sa.Column('nomeroYaTelephone', sa.String(length=200), nullable=True),
    sa.Column('Amashuri', sa.String(length=200), nullable=True),
    sa.Column('Ubumuga', sa.String(length=200), nullable=True),
    sa.Column('Arubatse', sa.String(length=200), nullable=True),
    sa.Column('umubareWabana', sa.String(length=200), nullable=True),
    sa.Column('icyiciroCyubudehe', sa.String(length=200), nullable=True),
    sa.Column('Ubwishingizi', sa.String(length=200), nullable=True),
    sa.Column('akaziAkoraMuriCoop', sa.String(length=200), nullable=True),
    sa.Column('akandiKazi', sa.String(length=200), nullable=True),
    sa.Column('ubusoAhingaho', sa.String(length=200), nullable=True),
    sa.Column('ubwokoBwigihingwa', sa.String(length=200), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.Column('department_id', sa.String(length=200), nullable=True),
    sa.ForeignKeyConstraint(['department_id'], ['departments.email'], ),
    sa.ForeignKeyConstraint(['role_id'], ['roles.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('notifications',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('action', sa.String(length=200), nullable=True),
    sa.Column('done_by', sa.String(length=200), nullable=True),
    sa.Column('done_from', sa.String(length=200), nullable=True),
    sa.Column('done_date', sa.DateTime(), nullable=True),
    sa.Column('done_time', sa.String(length=200), nullable=True),
    sa.Column('done_to', sa.String(length=200), nullable=True),
    sa.Column('effect', sa.String(length=200), nullable=True),
    sa.Column('department_id', sa.String(length=200), nullable=True),
    sa.ForeignKeyConstraint(['department_id'], ['departments.email'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('ordes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=True),
    sa.Column('product', sa.String(length=200), nullable=True),
    sa.Column('description', sa.String(length=200), nullable=True),
    sa.Column('quantity', sa.String(length=200), nullable=True),
    sa.Column('in_date', sa.String(length=200), nullable=True),
    sa.Column('status', sa.String(length=200), nullable=True),
    sa.Column('department_id', sa.String(length=200), nullable=True),
    sa.ForeignKeyConstraint(['department_id'], ['departments.email'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=80), nullable=True),
    sa.Column('body', sa.Text(), nullable=True),
    sa.Column('pub_date', sa.DateTime(), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('products',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=True),
    sa.Column('description', sa.String(length=200), nullable=True),
    sa.Column('quantity', sa.String(length=200), nullable=True),
    sa.Column('in_date', sa.String(length=200), nullable=True),
    sa.Column('status', sa.String(length=200), nullable=True),
    sa.Column('department_id', sa.String(length=200), nullable=True),
    sa.ForeignKeyConstraint(['department_id'], ['departments.email'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('reports',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('status', sa.String(length=200), nullable=True),
    sa.Column('project', sa.String(length=200), nullable=True),
    sa.Column('task', sa.String(length=200), nullable=True),
    sa.Column('description', sa.String(length=200), nullable=True),
    sa.Column('notes', sa.String(length=200), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('department_id', sa.String(length=200), nullable=True),
    sa.ForeignKeyConstraint(['department_id'], ['departments.email'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('trainings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=True),
    sa.Column('trainer', sa.String(length=200), nullable=True),
    sa.Column('about', sa.String(length=200), nullable=True),
    sa.Column('description', sa.String(length=200), nullable=True),
    sa.Column('date', sa.String(length=200), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('department_id', sa.String(length=200), nullable=True),
    sa.ForeignKeyConstraint(['department_id'], ['departments.email'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('ubugenzuzi',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('status', sa.String(length=200), nullable=True),
    sa.Column('decision', sa.String(length=200), nullable=True),
    sa.Column('owner', sa.String(length=200), nullable=True),
    sa.Column('stakeholders', sa.String(length=200), nullable=True),
    sa.Column('due_date', sa.String(length=200), nullable=True),
    sa.Column('background', sa.String(length=200), nullable=True),
    sa.Column('department_id', sa.String(length=200), nullable=True),
    sa.ForeignKeyConstraint(['department_id'], ['departments.email'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('umusaruro',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('Amazina', sa.String(length=200), nullable=True),
    sa.Column('Taliki', sa.String(length=200), nullable=True),
    sa.Column('Uwagemuye', sa.String(length=200), nullable=True),
    sa.Column('Ibiro', sa.String(length=200), nullable=True),
    sa.Column('Igiciro', sa.String(length=200), nullable=True),
    sa.Column('IkiguziCyose', sa.String(length=200), nullable=True),
    sa.Column('amafarangaYishyuweKuKiro', sa.String(length=200), nullable=True),
    sa.Column('done_by', sa.String(length=200), nullable=True),
    sa.Column('done_to', sa.String(length=200), nullable=True),
    sa.Column('on_market', sa.Boolean(), nullable=True),
    sa.Column('department_id', sa.String(length=200), nullable=True),
    sa.ForeignKeyConstraint(['department_id'], ['departments.email'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('unions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sno', sa.String(length=200), nullable=True),
    sa.Column('code', sa.String(length=200), nullable=True),
    sa.Column('name', sa.String(length=200), nullable=True),
    sa.Column('certificate', sa.String(length=200), nullable=True),
    sa.Column('reg_date', sa.String(length=200), nullable=True),
    sa.Column('province', sa.String(length=200), nullable=True),
    sa.Column('district', sa.String(length=200), nullable=True),
    sa.Column('sector', sa.String(length=200), nullable=True),
    sa.Column('activity', sa.String(length=200), nullable=True),
    sa.Column('federation_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['federation_id'], ['federations.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('contributions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('owner', sa.String(length=200), nullable=True),
    sa.Column('contributionFor', sa.String(length=200), nullable=True),
    sa.Column('amount', sa.String(length=200), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('comment', sa.String(length=200), nullable=True),
    sa.Column('member_id', sa.Integer(), nullable=True),
    sa.Column('department_id', sa.String(length=200), nullable=True),
    sa.ForeignKeyConstraint(['department_id'], ['departments.email'], ),
    sa.ForeignKeyConstraint(['member_id'], ['members.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('motos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=True),
    sa.Column('plate', sa.String(length=200), nullable=True),
    sa.Column('owner', sa.String(length=200), nullable=True),
    sa.Column('owner_tel', sa.String(length=200), nullable=True),
    sa.Column('member_id', sa.Integer(), nullable=True),
    sa.Column('department_id', sa.String(length=200), nullable=True),
    sa.ForeignKeyConstraint(['department_id'], ['departments.email'], ),
    sa.ForeignKeyConstraint(['member_id'], ['members.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('profiles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('primary_school', sa.String(length=200), nullable=True),
    sa.Column('secondary_school', sa.String(length=200), nullable=True),
    sa.Column('university_school', sa.String(length=200), nullable=True),
    sa.Column('vocational_school', sa.String(length=200), nullable=True),
    sa.Column('exp1', sa.String(length=200), nullable=True),
    sa.Column('exp2', sa.String(length=200), nullable=True),
    sa.Column('exp3', sa.String(length=200), nullable=True),
    sa.Column('strn1', sa.String(length=200), nullable=True),
    sa.Column('strn2', sa.String(length=200), nullable=True),
    sa.Column('strn3', sa.String(length=200), nullable=True),
    sa.Column('car1', sa.String(length=200), nullable=True),
    sa.Column('car2', sa.String(length=200), nullable=True),
    sa.Column('car3', sa.String(length=200), nullable=True),
    sa.Column('inter1', sa.String(length=200), nullable=True),
    sa.Column('inter2', sa.String(length=200), nullable=True),
    sa.Column('inter3', sa.String(length=200), nullable=True),
    sa.Column('district', sa.String(length=200), nullable=True),
    sa.Column('employee_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['employee_id'], ['employees.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('subs',
    sa.Column('employee_id', sa.Integer(), nullable=True),
    sa.Column('department_id', sa.String(length=399), nullable=True),
    sa.ForeignKeyConstraint(['department_id'], ['departments.email'], ),
    sa.ForeignKeyConstraint(['employee_id'], ['employees.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('subs')
    op.drop_table('profiles')
    op.drop_table('motos')
    op.drop_table('contributions')
    op.drop_table('unions')
    op.drop_table('umusaruro')
    op.drop_table('ubugenzuzi')
    op.drop_table('trainings')
    op.drop_table('reports')
    op.drop_table('products')
    op.drop_table('post')
    op.drop_table('ordes')
    op.drop_table('notifications')
    op.drop_table('members')
    op.drop_table('loans')
    op.drop_table('links')
    op.drop_table('isanduku')
    op.drop_table('intekorusange')
    op.drop_table('inamaubuyobozi')
    op.drop_table('ibitabobyabanks')
    op.drop_table('howtos')
    op.drop_table('goals')
    op.drop_table('files')
    op.drop_index(op.f('ix_employees_username'), table_name='employees')
    op.drop_index(op.f('ix_employees_phone_number'), table_name='employees')
    op.drop_index(op.f('ix_employees_last_name'), table_name='employees')
    op.drop_index(op.f('ix_employees_first_name'), table_name='employees')
    op.drop_index(op.f('ix_employees_email'), table_name='employees')
    op.drop_table('employees')
    op.drop_table('decisions')
    op.drop_table('communications')
    op.drop_table('bankaccounts')
    op.drop_table('applytrainings')
    op.drop_table('applications')
    op.drop_table('userinfo')
    op.drop_table('transactions')
    op.drop_table('shares')
    op.drop_table('roles')
    op.drop_table('projects')
    op.drop_table('payments')
    op.drop_table('installments')
    op.drop_table('fixeddepositaccounts')
    op.drop_table('federations')
    op.drop_table('departments')
    op.drop_table('cooperatives')
    op.drop_table('clients')
    op.drop_table('category')
    # ### end Alembic commands ###
