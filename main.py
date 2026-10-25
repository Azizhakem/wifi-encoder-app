from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.utils import get_color_from_hex

class WifiEncoderApp(App):
    def build(self):
        self.title = "مفعل رموز الواي فاي"
        
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        # عنوان
        layout.add_widget(Label(text="أدخل الاسم أو الرمز:", font_size=18, size_hint=(1, 0.1)))
        
        # خانة الإدخال
        self.entry = TextInput(font_size=20, multiline=False, size_hint=(1, 0.15), halign="center")
        self.entry.bind(text=self.translate_text)
        layout.add_widget(self.entry)
        
        # مكان عرض النتيجة
        layout.add_widget(Label(text="النتيجة:", font_size=14, color=(0.5, 0.5, 0.5, 1), size_hint=(1, 0.1)))
        
        self.result_label = Label(text="", font_size=22, color=get_color_from_hex("#2e7d32"), size_hint=(1, 0.2))
        layout.add_widget(self.result_label)
        
        return layout

    def translate_text(self, instance, value):
        user_input = value.strip().lower()
        
        if user_input.startswith("fh"):
            remaining_text = user_input[2:]
        else:
            remaining_text = user_input
            
        translation_table = str.maketrans({
            '7': '8', '8': '7',
            '6': '9', '9': '6',
            '5': 'a', 'a': '5',
            '4': 'b', 'b': '4',
            '3': 'c', 'c': '3',
            '2': 'd', 'd': '2',
            '1': 'e', 'e': '1',
            '0': 'f', 'f': '0'
        })
        
        translated_part = remaining_text.translate(translation_table)
        
        if user_input.startswith("fh"):
            final_password = "wlan" + translated_part
        else:
            final_password = translated_part
            
        self.result_label.text = final_password

if __name__ == '__main__':
    WifiEncoderApp().run()