from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Информация для главной страницы Баннер + краткое содержание о компании


class MainPage(models.Model):
    banner_background = models.ImageField(
        upload_to='banner_backg/', blank=True, null=True, verbose_name='Banneryň arka fondaky suraty')
    banner_image = models.ImageField(
        upload_to='banner_image/', blank=True, null=True, verbose_name="Banneryň esasy suraty(merkezdäki)")

    mini_about = models.CharField(max_length=255, blank=True, null=True,
                                  verbose_name='Baş sahypadaky banneryň aşagyndaky gysgaça düşündiriş')
    mini_about_image = models.ImageField(upload_to='mini_about_image', blank=True, null=True,
                                         verbose_name='Baş sahypadaky banneryň aşagyndaky gysgaça düşündiriň suraty')

    def __str__(self):
        return self.mini_about

    class Meta:
        verbose_name = 'Baş sahypadaky banner we gysgaça maglumat'
        verbose_name_plural = 'Baş sahypadaky banner we gysgaça maglumatlar'

# Разделя для медии


class MediaSections(models.Model):
    title = models.CharField(max_length=100, blank=True,
                             null=True, verbose_name="Bildirişiň gysgaça ady")
    category_media = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Bildirişiň haýsy sektora degişliligi")
    description = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Bildirişiň beýany")
    media_image = models.ImageField(
        upload_to='media_image', blank=True, null=True, verbose_name='Bildirişiň suraty')
    link = models.CharField(max_length=255, blank=True,
                            null=True, verbose_name="Wideonyň ssylkasy")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Bildiriş'
        verbose_name_plural = 'Bildirişler bölümi'


# Приказы

class Decress(models.Model):
    title = models.CharField(max_length=255, blank=True,
                             null=True, verbose_name="Buýruklaň ady")
    media_image = models.ImageField(
        upload_to='decress_image', blank=True, null=True, verbose_name='Buýrugyň suraty')
    description = RichTextUploadingField(
        blank=True, null=True, verbose_name="Buýruklaryň giňişleýin beýany")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Buýruk'
        verbose_name_plural = 'Buýruklar bölümi'


# Планы прилетов и отлетов

class Flight(models.Model):
    FLIGHT_CATEGORY = [
        ('DEPARTURE', 'Uçuş'),
        ('ARRIVAL', 'Gonuş'),
    ]
    departure = models.CharField(
        max_length=10, blank=True, null=True, verbose_name="Uçan wagty")
    arrival = models.CharField(
        max_length=10, blank=True, null=True, verbose_name="Gonan wagty")
    flight_category = models.CharField(
        max_length=15, choices=FLIGHT_CATEGORY, default="DEPARTURE", verbose_name="Uçuş, Gonuş ?")
    title = models.CharField(max_length=255, blank=True,
                             null=True, verbose_name='Reýsyň ady')
    model_plane = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Uçaryň modeli")
    flight_image = models.ImageField(
        upload_to='flight_image', blank=True, null=True, verbose_name='Reýsyň suraty')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Üçuş-Gonuş'
        verbose_name_plural = 'Üçuş-Gonuşlar'


# баннеры + инфо о службах аэропорта

class BannerForAirlinesServices(models.Model):
    title = models.CharField(max_length=150, blank=True,
                             null=True, verbose_name="Bannerdaky esasy ýazgy")
    image = models.ImageField(upload_to="banner_airlines_services/",
                              blank=True, null=True, verbose_name="Banner suraty")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Banner'
        verbose_name_plural = 'H.M gulluklar bölümindäki banner'

# службы аэропорта


class AirlinesServices(models.Model):
    title = models.CharField(max_length=250, blank=True,
                             null=True, verbose_name="Gullugyň ady")
    image = models.ImageField(upload_to="airlines_services/",
                              blank=True, null=True, verbose_name="Gullugyň suraty")
    description = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Gysgaça beýany")
    full_desc = RichTextUploadingField(
        blank=True, null=True, verbose_name='Doly beýany')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Gulluk'
        verbose_name_plural = 'H.M gulluklar bölümi'


#  история авиокомпании

class AboutUs(models.Model):
    title = models.CharField(max_length=150, blank=True,
                             null=True, verbose_name="Bannerdaky esasy ýazgy")
    image = models.ImageField(
        upload_to="about_us/", blank=True, null=True, verbose_name="Banner suraty")

    title_to_sections = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Esasy ýazgy taryh barada")
    description = RichTextUploadingField(
        blank=True, null=True, verbose_name="Giňişleýin beýany")

    dowlaod_icon = models.ImageField(
        upload_to='dowload_icon/', blank=True, null=True, verbose_name="Pdf skaçat etmek düwmesi")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Banner'
        verbose_name_plural = 'H.Menzil baradaky maglumat'

