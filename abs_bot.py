import abc

class BaseChatBot(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractproperty
    def chat_handler(self):
        pass

    @abc.abstractmethod
    def send_message(self, msg):
        pass 

    @classmethod
    def __subclasshook__(cls, C):
        if cls is Container:
            if any("send_message" in B.__dict__ for B in C.__mro__):
                return True
        return NotImplemented


class AIBaseChatBot(BaseChatBot):
    __metaclass__ = abc.ABCMeta

    @abc.abstractproperty
    def brain(self):
        pass


class LookUpBaseChatBot(BaseChatBot):
    __metaclass__ = abc.ABCMeta

    @abc.abstractproperty
    def lookup_table(self, msg):
        pass