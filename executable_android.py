from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.webview import WebView

class WebViewApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        
        webview = WebView(url='home.py', size_hint=(1, 1))
        layout.add_widget(webview)
        
        return layout

if __name__ == '__main__':
    WebViewApp().run()
