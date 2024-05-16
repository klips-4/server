from flask import jsonify
from serializator import *
from Model.Client import Client
from flask import request
from classes.EndpointFactory import EndpointFactory

from app import app, engine, db


@app.route('/clients', methods=['POST'])
def main_route():
    request_data = request.get_json() or {}
    EndpointFactory(request_data)
    return EndpointFactory(request_data).process()

    # hui = db.session.query('select  *
    # from
    # ((SELECT nature_of_appeal, count (*) as acount
    # FROM public.clients
    # WHERE client_date_application BETWEEN '2024-01-01 00:00:00' and '2024-03-03 00:00:00'
    #  	and public.clients.result = 'done'
    # GROUP BY nature_of_appeal) a
    # full outer join
    # (SELECT nature_of_appeal, count (*) as bcount
    # FROM public.clients
    # WHERE client_date_application BETWEEN '2024-01-01 00:00:00' and '2024-03-03 00:00:00'
    #  			and public.clients.result = 'process'
    # GROUP BY nature_of_appeal) b on a.nature_of_appeal = b.nature_of_appeal)');

