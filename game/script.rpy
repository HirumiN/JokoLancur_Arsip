# Kamu dapat taruh script game mu di file ini.

label splashscreen:
    scene black
    $ renpy.pause(1)

    show text "Tim kami mempersembahkan" with dissolve

    $ renpy.pause(2)

    hide text with dissolve

    $ renpy.pause(1)

    return


# Deklarasikan gambar di bawah line ini, menggunakan pernyataan image.
# cnth. image eileen happy = "eileen_happy.png"
#image bg blck = "images/blck.png"
image lapangan = "lapangan.png"
image gudang = "gudang.png"
image hutan = "hutan.png"
image pekarangan = "pekarangan.png"
image ruang_tamu = "ruang_tamu.png"
image pernikahan = "pernikahan.png"
image sawah = "bengi.png"
image teras = "teras.png"
image siluet = "siluet.png"
image jalan = "jalan.png"
image tamu2 = "ruangtamukiai.png"
image danau = "danau.png"
image halaman = "halaman.png"
image white = "light.png"
image true = "true.png"
image good = "good.png"
image bad = "bad.png"
image peace = "peace.png"
image bg = "bg.png"
image jnetral = "pa_netral.png"
image jblush = "jblush.png"
image jmarah = "jmarah.png"
image jmarah flip= im.Flip ("jmarah.png", horizontal="true")
image jsad = "jsad.png"
image ssad = "ssad.png"
image sblush = "sblush.png"
image smarah = "smarah.png"
image skaget = "skaget.png"
image snetral = "snetral.png"
image snetral flip= im.Flip ("snetral.png", horizontal="true")
image skaget flip= im.Flip ("skaget.png", horizontal="true")
image sblush flip= im.Flip ("sblush.png", horizontal="true")
image hnetral flip= im.Flip ("hnetral.png", horizontal="true")
image hkaget flip= im.Flip ("hkaget.png", horizontal="true")
image hmarah flip= im.Flip ("hmarah.png", horizontal="true")
image hrmarah flip= im.Flip ("hrmarah.png", horizontal="true")
image daryoto = "daryoto.png"
image besok = "besok.png"
image mmarah = "mmarah.png"
image msedih = "msedih.png"
image mkaget = "mkaget.png"
image hkaget = "hkaget.png"
image hrkaget = "hrkaget.png"
image hmarah = "hmarah.png"
image hrmarah = "hrmarah.png"
image hnetral = "hnetral.png"
image hsedih = "hsedih.png"
image hrsedih = "hrsedih.png"



# Deklarasikan karakter yang digunakan di game.
define W1 = Character('Warga #1', color="#c8ffc8")
define W2 = Character('Warga #2', color="#c8ffc8")
define warga = Character ('Semua warga', color="#eeffc8")
define Joko = Character ('Joko Lancur', color="#ffc8c8")
define Daryoto = Character ('Daryoto', color="#068877")
define Siti = Character ('Siti Amirah', color="#88067d")
define kiai = Character ('Kiai Muslim', color="#2c8d2c")
define Han = Character ('Ki Hanggolono', color="#f80f0f")

transform jright:
    xalign 0.99
    yalign -1.5
    zoom 1.2
transform jleft:
    xalign 0.01
    yalign -1.5
    zoom 1.2
transform sright:
    xalign 0.92
    yalign 1.1
transform sleft:
    xalign 0.08
    yalign 1.1
transform dright:
    xalign 1.15
    yalign -1
    zoom 1.4
transform mright:
    xalign 1.3
    yalign -0.2
    zoom 2.0
transform hright:
    xalign 1.15
    yalign 0.98
    zoom 2
transform hleft:
    xalign -0.15
    yalign 0.98
    zoom 2

init:
    python:
        _preferences.set_volume('music', 0.9)
        renpy.restart_interaction()
init:

    python:
    
        import math

        class Shaker(object):
        
            anchors = {
                'top' : 0.0,
                'center' : 0.5,
                'bottom' : 1.0,
                'left' : 0.0,
                'right' : 1.0,
                }
        
            def __init__(self, start, child, dist):
                if start is None:
                    start = child.get_placement()
                #
                self.start = [ self.anchors.get(i, i) for i in start ]  # central position
                self.dist = dist    # maximum distance, in pixels, from the starting point
                self.child = child
                
            def __call__(self, t, sizes):
                # Float to integer... turns floating point numbers to
                # integers.                
                def fti(x, r):
                    if x is None:
                        x = 0
                    if isinstance(x, float):
                        return int(x * r)
                    else:
                        return x

                xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

                xpos = xpos - xanchor
                ypos = ypos - yanchor
                
                nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

                return (int(nx), int(ny), 0, 0)
        
        def _Shake(start, time, child=None, dist=100.0, **properties):

            move = Shaker(start, child, dist=dist)
        
            return renpy.display.layout.Motion(move,
                        time,
                        child,
                        add_sizes=True,
                        **properties)

        Shake = renpy.curry(_Shake)
init:
    $ sshake = Shake((0, 0, 0, 0), 1.0, dist=15)
init python:
    def eyewarp(x):
        return x**1.33
    eye_open = ImageDissolve("eye.png", .5, ramplen=128, reverse=False, time_warp=eyewarp)
    eye_shut = ImageDissolve("eye.png", .5, ramplen=128, reverse=True, time_warp=eyewarp)
image black:
    Solid("#000")
image white:
    Solid("#FFF")

# Game dimulai disini.
label start:
    stop music fadeout 1.0
    scene lapangan with fade
    "Di tengah keramaian lapangan Desa Mirah yang dikunjungi oleh para bapak-bapak, terdapat sebuah kegiatan rutin yang selalu menarik perhatian masyarakat: sabung ayam."
    play music "audio/tema_utama.mp3" fadein 3.0
    "Meskipun bukan merupakan sebuah festival, tarung ayam telah menjadi bagian dari tradisi yang dijalankan oleh masyarakat setempat."
    "Saat matahari mulai terbenam di ufuk barat, lapangan ini selalu dipenuhi oleh warga yang ingin mendaftarkan ayam mereka, para taruhan, atau bahkan hanya sekadar menjadi penonton."
    "Ayam-ayam yang akan bertarung dipersiapkan dan dimasukkan ke dalam sebuah arena yang dikelilingi oleh pagar kayu setinggi 70 cm."
    "Dengan antusias tinggi, para warga berkumpul mengelilingi arena pertandingan seperti para pendukung yang mendukung jagoan mereka."
    "Suara sorakan dan seruan semakin memeriahkan suasana, menciptakan atmosfer yang penuh gairah di sekitar arena."
    "*kkrrrroooookk..!! (suara ayam)"
    scene lapangan at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=5)
    W1 "Tiidaaaakk..!!"
    "Kelihatannya ayam jago milik Ki Daryoto menang lagi"
    "Pada beberapa kali pertandingan terakhir, ayam jago milik Ki Daryoto tampaknya meraih kemenangan yang gemilang."
    "Kehebatan ayamnya begitu mendominasi di arena tarung selama dua minggu terakhir"
    "Dengan kepiawaian dan kekuatan yang dimiliki ayam jago tersebut, Ki Daryoto menjadi sorotan utama di antara para penonton dan peserta lainnya."

    show siluet with moveinright:
        xalign 0.94
        yalign 1.5
        zoom 1.5
    W2 "Joko Lancur? kau mau adu ayam dengannya?"
    show jnetral at jleft with moveinleft
    play music "audio/gelut.mp3" fadein 1.0 volume 0.8
    Joko "iya..,"
    Joko "kali ini aku akan menang."
    W2 "kau yakin..?"
    hide siluet with moveoutright
    menu:
        "Pastinya":
            jump pilih1_a
        "...":
            jump tarung

label pilih1_a:
    Joko "Sangat Yakin"
    jump tarung

label tarung:
    hide jnetral with moveoutright
    "Suasana begitu ramai dan energi penuh semangat terasa di udara."
    "Para penonton memenuhi tepi arena, menanti pertandingan yang akan segera dimulai."
    "Di tengah kerumunan, terlihat Ki Daryoto dengan wajah berbinar-binar. Ia memegang erat ayam jago kesayangannya sambil tersenyum bangga."
    "Tidak hanya kebahagiaan yang terpancar dari wajah Ki Daryoto, tetapi juga kepuasan finansial. Ia sibuk menghitung uang hasil kemenangan ayam jago tersebut. Rupiah demi rupiah naik seiring kemenangan yang diraih"
    show daryoto at dright with moveinright
    Daryoto "siapa lagi yang ingin ayamnya pincang? maju sini!"
    show jnetral at jleft with moveinleft:
        ease 0.5 zoom 1.01
    Joko "hanya menang beberapa kali saja kau sudah sombong Ki.."
    show jnetral at jleft:
        ease 0.5 zoom 1.0
    Daryoto "Lihat siapa ini..? Joko Lancur!! Hahaha..,"
    Joko "..."
    Daryoto "apa kisanak yakin? Jangan merengek ke ayahmu jika peliharaanmu mati"
    show jnetral at jleft:
        ease 0.5 zoom 1.01
    Joko "Ayam yang akan mati adalah milikmu."
    show jnetral at jleft:
        ease 0.5 zoom 1.0
    Daryoto "Hah! Percuma bicara besar tanpa tindakan, Joko. Mari kita buktikan siapa yang lebih unggul di sini."
    show jnetral at jleft:
        ease 0.5 zoom 1.01
    Joko "Jangan berangan-angan terlalu jauh, Daryoto. Kejayaanmu hanya sementara!"
    Joko "Karena akulah yang akan menjatuhkan kejayaanmu hari ini."
    show jnetral at jleft:
        ease 0.5 zoom 1.0
    Daryoto "Hahaha! Sepertinya kau berpikir kau adalah manusia pilihan yang sempurna."
    show jnetral at jleft:
        ease 0.5 zoom 1.01
    Joko "Memang benar, aku memiliki apa yang tidak kau miliki."
    show jnetral at jleft:
        ease 0.5 zoom 1.0
    Daryoto "BOCAH BRENGSEK!! kau akan membayar ucapanmu!"
    show jnetral at jleft:
        ease 0.5 zoom 1.01
    Joko "Coba saja."
    show jnetral at jleft:
        ease 0.5 zoom 1.0
    hide jnetral with fade
    hide daryoto with fade
    "Aku berjalan mendekati arena. diiringi dengan sorakan para warga yang tidak sabar melihat pertandingan."
    "Banyak uang yang terkumpul untuk bertaruh siapa yang akan menjadi pemenang."
    "orang angkuh seperti Ki Daryoto sangat memuaskan bila dijatuhkan."
    "jadi, aku harus menang."
    "Aku dan Ki Daryoto menyekal ayam di pinggir arena dan bersiap untuk melepas genggaman."
    scene lapangan at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=2)
    warga "ji.. ro.. lu..!!"
    "Di tengah arena yang dipenuhi oleh hiruk-pikuk suara penonton, ayam kami berdua saling melompat dan mencakar satu sama lain. Gerakan yang cepat dan tajam menggambarkan keganasan pertarungan mereka."
    "Dalam suasana yang begitu sengit, sorakan meriah terdengar di sekeliling. Suporter dari kedua belah pihak berteriak-teriak memberikan dukungan kepada ayam jago yang mereka jagokan."
    play sound "audio/Suara ayam.mp3" volume 0.5
    "Sorakan gemuruh tersebut menciptakan aura kegembiraan dan ketegangan yang tidak terbendung."
    "Setiap serangan dan pertahanan dari kedua ayam jago tersebut disambut dengan sorakan dan teriakan dari para penonton."
    menu:
        "Strategi yang digunakan."
        "menyerang":
            jump menang
        "bertahan":
            jump kalah

