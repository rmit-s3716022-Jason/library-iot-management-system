class Book:
    """
    This class will be used to contain the parameters of a book
    """

    def __init__(self, book_id, title, author, published_date):
        """
        Creates the variables associated with this class

        :type book_id: int
        :param book_id: the unique identifier given to the book

        :type title: string
        :param title: the name of the book

        :type author: string
        :param author: the name of the person who wrote the book

        :type published_date: string
        :param published_date: date book was published
        """

        self.book_id = book_id
        self.title = title
        self.author = author
        self.published_date = published_date