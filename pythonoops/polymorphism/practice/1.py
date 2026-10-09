'''
Question 1: The Notification System
Create a multi-channel notification sender using duck typing:

Create three completely independent classes: EmailSender, SMSSender, and WhatsAppSender.

Give each class a method named send_message(self, message).

Write a separate function called broadcast(sender_obj, message) that takes any sender object and invokes its send_message method.

Instantiate all three classes and pass them one by one into your broadcast function.
'''
class EmailSender:
    
    
    def send_message(self):
        print(f"{self.message} as sent as a message in your Email.")
 
class SMSSender:
    def send_message(self,message) 