label menang:
    "Ayam yang menjadi milikku melepaskan kemarahan melalui serangan-serangannya yang penuh keganasan terhadap ayam Daryoto."
    "Dengan setiap gerakan yang dipenuhi kecepatan yang memukau, ia dengan ganas melancarkan serangan-serangan bertubi-tubi yang menghujam habis ke tubuh lawannya. Tak ada kesempatan bagi ayam Daryoto untuk menghindar atau membalas serangan."
    "Namun, dalam keberaniannya yang menakjubkan, ayamku tidak luput dari serangan mematikan yang dilancarkan oleh ayam Daryoto."
    "Semakin terluka, ayamku malah semakin mengamuk. Hingga beberapa detik kemudian ia berhasil menumbangkan Ayam Daryoto."
    "Namun, meski telah memenangkan pertandingan, ayamku masih mengamul. Ia lari kesana kemari mengitari arena."
    jump kabur

label kalah:
    "Ayam milikku berusaha bertahan dari serangan ayam Daryoto."
    "Bertahan dengan segenap tenaganya dari serangan dahsyat yang dilancarkan oleh ayam Daryoto. Setiap serangan itu membawa kekuatan yang melumpuhkan, menghempaskan ayamku berkali-kali"
    "Mengetahui bahwa dirinya kalah, ayamku berlari-lari di arena."
    jump kabur


label kabur:
    "Ternyata ayamku terluka parah, kelihatan darah mengalir melewati pahanya. Ia menggila hingga melompat keluar arena."
    show jmarah at center:
        yalign 1
        zoom 1.3
    show jmarah at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=5)
    Joko "Berhenti! ayam BODOHH..!!"
    play music "audio/buru.mp3" volume 0.5
    "Aku mencoba menangkap ayam tersebut yang terus melompat kesini dan kemari. meskipun sudah terluka, ayam tetap saja gesit dalam menghindari cengkramanku."
    "Aku terus mengejarnya, tetapi ayamku malah kabur masuk ke kebun liar."
    show jmarah at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=1)
    Joko "SIALAN..!!"
    scene black
    hide lapangan
    "..."
    stop sound fadeout 1.0
    scene hutan with fade
    play sound "audio/lari.mp3" noloop volume 0.5
    $ renpy.pause(1)
    "Aku kehilangan jejak ayam sampai ke tengah rerumputan liar. tubuh yang kecil memudahkannya berlari melewati antara pepohonan."
    stop sound
    Joko "Sialan..! kemana ayam itu pergi?"

menu:
    "Kemana aku harus pergi?"
    "Ke kiri":
        jump sasar
    "Ke kanan":
        jump bertemu

label sasar:
    scene gudang with dissolve
    play sound "audio/lari.mp3" noloop volume 0.4
    $ renpy.pause(1)
    hide hutan
    "Ayam terluka parah, seharusnya tidak bisa lari jauh"
    stop sound
    "Aku melihat-lihat area sekitar gudang"
    "Sayangnya, aku hanya melihat bangunan dalam kumuh dan beberapa peralatan yang sudah dihiasi jaring laba-laba."
    Joko "Ayamku tidak berada di sini"
    scene hutan with dissolve
    hide gudang

    menu:
        "Kemana aku harus pergi?"
        "Ke kanan":
            stop music fadeout 1.0
            jump bertemu
        

label bertemu:
    scene pekarangan with dissolve
    play sound "audio/lari.mp3" noloop volume 0.4
    $ renpy.pause(1)
    "Aku menemukan pekarangan rumah seseorang. di tengah pekarangan hijau terdapat ayam peliharaan. beberapa berjalan bebas di luar, sebagian yang lain berada di kandang"
    stop sound
    stop music fadeout 1.0
    "Di antara ayam yang mengais-ngais tanah, aku melihat ayamku yang berdiri diam. dia benar-benar mematung di sana."
    "Sepertinya ayamku sudah kehabisan tenaga."
    window hide dissolve
    play music "audio/siti.mp3" volume 1
    $ renpy.pause(3)
    window show dissolve
    "Ini kesempatanku.."
    "Aku berjalan beberapa langkah hingga.."
    show sblush :
        xalign 0.5
        yalign 1.0
        zoom 1.2
    Siti "Ah...?"
    "Seorang gadis elok melihatku keheranan. Dia memancarkan keanggunan dengan wajah yang mempesona dan senyum yang menghiasi bibirnya. Namun, yang paling menakjubkan adalah mata indahnya yang begitu lebar dan menawan."
    "Sementara itu, wajah yang penuh keheranan dan rasa ingin tahu memberikan daya tarik yang tak terlupakan."
    "Aku mengingatnya, kembang Desan Mirah. Aku memang pernah pernah mendengar tentang kecantikan dan kelembutan sosok itu, Siti Amirah. Tetapi tidak pernah sedekat ini."
    "Tak bisa membayangkan betapa beruntung orang yang bisa melihat senyumannya dan menatap mata indahnya setiap hari"
    "Dalam keheningan singkat itu, kami saling bertatap mata, terjebak dalam momen keajaiban yang tak terungkapkan."
    "Aku merasa gugup."
    "Apa yang harus kulakukan?"
    hide sblush with fade

    menu:
        "Sapa":
            jump senyum
        "Abaikan":
            jump pergi

label senyum:
    show jblush at jleft:
        ease 0.5 zoom 1.01
    Joko "Ha, hai.."
    show jblush at jleft:
        ease 0.5 zoom 1.0
    show sblush at sright:
        ease 0.5 zoom 1.02
    Siti "Eh, hai..?"
    show sblush at sright:
        ease 0.5 zoom 1.0
    "Padahal hanya ingin menyapa.. sialan! aku malah seperti orang bodoh."
    show jblush at jleft:
        ease 0.5 zoom 1.01
    Joko "Saya..."
    Joko "Maaf, saya ingin mengambil ayam itu"
    show jblush at jleft:
        ease 0.5 zoom 1.0
    show sblush at sright:
        ease 0.5 zoom 1.02
    Siti "Ayam itu punya mas?"
    show sblush at sright:
        ease 0.5 zoom 1.0
    Joko "Iya.."
    "Aku mengaambil ayamku yang masih mematung dan segera pergi meninggalkan rumah Siti Amirah."
    scene black with dissolve
    hide pekaranga
    "Pertemuan ini begitu singkat, tetapi perasaan yang gak jelas terus bertahan seiring aku melangkah pergi. perasaan letih menangkap ayam hilan begitu saja."
    "Siti Amirah"
    "..."
    stop music fadeout 1.0
    "Aku harap kita bisa bertemu kembali.."
    jump part2

label pergi:
    Joko "Maaf, saya ingin mengambil ayam itu"
    show sblush at sright:
        ease 0.5 zoom 1.02
    Siti "Ayam itu punya mas?"
    show sblush at sright:
        ease 0.5 zoom 1.0
    Joko "Iya.."
    "Aku mengaambil ayamku yang masih mematung dan segera pergi meninggalkan rumah Siti Amirah."
    scene black with dissolve
    hide pekarangan
    "Pertemuan ini begitu singkat, tetapi perasaan yang gak jelas terus bertahan seiring aku melangkah pergi. perasaan letih menangkap ayam hilang begitu saja."
    "Siti Amirah"
    "..."
    stop music fadeout 1.0
    "Aku harap kita bisa bertemu kembali.."


    jump part2

label part2:
    pause 1.0
    "Namaku Joko Lancur. Aku suka bermain judi, terutama jika melibatkan tarung ayam. aku juga sering mabuk-mabukan. Kehidupanku penuh dengan kegiatan yang melibatkan risiko dan kegembiraan cepat."
    show jnetral with fade:
        xalign 0.5
        yalign -1.5
        zoom 1.2
    "Aku hidup dengan caraku sendiri. hanya kebebasan, tidak ada yang bisa mengaturku. Kerna manusia hidup hanya sesaat, menikmati adalah satu-satunya cara untuk hidup."
    "Apalagi aku adalah anak tunggal dari Lurah Desa Nggolan, Ki Hanggolono. Dia adalah sosok yang sakti mandraguna, memiliki hubungan kuat dengan para lelembut."
    "Dengan latar belakang seperti itu, tidak ada satupun orang yang berani denganku."
    "Tidak berniat sombong, tetapi orang-orang sekitar juga menganggapku tampan. aku menjadi idola para gadis desa karena ketampananku ini. Jika ingin, aku bisa memilih salah satu dari mereka."
    "Tapi untuk pertama kalinya.."
    show jnetral at jleft
    show snetral at sright with moveinright
    "Dia..,"
    "Seseorang membuatku merasakan sesuatu yang tidak pernah kurasakan."
    "Perasaan yang tidak dapat dijelaskan oleh diriku sendiri."
    "Siti Amirah.."
    hide jnetral with fade
    hide snetral with fade
    "Gadis itu.."
    $ renpy.pause(1)

    Han "Hei Joko, heii!!"
    scene ruang_tamu with eye_open
    "Suara ayahku langsung membangunkanku dari lamunan"
    show hnetral at hright 
    show jnetral at jleft with moveinleft:
        ease 0.5 zoom 1.01
    Joko "Ada apa to, yah?"
    show jnetral at jleft:
        ease 0.5 zoom 1.0
    Han "Ayah lihat akhir-akhir ini kau selalu melamun. Ada apa?"
    show jnetral at jleft:
        ease 0.5 zoom 1.01
    Joko "Ah, tidak, Ayah. Tidak ada apa-apa"
    show jnetral at jleft:
        ease 0.5 zoom 1.0
    Han "Jangan bohong. Ayah bisa melihatnya. Coba ceritakan, siapa tahu ayah dapat membantu."
    hide jnetral
    hide hnetral
    menu:
        "Tidak cerita":
            jump cerita1
        "Cerita":
            jump cerita2

label cerita1:
    "Aku tidak ingin ayahku tahu apa yang kupikirkan. karena bagiku, ini adalah masalahku sendiri."
    "Apalagi ini cukup memalukan."
    show jnetral at jleft:
        ease 0.5 zoom 1.01
    Joko "Beneran yah.. cuman, kepikiran masalah ayamku kemarin."
    show jnetral at jleft:
        ease 0.5 zoom 1.0
    show hnetral at hright:
        ease 0.5 zoom 1.02
    Han "Bukan, itu berbeda.."
    Han "kau memiliki masalah seperti ini sebelumnya, bahkan lebih buruk."
    "Ayah benar, aku tidak pernah merasakan ini sebelumnya.."
    jump cerita2

