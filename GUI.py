import tkinter
from tkinter import colorchooser
from tkinter import PhotoImage
from Keys_loader import Keys_Loader
from os import getcwd
from Registry_checker import Registry_checker




class App():
	def __init__(self):
		self.root = tkinter.Tk()
		self.loader = Keys_Loader()
		#self.loader.load_app_light_theme()
		self.registry_checker = Registry_checker()

		self.options = {"system_light_theme": None, "apps_light_theme": None, "transparency": None, "color_prevalence": None, "old_context_menu": None, "window_borders": None}


		self.options["apps_light_theme"] = self.registry_checker.check_if_app_light_theme()[0]
		self.options["system_light_theme"] = self.registry_checker.check_if_system_light_theme()[0]
		self.options["transparency"] = self.registry_checker.check_if_transparency_enabled()[0]
		self.options["color_prevalence"] = self.registry_checker.check_if_color_prevalence()[0]


		self.options["old_context_menu"] = self.registry_checker.check_old_context_menu()
		self.options["window_borders"] = self.registry_checker.check_if_window_borders()[0]
		#self.options["colorization_hex"] = hex(self.registry_checker.return_colorization_hex()[0])
		print(self.options)
		self.if_light_system_theme = None
		self.root.grid_columnconfigure(0, weight=1)

		self.load_icons()
		self.app_theme_buttons()
		self.system_theme_buttons()
		self.color_prevalency_buttons()
		self.old_contextmenu_button()
		

		# self.auto_colourisation()
		self.transparency_buttons()	
		self.controls()
		self.root.mainloop()


	def load_icons(self):
		pass
		# self.colour_picker_icon = PhotoImage(file=getcwd() + "\colour_picker_black.png")


	def app_theme_buttons(self):
		# dark = 2 || light = 1
		self.var_app_light_or_dark = tkinter.IntVar(value=self.options["apps_light_theme"])
		app_theme_frame = tkinter.LabelFrame(self.root, text="App themes:")
		app_theme_frame.grid()
		app_light_theme_button = tkinter.Radiobutton(app_theme_frame, text="Light Theme", value=1, variable=self.var_app_light_or_dark)
		app_light_theme_button.grid(column=0, row=0)
		app_dark_theme_button = tkinter.Radiobutton(app_theme_frame, text="Dark Theme", value=0, variable=self.var_app_light_or_dark)
		app_dark_theme_button.grid(column=1, row=0)

		# if self.options["apps_light_theme"] == 1: 
		# 	app_light_theme_button.select()
		# else:
		# 	app_dark_theme_button.select()

	def system_theme_buttons(self):
		# dark = 2 || light = 1
		self.var_system_light_or_dark = tkinter.IntVar(value=self.options["system_light_theme"])
		system_theme_frame = tkinter.LabelFrame(self.root, text="System themes:")
		system_theme_frame.grid()
		system_light_theme_button = tkinter.Radiobutton(system_theme_frame, text="Light Theme", value=1, variable=self.var_system_light_or_dark)
		system_light_theme_button.grid(column=0, row=0)
		system_dark_theme_button = tkinter.Radiobutton(system_theme_frame, text="Dark Theme", value=0, variable=self.var_system_light_or_dark)
		system_dark_theme_button.grid(column=1, row=0)

		# if self.options["system_light_theme"] == 1: 
		# 	system_light_theme_button.select()
		# else:
		# 	system_dark_theme_button.select()



	def transparency_buttons(self):
		#add transparency checking. Function for regedit is done. 
		self.transparency_enabled = tkinter.IntVar(value=self.options["transparency"])
		transparency_frame = tkinter.LabelFrame(self.root, text="Transparency")
		transparency_frame.grid()
		transparency_button = tkinter.Checkbutton(transparency_frame, text="Transparency", onvalue=1, offvalue=0, variable=self.transparency_enabled)
		transparency_button.grid()

		# if self.options["transparency"] == 1:
		# 	transparency_button.select()


	def color_prevalency_buttons(self):
		self.color_prevalency_enabled = tkinter.IntVar(value=self.options["color_prevalence"])
		self.window_borders_enabled = tkinter.IntVar(value=self.options["window_borders"])

		colors_frame = tkinter.LabelFrame(self.root, text="Colors")
		colors_frame.grid()

		none_radiobutton = tkinter.Radiobutton(colors_frame, text="None", variable=self.color_prevalency_enabled, value=0)
		none_radiobutton.grid(column=0, row=0)
		taskbar_radiobutton = tkinter.Radiobutton(colors_frame, text="Taskbar", variable=self.color_prevalency_enabled, value=2)
		taskbar_radiobutton.grid(column=1, row=0)
		start_taskbar_radiobutton = tkinter.Radiobutton(colors_frame, text="Start + Taskbar", variable=self.color_prevalency_enabled, value=1)
		start_taskbar_radiobutton.grid(column=2, row=0)

		# if self.options["color_prevalence"] == 0:
		# 	none_radiobutton.select()
		# if self.options["color_prevalence"] == 1:
		# 	start_taskbar_radiobutton.select()
		# if self.options["color_prevalence"] == 2:
		# 	taskbar_radiobutton.select()

		window_borders_checkbutton = tkinter.Checkbutton(colors_frame, text="Window Borders", variable=self.window_borders_enabled, onvalue=1, offvalue=0)
		window_borders_checkbutton.grid(column=0, columnspan=3, row=1)

		

	def old_contextmenu_button(self):
		self.contextmenu_enabled = tkinter.IntVar(value=self.options["old_context_menu"])

		contextmenu_frame = tkinter.LabelFrame(self.root, text="Old Context Menu")
		contextmenu_frame.grid()

		contextmenu_checkbutton = tkinter.Checkbutton(contextmenu_frame, text="Enabled", variable=self.contextmenu_enabled, onvalue=1, offvalue=0)
		contextmenu_checkbutton.grid()

		# if self.options["old_context_menu"] == 1:
		# 	contextmenu_checkbutton.select()


	def controls(self):
		controls_frame = tkinter.Frame(self.root)
		controls_frame.grid()

		cancel_button = tkinter.Button(controls_frame, text="Exit", command=lambda:[self.registry_checker.close_registry(), self.root.quit()])
		# cancel_button = tkinter.Button(controls_frame, text="Exit", command=lambda:[self.registry_checker.close_registry()])
		cancel_button.grid(column=0, row=0, padx=10)

		apply_button = tkinter.Button(controls_frame, text="Apply", command=lambda:self.apply_options())
		apply_button.grid(column=2, row=0)
		

	def apply_options(self):
		self.options["apps_light_theme"] = self.var_app_light_or_dark.get()
		self.options["system_light_theme"] = self.var_system_light_or_dark.get()
		self.options["transparency"] = self.transparency_enabled.get()
		self.options["color_prevalence"] = self.color_prevalency_enabled.get()
		self.options["old_context_menu"] = self.contextmenu_enabled.get()

		print(self.options)
		self.loader.load_options(self.options)
		self.loader.restart_explorer()

		
