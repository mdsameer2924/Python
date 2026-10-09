"""
Question 1: The Notification System
Create a multi-channel notification sender using duck typing:

Create three completely independent classes: EmailSender, SMSSender, and WhatsAppSender.

Give each class a method named send_message(self, message).

Write a separate function called broadcast(sender_obj, message) that takes any sender object and invokes its send_message method.

Instantiate all three classes and pass them one by one into your broadcast function.
"""


class EmailSender:
    def send_message(self, message):
        print(f"{self.message} as sent as a message in your Email.")


class SMSSender:
    def send_message(self, message):
        print(f"{self.message} as sent a message in your SMS")


class WhatsAppSender:
    def send_message(self, message):
        print(f"{self.send_message} as sent a message in your Whatsapp")


def broadcast(obj, message):
    return obj.send_message(message)


E = EmailSender()
S = SMSSender()
W = WhatsAppSender()

broadcast(E, "Hi bro")
broadcast(S, "meat")
broadcast(W, "one piece")
