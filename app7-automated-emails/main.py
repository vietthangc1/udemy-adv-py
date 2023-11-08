import sys
from pkg.emailx import CustomerEmails, EmailSender
from pkg.requestx import RequestClient
from pkg.newsx import NewsFeed
from argparse import ArgumentParser


if __name__ == "__main__":
    parser = ArgumentParser(description="Email and Password info")
    parser.add_argument("--email", help="Sender email")
    parser.add_argument("--password", help="Google app password")
    parser.add_argument("--api_key", help="Newsapi API Key")
    args = parser.parse_args(sys.argv[1:])

    email_readers = CustomerEmails("./static/customers.xlsx", "email", "email")
    list_emails = email_readers.get_emails()

    req = RequestClient(base_url="https://newsapi.org/v2/top-headlines",
                                country="us",
                                category="business",
                                sortBy="publishedAt",
                                apiKey=args.api_key)
    data = req.get_result()
    list_news = data["articles"]

    news = NewsFeed(list_news)
    news_content = news.generate_content()

    email_sender = EmailSender(user=args.email,
                               password=args.password)
    for email in list_emails:
        email_sender.send(to=email,
                          subject="Daily News",
                          contents=news_content)
