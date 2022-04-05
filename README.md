# Mailganer_mail_sender
mailer service
Allows you to create two types of users - senders (owner) and recipients (respondent). 
Recipients can subscribe to any sender, the sender can create and send mailings to subscribers 
according to the specified parameters (after N minutes, at a specified date and time, on a birthday, etc.).

To install, run:
git clone <repo>
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic (if you deploy the project on the server)

create a file .env in the project directory with the following content:

SECRET_KEY=your django secret
DEFAULT_DOMAIN=http://127.0.0.1:8000/ if locally or your server domain
DEFAULT_DOMAIN_IP=127.0.0.1 or your server IP
DEBUG=1 if you want debug-mode otherwise nothing
EMAIL_HOST=smtp.mail.ru or any other service
EMAIL_HOST_USER=your email service login
EMAIL_HOST_PASSWORD=your mail service password or application password
EMAIL_PORT=2525 the port of the mail service (see the documentation of the mail service)