label cerita2:
    show jnetral at jleft:
        ease 0.5 zoom 1.01
    Joko "Ayah.."
    show jnetral at jleft:
        ease 0.5 zoom 1.0
    show hnetral at hright:
        ease 0.5 zoom 1.02
    Han "Ceritakan saja, tidak usah ragu-ragu. Jangan membuat Ayah semakin bingung."
    show hnetral at hright:
        ease 0.5 zoom 1.0
    show jnetral at jleft:
        ease 0.5 zoom 1.01
    Joko "Tapi, Ayah harus berjanji tidak akan marah."
    show jnetral at jleft:
        ease 0.5 zoom 1.0
    show hnetral at hright:
        ease 0.5 zoom 1.02
    Han "Sudahlah. Untuk apa Ayah marah. Ceritakan saja."
    show hnetral at hright:
        ease 0.5 zoom 1.0
    show jblush at jleft:
        ease 0.5 zoom 1.01
    hide jnetral
    Joko "Ayah... aku ingin kawin."
    show jblush at jleft:
        ease 0.5 zoom 1.0
    show hkaget at hright:
        ease 0.5 zoom 1.02
    hide hnetral
    Han "Apa? Mau kawin?"
    show hkaget at hright:
        ease 0.5 zoom 1.0
    show jblush at jleft:
        ease 0.5 zoom 1.01
    Joko "Ayah sudah berjanji tidak akan marah."
    show jblush at jleft:
        ease 0.5 zoom 1.0
    show hkaget at hright:
        ease 0.5 zoom 1.02
    Han "Ayah tidak marah, hanya sedikit terkejut saja. Rupanya itu yang membuatmu melamun terus. Harusnya Ayah tahu. Siapa gadis itu?"
    show hkaget at hright:
        ease 0.5 zoom 1.0
    show jblush at jleft:
        ease 0.5 zoom 1.01
    Joko "Gadis Mirah..."
    show jblush at jleft:
        ease 0.5 zoom 1.01
    show hsedih at hright:
        ease 0.5 zoom 1.02
    hide hkaget
    Han "Gadis Mirah? Tidak bisa, Nak. Kita beda agama, cari gadis lain saja."
    show hsedih at hright:
        ease 0.5 zoom 1.0
    show jmarah at jleft:
        ease 0.5 zoom 1.01
    hide jblush
    Joko "Walau beda agama, tidak apa-apa. Ayah harus membantuku mendapatkan gadis Mirah.Ayah sudah berjanji."
    show jmarah at jleft:
        ease 0.5 zoom 1.0
    show hkaget at hright:
        ease 0.5 zoom 1.02
    hide hsedih
    Han "Apa kau bilang? Tidak apa-apa? Mereka itu orang Islam, sedangkan kita bukan, kau bilang tidak apa-apa? Ayah tidak setuju. Kau tidak boleh membantah"
    show hkaget at hright:
        ease 0.5 zoom 1.02
    show jmarah at jleft:
        ease 0.5 zoom 1.01
    Joko "Kalau bukan gadis Mirah, aku tidak mau. Kalau Ayah tidak rnau melamar, lebih baik aku mati saja"
    show jmarah at jleft:
        ease 0.5 zoom 1.0
    hide jmarah with fade
    hide hkaget with fade
    "Mendengar ancamanku, ayah terdiam. Sebenarnya sebagai kepala desa, dia terkenal memiliki darah yang dingin sehingga warga takut padanya."
    "Tetapi jika mengenai diriku, dia selalu takut. karena akulah satu-satunya keturunan yang ayah punya."
    Han "Baiklah, kalau kau memaksa. Ayah tidak mau tahu apa yang akan terjadi nanti. Ini diluar tradisi kita. Besok Ayah akan berangkat ke rumah Kiai Muslim itu."
    "Suaranya terlihat pasrah.."
    scene black with dissolve
    hide ruang_tamu
    stop music fadeout 1.0
    "Kiai Muslim bukan orang sembarangan. Ia adalah putra Sunan Gribig yang masih keturunan Prabu Brawijaya V, jadi masih trah Majapahit."
    "Sebenamya, ayahku merasa bangga dan terhormat bila bisa mendapat menantu anak Kiai Muslim ini. Akan tetapi, banyak sekali perbedaan antara dirinya dan Kiai Muslim."
    "Ki Hanggolo adalah sosok sakti, tetapi kasar dan suka berbuat semena-mena untuk kepentingannya sendiri. Ia penguasa Desa Nggolan"
    "Sedangkan Kiai Muslim adalah guru Agama Islam. Kiai Muslimlah yang membentuk komunitas muslim di Desa Mirah."
    "Desa itu juga dinamakan Desa Mirah dengan mengambil nama putri Kiai Muslim, yaitu Siti Amirah"
    "Desa Nggolan dan Desa Mirah letaknya berdekatan. Desa Mirah terletak di sebelah timur Desa Nggolan. Sejalan dengan sosok tetuanya yang berbeda, kedua desa itu juga mempunyai karakter berbeda."
    scene teras with dissolve
    play music "audio/gitar.mp3" volume 0.5
    "Tiba di rumah Kiai Muslim, aku dan ayahku disambut ramah oleh tuan rumah."
    "Tentu saja, bagi mereka kedatangan kami merupakan hal yang mengejutkan. kami berdua dipersilahkan duduk di tempat duduk teras."
    show hnetral flip at hleft with moveinleft
    Han "Anda memiliki desa yang indah Pak Kiai.."
    show msedih at mright:
        ease 0.5 zoom 1.01
    kiai "Terima kasih Ki, kami tersanjung mendengar itu."
    show msedih at mright:
        ease 0.5 zoom 1.0
    Han "hahaha.. Pak Kiai begitu rendah hati."
    hide msedih
    hide hnetral
    $ renpy.pause(1)
    "Kiai tersenyum."
    "Keheningan sesaat melewati ruangan. aku sangat gugup menunggu ayahku memulai pembicaraan lagi"
    show hnetral flip at hleft:
        ease 0.5 zoom 1.02
    Han "Jadi Pak Kiai, kedatangan saya kemari sebenamya ada maksud penting."
    show hnetral flip at hleft:
        ease 0.5 zoom 1.0
    show msedih at mright:
        ease 0.5 zoom 1.01
    kiai "Maksud penting apa, Ki?"
    show msedih at mright:
        ease 0.5 zoom 1.0
    Han "Eh.. anu.. begini.. Kiai punya putri yang cantik, Siti Amirah. Saya juga punya anak laki-laki yang tidak kalah tampan. Putri Kiai sudah cukup umur, demikian juga putra saya ..."
    show msedih at mright:
        ease 0.5 zoom 1.01
    kiai "Maaf, Ki. Sebaiknya Ki Hanggolono terus terang saja. Silakan."
    show msedih at mright:
        ease 0.5 zoom 1.0
    Han "Karena sudah sama-sama dewasa, bagaimana kalau anak kita, kita jodohkan saja. Apa Kiai setuju?"
    hide hnetral flip
    show mkaget at mright
    hide msedih
    show mkaget at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=2)
    "Kiai Muslim sangat terkejut dan bingung dengan keterusterangan dan pertanyaan yang sangat yakin dan setengah mendesak itu."
    "Beliau memandangku, caranya memandang mencoba menilai diriku apakah sudah siap apa belum."
    show mkaget at mright:
        ease 0.5 zoom 1.01
    kiai "Apa kau yakin, anak muda..?"
    show mkaget at mright:
        ease 0.5 zoom 1.0
    show jnetral at jleft with moveinleft:
        ease 0.5 zoom 1.01
    Joko "Ah, hamba sangat yakin Pak Kiai, saya sudah memikirkan ini matang-matang sebelumnya."
    hide jnetral with fade
    "Kiai Muslim kembali berpikir, dia memperhitungkan baik-baik apa jawaban yang harus dikatakan."
    Han "Bagaimana, cocok tidak..?"
    "..."
    show msedih at mright:
        ease 0.5 zoom 1.01
    hide mkaget
    kiai "Begini, Ki...,"
    show msedih at mright:
        ease 0.5 zoom 1.0
    show hnetral flip at hleft:
        ease 0.5 zoom 1.02
    Han "Apa? Perkara mas kawin, jangan khawatir. Saya tidak akan mengecewakan Kiai"
    Han "Kalau Kiai ingin mengajukan permintaan, silakan. Demi joko Lancur, saya akan penuhi semua keinginan Kiai ... ,"
    show hnetral flip at hleft:
        ease 0.5 zoom 1.0
    show msedih at mright:
        ease 0.5 zoom 1.01
    kiai "Sebentar.. sebentar.. Ki, sabar... Begini... mohon maaf sebelumnya, Ki. Saya belum bisa menerima atau menolak keinginan Ki Hanggolono. Saya memang punya perrnintaan..."
    show msedih at mright:
        ease 0.5 zoom 1.0
    show hnetral flip at hleft:
        ease 0.5 zoom 1.02
    Han "Sebutkan saja, Kiai . Saya pasti akan segera memenuhinya.."
    show hnetral flip at hleft:
        ease 0.5 zoom 1.0
    "Ayahku spontan memotong dengan tidak sabar. dia terlihat sedikit kegirangan."
    "Begitupun aku."
    show msedih at mright:
        ease 0.5 zoom 1.01
    kiai "Baiklah, Ki. Saya punya perrnintaan untuk mahar anak saya. Saya minta satu peti besar padi dan satu peti kedelai. Kedua barang ini harus tiba di rumah saya menjelang pesta perkawinan anak kita. Dua peti itu harus jalan sendiri, tidak boleh ditarik binatang temak atau digotong orang."
    kiai "Satu lagi, Ki, persawahan di desa saya ini kering. Saya mohon diairi dengan air yang cukup dalam waktu semalam."
    show msedih at mright:
        ease 0.5 zoom 1.0
    hide msedih
    hide hnetral flip
    menu:
        "gampang":
            jump bisa
        "Keberatan":
            jump gak

label gak:
    "Aku merasa curiga, mungkin saja ini sebuah tipu muslihat. Meskipun Kiai Muslim terkenal karena kebaikannya, tapi tetap saja..."
    "Aku mendekat pada ayahku dan berbisik."
    show jmarah at jleft with fade:
        ease 0.5 zoom 1.01
    Joko "Ayah.. jangan lakukan ini."
    show jmarah at jleft:
        ease 0.5 zoom 1.0
    show hnetral at hright with moveinright:
        ease 0.5 xalign 0.5 zoom 1.02
    Han "Tidak perlu khawatir.."
    show hnetral at hright:
        ease 0.5 xalign 0.5 zoom 1.0
    show jmarah at jleft:
        ease 0.5 zoom 1.01
    Joko "Tetapi..?"
    show jmarah at jleft:
        ease 0.5 zoom 1.01
    show hnetral at hright:
        ease 0.5 xalign 0.5 zoom 1.02
    Han "Percayalah padaku Joko.."
    show hnetral at hright:
        ease 0.5 xalign 0.5 zoom 1.0
    hide jmarah with fade
    hide hnetral with fade
    menu percaya:
        "Apa pilihanmu?"
        "Percaya.":
            jump bisa
        "Tidak percaya.":
            jump batal

