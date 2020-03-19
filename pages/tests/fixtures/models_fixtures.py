import pytest
from faker import Faker


fake = Faker('pl_PL')


'''
Faker helpers

'''

def fixture_fake_helper(number_of_element, *args):
    data_list = [arg() for arg in args for i in range(number_of_element)]
    return data_list

'''


Global fixtures

'''

@pytest.fixture(scope='module')
def title_list():
    return fixture_fake_helper(20, fake.name, fake.random_number)

@pytest.fixture(scope='module')
def words_list():
    data_list = fake.sentence(nb_words=10, ext_word_list=None)
    return data_list

@pytest.fixture(scope='module')
def sentence_list():
    data_list = fake.sentences(nb=5, ext_word_list=None)
    return data_list

'''

SiteSeoTools fixtures

'''


@pytest.fixture(scope='module')
def site_url_list():
    return fixture_fake_helper(30, fake.url)


@pytest.fixture(scope='module')
def meta_title_list():
    data_list = ['To jest przykładowy title', 'AĄ ŚĆŚ w łł tqwr q', 
                '54654654 ', 'gger-gt34-ść- TESt']
    return data_list

@pytest.fixture(scope='module')
def meta_description_list():
    data_list = ['To jest przykładowy title', 'AĄ ŚĆŚ w łł tqwr q', 
                '54654654 ', 'gger-gt34-ść- TESt', 'to-Jest-001-test']
    return data_list

@pytest.fixture(scope='module')
def logo_text_list():
    data_list = ['To jest logo', 'To-jest-logo', 'Firma 001', 
                '-Hey!-logo', '001 LOGO']
    return data_list

@pytest.fixture(scope='module')
def google_map_iframe():
    data_list = ['<iframe src="https://www.google.com/maps/embed?pb=!1m14!1m12!1m3!1d4094.0606006095313!2d16.917226880496717!3d52.400459570505234!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!5e0!3m2!1spl!2spl!4v1574167223788!5m2!1spl!2spl" width="600" height="450" frameborder="0" style="border:0;" allowfullscreen=""></iframe>',
                '<iframe src="https://www.google.com/maps/embed?pb=!1m14!1m12!1m3!1d4094.0606006095313!2d16.917226880496717!3d52.400459570505234!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!5e0!3m2!1spl!2spl!4v1574167223788!5m2!1spl!2spl" width="100%" height="450" frameborder="0" style="border:0;" allowfullscreen=""></iframe>']
    return data_list

@pytest.fixture(scope='module')
def head_widgets():
    data_list = ['''
                <!-- Schema.org -->		<script type="application/ld+json">	{	"@context": "http://schema.org",	
                "@type": "LocalBusiness",	"address": {	"@type": "PostalAddress",	"addressLocality": "Radzionków",	
                "addressRegion": "śląskie",	"postalCode":"41-922",	"streetAddress": "ul. Kużaja 57"	},	
                "description": "Firma Samel oferuje geotkaniny poliestrowe, geowłókniny separacyjne, komory betonowe 
                oraz pierścienie regulacyjne i wyrównujące.",	"name": "SAMEL - materiały instalacyjne (Radzionków/Katowice)"
                ,	"telephone": "694500040",	"image": "http://samel.com.pl/images/logo.png",	"url": "http://samel.com.pl"
                ,"sameAs" : [	"https://twitter.com/samelpl",	"https://plus.google.com/b/101987331183009856280"],	
                "geo": {	"@type": "GeoCoordinates",	"latitude": "50.3854084",	"longitude": "18.9001732"	}	}	
                </script>
                '''
                ]
    return data_list

