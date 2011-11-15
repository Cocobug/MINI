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
#    along with YASMS. If not, see <http://www.gnu.org/licenses/>.
#
#########################################################

#======================+
#  Modules             |
#----------------------+
from random import randint

#----------------------+
# Variables            |
#- - - - - - - - - - - +

#----------------------+
# Initialisation       |
#- - - - - - - - - - - +

def init_NETvars():
	"""Initialisation des variables connection."""
	P_Def=8080
	HOST=raw_input("Entrez l'addrese du server : ")
	PORT=raw_input("Entrez le port [Default:"+str(P_Def)+"]: ")
	PORT=force(PORT,P_Def)
	PORT=int(PORT)
	return (HOST,PORT)

def force(var, def_var):
	if var=='':
		var=def_var
	return var