label batal:
    "Tidak.., aku rasa perlu menggunakan pendekatan lain."
    "Perbedaan agama dalam pernikahan tidak akan berhasil jika hanya dengan persyaratan seperti ini. Selalu ada sesuatu.."
    show jnetral at jleft with fade:
        ease 0.5 zoom 1.01
    Joko "Mohon maaf Pak Kiai, bolehkah kami membicarakan ini terlebih dahulu?"
    show jnetral at jleft:
        ease 0.5 zoom 1.0
    show msedih at mright with fade
    kiai "Tidak apa-apa.., Saya akan memberikan waktu untuk kalian bicara."
    kiai "Saya akan kembali dalam beberapa menit."
    show jnetral at jleft:
        ease 0.5 zoom 1.01
    Joko "Terima kasih, Pak Kiai."
    show jnetral at jleft:
        ease 0.5 zoom 1.0
    hide msedih with moveoutright
    "Kiai Muslim masuk ke dalam rumah, meningalkan kami berdua untuk berdiskusi."
    show hkaget at hright with moveinright:
        ease 0.5 zoom 1.02
    Han "Apa yang kau lakukan..?"
    show hkaget at hright:
        ease 0.5 zoom 1.0
    show jmarah at jleft:
        ease 0.5 zoom 1.01
    Joko "Kenapa? Kiai juga tidak keberatan."
    show jmarah at jleft:
        ease 0.5 zoom 1.0
    show hkaget at hright:
        ease 0.5 zoom 1.02
    Han "Bukan, maksud ayah apalagi yang harus dibicarakan? Ini adalah hal sepele."
    show hkaget at hright:
        ease 0.5 zoom 1.0
    show jmarah at jleft:
        ease 0.5 zoom 1.01
    Joko "Aku yakin ayah bisa memenuhi permintaan Kiai Muslim, tetapi bagaimana setelahnya..?"
    show jmarah at jleft:
        ease 0.5 zoom 1.0
    show hkaget at hright:
        ease 0.5 zoom 1.02
    Han "Tapi ini kesempatanmu Joko.."
    show hkaget at hright:
        ease 0.5 zoom 1.0
    show jnetral at jleft:
        ease 0.5 zoom 1.01
    hide jmarah
    Joko "Masih ada cara lain."
    show jnetral at jleft:
        ease 0.5 zoom 1.0
    show hnetral at hright:
        ease 0.5 zoom 1.02
    hide hkaget
    Han "Bagaimana..?"
    show hnetral at hright:
        ease 0.5 zoom 1.0
    show jnetral at jleft:
        ease 0.5 zoom 1.01
    Joko "Aku akan memikirkannya nanti, pokoknya ayah tidak boleh menerima permintaan Pak Kiai"
    show jnetral at jleft:
        ease 0.5 zoom 1.0
    show hnetral at hright:
        ease 0.5 zoom 1.02
    Han "Baiklah, jika begitu maumu."
    show hnetral at hright:
        ease 0.5 zoom 1.0
    hide jnetral with fade
    hide hnetral with fade
    "Beberapa saat kemudian, Kiai Muslim kembali ke depan untuk menjamu kami."
    "Beliau mengonfirmasi keputusan kami."
    show msedih at mright with moveinright
    kiai "Jadi bagaimana Ki? apa keputusan kalian?"
    show msedih at mright:
        ease 0.5 zoom 1.0
    Han "Anak saya berpikir bahwa pengumuman kami terlalu mendadak, jadi kami mengurungkan niat kami."
    show msedih at mright:
        ease 0.5 zoom 1.01
    kiai "Baiklah Ki.., jika itu keputusan kalian, saya tidak akan melarang."
    show msedih at mright:
        ease 0.5 zoom 1.0
    Joko "Maaf telah mengganggu waktunya Pak Kiai."
    Han "Kalau begitu, kami pamit undur diri."
    kiai "Wassalamualaikum.."
    hide msedih with fade

    "Aku dan ayahku mengangkat kaki dari kediaman keluarga Kiai Muslim. Sedikit kecewa, tapi aku yakin ini adalah keputusan yang tepat."
    scene black with dissolve
    "Ini hanya untuk sementara."
    "Kumohon tunggu sebentar lagi,"
    "aku akan kembali,"
    "Sumpahku."
    jump jalan

label bisa:
    Han "Baiklah, saya akan memenuhinya. Hanya itu? Kalau masih ada.."
    kiai "Hanya itu...hanya itu,"
    Han "Kalau tidak ada lagi, saya mohon diri."
    "Tanpa lanjut basa-basi kami segera berdiri dan mengulurkan tangan untuk bersalaman dengan Kiai Muslim."
    scene black
    scene ruang_tamu with dissolve
    play music "audio/ki.mp3" volume 0.7
    "Ayahku, Ki Hanggolono adalah orang sakti. Ia biasa bersekutu dengail roh-roh jahat untuk membantu memuluskan dan mewujudkan keinginarmya."
    "Oleh karena itu, ia merasa ringan saja menerima permintaan Kiai Muslim. Sesampai di rumah pada malam hari, Ayahku segera masuk ke ruang pemujaan untuk bersemedi."
    show hnetral at hright with fade
    Han "Tunggu sebentar, nak."
    hide hnetral with moveoutright
    "..."
    pause 1.0
    "Aku menunggu di ruang tamu sampai beberapa saat kemudian ayahku kembali dengan ekspresi berbeda."
    show hrkaget at hright with moveinright:
        ease 0.5 zoom 1.02
    Han "Ayo, Joko!!"
    show hrkaget at hright:
        ease 0.5 zoom 1.0

    menu:
        "Apa jawabanmu?"
        "Baik":
            jump baik
        "menyusul":
            jump menyusul

label baik:
    Joko "Baik.."
    show hrkaget with dissolve
    "Sedetik setelah aku berdiri, Ki Hanggolono menghilang."
    Joko "Sialan, aku lupa ayahku memiliki kemampuan berpindah tempat."
    "Beruntung tempat sawah tidak jauh dari sini. Jika berjalan tidak perlu waktu lama."
    stop music fadeout 0.5
    jump end

label menyusul:
    Joko "Ayah bisa duluan..."
    show hrkaget with dissolve
    "Sedetik kemudian, Ki Hanggolono menghilang."
    "Jika sudah memanggil roh-roh jahat, Ayahku seperti bisa melakukan apapun."
    Joko "...Karena aku tidak memiliki kemampuan itu."
    "Beruntung tempat sawah tidak jauh dari sini. Jika berjalan tidak perlu waktu lama."
    stop music fadeout 0.5
    jump end

label jalan:
    window hide
    scene black
    scene besok with fade
    $ renpy.pause(4)
    hide besok with fade
    scene jalan with dissolve
    window show
    "Kemarin benar-benar hari yang melelahkan. Aku rasa diriku memerlukan waktu untuk melupakan semuanya dan mencari ketenangan di tengah kesunyian desa."
    play music "audio/ceria.mp3" fadein 1.0 volume 0.7
    Joko "Sungguh perasaan yang begitu damai."
    "Jalanan desa yang kecil dan sempit memberi perasaan intim dan damai. Rumah-rumah penduduk terlihat dengan atap jerami yang terhampar rapi, dan beberapa warga desa mengobrol di halaman mereka sambil menikmati udara segar pagi."
    "Aku berjalan menyusuri jalan-jalan yang tidak begitu ramai, menyerap suasana desa yang tenang"
    "Berjalan melewati sawah hijau yang luas, dengan pepohonan dan gunung di kejauhan. Suara riak air dari sungai kecil yang melintasi desa menambahkan sentuhan harmoni alam."
    "Saat aku terpesona oleh pemandangan alam yang memukau, aku tiba-tiba melihat sosok familiar di seberang jalan."
    Joko "Bukankah dia...?"
    "Itu adalah Siti Amirah, seorang wanita cantik yang kudambakan. Dia duduk di bawah pohon rindang, menikmati keindahan alam seperti yang aku lakukan."
    "Aku tidak bisa menahan senyum saat aku melihatnya. Ketika Siti melihatku, senyum terukir di wajahnya. Kami saling bertatapan dengan bahagia, merasa takjub bahwa takdir telah mempertemukan kami lagi."
    "Dengan hati yang berdebar, aku memberanikan diri mendekati Siti Amirah. Sekali lagi aku tersenyum kepadanya, mencoba menunjukkan keberanian dan ketertarikan yang aku rasakan."
    show snetral at sright with dissolve
    show jblush at jleft with moveinleft:
        ease 0.5 zoom 1.01
    Joko "Hai..,"
    Joko "Kita pernah bertemu beberapa hari lalu., ingat?"
    show jblush at jleft:
        ease 0.5 zoom 1.0
    show sblush at sright:
        ease 0.5 zoom 1.02
    Siti "Hai, aku masih mengingatnya. Ketika ayam milikmu, masuk ke pekarangan rumahku"
    show sblush at sright:
        ease 0.5 zoom 1.0
    show jnetral at jleft:
        ease 0.5 zoom 1.01
    hide jblush
    Joko "Hahaha.. kau membuatnya terdengar konyol."
    show jnetral at jleft:
        ease 0.5 zoom 1.0
    show snetral at sright:
        ease 0.5 zoom 1.02
    hide sblush
    Siti "Hehe.., tidak apa. Jadi, bagaimana keadaan ayam itu sekarang?"
    show snetral at sright:
        ease 0.5 zoom 1.0
    show jnetral at jleft:
        ease 0.5 zoom 1.01
    Joko "Sudah membaik."
    show jnetral at jleft:
        ease 0.5 zoom 1.0
    show snetral at sright:
        ease 0.5 zoom 1.02
    Siti "Alhamdulillah.., memang kenapa ayamnya kok sampai terluka begitu?"
    show snetral at sright:
        ease 0.5 zoom 1.0
    show jnetral at jleft:
        ease 0.5 zoom 1.01
    Joko "Karena ikut laga sabung ayam."
    show jnetral at jleft:
        ease 0.5 zoom 1.0
    show snetral at sright:
        ease 0.5 zoom 1.02
    Siti "Huh, jangan begitu. Nantinya di kehidupan berikutnya, kamu justru akan diadu oleh ayam."
    show snetral at sright:
        ease 0.5 zoom 1.0
    show jmarah at jleft:
        ease 0.5 zoom 1.01
    Joko "Bagaimana mungkin..?"
    show jmarah at jleft:
        ease 0.5 zoom 1.0
    show smarah at sright:
        ease 0.5 zoom 1.02
    Siti "Bukankah kamu percaya dengan reinkarnasi, kamu juga percayakan dengan istilah karma??"
    show smarah at sright:
        ease 0.5 zoom 1.0
    show jnetral at jleft:
        ease 0.5 zoom 1.01
    hide jmarah
    Joko "Benar juga, akhir-akhir ini aku merasa kehilangan semangat hidup. Segala apa yang aku lakukan terasa tidak berarti dan sia-sia."
    "Tiba-tiba aku tersadar bahwa kita belum saling berkenalan dengan baik. Meskipun mungkin kita sudah tahu nama masing-masing, tetapi alangkah baiknya..."
    Joko "oh ya, kita belum kenalan sebelumnya, aku Joko Lancur."
    show jnetral at jleft:
        ease 0.5 zoom 1.0
    show snetral at sright:
        ease 0.5 zoom 1.02
    Siti "Siti Amirah."
    show snetral at sright:
        ease 0.5 zoom 1.0
    "Aku berusaha menjabat tangannya, namun dia menolak dengan sopan dan mengangkat tangannya dengan permohonan agar saya mengerti."
    "Sepertinya Siti Almirah adalah tipe gadis yang enggan disentuh oleh lawan jenis."
    show jnetral at jleft:
        ease 0.5 zoom 1.01
    Joko "Jadi sekarang kita bisa memanggil dengan nama bukan..?"
    show jnetral at jleft:
        ease 0.5 zoom 1.0
    show sblush at sright:
        ease 0.5 zoom 1.02
    hide snetral
    Siti "Iya.., Joko.."
    show sblush at sright:
        ease 0.5 zoom 1.0
    show jblush at jleft:
        ease 0.5 zoom 1.01
    Joko "Siti.."
    show jblush at jleft:
        ease 0.5 zoom 1.0
    "Kemudian, keheningan yang gugup melintas, menciptakan suasana yang tegang di antara kami berdua."
    "Mata kami saling bertemu, mencerminkan rasa ragu dan keraguan yang melintas di dalam pikiran masing-masing."
    show sblush at sright:
        ease 0.5 zoom 1.02
    Siti "Aku mendengarnya.."
    show sblush at sright:
        ease 0.5 zoom 1.0
    show jnetral at jleft:
        ease 0.5 zoom 1.01
    hide jblush
    Joko "Mendengar apa?"
    show jnetral at jleft:
        ease 0.5 zoom 1.0
    "Siti Amirah terdiam sejenak, kemudian tersenyum malu-malu seolah menunjukkan rasa lega. Matanya yang penuh kehangatan memandangku, dan dia dengan hati-hati melanjutkan kalimatnya yang terputus."
    show sblush at sright:
        ease 0.5 zoom 1.02
    Siti "Percakapan Joko dengan ayahku."
    show sblush at sright:
        ease 0.5 zoom 1.0
    show jnetral at jleft:
        ease 0.5 zoom 1.01
    Joko "Maksudnya-"
    show jnetral at jleft:
        ease 0.5 zoom 1.0
    show sblush at sright:
        ease 0.5 zoom 1.02
    Siti "Aku mendengar semuanya. Aku diam-diam menguping kalian dari dalam."
    show sblush at sright:
        ease 0.5 zoom 1.0
    show jblush at jleft:
        ease 0.5 zoom 1.01
    Joko "Begitu..? Hehehe.. terlalu terburu-buru ya..?"
    show jblush at jleft:
        ease 0.5 zoom 1.0
    show skaget at sright:
        ease 0.5 zoom 1.02
    hide sblush
    Siti "Memang benar.. tapi aku lebih penasaran, kenapa Joko menolak permintaan ayahku."
    show skaget at sright:
        ease 0.5 zoom 1.0
    show jnetral at jleft:
        ease 0.5 zoom 1.01
    hide jblush
    Joko "Karena itu hanyalah ujian. Seingatku Kiai Muslim tidak akanmenerima apapun yang dibuat dari roh jahat."
    "Siti Almirah tersenyum lapang, puas dengan jawabanku."
    show skaget at sright:
        ease 0.5 zoom 1.02
    Siti "Lalu.. Bagaimana? Apa Joko ada rencana lain?"
    show skaget at sright:
        ease 0.5 zoom 1.0
    show jnetral at jleft:
        ease 0.5 zoom 1.01
    Joko "Sebelum itu aku ingin mengetahui perasaan Siti dulu.."
    show jnetral at jleft:
        ease 0.5 zoom 1.0
    "Dia terlihat ragu dan kebingungan dengan perasaannya yang bercampur aduk. Ekspresi wajahnya mencerminkan ketidakpastian yang dalam, seolah-olah dia tidak yakin tentang apa yang sebenarnya dirasakannya."
    show jblush at jleft:
        ease 0.5 zoom 1.01
    Joko "Aku mencintaimu..," 
    Joko "Engkau adalah satu-satunya perempuan yang membuatku seperti ini. Perasaan yang belum pernah kurasakan sebelumnya."
    "Bingungnya semakin tampak jelas di wajahnya. Ekspresi kebingungannya menggambarkan ketidakmampuannya untuk memahami dan mengelompokkan perasaannya dengan jelas. Aku bisa merasakan kegundahannya dan rasa takut akan membuat keputusan yang salah."
    "Aku mendekatinya dengan penuh kelembutan, memahami bahwa proses ini membutuhkan waktu dan kesabaran."
    Joko "Aku tahu ini sulit bagimu. Jangan terburu-buru dalam menentukan perasaanmu. Biarkan waktu membantumu menemukan kejelasan yang kau cari."
    show jblush at jleft:
        ease 0.5 zoom 1.01
    show sblush at sright:
        ease 0.5 zoom 1.02
    hide skaget
    Siti "Jujur, aku tertarik dengan Joko. Tetapi..."
    show sblush at sright:
        ease 0.5 zoom 1.0
    show jnetral at jleft:
        ease 0.5 zoom 1.01
    hide jblush
    Joko "Tidak apa, akau tahu apa yang harus kita lakukan."
    hide jnetral
    hide sblush
    jump yakin

