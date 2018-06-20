from time import sleep

from twisted.internet.defer import inlineCallbacks

from autobahn.wamp.types import PublishOptions
from autobahn.wamp.exception import ApplicationError, SerializationError

from autobahn.twisted.wamp import ApplicationSession
from autobahn.twisted.wamp import ApplicationRunner


class MyComponent(ApplicationSession):

    @inlineCallbacks
    def onJoin(self, details):
        print("session ready")
        while True:
            print('a')
            self.publish("data", {'bat': {'tag': 'gauge6', 'value': '10'}})
            sleep(0.1)


if __name__ == '__main__':
    runner = ApplicationRunner(url=u"ws://127.0.0.1:8080/ws", realm=u"realm1")
    runner.run(MyComponent)
