from dotenv import load_dotenv
load_dotenv()

try:
    from API import (app, api, HealthController, NameController, docs)
except Exception as e:
    print("Modules are Missing: {}".format(e))

api.add_resource(HealthController, '/health_check')
docs.register(HealthController)
api.add_resource(NameController, '/greet_person')
docs.register(NameController)