label yakin:    
    menu:
        "Apa yang sebaiknya kita lakukan?"
        "Meminta saran Kiai Muslim":
            jump a
        "Meminta saran Ki Hanggolono":
            jump b
        "Menghabiskan waktu bersama dahulu":
            jump c

label a:
    Joko "Aku merasa kita perlu pendapat dari ayahmu."
    Siti "Joko yakin?"
    menu:
        "Yakin.":
            jump end2
        "Tidak.":
            jump yakin

label b:
    show jnetral at jleft:
        ease 0.5 zoom 1.01
    Joko "Aku merasa kita perlu pendapat dari ayahku."
    show jnetral at jleft:
        ease 0.5 zoom 1.0
    Siti "Joko yakin?"
    hide jnetral
    menu:
        "Yakin.":
            jump end3
        "Tidak.":
            jump yakin

label c:
    show jblush at jleft:
        ease 0.5 zoom 1.01
    Joko "Aku merasa kita perlu mengenal satu sama lain."
    Siti "Joko yakin?"
    menu:
        "Yakin.":
            jump end4
        "Tidak.":
            jump yakin

label end:
    scene sawah with dissolve
    play music "audio/demit.mp3" volume 0.75
    "Pekerjaan telah di mulai sesampainya aku di sawah."
    "Dengan arahan Ki Hanggolono, para roh jahat bekerja membuat pengairan di sawah Desa Mirah. Mereka bekerja dengan cermat dan penuh keahlian, memanfaatkan kemampuan gaib mereka untuk menciptakan sistem pengairan yang efektif."
    "Sangat jelas permintaan Kiai Muslim akan terpenuhi dengan mudah apabila situasi dan kondisi terus berjalan seperti sekarang."
    "Bahkan, kurasa aku tidak perlu ikut campur."
    show hrkaget at hright with moveinright:
        ease 0.5 zoom 1.0
    Han "HAHAHA... Bagaimana menurutmu, Joko?"

    menu:
        "Apa yang kau pikirkan?"
        "Tetap Membantu":
            jump bantu
        "Melihat saja":
            jump lihat
        "Pergi":
            jump end24

label bantu:
    show jnetral at jleft:
        ease 0.5 zoom 1.01
    Joko "Menakjubkan..,"
    Joko "Ijinkan saya ikut membantu, ayah."
    show jnetral at jleft:
        ease 0.5 zoom 1.0
    show hrkaget at hright:
        ease 0.5 zoom 1.02
    Han "Jika kau ingin ikut membantu, maka aku memberikan izinmu. Namun, ingatlah bahwa ini bukanlah tugas yang mudah. Kita menghadapi kekuatan gaib yang kompleks, dan kita harus waspada."
    show hrkaget at hright:
        ease 0.5 zoom 1.0
    show jnetral at jleft:
        ease 0.5 zoom 1.01
    Joko "Ayah, aku siap menghadapi tantangan ini."
    show jnetral at jleft:
        ease 0.5 zoom 1.0
    show hrkaget at hright:
        ease 0.5 zoom 1.02
    Han "Ayah bangga padamu."
    show hrkaget at hright:
        ease 0.5 zoom 1.0
    "Ki Hanggolono memberikan senyuman hangat kepada Joko dan memberikan beberapa petunjuk terakhir sebelum Joko bergabung dengan para roh jahat."
    show hrkaget at hright:
        ease 0.5 zoom 1.02
    Han "Jaga dirimu dengan baik, Joko. Dengarkan instruksi para roh jahat dengan seksama dan kerjakan tugasmu dengan penuh konsentrasi."
    Han "Percayalah pada kemampuanmu sendiri dan percayalah pada kekuatan gaib yang ada di dalammu."
    show hrkaget at hright:
        ease 0.5 zoom 1.0
    show jnetral at jleft:
        ease 0.5 zoom 1.01
    Joko "Terima kasih, ayah. Aku akan melakukannya dengan sebaik-baiknya."
    show jnetral at jleft:
        ease 0.5 zoom 1.0
    hide jnetral with fade
    hide hrkaget with fade
    "Aku bergabung dengan roh jahat dalam pekerjaan sembari belajar memanfaatkan kekuatan ghaib."
    "Hingga akhirnya persawahan Desa Mirah dapat terairi dengan baik dalam waktu semalam."
    "Sekarang tinggal menyiapkan satu peti padi dan satu petikedelai yang bisa berjalan sendiri menuju ke rumah Kiai Muslim."
    "Untuk menyiapkan permintaan itu, Ki Hanggolono mengerahkan dan menyalurkan segenap kekuatan diri dan roh-roh jahat yang ada. Menjelang asa menjemput, persiapan tu sudah tersedia dan siap menuju ke rumah Kiai Muslim"
    scene black with dissolve

    jump end1

label lihat:
    Joko "Aku akan mengamati dari sini, kurasa bantuanku tidak diperlukan."
    Han "Jika memang itu mau Joko, Baiklah."
    "Aku hanya melihat para roh bekerja dari kejauhan."
    "Hingga akhirnya persawahan Desa Mirah dapat terairi dengan baik dalam waktu semalam."
    "Sekarang tinggal menyiapkan satu peti padi dan satu petikedelai yang bisa berjalan sendiri menuju ke rumah Kiai Muslim."
    "Untuk menyiapkan permintaan itu, Ki Hanggolono mengerahkan dan menyalurkan segenap kekuatan diri dan roh-roh jahat yang ada. Menjelang asa menjemput, persiapan tu sudah tersedia dan siap menuju ke rumah Kiai Muslim"
    hide hrkaget with fade
    scene black with dissolve
    hide sawah
    jump end1

