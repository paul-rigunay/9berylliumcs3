class Publication:    # Creates a parent class
  def __init__(self, title, author):    # initializes self, title, and author
    self.title = title
    self.author = author

  def get_title(self):    # gets the title name
    return self.title

  def get_author(self):    # gets the author name
    return self.author

  def set_title(self, title):    # sets the title name
    self.title = title

  def set_author(self, author):    # sets the authors name
    self.author = author

  def display_info(self):    # displays the information on each publication
    print(f"Title: {self.title}")
    print(f"Author: {self.author}")

class Book(Publication):    # Creates a "minor" class which inherits the parent class Publication
  def __init__(self, title, author, number_pages):    # initializes self, title, author, and number of pages
    self.number_pages = int(number_pages)
    self.title = title
    self.author = author

  def get_number_of_pages(self):    # gets the number of pages in a book
    return f"Page number: {self.number_pages}"

  def set_number_of_pages(self, number_pages):    # sets the number of pages in a book
    if number_pages > 0:    # checks if the number of pages is/are positive
      self.number_pages = number_pages
    else:
      print("The number of pages must be positive.")

class Magazine(Publication):    # Creates a "minor" class. Similar to class Book, it inherits the parent class Publication
  def __init__(self, title, author, issue_number):    # initializes self, title, author, and issue number
    self.issue_number = int(issue_number)
    self.title = title
    self.author = author

  def get_issue_number(self):    # gets the issue number of a magazine
    return f"Issue number: {self.issue_number}"

  def set_issue_number(self, issue_number):    # sets the issue number of a magazine
    if issue_number > 0:    # checks if the issue number is/are positive
      self.issue_number = issue_number
    else:
      print("The issue number must be positive.")

# Creating objects
pub1 = Publication("Journal of Experimental Psychology", "Ratchiff, R. & Van Dongen, H.")
book1 = Book("Mankind: The story of all of us", "Pamela D. Toler", 448)
mag1 = Magazine("National Geographic", "Various Authors", 202)

# Printing the information
print("Publication Information:")
pub1.display_info()

print("\nBook Information:")
book1.set_number_of_pages(-448)
book1.display_info()
print(book1.get_number_of_pages())

print("\nMagazine Information:")
mag1.display_info()
print(mag1.get_issue_number())
