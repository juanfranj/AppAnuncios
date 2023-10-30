from kivads import (
    BannerAd,
    InterstitialAd,
    KivAds,
    RewardedAd,
    RewardedInterstitial,
    TestID,
)

from kivymd.app import MDApp 
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
    
    


class Pantalla(BoxLayout):
    

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app = MDApp.get_running_app()

    def mostrar(self):
        self.ids.label.text = "Mostrar Banner"
        self.app.banner.show()

    def cargar_anuncios(self):
        self.ids.label.text = "Cargando anuncios"
        self.app.interstitial = InterstitialAd(TestID.INTERSTITIAL)
        self.app.banner.hide()

    def mostrar_intersticial(self):
        self.ids.label.text = "Mostrar Intersticial"
        self.app.interstitial.show()
    
    def mostrar_video(self):
        self.ids.label.text = "Mostrar video"

class MainApp(MDApp):

    def build(self):
        self.root = Builder.load_file("main.kv")
        self.title = "PruebaAnuncios"
        self.ads = KivAds()
        self.banner = BannerAd(TestID.BANNER, int(Window.width), True)
        self.interstitial = InterstitialAd(TestID.INTERSTITIAL)

        return self.root
    
    def on_pre_enter(self):
        self.banner.show()
    

if __name__ == '__main__':
    MainApp().run()