label end24:
    "Aku berubah pikiran, aku berjalan pergi dan menyuruh ayah untuk menghentikannya saja."
    "Ternyata itu membuat roh jahat murka.., mereka mengamuk dan mulai menyerang."
    "Tanpa merasa bersalah aku meninggalkan ayahku yang mati dikeroyok oleh roh jahat."
    hide hrkaget with fade
    window hide
    scene black with dissolve
    stop music fadeout 0.5
    show besok with fade
    $ renpy.pause(4)
    hide besok with fade
    scene jalan with dissolve
    window show
    "Kemarin benar-benar hari yang melelahkan. Aku rasa diriku memerlukan waktu untuk melupakan semuanya dan mencari ketenangan di tengah kesunyian desa."
    play music "audio/ceria.mp3" fadein 1.0 volume 0.4
    Joko "Sungguh perasaan yang begitu damai."
    "Jalanan desa yang kecil dan sempit memberi perasaan intim dan damai. Rumah-rumah penduduk terlihat dengan atap jerami yang terhampar rapi, dan beberapa warga desa mengobrol di halaman mereka sambil menikmati udara segar pagi."
    "Aku berjalan menyusuri jalan-jalan yang tidak begitu ramai, menyerap suasana desa yang tenang"
    "Berjalan melewati sawah hijau yang luas, dengan pepohonan dan gunung di kejauhan. Suara riak air dari sungai kecil yang melintasi desa menambahkan sentuhan harmoni alam."
    "Saat aku terpesona oleh pemandangan alam yang memukau, aku tiba-tiba melihat sosok familiar di seberang jalan."
    Joko "Bukankah dia...?"
    "Itu adalah Siti Amirah, seorang wanita cantik yang kudambakan. Dia duduk di bawah pohon rindang, menikmati keindahan alam seperti yang aku lakukan."
    "Aku tidak bisa menahan senyum saat aku melihatnya. Ketika Siti melihatku, senyum terukir di wajahnya. Kami saling bertatapan dengan bahagia, merasa takjub bahwa takdir telah mempertemukan kami lagi."
    "Dengan hati yang berdebar, aku memberanikan diri mendekati Siti Amirah. Sekali lagi aku tersenyum kepadanya, mencoba menunjukkan keberanian dan ketertarikan yang aku rasakan."
    show snetral at sright with dissolve
    show jblush at jleft with moveinleft:
        ease 0.5 zoom 1.01
    Joko "Hai..,"
    Joko "Kita pernah bertemu beberapa hari lalu., ingat?"
    show jblush at jleft:
        ease 0.5 zoom 1.0
    show sblush at sright:
        ease 0.5 zoom 1.02
    Siti "Hai, aku masih mengingatnya. Ketika ayam milikmu, masuk ke pekarangan rumahku"
    show sblush at sright:
        ease 0.5 zoom 1.0
    show jnetral at jleft:
        ease 0.5 zoom 1.01
    hide jblush
    Joko "Hahaha.. kau membuatnya terdengar konyol."
    show jnetral at jleft:
        ease 0.5 zoom 1.0
    show snetral at sright:
        ease 0.5 zoom 1.02
    hide sblush
    Siti "Hehe.., tidak apa. Jadi, bagaimana keadaan ayam itu sekarang?"
    show snetral at sright:
        ease 0.5 zoom 1.0
    show jnetral at jleft:
        ease 0.5 zoom 1.01
    Joko "Sudah membaik."
    show jnetral at jleft:
        ease 0.5 zoom 1.0
    show snetral at sright:
        ease 0.5 zoom 1.02
    Siti "Alhamdulillah.., memang kenapa ayamnya kok sampai terluka begitu?"
    show snetral at sright:
        ease 0.5 zoom 1.0
    show jnetral at jleft:
        ease 0.5 zoom 1.01
    Joko "Karena ikut laga sabung ayam."
    show jnetral at jleft:
        ease 0.5 zoom 1.0
    show snetral at sright:
        ease 0.5 zoom 1.02
    Siti "Huh, jangan begitu. Nantinya di kehidupan berikutnya, kamu justru akan diadu oleh ayam."
    show snetral at sright:
        ease 0.5 zoom 1.0
    show jmarah at jleft:
        ease 0.5 zoom 1.01
    Joko "Bagaimana mungkin..?"
    show jmarah at jleft:
        ease 0.5 zoom 1.0
    show smarah at sright:
        ease 0.5 zoom 1.02
    Siti "Bukankah kamu percaya dengan reinkarnasi, kamu juga percayakan dengan istilah karma??"
    show smarah at sright:
        ease 0.5 zoom 1.0
    show jnetral at jleft:
        ease 0.5 zoom 1.01
    hide jmarah
    Joko "Benar juga, akhir-akhir ini aku merasa kehilangan semangat hidup. Segala apa yang aku lakukan terasa tidak berarti dan sia-sia."
    "Tiba-tiba aku tersadar bahwa kita belum saling berkenalan dengan baik. Meskipun mungkin kita sudah tahu nama masing-masing, tetapi alangkah baiknya..."
    Joko "oh ya, kita belum kenalan sebelumnya, aku Joko Lancur."
    show jnetral at jleft:
        ease 0.5 zoom 1.0
    show snetral at sright:
        ease 0.5 zoom 1.02
    Siti "Siti Amirah."
    show snetral at sright:
        ease 0.5 zoom 1.0
    "Aku berusaha menjabat tangannya, namun dia menolak dengan sopan dan mengangkat tangannya dengan permohonan agar saya mengerti."
    "Sepertinya Siti Almirah adalah tipe gadis yang enggan disentuh oleh lawan jenis."
    show jnetral at jleft:
        ease 0.5 zoom 1.01
    Joko "Jadi sekarang kita bisa memanggil dengan nama bukan..?"
    show jnetral at jleft:
        ease 0.5 zoom 1.0
    show sblush at sright:
        ease 0.5 zoom 1.02
    hide snetral
    Siti "Iya.., Joko.."
    show sblush at sright:
        ease 0.5 zoom 1.0
    show jblush at jleft:
        ease 0.5 zoom 1.01
    Joko "Siti.."
    show jblush at jleft:
        ease 0.5 zoom 1.0
    "Kemudian, keheningan yang gugup melintas, menciptakan suasana yang tegang di antara kami berdua."
    "Mata kami saling bertemu, mencerminkan rasa ragu dan keraguan yang melintas di dalam pikiran masing-masing."
    show sblush at sright:
        ease 0.5 zoom 1.02
    Siti "Aku mendengarnya.."
    show sblush at sright:
        ease 0.5 zoom 1.0
    show jnetral at jleft:
        ease 0.5 zoom 1.01
    hide jblush
    Joko "Mendengar apa?"
    show jnetral at jleft:
        ease 0.5 zoom 1.0
    "Siti Amirah terdiam sejenak, kemudian tersenyum malu-malu seolah menunjukkan rasa lega. Matanya yang penuh kehangatan memandangku, dan dia dengan hati-hati melanjutkan kalimatnya yang terputus."
    show sblush at sright:
        ease 0.5 zoom 1.02
    Siti "Percakapan Joko dengan ayahku."
    show sblush at sright:
        ease 0.5 zoom 1.0
    show jnetral at jleft:
        ease 0.5 zoom 1.01
    Joko "Maksudnya-"
    show jnetral at jleft:
        ease 0.5 zoom 1.0
    show sblush at sright:
        ease 0.5 zoom 1.02
    Siti "Aku mendengar semuanya. Aku diam-diam menguping kalian dari dalam."
    show sblush at sright:
        ease 0.5 zoom 1.0
    show jblush at jleft:
        ease 0.5 zoom 1.01
    Joko "Begitu..? Hehehe.. terlalu terburu-buru ya..?"
    show jblush at jleft:
        ease 0.5 zoom 1.0
    show skaget at sright:
        ease 0.5 zoom 1.02
    hide sblush
    Siti "Memang benar.. tapi aku lebih penasaran, kenapa Joko menolak permintaan ayahku."
    show skaget at sright:
        ease 0.5 zoom 1.0
    show jnetral at jleft:
        ease 0.5 zoom 1.01
    hide jblush
    Joko "Karena itu hanyalah ujian. Seingatku Kiai Muslim tidak akanmenerima apapun yang dibuat dari roh jahat."
    "Siti Almirah tersenyum lapang, puas dengan jawabanku."
    show skaget at sright:
        ease 0.5 zoom 1.02
    Siti "Lalu.. Bagaimana? Apa Joko ada rencana lain?"
    show skaget at sright:
        ease 0.5 zoom 1.0
    show jnetral at jleft:
        ease 0.5 zoom 1.01
    Joko "Sebelum itu aku ingin mengetahui perasaan Siti dulu.."
    show jnetral at jleft:
        ease 0.5 zoom 1.0
    "Dia terlihat ragu dan kebingungan dengan perasaannya yang bercampur aduk. Ekspresi wajahnya mencerminkan ketidakpastian yang dalam, seolah-olah dia tidak yakin tentang apa yang sebenarnya dirasakannya."
    show jblush at jleft:
        ease 0.5 zoom 1.01
    Joko "Aku mencintaimu..," 
    Joko "Engkau adalah satu-satunya perempuan yang membuatku seperti ini. Perasaan yang belum pernah kurasakan sebelumnya."
    "Bingungnya semakin tampak jelas di wajahnya. Ekspresi kebingungannya menggambarkan ketidakmampuannya untuk memahami dan mengelompokkan perasaannya dengan jelas. Aku bisa merasakan kegundahannya dan rasa takut akan membuat keputusan yang salah."
    "Aku mendekatinya dengan penuh kelembutan, memahami bahwa proses ini membutuhkan waktu dan kesabaran."
    Joko "Aku tahu ini sulit bagimu. Jangan terburu-buru dalam menentukan perasaanmu. Biarkan waktu membantumu menemukan kejelasan yang kau cari."
    show jblush at jleft:
        ease 0.5 zoom 1.01
    show sblush at sright:
        ease 0.5 zoom 1.02
    hide skaget
    Siti "Jujur, aku tertarik dengan Joko. Tetapi..."
    show sblush at sright:
        ease 0.5 zoom 1.0
    show jnetral at jleft:
        ease 0.5 zoom 1.01
    hide jblush
    Joko "Tidak apa, akau tahu apa yang harus kita lakukan."
    hide jnetral
    hide sblush

    menu:
        "Apa yang sebaiknya kita lakukan?"
        "Meminta saran Kiai Muslim":
            jump end2
        "Menghabiskan waktu bersama dahulu":
            jump end4
      


