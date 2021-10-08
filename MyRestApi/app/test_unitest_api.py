try:
    import os
    import unittest
    import json
    import app
    from API import app

except Exception as e:
    print(e)


class FlaskTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def setUp(self) -> None:
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self) -> None:
        pass

    def test_health_endpoint(self):
        tester = app.test_client(self)
        response = tester.get("/health_check")
        self.assertEqual(response.status_code, 200)

    def test_name_greet(self):
        tester = app.test_client(self)
        response = tester.post('/greet_person', data=json.dumps({
            "name":"shan"
        }), content_type='application/json')
        print(response.data)
        self.assertEqual(response.get_json(), {
            "message": "shan"
        })