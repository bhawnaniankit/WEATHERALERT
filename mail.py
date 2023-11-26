import smtplib
import os
import dotenv

def alert_email(email:str):
    dotenv.load_dotenv("./.env")
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(os.getenv("email"),os.getenv("passwrd"))
        connection.sendmail(os.getenv("email"),email,"Subject:Weather Alert\n\nThe weather might get unpleasent please carry a umbrella")
        
if __name__=="__main__":
    alert_email("bhawnaniankit@gmail.com")