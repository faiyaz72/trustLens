class ArticleDetail:
    
    title: str

    def __init__(self, title, content, author, publication_date):
        self.title = title
        self.content = content
        self.author = author
        self.publication_date = publication_date

    def get_summary(self):
        return f"Title: {self.title}, Author: {self.author}, Date: {self.publication_date}"

    def get_content(self):
        return self.content