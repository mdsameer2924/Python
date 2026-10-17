'''
Mock Problem: The Notification System

Import ABC and abstractmethod from the abc module.

Create an abstract parent class named Notification with an abstract method named send(message).

Create two child classes, EmailNotification and SMSNotification, that inherit from Notification.

Give each child class its own implementation of the send(message) method (for example, returning "Sending Email: {message}" and "Sending SMS: {message}").

Instantiate both child classes, call their send() methods, and print the results.

UnicodeEncodeErrorp your code for the mock problem whenever you are ready!
'''
from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send(message):
        pass

class EmailNotification(Notification):
    def __init(self,message):
        def send(message):
            
