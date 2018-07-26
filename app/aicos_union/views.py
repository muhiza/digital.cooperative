from flask import Flask
from . import aicos_union



@aicos_union.route('/')
def indexUnion():
	return "Hello Unions"

