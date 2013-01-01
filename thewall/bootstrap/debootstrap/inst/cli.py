# -*- coding: utf-8 -*-
# thewall bootstrap.debootstrap module install - (C) 2013 Eugenio "g7" Paolantonio and the Semplice Team.
# All rights reserved. Work released under the GNU GPL license, version 3 or later.
#
# This is a module of linstaller, should not be executed as a standalone application.

import linstaller.frontends.cli as cli
import linstaller.core.main as m
import t9n.library
_ = t9n.library.translation_init("linstaller")

from linstaller.core.main import warn,info,verbose

class Frontend(cli.Frontend):
	def start(self):
		""" Start the frontend """

		# Get a progressbar
		progress = self.progressbar(_("Bootstrapping system:"), 1)

		# Start progressbar
		progress.start()
		
		self.moduleclass.bootstrap()
		progress.update(1)
		
		
		progress.finish()