@pytest.fixture(scope='module')
def body_widgets():
    data_list = ['''
                <div id="profilki_socialbuttons_117635880">
                <a href="https://www.facebook.com/pptpolska" class="profilki_social_buttons_117635880">
                <svg xmlns="http://www.w3.org/2000/svg"" xml:space="preserve" width="100px" height="100px"
                 style="shape-rendering:geometricPrecision; text-rendering:geometricPrecision; 
                 image-rendering:optimizeQuality; fill-rule:evenodd; clip-rule:evenodd" viewBox="0 0 100 100" 
                 xmlns:xlink="http://www.w3.org/1999/xlink"><circle style="fill: hsl(221, 44%, 41%)" cx="50" 
                 cy="50" r="50"/><path style="fill: rgba(0,0,0,0.2);" d="M99.7354 55.165c-2.23584,21.7738 
                 -18.449,39.4102 -39.5165,43.7874l-18.3875 -18.3875 4.69964 -19.8072 -10.7339 -10.7339 28.2475 
                 -30.5495 35.6908 35.6908z"/><path style="fill: white;" d="M54.5296 39.2306l0 -6.34493c0,-2.38112 
                 1.57797,-2.93742 2.68939,-2.93742 1.11024,-0.00118111 6.82564,0 6.82564,0l0 -10.4741 -9.39929 
                 -0.0377956c-10.4375,0 -12.8139,7.81305 -12.8139,12.8127l0 6.98155 -6.0343 0 0 10.793 6.0343 
                 0c0,13.8509 0,30.5412 0,30.5412l12.6981 -0.00118111c0,0 0,-16.8545 0,-30.54l8.56424 0 1.10906 
                 -10.793 -9.6733 0z"/><circle id="front_svg_circle" style="fill: rgba(0,0,0,0.0)" cx="50" cy="50" 
                 r="50"/></svg></a>
                </div>
                ''',
                '''
                <div id="profilki_socialbuttons_117635883">
                <a href="https://www.instagram.com/scandiacosmetics/" class="profilki_social_buttons_117635883">
                <svg viewBox="0 0 512 512"><path d="M256 109.3c47.8 0 53.4 0.2 72.3 1 17.4 0.8 26.9 3.7 33.2 6.2 
                8.4 3.2 14.3 7.1 20.6 13.4 6.3 6.3 10.1 12.2 13.4 20.6 2.5 6.3 5.4 15.8 6.2 33.2 0.9 18.9 1 24.5 
                1 72.3s-0.2 53.4-1 72.3c-0.8 17.4-3.7 26.9-6.2 33.2 -3.2 8.4-7.1 14.3-13.4 20.6 -6.3 6.3-12.2 
                10.1-20.6 13.4 -6.3 2.5-15.8 5.4-33.2 6.2 -18.9 0.9-24.5 1-72.3 1s-53.4-0.2-72.3-1c-17.4-0.8-26.9-3.7-33.2-6.2 
                -8.4-3.2-14.3-7.1-20.6-13.4 -6.3-6.3-10.1-12.2-13.4-20.6 -2.5-6.3-5.4-15.8-6.2-33.2 -0.9-18.9-1-24.5-1-72.3s0.2-53.4 
                1-72.3c0.8-17.4 3.7-26.9 6.2-33.2 3.2-8.4 7.1-14.3 13.4-20.6 6.3-6.3 12.2-10.1 20.6-13.4 6.3-2.5 15.8-5.4 
                33.2-6.2C202.6 109.5 208.2 109.3 256 109.3M256 77.1c-48.6 0-54.7 0.2-73.8 1.1 -19 0.9-32.1 3.9-43.4 8.3 -11.8 
                4.6-21.7 10.7-31.7 20.6 -9.9 9.9-16.1 19.9-20.6 31.7 -4.4 11.4-7.4 24.4-8.3 43.4 -0.9 19.1-1.1 25.2-1.1 73.8 0 
                48.6 0.2 54.7 1.1 73.8 0.9 19 3.9 32.1 8.3 43.4 4.6 11.8 10.7 21.7 20.6 31.7 9.9 9.9 19.9 16.1 31.7 20.6 11.4 4.4 
                24.4 7.4 43.4 8.3 19.1 0.9 25.2 1.1 73.8 1.1s54.7-0.2 73.8-1.1c19-0.9 32.1-3.9 43.4-8.3 11.8-4.6 21.7-10.7 
                31.7-20.6 9.9-9.9 16.1-19.9 20.6-31.7 
                4.4-11.4 7.4-24.4 8.3-43.4 0.9-19.1 1.1-25.2 1.1-73.8s-0.2-54.7-1.1-73.8c-0.9-19-3.9-32.1-8.3-43.4 
                -4.6-11.8-10.7-21.7-20.6-31.7 -9.9-9.9-19.9-16.1-31.7-20.6 -11.4-4.4-24.4-7.4-43.4-8.3C310.7 77.3 304.6 
                77.1 256 77.1L256 77.1z"/><path d="M256 164.1c-50.7 0-91.9 41.1-91.9 91.9s41.1 91.9 91.9 91.9 91.9-41.1 
                91.9-91.9S306.7 164.1 256 164.1zM256 315.6c-32.9 0-59.6-26.7-59.6-59.6s26.7-59.6 59.6-59.6 59.6 26.7 59.6 
                59.6S288.9 315.6 256 315.6z"/><circle cx="351.5" cy="160.5" r="21.5"/></svg></a>
                </div>
                ''',
                '''
                <style>
                #profilki_socialbuttons_117635880 a{margin: 0 6px; display: block; z-index: 99999; top: 240px; 
                # right: 1px;  position: fixed;} 
                #profilki_socialbuttons_117635882 a{margin: 0 6px; display: block; z-index: 99999; top: 300px; 
                # right: 1px;  position: fixed;}
                #profilki_socialbuttons_117635880 svg *{pointer-events: all;} 
                #profilki_socialbuttons_117635880 svg {display: block; margin: 6px; margin-left: auto; margin-right: 
                # auto; pointer-events: all;height: 52px; width: 52px}
                #profilki_socialbuttons_117635880 svg:hover #front_svg_circle{fill: rgba(255,255,255,0.2) !important;}
                #profilki_socialbuttons_117635882 svg *{pointer-events: all;} 
                #profilki_socialbuttons_117635882 svg {display: block; margin: 6px; margin-left: auto; margin-right: 
                # auto; pointer-events: all;height: 52px; width: 52px}
                #profilki_socialbuttons_117635882 svg:hover #front_svg_circle{fill: rgba(255,255,255,0.2) !important;}
                # </style>
                '''

                ]
    return data_list


