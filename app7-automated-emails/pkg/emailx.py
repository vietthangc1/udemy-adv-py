import pandas as pd
import yagmail


class EmailSender:
    
    def __init__(self, user, password) -> None:
        self.user = user
        self.password = password
        self.email = yagmail.SMTP(user=user,
                                  password=password)

    def send(self, to, subject, contents) -> None:
        email_content = "Hi! Have a nice day \n\n"
        email_content += contents
        self.email.send(to=to,
                        subject=subject,
                        contents=email_content)  


class CustomerEmails:

    def __init__(self, filepath: str, sheet_name: str, col_name: str) -> None:
        self.filepath = filepath
        self.sheet_name = sheet_name
        self.col_name = col_name
    
    def get_emails(self) -> list:
        df = pd.read_excel(self.filepath,
                           self.sheet_name)
        emails = df[self.col_name].values
        return list(emails)  


if __name__ == "__main__":
    pass