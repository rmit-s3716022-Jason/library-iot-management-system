class Book:
    """
    This class will be used to contain the parameters of a book
    """

    def __init__(self, **kwargs):
        """
        Creates the variables associated with this class

        :type book_id: int
        :param book_id: the unique identifier given to the book

        :type title: string
        :param title: the name of the book

        :type author: string
        :param author: the name of the person who wrote the book

        :type isbn: string
        :param isbn: international book identifier
        """

        self.book_id = kwargs.get('book_id', 0)
        self.title = kwargs.get('title', '')
        self.author = kwargs.get('author', '')
        self.isbn = kwargs.get('isbn', '')