label end1:
    window hide
    scene black
    stop music fadeout 1.0
    scene besok with fade
    $ renpy.pause(4)
    hide besok with fade
    scene pernikahan with dissolve
    play sound "audio/nikah.mp3" noloop volume 0.9
    window show
    "Persiapan untuk pesta besar telah selesai. Siti Amirah, si pengantin putri pun sudah tidak sabar menyambut kedatangan Joko Lancur"
    "Warga memainkan irama yang menggema di udara, mengisi seluruh desa dengan kegembiraan. Barisan pengiring pengantin pria, Joko lancur dengan penuh semangat melangkah maju."
    "Tetabuhan terus mengiringi langkah pengantin, menciptakan ritme yang menggugah semangat dan kebahagiaan. Suara riuh penonton dan sorak-sorai pengiring semakin membuat suasana semarak."
    "Ki Hanggolono turon dari kuda dan maju terlebih dahulu untuk menyalami Kiai Muslim yang sudah berdiri menanti di pintu gerbang."
    Han "Kiai, ini saya serahkan anak saya berikut mas kawin sesuai dengan permintaan Kiai. Saya persilakan Kiai untuk memeriksanya"
    play music "audio/tegang.mp3" volume 0.8
    "Kiai Muslim tahu betul apa yang ia lihat hanyalah tipuan. Peti-peti itu bukanlah berisi padi dan kedelai melainkan hanya berupa damen (jerami padi) dan titen (jerami kedelai)."
    "ltu semua hanya sihir. Dengan kekuatan sihir Ki Hanggolono, jerami-jerami itu diubah menjadi satu peti padi dan satu peti kedelai."
    "Jadi menurut Kiai Muslim, mahar pernikahan tidak terpenuhi."
    show msedih at mright:
        ease 0.5 zoom 1.01
    kiai "Ki Hanggolono, saya tahu semua sudah dipenuhi, tetapi saya harap jangan kecewa dan sakit hati"
    show msedih at mright:
        ease 0.5 zoom 1.0
    Han "Apa maksud, Kiai?"
    show mmarah at mright
    hide msedih
    show mmarah at mright:
        ease 0.5 zoom 1.01
    kiai "Mohon maaf, Ki. Peti itu itu bukan berisi padi dan kedelai, tetapi hanya berupaa damen dan titen."
    show mmarah at mright:
        ease 0.5 zoom 1.0
    Han "Jangan sembarangan menuduh. Saya sudah berusaha memenuhi permintaan Kiai. Apa Kiai sengaja mempermainkan saya?"
    show mmarah at mright:
        ease 0.5 zoom 1.01
    Kiai "Sabar... sabar.. Ki. Saya tidak ada niat untuk mempermainkan Ki Hanggolono. Tapi, penglihatan saya memang begitu. Kalau Ki Hanggolono tidak percaya, silakan buka peti-peti itu."
    show mmarah at mright:
        ease 0.5 zoom 1.0
    hide mmarah with fade
    "Mendengar ucapan Kiai Muslim, muka Ki Hanggolono memerah."
    play music "audio/marah.mp3"
    "Dengan sigap dan cepat, Ki Hanggolono mendekati dua peti itu dan langsung membukanya. Kedua peti itu ternyata hanya berisi damen dan titen."
    "Semua rnata orang yang berada di halaman juga melotot tidak percaya. Karena ini berarti pernikahan tidak dilanjutkan."
    "Ki Hanggolono merasa dipermalukan dan dipermainkan di hadapan banyak orang. Dia marah bukan main, darah benar-benar naik ke kepalanya."
    Han "Kau sengaja mempermalukanku, Kiai. Kau menolak lamaran putraku, sudah buat aku malu, kau seharusnya menolaknya sejak awal. Ini sungguh keterlaluan. Saya tidak terima. Kau harus membayarnya!"
    "Ki Hanggolono membuka mulutnya dan mulai mengucapkan mantra dengan suara yang tenang dan tegas"
    show jmarah at jleft:
        ease 0.5 zoom 1.01
    Joko "Ayah!! apa yang coba kau lakukan?!"
    hide jmarah
    "Tiba-tiba, sekejap angin kencang melintasi area sekitar, menciptakan semburat hawa yang membelai wajah semua yang berada di sekitarnya."
    "Seolah-olah angin itu memiliki kekuatan gaib, hembusan tersebut membawa aroma mistis dan sensasi keajaiban yang menyelimuti seluruh tempat."
    Han "Sekarang, lihatlah ke belakang, lihat anak perawanmu itu!!"
    "Kiai Muslim segera berpaling ke belakang. Betapa terkejutnya ia melihat anak gadisnyacitu sudah tergeletak di tanah tidak bergerak."
    "Kiai Muslim segera berlari ke arah anak gadisnya. Diguncang-guncangkan tubuh Siti Amirah, tetapi tubuh itu sudah kaku dan dingin."
    "Dalam momen yang penuh duka, Kiai Muslim memeluk anak gadisnya dengan erat, mencoba menenangkan hatinya yang penuh kesedihan. Air mata mengalir di pipinya, sedangkan tangannya tetap memeluk erat tubuh Siti Amirah yang kini terbaring tak bernyawa di pelukannya."
    "Sementara itu, Joko Lancur, yang juga berada di tengah kejadian tragis ini, hanya bisa terdiam dengan perasaan terkejut dan syok yang tak tergambarkan."
    "Dia melihat dengan mata yang penuh air mata bahwa gadis yang menjadi satu-satunya cintanya, Siti Amirah, telah meninggalkan dunia ini untuk selamanya."
    Joko "Mustahil.."
    Joko "I-ni hanya mimpi, kan..?"
    "Kesedihan yang mendalam menyelimuti hati Joko Lancur. Dia merasa kehilangan, seolah-olah dunia yang ia kenal tiba-tiba runtuh di hadapannya."
    "Semua mimpi dan harapan mereka bersama hancur dalam sekejap, meninggalkan Joko dalam kekosongan yang tak terhingga."
    "Ki Hanggolono yang sudah dikuasai amarah semakin menjadi melihat kesedihan Kiai Muslim dan keluarganya. Dia bahkan sudah tidak ingat dengan anaknya sendiri."
    "Kemudian Ki Hanggolono melepaskan sumpah serapah yang keluar dari mulutnya dengan kata-kata yang penuh kebencian."
    Han "Wahai semua warga Mirah, jangan sampai kalian menyimpan damen dan titen, dan jangan pula berani menanam kedelai. Orang Nggolan tidak boleh kawin dengan orang Mirah selamanya. Kalau dilanggar kalian akan celaka."
    "Joko Lancur merasakan kegelisahan dan keputusasaan yang tak terkatakan dalam hatinya. Seperti refleks yang tak terkontrol, dia menghunuskan keris yang ada di pinggangnya dengan gerakan yang tajam."
    "Matanya terpaku pada bilah keris yang berkilau di bawah cahaya, sementara pikirannya dipenuhi oleh pertanyaan dan keraguan."
    show jsad at jleft:
        ease 0.5 zoom 1.01
    Joko "Apalah arti hidup ini..?"
    Joko "Ayahku sudah gila, dan satu-satunya gadis yang kucintai telah tiada."
    show jsad at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=2)
    Joko "Aku sudah tidak memiliki alasan lagi untu hidup"
    hide jsad with dissolve
    "Joko Lancur menusuk perutnya dengan keris tersebut. Darah mengalir deras dari tubuhnya."
    scene black with eye_shut
    Joko "Siti.., A..mirah.."
    stop music fadeout 1.0
    "Joko Lancur meninggal dunia dengan penuh keputusasaan."
    window hide
    $ renpy.pause(2)
    scene bg with fade
    show true at center with dissolve
    $ renpy.pause(3)
    return

label end2:
    scene black
    stop music fadeout 1.0
    pause(1)
    scene teras with dissolve
    "Dalam keputusasaan, kami memutuskan untuk meminta nasihat kepada Kiai Musli, ayah Siti Amirah yang sangat dihormati sebagai pemuka agama di kampung mereka. Kami mendatangi rumah Kiai Muslim dengan hati-hati dan penuh harapan."
    Siti "Assalamualaikum, ayahanda..,"
    show msedih at mright with moveinright
    kiai "Waalaikumsalam, nak.."
    play music "audio/damai.mp3" fadein 0.5 volume 0.8
    "Wajah Kiai Muslim terlihat masam ketika melihatku datang bersama Siti Amirah."
    "Kami berdua mencium tangan Kiai Muslim."
    show jnetral at jleft with moveinleft:
        ease 0.5 zoom 1.01
    Joko "Kiai, maafkan bila saya lancang.. Saya kesini ingin meminta pendapat mengenai masa depan Saya dan Siti Amirah."
    show jnetral at jleft:
        ease 0.5 zoom 1.0
    show msedih at mright:
        ease 0.5 zoom 1.01
    kiai "Sebaiknya mari kita bahas di dalam saja."
    hide msedih with moveoutright
    hide jnetral with moveoutright
    scene black with dissolve
    hide teras
    scene tamu2 with dissolve
    "Kami bertiga berkumpul di ruang tamu rumah Kiai Muslim. Meski dari luar rumahnya terlihat besar, tetapi desain interior begitu sederhana."
    "Siti Amirah duduk di kursi samping Ayahnya. Sedangkan aku duduk menghadap Kiai Muslim. Semua tekanan jatuh pada punggungku."
    show snetral flip at sleft:
        ease 0.5 zoom 1.02
    Siti "Begini, Ayahanda-"
    show snetral flip at sleft:
        ease 0.5 zoom 1.0
    kiai "Biarkan Joko yang menjelaskan." 
    hide snetral with moveoutright
    "Aku mengambil nafas dalam-dalam, merasakan nafas masuk dan keluar dari paru-paruku dengan perlahan. Aku mencoba memfokuskan perhatianku pada perasaan dan pikiran yang muncul di dalam diriku."
    "Dalam momen ini, aku harus berpikir secara hati-hati sebelum mengungkapkan kata-kata apa pun"
    "Tapi sudah kuputuskan."
    show jnetral at jleft:
        ease 0.5 zoom 1.0
    Joko "Saya ingin masuk islam."
    show skaget at sright
    show skaget at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=2)
    Siti "Apa..?"
    hide skaget
    show mkaget at sleft:
        ease 0.5 zoom 1.01
    kiai "Saya mengerti.., tetapi sebelumnya, apa alasan Joko?"
    show mkaget at mright:
        ease 0.5 zoom 1.0
    show jnetral at jleft:
        ease 0.5 zoom 1.01
    Joko "Saya merasa bahwa kehidupan yang saya lakukan tidak artinya. Kesenangan foya-foya dulu, sudah tidak bisa saya rasakan."
    Joko "Kemudian saya cukup tertarik dengan ajaran Islam. Dimana pak Kiai dapat membangun desa tanpa harus dengankekerasan."
    Joko "Saya juga mendengar dari Siti bahwa dalam agama Islam diajarkan tentang pembalasan di kehidupan selanjutnya. Karena itu saya berpikir mungkin dengan Islam, kehidupan saya akan lebih tertata."
    show jnetral at jleft:
        ease 0.5 zoom 1.0
    show mkaget at mright:
        ease 0.5 zoom 1.01
    kiai "Apakah itu alasan Joko ingin masuk Islam? Bukan karena Siti Amirah..?"
    show mkaget at mright:
        ease 0.5 zoom 1.0
    show jnetral at jleft:
        ease 0.5 zoom 1.0
    Joko "Saya tidak bisa menyangkal bahwa Siti Amirah menjadi motivasi saya masuk islam. Tetapi di lubuk hati terdalam, saya memang ingin berubah."
    show jnetral at jleft:
        ease 0.5 zoom 1.0
    hide jnetral
    hide mkaget
    "Aku merasa kehadiran Kiai Muslim begitu kuat dalam keheningan. Pandangannya yang tajam dan mendalam seolah-olah dapat menembus kedalaman pikiranku."
    "Aku merasakan tatapan matanya yang penuh perhatian, seakan-akan dia sedang membacasetiap pikiran dan perasaan yang ada dalam dirik."
    show sblush flip at sleft with moveinright
    Siti "Ayahanda..?"
    show msedih at mright:
        ease 0.5 zoom 1.01
    kiai "Itu adalah hal yang menggembirakan, Joko. Islam adalah agama yang menekankan keadilan, kasih sayang, dan kedamaian. Jika kau sungguh-sungguh dalam keinginanmu untuk memeluk Islam, aku siap membantumu dalam proses ini"
    kiai "Saya akan memberikanmu pengajaran dan mendampingimu dalam perjalananmu untuk memahami agama ini dengan lebih dalam."
    kiai "Dan juga anakku, cinta sejati adalah hadiah yang langka. Jika kalian berdua yakin dan saling mendukung dalam perjalanan spiritual ini, maka saya juga siap memberikan bimbingan sebaik mungkin."
    show msedih at mright:
        ease 0.5 zoom 1.0
    show sblush flip at sleft:
        ease 0.5 zoom 1.02
    Siti "Ayahanda serius..?"
    show sblush flip at sleft:
        ease 0.5 zoom 1.0
    hide sblush
    hide msedih
    "Kiai Muslim tersenyum mengiyakan pertanyaan Siti Amirah."
    "Siti Amirah menatapku sesaat dengan senyuman bangga. Tapi kemudian memalingkan wajahnya yang kemerahan."
    show jnetral at jleft with moveinleft:
        ease 0.5 zoom 1.01
    Joko "Terima kasih, Kiai Muslim. Aku bersyukur atas kesediaanmu membimbingku dalam perjalanan ini."
    Joko "Aku siap melangkah maju dan menghadapi tantangan yang ada. Lalu tentu saja, bersama Siti Amirah."
    hide jnetral with dissolve
    scene black with dissolve
    hide tamu2
    show white with dissolve(dissolve_time=3.0)
    $ renpy.pause(2)
    "Beberapa bulan berlalu, Aku mengikuti pengajaran agama bersama Kiai Muslim. Ia belajar tentang prinsip-prinsip Islam, melaksanakan shalat, dan memperdalam pemahaman tentang ajaran-ajaran agama."
    play music "audio/rabi.mp3" fadein 1.0 volume 0.7
    "Proses ini tidak mudah, tetapi Aku didukung oleh cinta dan pengertian Siti Amirah, serta bimbingan Kiai Muslim."
    "Pada akhirnya, Aku dengan yakin mengucapkan dua kalimat syahadat di hadapan Kiai Muslim dan Siti Amirah. Suasana bahagia dan sukacita terpancar dari wajah semuanya. aku resmi menjadi seorang Muslim."
    hide white with dissolve
    "Hingga waktunya tiba, momen paling bahagia dalam hidupku"
    scene pernikahan with dissolve
    play voice "audio/nikah.mp3" volume 0.7
    $ renpy.pause(1)
    "Aku dan Siti Amirah berdiri di depan semua orang. Saling berpegangan tangan, dengan wajah penuh harap dan cinta yang tak terhingga." 
    "Kami saling berjanji untuk mencintai, menghormati, dan mendukung satu sama lain dalam kehidupan yang akan datang."
    "Pernikahan dirayakan dengan sukacita dan kehangatan. Acara berlangsung dengan kebersamaan, doa, dan ungkapan kasih sayang dari semua yang hadir."
    Joko "Ini adalah hari terbaik dalam hidupku."
    Siti "Begitupun denganku."
    "Sesaat, kami saling bertatap mata dengan pandangan yang penuh makna.."
    Joko "Aku mencintaimu, Siti."
    Siti "Aku juga mencintaimu, Joko."
    window hide
    scene black with eye_shut
    $ renpy.pause(2)
    scene bg with fade
    show good at center with dissolve
    $ renpy.pause(3)
    return

