from django.db import models

#hero image changes
class hero_image(models.Model):
    card_img=models.ImageField(upload_to='static/')
    
#hero infornt information changes
class hero_information(models.Model):
    hero_info_first=models.TextField()
    hero_info_secound=models.TextField()
    hero_info_third=models.TextField()


#for the service changes
class serviec_heading(models.Model): 
    service_info=models.TextField()

#this all changes made in card so be consicus
class card(models.Model):
    card_img=models.ImageField(upload_to='static/')
    card_title=models.TextField()
    card_info=models.TextField()
    card_button_text=models.TextField()

#core language chanes in photo and theri name
class core_lang(models.Model):
    core_img=models.ImageField(upload_to='static/')
    core_title=models.TextField()

class front_lang(models.Model):
    front_img=models.ImageField(upload_to='static/')
    front_title=models.TextField()

class backend_lang(models.Model):
    backend_img=models.ImageField(upload_to='static/')
    backend_title=models.TextField()

class lets_cofee(models.Model):
    name=models.TextField()
    email=models.TextField()
    text=models.TextField()

