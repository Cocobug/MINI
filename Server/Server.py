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
sys.path.append(cwd+'/variables')
#- - - - - - - - - - - -

from Functions import *
from Moderation_System import *

#----------------------+
# Initialisation       |
#- - - - - - - - - - - +
(HOST,PORT)=init_NETvars()

#---------------------------------+
# Initialisation des classes      |
# - - - - - - - - - - - - - - - - +

class ThreadClient(threading.Thread):
	def __init__(self, conn):
		threading.Thread.__init__(self)
		self.connection=conn
	def run(self):
		# Dialogue
		nom=self.getName()
		while 1:
			message=self.connection.recv(1024)
			if message=='' or message=='FIN' or message=='END' or message[:5]=='/quit':
				break
			#elif message[9:]=='/bazarder':
			#	Moderation_kick(self,variables,client,arguments,message)
			else:
				print message
				self.msg('ALL',message)
			return True
		# Fermeture de la connection
		self.connection.shutdown(socket.SHUT_RDWR)
		self.connection.close()
		print 'Client déconnecté'
		self.msg('ALL', 'Client %s déconnecté'%nom)
		del variables.conn_clients[nom]
		# Le thread se termine ici
	def msg(self,cible,message):
		nom=self.getName()
		for client in variables.conn_clients:
			if client != nom:
				variables.conn_clients[client].send(message)
class Server_variables(object):
	def __init__(self):
		self.conn_clients={}
		self.clients_ip={}
		self.threads={}
		self.ipban=[]
#==========================
# Programme principal
#--------------------------
# Variables
# - - - - - - - - - -

#---------------------------
# Chargement des variables
# - - - - - - - - - -
variables=Server_variables()
#---------------------------
# Initialisation
# - - - - - - - - - -

#==========================
# Demmarage connection

mySocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#try:
#	if hashlib.md5('/bazarder').hexdigest()=='298426e82362e35b591419aa013564eb':
#		print "Module hash OK : Commandes admin utilisables" 
#except:
#	print "Module hash impossible a charger : Commandes admin inutilisables"

try:
	mySocket.bind((HOST,PORT))
except socket.error:
	print "La liaison du socket a l'addrese choisie a échoué...\nVerifiez que le port n'est pas déjà utilisé..."
	print "Test avec le port de secours..."
	try:
		mySocket.bind((HOST,9999))
	except socket.error:
		print "La liaison du socket a l'addrese choisie a échoué..."
		sys.exit()
print "Serveur en attente de connections..."
mySocket.listen(5)

#--------------------------
# Attente et prise en charge des connections entrantes

while 1:
	try:
		connection, adresse = mySocket.accept()
		# Creation du thread
		if adresse not in variables.ipban:
			th=ThreadClient(connection)
			th.start()
			
			# Memorisation de la connection
			it=th.getName()
			variables.conn_clients[it]=connection
			variables.clients_ip[it]=adresse
			variables.threads[it]=th

			print "Client %s connecté [%s] " % (it,adresse[0])
			
			# Dialogue
			connection.send("Vous etes connecté ")
	except:
		print "\n Connection Over"
		for it in variables.conn_clients:
			th=variables.conn_clients[it]
			th.connection.shutdown(socket.SHUT_RDWR)
			th.close()
		break