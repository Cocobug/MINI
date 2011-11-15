#!/usr/bin/env python
# encoding: utf-8

#######################################################
# MINI - MINI Is Not Irc
# [CONFIG]
#######################################################
#
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
#@
#########################################################

#======================+
#  Modules             |
#----------------------+
from random import randint

#----------------------+
# Initialisation       |
#- - - - - - - - - - - +

def init_NETvars():
	"""Initialisation des variables connection."""
	H_Def="127.0.0.1"
	P_Def=8080
	Nom_Def='Invité'+str(randint(1,10000))
	Nom=raw_input("Entrez un nom [Default:%s]: "%Nom_Def)
	HOST=raw_input("Entrez l'addrese du server [Defaut:"+H_Def+"]: ")
	PORT=raw_input("Entrez le port [Default:"+str(P_Def)+"]: ")
	Nom=force(Nom,Nom_Def)
	HOST=force(HOST,H_Def)
	PORT=force(PORT,P_Def)
	PORT=int(PORT)
	return (HOST,PORT,Nom)

def force(var, def_var):
	if var=='':
		var=def_var
	return var
