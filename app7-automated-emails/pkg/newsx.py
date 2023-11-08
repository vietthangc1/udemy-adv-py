class NewsFeed:
   
    def __init__(self, data) -> None:
        self.data = data

    def generate_content(self):
        news_content = "News today\n\n"
        for news in self.data:
            news_content += "From {}\n".format(news['source']['name'])
            news_content += "{title}, by {author}. Visit at: {url}\n".format(**news)
            news_content += "\n"
        return news_content