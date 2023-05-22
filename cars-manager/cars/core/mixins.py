import random
import requests
from cloudinary import uploader
from django.core.files.uploadedfile import InMemoryUploadedFile

from cars.ad.models import Photo
from cars.profiles.models import DeleteCode


class ImageControlsMixin:
    def add_default_images(self, ad_object):
        photo_set = ad_object.photo_set.all()
        for i in range(4):
            try:
                if photo_set[i]:
                    continue
            except IndexError:
                image = Photo.objects.create(ad=ad_object)
                image.save()

    def delete_changed_images(self, old_photos, new_photos):
        old_photo_names_ll = []
        new_photo_names_ll = []
        for old_photo in old_photos:
            old_photo_names_ll.append(old_photo.image.public_id)
        for new_photo in new_photos:
            new_photo_names_ll.append(new_photo.image.public_id)
        for old_photo_name in old_photo_names_ll:
            if old_photo_name not in new_photo_names_ll:
                uploader.destroy(f'{old_photo_name}')



class FormControlsMixin:
    placeholders = {}
    classes = {}
    required_fields = []

    def add_form_control_class(self):
        for name, field in self.fields.items():
            if 'class' not in field.widget.attrs:
                field.widget.attrs['class'] = ''
            field.widget.attrs['class'] += 'form-control'

    def add_place_holders(self):
        for field, placeholder in self.placeholders.items():
            self.fields[field].widget.attrs['placeholder'] = placeholder

    def add_classes(self):
        for field, class_name in self.classes.items():
            if self.fields[field].widget.attrs.get('class') is None:
                self.fields[field].widget.attrs['class'] = ''
            self.fields[field].widget.attrs['class'] += f' {class_name}'

    def disable_fields(self):
        for name, field in self.fields.items():
            field.disabled = True

    def field_required(self):
        for field_name in self.required_fields:
            self.fields[field_name].required = True


