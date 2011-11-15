# -*- coding:latin-1 -*-

#####################################
# Date: 05/04/10                    #
# Auteur: Rigaut Maximilien         #
# Nom: Packer                       #
# Version: 1.0                      #
# Copyright 2010: Rigaut Maximilien #
#####################################
#    This file is part of YASMS.
#
#    YASMS is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    YASMS is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with YASMS. If not, see <http://www.gnu.org/licenses/>.
#################################

from tarfile import open
import os

nom="YASMS"
v=raw_input("Version du programme: ")
nom=nom+'_All '+v+'.tar.gz'
tFile= open(nom,'w:gz')
fichiers=os.listdir('.')
fichiers.pop(fichiers.index('Archives'))
for fichier in fichiers:
    tFile.add(fichier,fichier,True)
tFile.close()
os.rename(nom,'./Archives/'+nom)