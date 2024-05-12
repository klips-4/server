def to_dict(param):
    serialized_param = [
        {'id': entity.id, 'client_name': entity.client_name, 'client_surname': entity.client_surname,
         'client_patronymic': entity.client_patronymic, 'client_date_application': entity.client_date_application,
         'client_executor': entity. client_executor, 'nature_of_appeal': entity.nature_of_appeal,
         'result': entity.result, 'color': entity.color
         }
        for entity in param
    ]

    return serialized_param
