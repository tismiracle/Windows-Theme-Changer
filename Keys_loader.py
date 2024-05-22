
import subprocess
import os

#REG QUERY HKCU\Software\Microsoft\Windows\CurrentVersion\Themes\Personalize - sprawdzanie wartosci personalize

#LIGHT THEME FOR APPS
#REG ADD HKCU\Software\Microsoft\Windows\CurrentVersion\Themes\Personalize /v AppsUseLightTheme /d 1 /t REG_DWORD /f - light theme apps
#REG ADD HKCU\Software\Microsoft\Windows\CurrentVersion\Themes\Personalize /v AppsUseLightTheme /d 0 /t REG_DWORD /f - dark theme apps

#LIGHT THEME FOR SYSTEM
#REG ADD HKCU\Software\Microsoft\Windows\CurrentVersion\Themes\Personalize /v SystemUsesLightTheme /d 1 /t REG_DWORD /f
#REG ADD HKCU\Software\Microsoft\Windows\CurrentVersion\Themes\Personalize /v SystemUsesLightTheme /d 0 /t REG_DWORD /f

#TRANSPARENCY
#REG ADD HKCU\Software\Microsoft\Windows\CurrentVersion\Themes\Personalize /v EnableTransparency /d 1 /t REG_DWORD /f
#REG ADD HKCU\Software\Microsoft\Windows\CurrentVersion\Themes\Personalize /v EnableTransparency /d 0 /t REG_DWORD /f

#COLOR PRELEVANCE
#Reg Add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize" /v ColorPrevalence /t REG_DWORD /d 2 /f - taskbar only
#Reg Add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize" /v ColorPrevalence /t REG_DWORD /d 1 /f - start + taskbar
#Reg Add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize" /v ColorPrevalence /t REG_DWORD /d 0 /f - none

#WINDOW BORDERS NEED A SIGNOUT
#HKEY_CURRENT_USER\Software\Microsoft\Windows\DWM
#Reg Add "HKCU\SOFTWARE\Microsoft\Windows\DWM" /v ColorPrevalence /t REG_DWORD /d 1 /f
#Reg Add "HKCU\SOFTWARE\Microsoft\Windows\DWM" /v ColorPrevalence /t REG_DWORD /d 0 /f

#ACCENT PALETTE
#REG ADD Computer\HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\Accent /v AccentColorMenu BGR values
#REG ADD Computer\HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\Accent /v StartColorMenu
#REG ADD Computer\HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\Accent /v AccentPalette

#OLD CONTEXT MENU
#reg.exe add "HKCU\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}\InprocServer32" /f /ve

#ADD SQUARE CORNERS
#REG ADD HKCU\Software\Microsoft\Windows\DWM /v UseWindowFrameStagingBuffer /d 0 /t REG_DWORD 

class Keys_Loader():
	def __init__(self):
		print("Loader initiated")
		self.pwd = os.getcwd()
		print(self.pwd)
		

	# def load_app_light_theme(self):
	def app_light_theme_enable(self):
		subprocess.call(r'REG ADD HKCU\Software\Microsoft\Windows\CurrentVersion\Themes\Personalize /v AppsUseLightTheme /d 1 /t REG_DWORD /f')

	# def load_app_dark_theme(self):
	def app_light_theme_disable(self):
		subprocess.call(r'REG ADD HKCU\Software\Microsoft\Windows\CurrentVersion\Themes\Personalize /v AppsUseLightTheme /d 0 /t REG_DWORD /f')

	# def load_system_light_theme(self):
	def system_light_theme_enable(self):
		subprocess.call(r'REG ADD HKCU\Software\Microsoft\Windows\CurrentVersion\Themes\Personalize /v SystemUsesLightTheme /d 1 /t REG_DWORD /f')

	# def load_system_dark_theme(self):
	def system_light_theme_disable(self):
		subprocess.call(r'REG ADD HKCU\Software\Microsoft\Windows\CurrentVersion\Themes\Personalize /v SystemUsesLightTheme /d 0 /t REG_DWORD /f')

	def enable_transparency(self):
		subprocess.call(r'REG ADD HKCU\Software\Microsoft\Windows\CurrentVersion\Themes\Personalize /v EnableTransparency /d 1 /t REG_DWORD /f')

	def disable_transparency(self):
		subprocess.call(r'REG ADD HKCU\Software\Microsoft\Windows\CurrentVersion\Themes\Personalize /v EnableTransparency /d 0 /t REG_DWORD /f')

#Reg Add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize" /v ColorPrevalence /t REG_DWORD /d 2 /f - taskbar only
#Reg Add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize" /v ColorPrevalence /t REG_DWORD /d 1 /f - start + taskbar
#Reg Add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize" /v ColorPrevalence /t REG_DWORD /d 0 /f - none

	def color_prevalence_none(self):
		subprocess.call(r'Reg Add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize" /v ColorPrevalence /t REG_DWORD /d 0 /f')

	def color_prevalence_taskbar(self):
		subprocess.call(r'Reg Add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize" /v ColorPrevalence /t REG_DWORD /d 2 /f')
	
	def color_prevalence_taskbar_start(self):
		subprocess.call(r'Reg Add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize" /v ColorPrevalence /t REG_DWORD /d 1 /f')

#WINDOW BORDERS NEED A SIGNOUT
#HKEY_CURRENT_USER\Software\Microsoft\Windows\DWM
#Reg Add "HKCU\SOFTWARE\Microsoft\Windows\DWM" /v ColorPrevalence /t REG_DWORD /d 1 /f
#Reg Add "HKCU\SOFTWARE\Microsoft\Windows\DWM" /v ColorPrevalence /t REG_DWORD /d 0 /f

	def enable_window_borders(self):
		subprocess.call(r'Reg Add "HKCU\SOFTWARE\Microsoft\Windows\DWM" /v ColorPrevalence /t REG_DWORD /d 1 /f')

	def disable_window_borders(self):
		subprocess.call(r'Reg Add "HKCU\SOFTWARE\Microsoft\Windows\DWM" /v ColorPrevalence /t REG_DWORD /d 0 /f')

	def add_old_context_menu(self):
		subprocess.call(r'reg.exe add "HKCU\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}\InprocServer32" /f /ve')

	def delete_old_context_menu(self):
		subprocess.call(r'reg.exe delete "HKCU\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}" /f')

	def restart_explorer(self):
		#taskkill /F /IM explorer.exe & start explorer
		subprocess.call("taskkill /F /IM explorer.exe")
		subprocess.Popen("start explorer", shell=True)

	def load_options(self, options_dict):
		for key in options_dict:
			print(key)
			if key == "apps_light_theme":
				print("True")
				if options_dict[key] == 1:
					self.app_light_theme_enable()
				else:
					self.app_light_theme_disable()

			elif key == "system_light_theme":
				print("True")
				if options_dict[key] == 1:
					self.system_light_theme_enable()
				else:
					self.system_light_theme_disable()
			
			elif key == "transparency":
				print("True")
				if options_dict[key] == 1:
					self.enable_transparency()
				else:
					self.disable_transparency()

			elif key == "color_prevalence":
				print("True")
				if options_dict[key] == 0:
					self.color_prevalence_none()
				if options_dict[key] == 1:
					self.color_prevalence_taskbar_start()
				if options_dict[key] == 2:
					self.color_prevalence_taskbar()

			elif key == "old_context_menu":
				if options_dict[key] == 0:
					self.delete_old_context_menu()
				if options_dict[key] == 1:
					self.add_old_context_menu()