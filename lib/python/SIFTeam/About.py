from enigma import *
from Screens.Screen import Screen
from Components.Button import Button
from Components.Label import Label
from Components.ActionMap import ActionMap

class AboutTeam(Screen):
	def __init__(self, session, args = 0):
		Screen.__init__(self, session)
		
		abouttxt = """ST7TEAM (developer & coder)
For SH4 Box (sti 7111 & sti 7162)		
pop_popazerty (betatester)
Youssef El Arbi (betatester)"""
		
		self["about"] = Label(abouttxt)
		self["key_green"] = Button("")
		self["key_red"] = Button("")
		self["key_blue"] = Button(_("Exit"))
		self["key_yellow"] = Button("")
		self["actions"] = ActionMap(["OkCancelActions", "ColorActions"],
		{
			"blue": self.quit,
			"cancel": self.quit,
		}, -2)
		
	def quit(self):
		self.close()