# изаброжение о компании


class AboutUsImage(models.Model):
    title = models.CharField(max_length=150, blank=True,
                             null=True, verbose_name="Suratyň ýazgysy ")
    image = models.ImageField(upload_to="about_us/",
                              blank=True, null=True, verbose_name="Suraty")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Surat'
        verbose_name_plural = 'H.Menzil baradaky maglumat we taryhy suratlar'


# Сервисы аэропорта

class AirlinesServicesBanner(models.Model):
    image = models.ImageField(upload_to='Hyzmatlar sahypasynyň bannery')

    class Meta:
        verbose_name = 'Banner'
        verbose_name_plural = 'Hyzmatlar sahypasynyň banner '


class AirlinesServicesRightBar(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True,
                             verbose_name="Hyzmatlar sahypasynyň banner sag tarapy ýokarky")
    desc = models.CharField(max_length=255, blank=True, null=True,
                            verbose_name="Hyzmatlar sahypasynyň banner sag tarapy aşakdaky")
    icon = models.ImageField(upload_to="icon-services/",
                             blank=True, null=True, verbose_name='Ikonkasy')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Hyzmatlar'
        verbose_name_plural = 'Hyzmatlar sahypasynyň banner  maglumaty'


class AirlinesServicesDown(models.Model):

    title = models.CharField(max_length=255, blank=True,
                             null=True, verbose_name="Hyzmatlar ýokarky ýazgysy")
    desc = models.CharField(max_length=255, blank=True,
                            null=True, verbose_name="Hyzmatlar aşakdaky ýazgysy")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Hyzmatlar'
        verbose_name_plural = 'Hyzmatlar sahypasynyň maglumaty'


# модели для страницы администрации


class AdministrationPage(models.Model):
    banner_background = models.ImageField(
        upload_to='banner_backg/', blank=True, null=True, verbose_name='Banneryň arka fondaky suraty')
    banner_image = models.ImageField(
        upload_to='banner_image/', blank=True, null=True, verbose_name="Banneryň esasy suraty(merkezdäki)")

    class Meta:
        verbose_name = 'Banner'
        verbose_name_plural = 'Administrasiýa sahypadaky banner '


# должность
class Mission(models.Model):
    title = models.CharField(max_length=255, blank=True,
                             null=True, verbose_name='Wezipesi')
    image = models.ImageField(blank=True, null=True,
                              upload_to="Mission", verbose_name="Suraty")
    phone_number = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Telefon nomery")
    phone_number_2 = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Telefon nomery(goşmaça)")
    email = models.CharField(max_length=255, blank=True,
                             null=True, verbose_name="Elektron poçtasy")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Wezipe'
        verbose_name_plural = 'Administrasiýa wezipeleri '


class AdministrationTable(models.Model):
    mission = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Wezipesi")
    phone_number = models.CharField(
        max_length=25, blank=True, null=True, verbose_name="Telefon belgisi")

    def __str__(self):
        return self.mission

    class Meta:
        verbose_name = 'Wezipe'
        verbose_name_plural = 'Administrasiýa wezipeleri Tablisasy'


# Галерея аэропорта

class Gallery(models.Model):
    name = models.CharField(max_length=15, blank=True,
                            null=True, verbose_name="Suratyň ady")
    image = models.ImageField(upload_to="gallery/",
                              blank=True, null=True, verbose_name="Surat")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Surat'
        verbose_name_plural = 'Gallereýa'


# баннер для списка рейсов
class OnlineTableBanner(models.Model):
    name = models.CharField(max_length=15, blank=True,
                            null=True, verbose_name="Banneryň üstindäki ýazgy")
    image = models.ImageField(
        upload_to="online-table/", blank=True, null=True, verbose_name="Banner")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Banner'
        verbose_name_plural = 'Online-Tablodaky banner'


# баннер для онлайн заказов
class OnlineTaxesBanner(models.Model):
    name = models.CharField(max_length=15, blank=True,
                            null=True, verbose_name="Banneryň üstindäki ýazgy")
    image = models.ImageField(
        upload_to="online-taxes/", blank=True, null=True, verbose_name="Banner")
    desc = RichTextUploadingField(
        blank=True, null=True, verbose_name="Giňişleýin beýany")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Banner'
        verbose_name_plural = 'Onlaýn sargytlaryň banner'


# все рейсы

class AllFlightBanner(models.Model):
    name = models.CharField(max_length=150, blank=True,
                            null=True, verbose_name="Banneryň üstindäki ýazgy")
    image = models.ImageField(upload_to="all-flight/",
                              blank=True, null=True, verbose_name="Banner")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Banner'
        verbose_name_plural = 'Gatnawlaň rejesi bannery'


