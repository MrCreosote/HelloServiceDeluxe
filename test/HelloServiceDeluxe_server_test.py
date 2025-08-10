import unittest

from os import environ
from configparser import ConfigParser

from HelloServiceDeluxe.HelloServiceDeluxeImpl import HelloServiceDeluxe
from HelloServiceDeluxe import HelloServiceDeluxeServer


class HelloServiceDeluxeTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        token = environ.get('KB_AUTH_TOKEN', None)
        cls.ctx = {'token': token, 'provenance': [{'service': 'HelloServiceDeluxe',
            'method': 'please_never_use_it_in_production', 'method_params': []}],
            'authenticated': 1}
        config_file = environ.get('KB_DEPLOYMENT_CONFIG', None)
        cls.cfg = {}
        config = ConfigParser()
        config.read(config_file)
        for nameval in config.items('HelloServiceDeluxe'):
            cls.cfg[nameval[0]] = nameval[1]
        cls.wsURL = cls.cfg['workspace-url']
        cls.serviceImpl = HelloServiceDeluxe(cls.cfg)

    def getImpl(self):
        return self.__class__.serviceImpl

    def getContext(self):
        return self.__class__.ctx

    def test_your_method(self):
        ret = self.getImpl().say_hello(self.getContext(), "foo")
        self.assertEqual(ret, ["Hello, foo. I am a service."])

    def test_service(self):
        app = HelloServiceDeluxeServer.application
        ret = app.rpc_service.call({}, {
            "method": "HelloServiceDeluxe.say_hello",
            "params": ["bar"],
            "id": 1,
        })
        self.assertEqual(ret, '{"result": ["Hello, bar. I am a service."], "id": 1}')
