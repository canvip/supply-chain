from django.db import models

# Create your models here.
from shortener.utils import code_generator,create_shortcode

# Create your models here.
class Shortener(models.Model):
    """Model definition for shortener."""

    # TODO: Define fields here
    #url         = models.CharField(max_length=220,)
    url         = models.URLField()
    shortcode   = models.CharField(max_length = 15 ,unique= True,blank = True)
    updated     = models.DateTimeField(auto_now=True) 
    timestamp   = models.DateTimeField(auto_now_add=True) 
    #active      = models.BooleanField(default=True)

    class Meta:
        """Meta definition for shortener."""

        verbose_name        = 'shortener'
        verbose_name_plural = 'shorteners'

    def __str__(self):
        """Unicode representation of shortener."""
        ID = str(self.id)
        URL = str(self.url)
        return ID + " -   " + URL
        


    def __unicode__(self):
        return str(self.url)

    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode =="":
            self.shortcode = create_shortcode(self)      
        super(Shortener, self).save(*args, **kwargs)

        

 #""" python manage.py makemigrations"""

   # python manage.py migrate
   # python manage.py runserver



### Your Account SID from twilio.com/console
##account_sid = "AC9349131412f5f6f8e99ab109f36b4a1f"
### Your Auth Token from twilio.com/console
##auth_token  = "1e4b315801a422267aa1c84b930831bd"
##
##client = Client(account_sid, auth_token)
##
##message = client.messages.create(
##	to="+201280348055",
##	from_="+13027274502",
##	body="python django")
##
##print(message.sid)
##prinenio.__version__