class AllFlight(models.Model):
    FLIGHT_CATEGORY = [
        ('DEPARTURE', 'Uçuş'),
        ('ARRIVAL', 'Gonuş'),
    ]
    departure = models.CharField(
        max_length=10, blank=True, null=True, verbose_name="Uçan wagty")
    arrival = models.CharField(
        max_length=10, blank=True, null=True, verbose_name="Gonan wagty")
    flight_category = models.CharField(
        max_length=15, choices=FLIGHT_CATEGORY, default="DEPARTURE", verbose_name="Uçuş, Gonuş ?")
    title = models.CharField(max_length=255, blank=True,
                             null=True, verbose_name='Reýsyň ady')
    model_plane = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Uçaryň modeli")
    flight_day = models.CharField(
        max_length=50, blank=True, null=True, verbose_name="Uçýan günleri")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Üçuş-Gonuş'
        verbose_name_plural = 'Ahli uçuş-Gonuşlar'


# перевозка грузов

class Cargo(models.Model):
    name = models.CharField(max_length=15, blank=True,
                            null=True, verbose_name="Banneryň üstindäki ýazgy")
    image = models.ImageField(
        upload_to="online-taxes/", blank=True, null=True, verbose_name="Banner")
    desc = RichTextUploadingField(
        blank=True, null=True, verbose_name="Giňişleýin beýany")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Banner'
        verbose_name_plural = 'Goşlary geçirmegiň düzgünleri banner hemde maglumat'


class CargoPDF(models.Model):
    name = models.CharField(max_length=150, blank=True,
                            null=True, verbose_name="Filyň ady")
    file = models.FileField(blank=True, null=True,
                            verbose_name="File ýuklemek")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'File'
        verbose_name_plural = 'File ýuklemek "Goşlary geçirmegiň düzgünleri" '


# направление рейсов
class Directions(models.Model):
    name = models.CharField(max_length=15, blank=True, null=True,
                            verbose_name="Ugurlar banner üstindäki ýazgy")
    image = models.ImageField(upload_to="directions/",
                              blank=True, null=True, verbose_name="Banner")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Banner'
        verbose_name_plural = 'Ugurlar baradaky sahypa baradaky banner'


class DirectionsPlane(models.Model):
    name = models.CharField(max_length=15, blank=True,
                            null=True, verbose_name="Ugruň ady")
    image = models.ImageField(
        upload_to="directions_plane/", blank=True, null=True, verbose_name="Suraty")
    desc = RichTextUploadingField(
        blank=True, null=True, verbose_name="Giňişleýin beýany")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ugur'
        verbose_name_plural = 'Ugur goşmak'

# проверка перед полетом


class FlightCheck(models.Model):
    name = models.CharField(max_length=150, blank=True,
                            null=True, verbose_name="Banneryň üstindäki ýazgy")
    image = models.ImageField(
        upload_to="online-taxes/", blank=True, null=True, verbose_name="Banner")
    desc = RichTextUploadingField(
        blank=True, null=True, verbose_name="Giňişleýin beýany")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Banner'
        verbose_name_plural = 'Uçuşyň öň ýanyndaky barlag banner hemde maglumat'




# class MenuCat(models.Model):
    
#     name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Ady")



#     class Meta:
#         verbose_name = 'Menýu'
#         verbose_name_plural = 'Menýu bölümi'


#     def __str__(self):
#         return self.name





# добавит раздел

class Section(models.Model):
    MENU_CATEGORY = [
        ('HYZMATDAŞLARA', 'Hyzmatdaşlara'),
        ('HYZMATLAR', 'Hyzmatlar'),
    ]

    name = models.CharField(max_length=150, blank=True,
                            null=True, verbose_name="Banneryň üstindäki ýazgy")
    image = models.ImageField(
        upload_to="section/", blank=True, null=True, verbose_name="Banner")
    desc = RichTextUploadingField(
        blank=True, null=True, verbose_name="Bölümiň giňişleýin beýany")

    cat = models.CharField(
        max_length=150, choices=MENU_CATEGORY, default="HYZMATDAŞLARA", verbose_name="Haýsy menýu degişli ?")



    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Bölüm'
        verbose_name_plural = 'Bölüm goşmak'



# добавление разделов файлы пдф

class PDF(models.Model):
    name = models.CharField(max_length=150, blank=True,
                            null=True, verbose_name="Filyň ady")
    file = models.FileField(blank=True, null=True,
                            verbose_name="File ýuklemek")
    
    section = models.ForeignKey(Section, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Haýsy bölüme degişli")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'File'
        verbose_name_plural = 'File ýuklemek '
