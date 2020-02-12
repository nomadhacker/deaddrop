import sendgrid
from sendgrid.helpers.mail import (Content, MimeType)
from django.conf import settings

def send(sender, recipient, content, type):
	sg = sendgrid.SendGridAPIClient(settings.SENDGRID_API_KEY)

	message = sendgrid.Mail()
	message.to = recipient
	if( type == 1):
		message.subject = "A secret message from %s" % sender
	elif type == 2:
		message.subject = "A secret key from %s" % sender
	else:
		message.subject = "A secret from %s" % sender
	message.content = Content(MimeType.html, content)
	message.from_email = sender
	response = sg.send(message)
