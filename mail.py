import smtplib
import os   #to read enviroment variable
import dotenv   #load enviroment  variable from the file 

def alert_email(email:str):   #declare function
    dotenv.load_dotenv("./.env")  #load enviroment variable
    with smtplib.SMTP("smtp.gmail.com") as connection:  #connect is a smtp opject
        connection.starttls()  #establish connenction
        connection.login(os.getenv("email"),os.getenv("passwrd"))  #login email
        connection.sendmail(os.getenv("email"),email,"Subject:Weather Alert\n\nThe weather might get unpleasent please carry an umbrella")
        #send main
        
if __name__=="__main__":
    alert_email("bhawnaniankit@gmail.com")
    