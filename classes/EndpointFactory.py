from Model.Client import Client
from app import db


class EndpointFactory:

    def __init__(self, params: dict):
        self._check_params(params)
        self._extract_params(params)

    def _check_params(self, params: dict):
        if not params:
            params = {}

        self._method_name = params.get('method')

        if not self._method_name:
            raise RuntimeError('Не передано название метода')

    def _extract_params(self, params: dict):
        self._method = self._method_name
        data = params.get('params') or {}

        filters = params.get('filter') or {}

        self.active = data.get('active') or {}
        self.clientsId = data.get('clientsItem') or []
        self.color = data.get('color')

        for client_id in self.clientsId:
            client = Client.query.get(client_id)
            if client:
                client.result = self.active
                client.color = self.color
                db.session.commit()

        return data, self.active, self.clientsId