class CarImagesMapperMixin:
    CAR_MAKE_EMBLEM = {
        'bmw': 'https://m.media-amazon.com/images/I/61HobFlkn-L.jpg',
        'mercedes-benz': 'https://www.logodesignlove.com/wp-content/uploads/2009/11/mercedes-benz-logo-design.jpg',
        'audi': 'https://thumbs.dreamstime.com/b/snapdeal-logo-190673268.jpg',
        'volkswagen': 'https://w7.pngwing.com/pngs/647/1018/png-transparent-volkswagen-group-car-logo-mercedes-benz-volkswagen-emblem-trademark-logo.png',
        'mazda': 'https://1000logos.net/wp-content/uploads/2019/12/Mazda-Logo-2015.png',
        'ford': 'https://1000logos.net/wp-content/uploads/2018/02/Ford-Logo.png',
        'honda': 'https://d354nuoz4t18d4.cloudfront.net/3838a1c5ad3d367c10d124688af676d6/images/custom/honda-logo-silver.jpg',
        'porsche': 'https://di-uploads-pod3.dealerinspire.com/porscheoffremont/uploads/2018/09/porsche-logo.jpg',
        'ferrari': 'https://logos-world.net/wp-content/uploads/2020/07/Ferrari-Scuderia-Logo.jpg',
        'mitsubishi': 'https://1000logos.net/wp-content/uploads/2020/02/Mitsubishi-Logo.jpg',
        'renault': 'https://car-logos.net/wp-content/uploads/2018/09/renault-logo.jpg',
        'peugeot': 'https://www.media.stellantis.com/cache/1/a/b/a/0/1aba00ae2494614dad2083e6d1ee1fa4dd0953b7.png',
        'fiat': 'https://1000logos.net/wp-content/uploads/2020/02/Fiat-Logo.png',
    }
    CAR_MODEL_TO_IMG = {
        'bmw': {
            '7': {
                'first_model': 'https://www.edmunds.com/assets/m/bmw/7-series/1993/oem/1993_bmw_7-series_sedan_740il_fq_oem_1_500.jpg',
                'second_model': 'https://s1.cdn.autoevolution.com/images/gallery/BMW7Series-E38--1226_5.jpg',
                'third_model': 'https://carsguide-res.cloudinary.com/image/upload/f_auto,fl_lossy,q_auto,t_cg_hero_large/v1/editorial/2006-BMW-7Series-750Li-Sedan-Grey-Press-Image-1001x565p.jpg',
                'fourth_model': 'https://media.ed.edmunds-media.com/bmw/7-series/2012/oem/2012_bmw_7-series_sedan_740i_fq_oem_1_1600.jpg',
                'fifth_model': 'https://media.ed.edmunds-media.com/bmw/7-series/2018/oem/2018_bmw_7-series_sedan_740e-xdrive-iperformance_fq_oem_1_1600.jpg',
            },
            '5': {
                'first_model': 'https://autotraderau-res.cloudinary.com/image/upload/t_gl/v1/glasses/CNjW.jpg',
                'second_model': 'https://img.autoabc.lv/bmw-5-serija/bmw-5-serija_2000_Sedans_151022122627_1.jpg',
                'third_model': 'https://media.autoexpress.co.uk/image/private/s--X-WVjvBW--/f_auto,t_content-image-full-desktop@1/v1562249935/autoexpress/images/car_photo_19766.jpg',
                'fourth_model': 'https://car-images.bauersecure.com/wp-images/13824/01bmw5-series2014carreview.jpg',
                'fifth_model': 'https://www.motortrend.com/uploads/sites/10/2019/08/2019-bmw-5-series-540i-m-sport-design-rwd-sedan-angular-front.png',
            },
            '3': {
                'first_model': 'https://www.topgear.com/sites/default/files/images/news-article/2015/07/e2f1bf52666faa94421251f8e39fa686/e36_1.jpg',
                'second_model': 'https://i.ytimg.com/vi/VuqAMTDouQA/sddefault.jpg',
                'third_model': 'https://parkers-images.bauersecure.com/Scale/wp-images/960/cut-out/450x300/bmw_3series_saloon.jpg',
                'fourth_model': 'https://i.gaw.to/content/photos/50/79/507923-bmw-serie-3-2013-2018-quoi-savoir-avant-d-acheter.jpeg',
                'fifth_model': 'https://hips.hearstapps.com/hmg-prod/images/2020-bmw-m340i-v-2020-genesis-g70-3p3t-1016-hdr-1571838328.jpg?crop=0.673xw:0.824xh;0.0717xw,0.176xh&resize=640:*',
            },
            '1': {
                'third_model': 'https://www.topgear.com/sites/default/files/news/image/2015/04/Large%20Image_6229.jpg?w=1280&h=720',
                'fourth_model': 'https://m.atcdn.co.uk/vms/media/2c399467ec404243ad517cbe76d6ef9f.jpg',
                'fifth_model': 'https://www.nastarta.com/wp-content/uploads/2019/05/b056c2ce-bmw-1-series-2.jpg',
            }
        },
        'audi': {
            '80': {
                'first_model': 'https://img.autoabc.lv/audi-80/audi-80_1991_Sedans_15111191642_0.jpg',
            },
            '90': {
                'first_model': 'https://prod.pictures.autoscout24.net/listing-images/67e6549e-c719-472f-a54a-b4662de56db3_09f3ad41-c3dc-4fe2-bb2c-6f4ac976baa6.jpg/420x315.jpg',
            },
            '100': {
                'first_model': 'https://img.autoabc.lv/audi-100/audi-100_1982_Sedans_151116124912_2.jpg',
            },
            '4': {
                'first_model': 'https://www.nastarta.com/wp-content/uploads/2018/04/Audi-B5-%E2%80%93-8D-844.jpg',
                'second_model': 'https://img.autoabc.lv/audi-a4/audi-a4_2001_Sedans_151019110935_19.jpg',
                'third_model': 'https://www.edmunds.com/assets/m/audi/a4/2005/oem/2005_audi_a4_sedan_32-quattro_fq_oem_1_500.jpg',
                'fourth_model': 'https://cars.usnews.com/static/images/Auto/izmo/310415/2010_audi_a4_angularfront.jpg',
                'fifth_model': 'https://cdn.euroncap.com/media/19651/audi_a4_2015_uncrashed-media-gallery.jpg',
            },
            '6': {
                'first_model': 'https://media.ed.edmunds-media.com/audi/a6/1997/oem/1997_audi_a6_sedan_28_fq_oem_1_500.jpg',
                'second_model': 'https://preview2.netcarshow.com/Audi-A6-2002-hd.jpg',
                'third_model': 'https://media.ed.edmunds-media.com/audi/a6/2007/oem/2007_audi_a6_wagon_32-avant-quattro_fq_oem_2_1600.jpg',
                'fourth_model': 'https://cdn.carbuzz.com/gallery-images/2012-audi-a6-carbuzz-626270.jpg',
                'fifth_model': 'https://hips.hearstapps.com/hmg-prod/images/2020-audi-a6-mmp-1-1567713400.jpg',

            },
            '8': {
                'first_model': 'https://autotraderau-res.cloudinary.com/image/upload/t_gl/v1/glasses/YV0U.jpg',
                'second_model': 'https://i.ytimg.com/vi/Fa8PIGHA1gw/hqdefault.jpg',
                'third_model': 'https://www.newcartestdrive.com/wp-content/uploads/2004/07/05-a8-hero.jpg',
                'fourth_model': 'https://img.autoabc.lv/audi-a8/audi-a8_2010_Sedans_15101363016_10.jpg',
                'fifth_model': 'https://media.ed.edmunds-media.com/audi/a8/2020/oem/2020_audi_a8_sedan_l-55-tfsi-quattro_fq_oem_1_600.jpg',
            }
        },
        'mercedes-benz': {
            'c': {
                'first_model': 'https://d1gymyavdvyjgt.cloudfront.net/drive/images/made/drive/images/remote/https_ssl.caranddriving.com/f2/images/used/big/mbcclas_750_500_70.jpg',
                'second_model': 'https://platform.cstatic-images.com/xlarge/in/v2/stock_photos/58730ff6-db22-4b09-a27f-66a649aa05e6/cdab4f9f-438e-4590-aca0-5708ed09c5b2.png',
                'third_model': 'https://car-images.bauersecure.com/wp-images/6146/mercc-classnew_1_560px.jpg',
                'fourth_model': 'https://www.auto-data.net/images/f3/file6126484.jpg',
                'fifth_model': 'https://cdn.jdpower.com/JDPA_2020%20Mercedes-AMG%20C63%20S%20Selenite%20Gray%20Front%20View.jpg',
            },
            'e': {
                'first_model': 'https://www.classicdriver.com/sites/default/files/cars_images/33362/PA19_r0042/8a22bd5267dd283a350286a080d93651.jpeg',
                'second_model': 'https://platform.cstatic-images.com/medium/in/v2/stock_photos/087a55bf-7c07-4ad1-8368-f2dc16661079/d09354dd-be72-448c-952f-fac4560fbf3a.png',
                'third_model': 'https://www.cars.com/i/large/in/v2/stock_photos/70cfa235-637a-47a8-ba05-f881bdcf97d7/b3ef0c04-5246-421c-acce-47f7222e0f21.png',
                'fourth_model': 'https://hips.hearstapps.com/autoweek/assets/s3fs-public/130319987.jpg',
                'fifth_model': 'https://www.auto-data.net/images/f51/Mercedes-Benz-E-class-Coupe-C238-facelift-2020.jpg',
            },
            's': {
                'first_model': 'https://www.carpixel.net/w/bc2b0e680d552efc029123f31c58e810/mercedes-benz-s-class-long-wallpaper-hd-55916.jpg',
                'second_model': 'https://www.classicdriver.com/sites/default/files/cars_images/120046/41582-22/e743f50961d8702671f9d8f9c1f87991.jpeg',
                'third_model': 'https://www.autocar.co.uk/sites/autocar.co.uk/files/mercedes-benz-s-class.jpg',
                'fourth_model': 'https://img.autoabc.lv/Mercedes-S-klase/Mercedes-S-klase_2013_Sedans_164830549_9.jpg',
                'fifth_model': 'https://www.autocar.co.uk/sites/autocar.co.uk/files/images/car-reviews/first-drives/legacy/1-mercedes-benz-s500-2020-fd-hero-front.jpg',
            },
        },
        'volkswagen': {
            'tiguan': {
                'fourth_model': 'https://hips.hearstapps.com/hmg-prod/amv-prod-cad-assets/images/11q3/409394/2012-volkswagen-tiguan-tdi-first-drive-review-car-and-driver-photo-410333-s-original.jpg'
            },
            'touareg': {
                'third_model': 'https://autotraderau-res.cloudinary.com/image/upload/t_gl/v1/glasses/BVDMOtER.jpg',
                'fourth_model': 'https://carsguide-res.cloudinary.com/image/upload/f_auto,fl_lossy,q_auto,t_cg_hero_large/v1/editorial/dp/albums/album-5446/lg/Volkswagen_Touareg_V8_TDI_R-Line_front.jpg',
            },
            'golf': {
                'first_model': 'https://www.auto-data.net/images/f54/Volkswagen-Golf-III-1HX_1.jpg',
                'second_model': 'https://www.autoscout24.nl/cms-content-assets/51J2Nki9JB9isw0Qaxu9Ah-d87bd8cf54ca42ab82ba97c68febacdc-volkswagen-golf-4-front-1100.jpeg',
            },
            'jetta': {
                'first_model': 'https://platform.cstatic-images.com/xlarge/in/v2/stock_photos/239ead43-6013-4aa6-bfa0-d5031089fa21/74b6492e-789f-4697-a5a2-fc9b72cb48e3.png',
                'second_model': 'https://picolio.auto123.com/00photo/volkswagen/jetta4dr-gl.jpg',
            },
            'passat': {
                'first_model': 'https://platform.cstatic-images.com/xlarge/in/v2/stock_photos/f83df29d-7993-4782-beab-e13780bfafe4/4d9e0c18-08ce-4d2e-872e-b2959620e1cf.png',
                'second_model': 'https://s1.cdn.autoevolution.com/images/gallery/VOLKSWAGENPassatB4-1509_3.jpg',
            }
        },
    }

    def map_images(self, data):
        for car_data in data:
            transformed_model_value = ''
            car_make = car_data['make']
            car_year = car_data['year']
            car_model = car_data['model']
            if car_make == 'audi':
                if car_model in ['80', '90', '100']:
                    transformed_model_value = car_model
                else:
                    transformed_model_value = car_model.split(' ')[0][1]
            elif car_make in ['bmw', 'mercedes-benz']:
                transformed_model_value = car_model[0]
            elif car_make == 'volkswagen':
                transformed_model_value = car_model.split(' ')[0]
                # if car_model.split(' ')[0] == 'golf':
                #     transformed_model_value = 'golf'
            try:
                car_body_type = self.year_to_model(car_year, car_make)
                car_img = self.CAR_MODEL_TO_IMG[car_make][transformed_model_value][car_body_type]
            except KeyError:
                if car_make not in self.CAR_MAKE_EMBLEM:
                    car_img = 'https://thumbs.dreamstime.com/b/no-image-available-icon-photo-camera-flat-vector-illustration-132483141.jpg'
                else:
                    car_img = self.CAR_MAKE_EMBLEM[car_make]
            car_data['current_img'] = car_img
        return data

    def year_to_model(self, year, car_make):
        if car_make == 'bmw' or car_make == 'mercedes-benz':
            if 1992 <= year <= 1997:
                return 'first_model'
            elif 1998 <= year <= 2004:
                return 'second_model'
            elif 2005 <= year <= 2011:
                return 'third_model'
            elif 2012 <= year <= 2018:
                return 'fourth_model'
            elif 2019 <= year <= 2023:
                return 'fifth_model'
        elif car_make == 'audi':
            if 1994 <= year <= 2000:
                return 'first_model'
            elif 2001 <= year <= 2004:
                return 'second_model'
            elif 2005 <= year <= 2008:
                return 'third_model'
            elif 2009 <= year <= 2016:
                return 'fourth_model'
            elif 2017 <= year <= 2023:
                return 'fifth_model'
        elif car_make == 'volkswagen':
            if 1993 <= year <= 1997:
                return 'first_model'
            elif 1998 <= year <= 2003:
                return 'second_model'
            elif 2004 <= year <= 2008:
                return 'third_model'
            elif 2009 <= year <= 2012:
                return 'fourth_model'
            elif 2013 <= year <= 2019:
                return 'fifth_model'


