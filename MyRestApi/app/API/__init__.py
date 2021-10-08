try:
    from flask import Flask
    from flask_restful import Resource, Api
    from apispec import APISpec
    from marshmallow import Schema, fields
    from apispec.ext.marshmallow import MarshmallowPlugin
    from flask_apispec.extension import FlaskApiSpec
    from flask_apispec.views import MethodResource
    from flask_apispec import marshal_with, doc, use_kwargs

    from API.ClusterHealth.views import HealthController
    from API.Name.views import NameController

    print("All modules are loaded")

except Exception as e:
    print("Error while loading the modules")


app = Flask(__name__)
api = Api(app)
app.config.update({
    'APISPEC_SPEC':APISpec(
        title='Awecome Project',
        version='v1',
        plugins=[MarshmallowPlugin()],
        openapi_version='2.0.0'
    ),
    'APISPEC_SWAGGER_URL':'/swagger/',
    'APISPEC_SWAGGER_UI_URL': '/swagger-ui/',

})
docs = FlaskApiSpec(app)
