#!/usr/bin/env python
# encoding: utf-8

#######################################################
# MINI - MINI Is Not Irc
# [CONFIG]
#######################################################
#
#	This file is part of MINI.
#
#	MINI is free software: you can redistribute it and/or modify
#	it under the terms of the GNU General Public License as published by
#	the Free Software Foundation, either version 3 of the License, or
#	(at your option) any later version.
#
#	Gomoku is distributed in the hope that it will be useful,
#	but WITHOUT ANY WARRANTY; without even the implied warranty of
#	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#	GNU General Public License for more details.
#
#	You should have received a copy of the GNU General Public License
#	along with MINI.  If not, see <http://www.gnu.org/licenses/>.
#
#########################################################

#======================+
#  Modules 			|
#----------------------+
import cPickle,os,sys,hashlib

#----------------------+
# Variables			|
#- - - - - - - - - - - +

#----------------------+
# Fonctions			|
#- - - - - - - - - - - +

#----------------------
# Moderation
#-----
def Moderation_kick(caller,variables,client,arguments,message):
	"Ejecter un utilisateur penible : 298426e82362e35b591419aa013564eb"
	if len(arguments)<2: return False
	message=message[len(arguments[0]+arguments[1])+3:]
	if message=='': message='For no reason'
	Id=System_findId(arguments[1],variables)
	print Id, client
	# Fermeture de la connection
	print 'Client déconnecté (kicked)'
	variables.threads[Id].msg('ALL', 'Client %s déconnecté (kicked: %s)'%(client,message))
	caller.msg(Id,"You've been kicked ! (%s)"%message)
	caller.msg(Id,'EOF')
	variables.threads[Id].connection.close()
	#variables.threads[Id]._Thread__stop()
	del variables.conn_clients[Id]
	del variables.clients_ip[Id]
	# Le thread se termine ici
def Moderation_ban(caller,variables,client,arguments,message):
	"Bannir un utilisateur penible : e2d0c6d0101801efc7b183e960a00f01"
	if len(arguments)<2: return False
	if variables.clients_privileges[client]==0:
		print 'Looser'
		return False
	Id=System_findId(arguments[1],variables)
	# Fermeture de la connection
	print 'Client déconnecté (banned)'
	caller.msg('ALL', 'Client %s déconnecté (banned: %s)'%(client,message))
	variables.threads[Id].connection.close()
	del variables.conn_clients[Id]
	variables.ipban+=[variables.clients_ip[Id]]
	# Le thread se termine ici

#---------------------------
# Classes
#----#
