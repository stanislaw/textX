from __future__ import unicode_literals
from textx.metamodel import metamodel_from_str

grammar = """
MyModel: 'model' name=ID
  connections+=Connection
  sender+=Sender
  receiver+=Receiver;


Sender: 
  'outgoing' name=ID 'over' connection=[Connection|ID];

Receiver: 
 'incoming' name=ID 'over' connection=[Connection|ID];

Connection: 
  'connection' name=ID
  'port' port=STRING 
  'ip' ip=STRING;
"""

modelstring = """
model Example
connection conn port "1" ip "127.0.0.1"

outgoing out0 over conn
incoming in0 over conn

"""
class ConnectionHandler(object):
    def _init_(self):
        print('')

    def awesomeMethod4SenderAndReceiver(self):
        print("I am really important for Sender and Receiver")

class Sender(ConnectionHandler):
    def _init_(self, name=None, port=None):
        print('')

class Receiver(ConnectionHandler):
    def _init_(self, name=None, port=None):
        print('')

def test_issue270():
    mm = metamodel_from_str(grammar, classes=[ConnectionHandler, Sender, Receiver])
    _ = mm.model_from_str(modelstring)