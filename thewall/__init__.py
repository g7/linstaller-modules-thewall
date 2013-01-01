# -*- coding: utf-8 -*-
# thewall main module install - (C) 2013 Eugenio "g7" Paolantonio and the Semplice Team.
# All rights reserved. Work released under the GNU GPL license, version 3 or later.
#
# This is a module of linstaller, should not be executed as a standalone application.

import linstaller.core.module as module
import linstaller.core.main as m

class Module(module.Module):
	def _associate_(self):
		""" Shut up _associate_ as we haven't any frontend. """

		pass
	
	def start(self):
		""" Shut up start as this is a fake module. """

		pass
	
	def seedpre(self):
		""" Cache configuration. """
		
		self.cache("arch", "i386")
		self.cache("insecure", False)
		self.cache("restore_security", True)
