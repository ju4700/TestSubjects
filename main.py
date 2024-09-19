import sqlite3
import hashlib
import smtplib
import random
import logging
import schedule
import time
import datetime
from email.mime.text import MIMEText
import customtkinter as ctk
import tkinter.messagebox as messagebox
import threading
import re

# Database setup
conn = sqlite3.connect('atm.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS accounts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                password TEXT,
                pin TEXT,
                email TEXT,
                history TEXT,
                failed_attempts INTEGER,
                account_locked INTEGER,
                security_question TEXT,
                security_answer TEXT
            )''')

c.execute('''CREATE TABLE IF NOT EXISTS scheduled_transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                amount REAL,
                transaction_type TEXT,
                scheduled_time TEXT
            )''')

conn.commit()


# Email sending function
def send_email(to, subject, body):
    sender_email = "your_email@example.com"
    sender_password = "your_password"

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = to

    with smtplib.SMTP("smtp.example.com", 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, to, msg.as_string())


# Password hashing function
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def hash_pin(pin):
    return hashlib.sha256(pin.encode()).hexdigest()


# Password strength check function
def is_password_strong(password):
    return (len(password) >= 8 and re.search(r"[a-z]", password) and
            re.search(r"[A-Z]", password) and re.search(r"\d", password) and
            re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))


# Logging setup
logging.basicConfig(filename='atm.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def log_transaction(username, transaction):
    logging.info(f"User: {username}, Transaction: {transaction}")


# Schedule monthly statements
def generate_monthly_statement(username):
    c.execute('SELECT history FROM accounts WHERE username=?', (username,))
    transactions = eval(c.fetchone()[0])
    statement = "\n".join(transactions)
    return statement


def send_monthly_statements():
    c.execute('SELECT username, email FROM accounts')
    for account in c.fetchall():
        username, email = account
        statement = generate_monthly_statement(username)
        send_email(email, "Monthly Statement", statement)


def check_and_send_monthly_statements():
    if datetime.datetime.now().day == 1:  # Check if today is the first day of the month
        send_monthly_statements()


schedule.every().day.at("00:00").do(check_and_send_monthly_statements)


def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)


# Main Application Logic
def user_exists(username):
    c.execute('SELECT * FROM accounts WHERE username=?', (username,))
    return c.fetchone() is not None


def register(username, password, pin, email, security_question, security_answer):
    if user_exists(username):
        return False, "Username already exists"
    if not is_password_strong(password):
        return False, "Password not strong enough"
    hashed_password = hash_password(password)
    hashed_pin = hash_pin(pin)
    hashed_answer = hash_password(security_answer)
    c.execute(
        'INSERT INTO accounts (username, password, pin, email, history, failed_attempts, account_locked, security_question, security_answer) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)',
        (username, hashed_password, hashed_pin, email, '[]', 0, 0, security_question, hashed_answer))
    conn.commit()
    return True, "Account created successfully"


def send_2fa_code(email):
    code = str(random.randint(100000, 999999))
    send_email(email, "Your 2FA Code", f"Your 2FA code is {code}")
    return code


def login(username, password, pin):
    hashed_password = hash_password(password)
    hashed_pin = hash_pin(pin)
    c.execute('SELECT * FROM accounts WHERE username=? AND password=?', (username, hashed_password))
    account = c.fetchone()
    if account:
        if account[6] >= 3:
            return "locked"
        if account[3] == hashed_pin:
            code = send_2fa_code(account[4])
            return "2fa", code
        else:
            c.execute('UPDATE accounts SET failed_attempts=failed_attempts+1 WHERE username=?', (username,))
            conn.commit()
            return "wrong_pin"
    else:
        return "wrong_credentials"


def schedule_transaction(username, amount, transaction_type, scheduled_time):
    c.execute(
        'INSERT INTO scheduled_transactions (username, amount, transaction_type, scheduled_time) VALUES (?, ?, ?, ?)',
        (username, amount, transaction_type, scheduled_time))
    conn.commit()


def recover_password(username, security_answer):
    hashed_answer = hash_password(security_answer)
    c.execute('SELECT * FROM accounts WHERE username=? AND security_answer=?', (username, hashed_answer))
    account = c.fetchone()
    if account:
        new_password = str(random.randint(100000, 999999))  # Generate a temporary password
        hashed_password = hash_password(new_password)
        c.execute('UPDATE accounts SET password=? WHERE username=?', (hashed_password, username))
        conn.commit()
        send_email(account[4], "Password Recovery", f"Your new password is {new_password}")
        return True
    return False


def update_profile(username, new_password, new_pin, new_email):
    if new_password:
        hashed_password = hash_password(new_password)
        c.execute('UPDATE accounts SET password=? WHERE username=?', (hashed_password, username))
    if new_pin:
        hashed_pin = hash_pin(new_pin)
        c.execute('UPDATE accounts SET pin=? WHERE username=?', (hashed_pin, username))
    if new_email:
        c.execute('UPDATE accounts SET email=? WHERE username=?', (new_email, username))
    conn.commit()


# UI Components
class ATMApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ATM System")
        self.root.geometry("400x425")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        self.username = None
        self.temp_2fa_code = None
        self.login_screen()

    def login_screen(self):
        self.clear_screen()
        frame = ctk.CTkFrame(self.root)
        frame.pack(pady=20, padx=20, fill="both", expand=True)

        ctk.CTkLabel(frame, text="Username").pack(pady=5)
        self.username_entry = ctk.CTkEntry(frame)
        self.username_entry.pack(pady=5)

        ctk.CTkLabel(frame, text="Password").pack(pady=5)
        self.password_entry = ctk.CTkEntry(frame, show='*')
        self.password_entry.pack(pady=5)

        ctk.CTkLabel(frame, text="PIN").pack(pady=5)
        self.pin_entry = ctk.CTkEntry(frame, show='*')
        self.pin_entry.pack(pady=5)

        ctk.CTkButton(frame, text="Login", command=self.login).pack(pady=10)
        ctk.CTkButton(frame, text="Register", command=self.register_screen).pack(pady=10)
        ctk.CTkButton(frame, text="Recover Password", command=self.recover_password_screen).pack(pady=10)

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        pin = self.pin_entry.get()
        result = login(username, password, pin)
        if result[0] == "2fa":
            self.username = username
            self.temp_2fa_code = result[1]
            self.two_factor_screen()
        elif result == "wrong_credentials":
            messagebox.showerror("Error", "Invalid username or password")
        elif result == "wrong_pin":
            messagebox.showerror("Error", "Incorrect PIN")
        elif result == "locked":
            messagebox.showerror("Error", "Account locked due to too many failed login attempts")

    def two_factor_screen(self):
        self.clear_screen()
        frame = ctk.CTkFrame(self.root)
        frame.pack(pady=20, padx=20, fill="both", expand=True)

        ctk.CTkLabel(frame, text="Enter 2FA Code").pack(pady=5)
        self.otp_entry = ctk.CTkEntry(frame)
        self.otp_entry.pack(pady=5)

        ctk.CTkButton(frame, text="Verify", command=self.verify_2fa).pack(pady=10)

    def verify_2fa(self):
        otp = self.otp_entry.get()
        if otp == self.temp_2fa_code:
            self.main_menu()
        else:
            messagebox.showerror("Error", "Incorrect 2FA code")
            self.login_screen()

    def main_menu(self):
        self.clear_screen()
        frame = ctk.CTkFrame(self.root)
        frame.pack(pady=20, padx=20, fill="both", expand=True)

        ctk.CTkButton(frame, text="Profile Management", command=self.profile_management_screen).pack(pady=10)
        ctk.CTkButton(frame, text="Schedule Transaction", command=self.schedule_transaction_screen).pack(pady=10)
        ctk.CTkButton(frame, text="Logout", command=self.login_screen).pack(pady=10)

    def schedule_transaction_screen(self):
        self.clear_screen()
        frame = ctk.CTkFrame(self.root)
        frame.pack(pady=20, padx=20, fill="both", expand=True)

        ctk.CTkLabel(frame, text="Amount").pack(pady=5)
        self.amount_entry = ctk.CTkEntry(frame)
        self.amount_entry.pack(pady=5)

        ctk.CTkLabel(frame, text="Transaction Type (deposit/withdraw)").pack(pady=5)
        self.transaction_type_entry = ctk.CTkEntry(frame)
        self.transaction_type_entry.pack(pady=5)

        ctk.CTkLabel(frame, text="Scheduled Time (YYYY-MM-DD HH:MM)").pack(pady=5)
        self.scheduled_time_entry = ctk.CTkEntry(frame)
        self.scheduled_time_entry.pack(pady=5)

        ctk.CTkButton(frame, text="Schedule", command=self.schedule_transaction).pack(pady=10)
        ctk.CTkButton(frame, text="Back", command=self.main_menu).pack(pady=10)

    def schedule_transaction(self):
        amount = float(self.amount_entry.get())
        transaction_type = self.transaction_type_entry.get()
        scheduled_time = self.scheduled_time_entry.get()
        schedule_transaction(self.username, amount, transaction_type, scheduled_time)
        messagebox.showinfo("Success", "Transaction scheduled successfully")
        self.main_menu()

    def profile_management_screen(self):
        self.clear_screen()
        frame = ctk.CTkFrame(self.root)
        frame.pack(pady=20, padx=20, fill="both", expand=True)

        ctk.CTkLabel(frame, text="New Password").pack(pady=5)
        self.new_password_entry = ctk.CTkEntry(frame, show='*')
        self.new_password_entry.pack(pady=5)

        ctk.CTkLabel(frame, text="New PIN").pack(pady=5)
        self.new_pin_entry = ctk.CTkEntry(frame, show='*')
        self.new_pin_entry.pack(pady=5)

        ctk.CTkLabel(frame, text="New Email").pack(pady=5)
        self.new_email_entry = ctk.CTkEntry(frame)
        self.new_email_entry.pack(pady=5)

        ctk.CTkButton(frame, text="Update", command=self.update_profile).pack(pady=10)
        ctk.CTkButton(frame, text="Back", command=self.main_menu).pack(pady=10)

    def update_profile(self):
        new_password = self.new_password_entry.get()
        new_pin = self.new_pin_entry.get()
        new_email = self.new_email_entry.get()
        update_profile(self.username, new_password, new_pin, new_email)
        messagebox.showinfo("Success", "Profile updated successfully")
        self.main_menu()

    def register_screen(self):
        self.clear_screen()
        frame = ctk.CTkFrame(self.root)
        frame.pack(pady=20, padx=20, fill="both", expand=True)

        ctk.CTkLabel(frame, text="Username").pack(pady=5)
        self.username_entry = ctk.CTkEntry(frame)
        self.username_entry.pack(pady=5)

        ctk.CTkLabel(frame, text="Password").pack(pady=5)
        self.password_entry = ctk.CTkEntry(frame, show='*')
        self.password_entry.pack(pady=5)

        ctk.CTkLabel(frame, text="PIN").pack(pady=5)
        self.pin_entry = ctk.CTkEntry(frame, show='*')
        self.pin_entry.pack(pady=5)

        ctk.CTkLabel(frame, text="Email").pack(pady=5)
        self.email_entry = ctk.CTkEntry(frame)
        self.email_entry.pack(pady=5)

        ctk.CTkLabel(frame, text="Security Question").pack(pady=5)
        self.security_question_entry = ctk.CTkEntry(frame)
        self.security_question_entry.pack(pady=5)

        ctk.CTkLabel(frame, text="Security Answer").pack(pady=5)
        self.security_answer_entry = ctk.CTkEntry(frame, show='*')
        self.security_answer_entry.pack(pady=5)

        ctk.CTkButton(frame, text="Register", command=self.register).pack(pady=10)
        ctk.CTkButton(frame, text="Back", command=self.login_screen).pack(pady=10)

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        pin = self.pin_entry.get()
        email = self.email_entry.get()
        security_question = self.security_question_entry.get()
        security_answer = self.security_answer_entry.get()
        success, message = register(username, password, pin, email, security_question, security_answer)
        if success:
            messagebox.showinfo("Success", message)
            self.login_screen()
        else:
            messagebox.showerror("Error", message)

    def recover_password_screen(self):
        self.clear_screen()
        frame = ctk.CTkFrame(self.root)
        frame.pack(pady=20, padx=20, fill="both", expand=True)

        ctk.CTkLabel(frame, text="Username").pack(pady=5)
        self.username_entry = ctk.CTkEntry(frame)
        self.username_entry.pack(pady=5)

        ctk.CTkLabel(frame, text="Security Answer").pack(pady=5)
        self.security_answer_entry = ctk.CTkEntry(frame, show='*')
        self.security_answer_entry.pack(pady=5)

        ctk.CTkButton(frame, text="Recover Password", command=self.recover_password).pack(pady=10)
        ctk.CTkButton(frame, text="Back", command=self.login_screen).pack(pady=10)

    def recover_password(self):
        username = self.username_entry.get()
        security_answer = self.security_answer_entry.get()
        if recover_password(username, security_answer):
            messagebox.showinfo("Success", "A new password has been sent to your email")
            self.login_screen()
        else:
            messagebox.showerror("Error", "Incorrect username or security answer")


if __name__ == "__main__":
    root = ctk.CTk()
    app = ATMApp(root)
    threading.Thread(target=run_scheduler).start()
    root.mainloop()
