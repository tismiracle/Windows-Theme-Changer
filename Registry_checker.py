import subprocess
from winreg import HKEY_CURRENT_USER, ConnectRegistry, QueryInfoKey, QueryValueEx, QueryValue, OpenKey, CloseKey, SetValueEx, REG_DWORD, DeleteKey

class Registry_checker():
    def __init__(self) -> None:
        self.connect_registry()
        self.reg = self.open_key(r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize")

        self.color_reg = self.open_key(r"Software\Microsoft\Windows\DWM")

    def connect_registry(self):
        ConnectRegistry(None, HKEY_CURRENT_USER)

    def open_key(self, path):
       key = OpenKey(HKEY_CURRENT_USER, path) 
       return key

    def check_if_app_light_theme(self):
        if_app_light_theme = QueryValueEx(self.reg, "AppsUseLightTheme")
        return if_app_light_theme
    
    def check_if_system_light_theme(self):
        if_system_light_theme = QueryValueEx(self.reg, "SystemUsesLightTheme")
        return if_system_light_theme
    
    def check_if_transparency_enabled(self):
        if_transparency = QueryValueEx(self.reg, "EnableTransparency")
        return if_transparency
    
    def check_if_color_prevalence(self):
        if_color_prevalence = QueryValueEx(self.reg, "ColorPrevalence")
        return if_color_prevalence

    def return_colorization_hex(self):
        colorization_color = QueryValueEx(self.color_reg, "ColorizationColor")
        return colorization_color
    
    def check_if_window_borders(self):
        window_borders = QueryValueEx(self.color_reg, "ColorPrevalence")
        return window_borders
    
    def check_old_context_menu(self):
        try:
            self.old_context_menu = self.open_key(r"Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}")
            return 1
        except:

            return 0
    
    def delete_old_context_menu(self):

        subprocess.call(r'reg.exe delete "HKCU\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}" /f')

    def add_old_context_menu(self):
        subprocess.call(r'reg.exe add "HKCU\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}\InprocServer32" /f /ve')
    
    def close_registry(self):
        CloseKey(self.reg)
        CloseKey(self.color_reg)

