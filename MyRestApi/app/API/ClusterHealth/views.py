try:
    from flask import Flask
    from flask_restful import Api, Resource
    from apispec import APISpec
    from marshmallow import Schema, fields
    from apispec.ext.marshmallow import MarshmallowPlugin
    from flask_apispec.extension import FlaskApiSpec
    from flask_apispec.views import MethodResource
    from flask_apispec import marshal_with, doc, use_kwargs

    print("All modules are loaded")

except Exception as e:
    print("Error while loading the modules")


class HealthController(MethodResource, Resource):

    @doc(description='This is a health endpoint', tags=['Heath endpoint'])
    def get(self):
        return {"message": "API is working fine"}, 200