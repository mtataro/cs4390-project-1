
[`smtplib`](https://docs.python.org/3/library/smtplib.html) is Python’s built-in module for sending emails to any Internet machine with an SMTP or ESMTP listener daemon.

two protocols that can be used to encrypt an SMTP connection are SSL (Secure sockets layer) and TLS (transport layer security)

We will use SSL (secure sockets layer) to secure our mail client

```python
import smtplib, ssl

port = 465  # For SSL
password = input("Type your password and press enter: ")

# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login("my@gmail.com", password)
    # TODO: Send email here
```

After you initiated a secure SMTP connection using the above method, you can send your email using `.sendmail()`, which pretty much does what it says on the tin


The code example below sends a plain-text email using `SMTP_SSL()`:

```python
import smtplib, ssl

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "email.sender.task.3@gmail.com"  # Enter your address
receiver_email = "andresflo883@gmail.com"  # Enter receiver address
password = input("Type your password and press enter: ")
message = """\
Subject: Hi there

This message is sent from Python."""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
```


b. Implement an email client to send an email with an attachment