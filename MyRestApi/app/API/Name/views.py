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


class NameControllerSchema(Schema):
    name = fields.String(required=True, description="name is required")


class NameController(MethodResource, Resource):

    @doc(description='This API would take and greet you', tags=['Name endpoint'])
    @use_kwargs(NameControllerSchema, location=('json'))
    def post(self, **kwargs):
        print("Post request received")
        _message = kwargs.get("name", "default")
        response = {"message": _message}
        print(response)
        return response
