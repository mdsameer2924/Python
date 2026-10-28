# Create a class named Book that accepts three attributes in its constructor: title, author, and price. 
# Write a method named get_summary() that returns a formatted string: "{title} by {author}, priced at ${price}".
class Book:
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price
    def get_summary(self):
        return f"{self.title} by {self.author}, priced at ${self.price}"


b1=Book('Rich Dad Poor Dad','Robert t kiyosaki',499) #object
print(b1.get_summary())