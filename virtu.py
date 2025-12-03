import os
import subprocess
import smtplib
import time
from email.message import EmailMessage

def send_email(receiver, subject, body, sender, password, smtp_server='smtp.gmail.com', smtp_port=587):
    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = receiver

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender, password)
        server.send_message(msg)
    print("Email sent successfully.")

def forecast_weather(location):
    # For offline mode, use cached/local weather data
    # For demo, read from a local file named 'weather.txt'
    try:
        with open('weather.txt', 'r') as f:
            print(f"Weather for {location}:")
            print(f.read())
    except FileNotFoundError:
        print("No offline weather data available. Please update 'weather.txt'.")

def open_app(app_name):
    # Add more apps as needed
    apps = {
        "word": r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE",
        "excel": r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE",
        "powerpoint": r"C:\Program Files\Microsoft Office\root\Office16\POWERPNT.EXE",
        "notepad": "notepad.exe",
        "calculator": "calc.exe"
    }
    path = apps.get(app_name.lower())
    if path:
        os.startfile(path)
        print(f"{app_name} opened.")
    else:
        print(f"App {app_name} not found in list.")

def shutdown_system():
    print("Shutting down system...")
    os.system("shutdown /s /t 1")  # Windows

def sleep_system():
    print("Putting system to sleep...")
    # Windows sleep command
    try:
        subprocess.run(["rundll32.exe", "powrprof.dll,SetSuspendState", "0,1,0"])
    except Exception as e:
        print(f"Failed to sleep: {e}")

def main():
    print("Offline Virtual Assistant")
    print("Commands: email, weather, open, shutdown, sleep, exit")
    while True:
        cmd = input("Enter command: ").strip().lower()
        if cmd == "email":
            receiver = input("Receiver: ")
            subject = input("Subject: ")
            body = input("Body: ")
            sender = input("Your Email: ")
            password = input("Your Email Password: ")
            send_email(receiver, subject, body, sender, password)
        elif cmd == "weather":
            location = input("Location: ")
            forecast_weather(location)
        elif cmd == "open":
            app = input("App name (word, excel, powerpoint, notepad, calculator): ")
            open_app(app)
        elif cmd == "shutdown":
            shutdown_system()
            break
        elif cmd == "sleep":
            sleep_system()
            break
        elif cmd == "exit":
            print("Goodbye!")
            break
        else:
            print("Unknown command.")

if __name__ == "__main__":
    main()em