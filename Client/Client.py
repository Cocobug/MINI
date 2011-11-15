#!/usr/bin/env python
# encoding: utf-8
#######################################################
# MINI - MINI Is Not Irc
# [CLIENT]
#######################################################
# Date: 05/04/10                                      #
# Auteurs: Rigaut Maximilien                          #
# Nom: MINI                                          #
# Version: 0.2a                                       #
# Copyright 2010: Rigaut Maximilien                   #
#######################################################
#    This file is part of MINI.
#
#    MINI is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    Gomoku is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with MINI.  If not, see <http://www.gnu.org/licenses/>.
#######################################################
# LICENCE                                             #
#######################################################
print """
+------------------------------------------------------------------+
| MINI Copyright (C) 2010 Rigaut Maximilien                       |
| Ce programme vient SANS ABSOLUMENT AUCUNE GARANTIE.              |
| Ceci est un logiciel libre et vous êtes invité à le redistribuer |
| suivant certaines conditions.                                    |
+------------------------------------------------------------------+
"""
#======================+
#  Modules             |
#----------------------+

#-----------------------
# Modules Externes
#- - - - - - - - - - - -
import sys, os, unittest, socket, threading
from random import randint

#-----------------------
# Modules internes
#- - - - - - - - - - - -
cwd=os.getcwd()
sys.path.append(cwd+'/Modules')
sys.path.append(cwd+'/Preferences')
#- - - - - - - - - - - -

from Functions import *

#----------------------+
# Initialisation       |
#- - - - - - - - - - - +
(HOST,PORT,Nom)=init_NETvars()


#---------------------------------+
# Initialisation des classes      |
# - - - - - - - - - - - - - - - - +

class ThreadReception(threading.Thread):
	"""Objet thread gerant la reception des messages."""
	def __init__(self, conn):
		threading.Thread.__init__(self)
		self.connection = conn # Reference du socket (connection)
	
	def run(self):
		while 1:
			message_recu = self.connection.recv(1024)
			print message_recu
			if message_recu=='' or message_recu.upper()=='FIN':
				break
			# Le thread <reception> ce termine ici
			# On force sa fermeture
		th_E._Thread__stop()
		print "Client Arreté. Connection interrompue..."
		self.connection.close()
class ThreadEmission(threading.Thread):
	"""Objet gerant l'émission des Messages"""
	def __init__(self, conn):
		threading.Thread.__init__(self)
		self.connection=conn # Reference du socket
	
	def run(self):
		#self.connection.send('/nick %s' % Nom)
		while 1:
			message_emis=raw_input()
			if len(message_emis)>0 and message_emis[0]=='/':
				self.commande('/')
			self.connection.send(message_emis)
	def commande(self,arguments):
		pass

#======================================================+
# Programme principal - Etablissement de la Connection |
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --+
connection=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
	connection.connect((HOST,PORT))
except socket.error:
	print "Connection échouée - ressayer plus tard..."
	sys.exit()
print "Connection établie avec le server..."


# On lance les deux threads pour gérer independement
# reception et émission des messages.

th_E = ThreadEmission(connection)
th_R = ThreadReception(connection)
th_E.start()
th_R.start()