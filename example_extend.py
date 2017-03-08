from abs_bot import BaseChatBot
"""
This module is here to exemplify how the abstract bot
class can be extended to implement any custom chat like
bot on any client
"""


class ExampleChatBot(BaseChatBot):

    def __init__(self, handler):
        self._handler = handler

    @property
    def chat_handler(self):
        if self._handler._con is not None:
            return self._handler._con
        else:
            return self._handler.__enter__()

    def send_message(self, msg):
        self.chat_handler.send(msg)


class ExampleHandler(object):

    def __init__(self):
        self._con = None

    def __enter__(self):
        if self._con is None:
            self._con = ExampleConnection.open()
            print("Connection to handler opened")
        return self._con

    def __exit__(self, *args):
        self._con.close()
        print("Connection handler closed")


class ExampleConnection(object):
    """
    Singleton datbase connection like object
    """

    con_bool = False  # Singleton pattern connection simmulator

    def send(self, msg):
        if self.con_bool:
            print "SENT {0}".format(msg)
        else:
            raise BaseException("Connection closed please connect")


    def close(self):
        self.con_bool = False

    @classmethod
    def open(cls):
        cls.con_bool = True
        return cls()

    def __str__(self):
        return ("___________________________\n"  + 
                "|Example Connection Object|"    + 
                "\n|Connection status: {0}  |\n" +
                "---------------------------").format(self.con_bool)



if __name__ == "__main__":
    handler = ExampleHandler()
    c = ExampleChatBot(handler)
    c.send_message("Testing Architecture")
    print c.chat_handler