from django.contrib import admin

from portfolio_app.models import backend_lang, card, core_lang, front_lang, hero_image, hero_information, serviec_heading


#user root
#password 123
# Register your models here.
class hero_imag1(admin.ModelAdmin):
    list_display=['card_img']
admin.site.register(hero_image,hero_imag1)


class hero_information1(admin.ModelAdmin):
    list_display=["hero_info_first","hero_info_third","hero_info_secound"]
admin.site.register(hero_information,hero_information1)


class serviec_heading1(admin.ModelAdmin):
    list_display=["service_info"]
admin.site.register(serviec_heading,serviec_heading1)

class card1(admin.ModelAdmin):
    list_display=["card_button_text","card_info","card_title"]
admin.site.register(card,card1)

class core_lang1(admin.ModelAdmin):
    list_display=["core_title","core_img"]
admin.site.register(core_lang,core_lang1)

class front_lang1(admin.ModelAdmin):
    list_display=["front_title","front_img"]
admin.site.register(front_lang,front_lang1)

class backend_lang1(admin.ModelAdmin):
    list_display=["backend_title","backend_img",]
admin.site.register(backend_lang,backend_lang1)