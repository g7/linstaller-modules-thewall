# -*- coding: utf-8 -*-
# thewall bootstrap.debootstrap module install - (C) 2013 Eugenio "g7" Paolantonio and the Semplice Team.
# All rights reserved. Work released under the GNU GPL license, version 3 or later.
#
# This is a module of linstaller, should not be executed as a standalone application.

import linstaller.core.module as module
import linstaller.core.main as m

import os

from linstaller.core.main import verbose

class Module(module.Module):
	def seed_setup(self):
		""" We are reading the settings from thewall.bootstrap module. """
		
		self.cfg.module = "module:thewall.bootstrap"
	
	def bootstrap(self):
		""" Actually run the bootstrap. """
				
		is_insecure = self.modules_settings["thewall"]["insecure"]
		is_foreign = False # FIXME!
		
		arch = self.modules_settings["thewall"]["arch"]
		areas = self.settings["areas"].split(" ")
		
		bootstrap_args = ["--arch=%s" % arch, "--components=%s" % ",".join(areas)]
		if is_foreign: bootstrap_args.append("--foreign")
		if is_insecure: bootstrap_args.append("--no-check-gpg")
		
		# Execute debootstrap...
		verbose("Executing debootstrap...")
		
		m.sexec("debootstrap %(options)s \"%(distro)s\" \"%(target)s\" \"%(mirror)s\"" %
			{
				"options":" ".join(bootstrap_args),
				"distro":self.settings["distro"],
				"target":self.main_settings["target"],
				"mirror":self.settings["mirror"]
			}
		)
		
		if is_foreign:
			# FIXME!
			pass
		
		# Remove newly created hosts file...
		os.remove(os.path.join(self.main_settings["target"], "etc/hosts"))
		
		# Remove package cache...
		base = os.path.join(self.main_settings["target"], "var/cache/apt/archives")
		for item in os.listdir(base):
			if item.endswith(".deb"):
				os.remove(os.path.join(base, item))
	
	def seedpre(self):
		""" Cache configuration """
		
		self.cache("distro")
		self.cache("mirror")
		self.cache("areas", "main")