'''

SiteSeoTools fixtures

'''

@pytest.fixture(scope='module')
def company_name_list():
    data_list = ['Nazwa firmy', 'NAZWA FIRMY', 'Nazwa-firmy', ' 01 Firma'
                '01-02-Firma', 'firma.pl', 'firma.com.pl', 'moja-firma.com.pl']
    return data_list

@pytest.fixture(scope='module')
def company_adress():
    return fixture_fake_helper(30, fake.address)

@pytest.fixture(scope='module')
def company_phone_list():
    data_list = ['123 123 123', '123123123', '+48 123456789', '+48 123 123 123',
                '(48) 345 345 344', '+(48)22 234 232']
    return data_list

@pytest.fixture(scope='module')
def company_email_list():
    return fixture_fake_helper(30, fake.company_email, fake.email, fake.free_email)

'''

Box fixtures

'''

@pytest.fixture(scope='module')
def box_list():
    data_list = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p']
    return data_list


'''

Homepage fixtures

'''

@pytest.fixture(scope='module')
def content_list():
    data_list = ['''<div>
                    <h1>Nagłówek strony</h1>
                    </div>

                    <div>
                    <p>officia ipsum vitae eos soluta suscipit ut nulla voluptate unde similique tempore itaque quo quia cumque sapiente magnam iure ratione porro iusto maxime delectus libero obcaecati harum in vero odio earum dolore dolorum odit accusamus aperiam et doloremque nisi labore quod esse a id perspiciatis ullam assumenda possimus quidem animi dignissimos consectetur enim blanditiis expedita nihil nobis atque accusantium fuga mollitia sed ipsa adipisci pariatur velit</p>
                    </div>
                    <div style="width:100%"><img style="text-align:center"alt="" src="/media/uploads/2019/11/21/junction-984045_1920.jpg" style="width: 720px; height: 404px;" /></div>'
                    ''',
                    '''
                    <div>
                        <h2>To jest test</h2>
                        <a href="www.google.com">Google</a>
                        <ul>
                            <li>test 1</li>
                            <li> test 2</li>
                        </ul>
                    </div>
                    ''',
                ]
    return data_list


'''

Subpage fixtures

'''

@pytest.fixture(scope='module')
def slug_list():
    return fixture_fake_helper(20, fake.slug, fake.word)


'''

CustomCSS fixtures

'''

@pytest.fixture(scope='module')
def css_list():
    data_list = ['''
                .klasa{color:red; background-color:#f22f2f;}
                #id1{ font-size:20px; transform: all 0.5s}
                .klasa #id1:hover{margin:20px 0 10px 0;}
    
                ''',
                '''
                div > * {text-transform:uppercase;}
                h1, h2, .klasa {font-weight:300;}
                '''
    ]
    return data_list