class CarApiMixin(CarImagesMapperMixin):
    __URL = 'https://api.api-ninjas.com/v1/cars'

    def parse_data(self, **data):
        parameters = []
        for k, v in data.items():
            if not v or v == 'all':
                continue
            parameters.append(f'{k}={v}')
        return '&'.join(parameters)

    def make_request(self, **data):
        url = self.__URL + f'?{self.parse_data(**data)}&limit=3000'
        headers = {
            'X-Api-Key': 'WNsOo0klVkYBZnAiRIqPWw==2cdefSnle0bZLX45',
        }
        response = requests.get(url, headers=headers)
        data = response.json()
        mapped_data = self.map_images(data)
        return mapped_data


class AssignDataUpdateAdForm:

    def asign_data_to_profile(self, profile, form):
        profile.first_name = form.cleaned_data['first_name']
        profile.last_name = form.cleaned_data['last_name']
        profile.age = form.cleaned_data['age']
        profile.phone_number = form.cleaned_data['phone_number']

    def update_profile_image(self, profile, form):
        if type(form.cleaned_data['image']) is InMemoryUploadedFile:
            profile.image = uploader.upload_resource(
                form.cleaned_data['image'],
                use_filename=True,
                unique_filename=False,
                filename_override=f'{profile.user.username}',
                folder=f'/profiles/',
            )


def generate_delete_code():
    nums = set()
    while len(nums) < 2:
        nums.add(random.randint(99999, 999999))
    delete_code = nums.pop()
    return delete_code


def add_generated_delete_code_to_profile(delete_code, profile):
    delete_code_obj = DeleteCode.objects.get(profile=profile)
    delete_code_obj.generated_code = delete_code
    delete_code_obj.save()


def delete_assets_cloudinary(ad):
    image_set = ad.photo_set.all()
    for object in image_set:
        uploader.destroy(f'{object.image}')