label end3:
    scene black
    stop music fadeout 1.0
    pause(1)
    "Aku dan Siti Amirah memutuskan untuk meminta pendapat ayahku, Ki Hanggolono. Meskipun agak kasar, ayahku adalah sosok yang bijak. Apalagi memutuskan perkara yang mengenai diriku."
    scene halaman with dissolve:
        blur 16
    show snetral at sright
    show jnetral at jleft
    Siti "Apakah ini akan baik-baik saja?"
    Joko "Tidak apa."
    "Wajar Siti Amirah takut karena nama Ki Hanggolono sudah terdengar kasar."
    scene halaman with dissolve
    play music "audio/ki.mp3" volume 0.6
    show  hnetral at hright with fade
    Han "Waduh.. waduh.. Ada apa ini?"
    Siti "Permisi, Ki.."
    Joko "Aku dan Siti Amirah masihkebingungan dengan masa depan kami, Tidakkah ayah mempunyai sebuah saran?"
    Han "Pernikahan beda agama..? Apakah sungguh dilarang?"
    "Aku menoleh pada Siti Amirah di samping."
    Siti "Mohon maaf, kami dilarang untuk menikah dengan orang yang tidak memeluk Islam."
    Han "Yasudah, bukankah kemarin Kiai Muslim menawarkan permintaan.. Tinggal dipenuhi saja."
    Joko "Sudah kubilang-"
    Siti "Ayahku tidak akan menerima sesuatu yang berasal dari jin dan setan."
    show hmarah at hright
    hide hnetral
    Han "Apa maksudmu??! Apa kau bilang bahwa aku sesat?! Apa menurutmu kepercayaan yang diturunkan dari leluhur adalah menyesatkan."
    "Sepertinya perkataan Siti Amirah membuat ayahku marah. Sebaiknya harus berhati-hati dengan kata-kata selanjutnya. Karena jika ayahku kehilangan kendali..."
    Joko "Ayah.., Tenanglah."
    Han "Tidak sebelum bocah itu menarik kata-katanya."
    "Aku melihat Siti Amirah dengan ekspresi memohon. Untuk kali ini saja untuk keselamatannya."
    "Siti Amirah melangkah mundur. Dia tetap diam sembari menggelengkan kepala."
    show hrmarah at hright with dissolve
    hide hmarah
    show hrmarah at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=3)
    Han "Keparat..!!"
    "Ayahku segera kehilangan kendali, emosi yang tidak stabil membuat membuat dirinya mudah kerasukan."
    Joko "Lari..! Aku bilang lari..!"
    "Aku segera menarik Siti Amirah menjauh dari hadapan ayahku."
    "Namun, sudah terlambat. Saat rapalan mantra dilakukan, energi sihir langsung muncul dan ditujukan kepada Siti Amirah."
    "Sudah jelas kita berdua tidak akan bisa mengelak."
    Joko "Apapun yang terjadi tetaplah berlari!"
    Siti "Joko..?"
    "Di saat detik-detik terakhir sebelum sihir sampai, aku mendorong Siti Amirah ke depan. Sehingga akulah yang akan terkena dampaknya."
    scene halaman at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=5)
    "(BOOMM!!!)"
    "Punggungku terkena sihir dengan sangat fatal."
    "Sekian detik, Siti Amirah menatapku diam dengan ekspresi yang tidak tega."
    Joko "Aku bilang tetap lari!!"
    Siti "Tapi, Joko.."
    Joko "Lari! Ayahku tidak akan bisa melukaiku!"
    Siti "Joko.."
    "Untuk terakhir kali dia memanggil namaku dengan penuh kesedihan. Aku tetap berdiri tegar untuknya. Lalu meski berat hati, Siti Amirah berlari meninggalkanku."
    "Beberapa detik setelah Siti Amirah pergi, aku mulai kehilangan kesadaran. Tubuhku terasa lemas, dan punggungku mati rasa."
    "Aku langsung tersungkur ke tanah. mataku terasa berat serta aku mulai tidak bisa merasakan tubuhku. Dari sini, aku masih bisa melihat titik kecil dimana Siti Amirah berlari."
    show hrsedih at hright with fade:
        xalign 0.5
    Han "Dasar bodoh..!"
    Han "Kenapa kamu melakukan..."
    hide hrsedih with fade
    stop music fadeout 1.0
    scene black with eye_shut
    "Secara samar-samar aku mendengar suara ayahku."
    "Sudahlah, aku tidak peduli lagi."
    "Setidaknya, aku masih bisa menyelamatkanmu..."
    "Maafkan aku.."
    window hide
    $ renpy.pause(2)
    scene bg with fade
    show bad at center with dissolve
    $ renpy.pause(3)
    return

label end4:
    scene black
    stop music fadeout 1.0
    pause(1)
    Siti "Kalau begitu, ikutlah denganku!"
    Joko "Kemana..?"
    scene danau with dissolve:
        blur 16
    "Ketika aku mengikuti Siti Amirah dalam perjalanan, kami mulai melakukan basa-basi untuk memulai percakapan."
    "Aku mencoba menjaga suasana santai dan ramah. Aku bertanya tentang minat atau hobi yang sedang dia tekuni, serta kegiatan yang sedang dia lakukan akhir-akhir ini."
    play music "audio/danau.mp3" volume 0.8
    "Aku juga berbagi sedikit tentang diriku, menjelaskan minat atau kegiatan saya sendiri untuk membangun koneksi dan saling mengenal lebih baik."
    scene danau with dissolve
    show snetral at sright with fade:
        ease 0.5 zoom 1.02
    Siti "Kita sudah sampai."
    show snetral at sright:
        ease 0.5 zoom 1.0
    show jnetral at jleft with moveinleft:
        ease 0.5 zoom 1.01
    Joko "Wah..! Aku tidak tau ada tempat seperti di sekitar desa."
    show jnetral at jleft:
        ease 0.5 zoom 1.0
    show snetral at sright:
        ease 0.5 zoom 1.02
    Siti "Memang jarang yang datang ke sini. Tapi aku senang bisa membawamu ke sini."
    show snetral at sright:
        ease 0.5 zoom 1.0
    show jnetral at jleft:
        ease 0.5 zoom 1.01
    Joko "Air terjun, Danau.., sungguh pemandangan yang indah."
    show jnetral at jleft:
        ease 0.5 zoom 1.0
    show snetral at sright:
        ease 0.5 zoom 1.02
    Siti "Ketika sedih atau kebingungan aku sering ke sini untuk mencariketeangan."
    show snetral at sright:
        ease 0.5 zoom 1.0
    show jnetral at jleft:
        ease 0.5 zoom 1.01
    Joko "Aku bisa memahami mengapa tempat ini begitu istimewa bagi Siti. Ini benar-benar tempat yang menyegarkan jiwa"
    show jnetral at jleft:
        ease 0.5 zoom 1.0
    show snetral at sright:
        ease 0.5 zoom 1.02
    Siti "Alhamdulillah.."
    show snetral at sright:
        ease 0.5 zoom 1.0
    show sblush at sright
    show jblush at jleft
    hide snetral
    hide jnetral
    "Kami berdua duduk di tepi danau, menikmati pemandangan yang indah sambil bercerita dan berbagi pengalaman."
    "Dalam perbincangan kami, aku mulai menyadari betapa bijaknya Siti Amirah. Dia memiliki wawasan dan pemikiran yang mendalam, serta pandangan hidup yang penuh kebijaksanaan."
    "Ketika Siti Amirah berbicara, aku terpesona oleh kearifan dan pemahamannya tentang berbagai hal. Dia memiliki kemampuan untuk melihat masalah dari berbagai sudut pandang dan memberikan perspektif yang berbeda. "
    "Aku merasa terinspirasi oleh kebijaksanaannya dalam menghadapi situasi dan mengambil keputusan."
    show jblush at jleft:
        ease 0.5 zoom 1.02
    Joko "Siti Amirah benar-benar perempuan yang hebat. Aku merasa tidak pantas bersamamu."
    show jblush at jleft:
        ease 0.5 zoom 1.0
    show sblush at sright:
        ease 0.5 zoom 1.02
    Siti "Jangan begitu, semua manusia melakukan kesalahan. Tergantung apakah dia mau berusaha menjadi lebih baik, atau tidak.."
    show sblush at sright:
        ease 0.5 zoom 1.0
    show jblush at jleft:
        ease 0.5 zoom 1.02
    Joko "Apakah menurutmu aku bisa menjadi orang baik..?"
    show jblush at jleft:
        ease 0.5 zoom 1.0
    show sblush at sright:
        ease 0.5 zoom 1.02
    Siti "Tentu saja."
    show sblush at sright:
        ease 0.5 zoom 1.0
    "Kami tersenyum memandang satu sama lain. Aku merasa kami bertambah dekat. Meski begitu, aku tahu aku tidak akan menggapai dirinya."
    show jblush at jleft:
        ease 0.5 zoom 1.02
    Joko "Aku sangat berterima kasih..,"
    Joko "Terima kasih telah hadir di hidupku meski sesaat. Engkau telah mengubah hidupku sejak pertama kali bertemu. Aku benar-benar belajar banyak darimu."
    show jblush at jleft:
        ease 0.5 zoom 1.0
    show sblush at sright:
        ease 0.5 zoom 1.02
    Siti "Sama-sama, baguslah jika aku memang membantumu."
    show sblush at sright:
        ease 0.5 zoom 1.0
    show jblush at jleft:
        ease 0.5 zoom 1.02
    Joko "Iya.., meskipun aku tahu kita tidak bisa bersatu..."
    show jblush at jleft:
        ease 0.5 zoom 1.0
    hide sblush
    hide jblush
    "Aku beranjak bangun, dengan segenap hati aku mencoba berpaling dari Siti Amirah. Karena inilah keputusan yang terbaik untuk kami berdua."
    scene black with eye_shut
    stop music fadeout 1.0
    Joko "...Terima kasih,"
    Joko "Dan sampai jumpa.."
    window hide
    $ renpy.pause(2)
    scene bg with fade
    show peace at center with dissolve
    $ renpy.pause(3)
    return
    