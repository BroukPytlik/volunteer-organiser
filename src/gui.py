#!/usr/bin/env python3
# vim: set noexpandtab cindent sw=4 ts=4:
#
# (C)2014 Jan Tulak <jan@tulak.me>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Sep 12 2010)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.grid

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 1000,700 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		#self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_notebook1 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pane_roster = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer5 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText3 = wx.StaticText( self.pane_roster, wx.ID_ANY, u"Birthdays", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		bSizer5.Add( self.m_staticText3, 0, wx.ALL, 5 )
		
		bSizer3.Add( bSizer5, 1, wx.EXPAND, 5 )
		
		self.m_staticline1 = wx.StaticLine( self.pane_roster, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer3.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer6 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText2 = wx.StaticText( self.pane_roster, wx.ID_ANY, u"Notes, services today", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		bSizer6.Add( self.m_staticText2, 0, wx.ALL, 5 )
		
		bSizer3.Add( bSizer6, 1, wx.EXPAND, 5 )
		
		bSizer2.Add( bSizer3, 1, wx.EXPAND, 5 )
		
		self.m_staticline2 = wx.StaticLine( self.pane_roster, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer2.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText4 = wx.StaticText( self.pane_roster, wx.ID_ANY, u"Services", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		bSizer4.Add( self.m_staticText4, 0, wx.ALL, 5 )
		
		self.m_grid1 = wx.grid.Grid( self.pane_roster, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.m_grid1.CreateGrid( 5, 5 )
		self.m_grid1.EnableEditing( True )
		self.m_grid1.EnableGridLines( True )
		self.m_grid1.EnableDragGridSize( False )
		self.m_grid1.SetMargins( 0, 0 )
		
		# Columns
		self.m_grid1.EnableDragColMove( False )
		self.m_grid1.EnableDragColSize( True )
		self.m_grid1.SetColLabelSize( 30 )
		self.m_grid1.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.m_grid1.EnableDragRowSize( True )
		self.m_grid1.SetRowLabelSize( 80 )
		self.m_grid1.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.m_grid1.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer4.Add( self.m_grid1, 0, wx.ALL, 5 )
		
		self.m_button1 = wx.Button( self.pane_roster, wx.ID_ANY, u"Add service", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.m_button1, 0, wx.ALL, 5 )
		
		self.m_button2 = wx.Button( self.pane_roster, wx.ID_ANY, u"Edit service", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.m_button2, 0, wx.ALL, 5 )
		
		self.m_button3 = wx.Button( self.pane_roster, wx.ID_ANY, u"Remove service", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.m_button3, 0, wx.ALL, 5 )
		
		bSizer2.Add( bSizer4, 1, wx.EXPAND, 5 )
		
		self.pane_roster.SetSizer( bSizer2 )
		self.pane_roster.Layout()
		bSizer2.Fit( self.pane_roster )
		self.m_notebook1.AddPage( self.pane_roster, u"Roster", False )
		self.pane_volunteers = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer8 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText5 = wx.StaticText( self.pane_volunteers, wx.ID_ANY, u"Volunteers List", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		bSizer8.Add( self.m_staticText5, 0, wx.ALL, 5 )
		
		m_listBox1Choices = []
		self.m_listBox1 = wx.ListBox( self.pane_volunteers, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox1Choices, 0 )
		bSizer8.Add( self.m_listBox1, 0, wx.ALL, 5 )
		
		self.m_checkBox1 = wx.CheckBox( self.pane_volunteers, wx.ID_ANY, u"Currently employed only", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.m_checkBox1, 0, wx.ALL, 5 )
		
		self.m_grid2 = wx.grid.Grid( self.pane_volunteers, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.m_grid2.CreateGrid( 5, 5 )
		self.m_grid2.EnableEditing( True )
		self.m_grid2.EnableGridLines( True )
		self.m_grid2.EnableDragGridSize( False )
		self.m_grid2.SetMargins( 0, 0 )
		
		# Columns
		self.m_grid2.EnableDragColMove( False )
		self.m_grid2.EnableDragColSize( True )
		self.m_grid2.SetColLabelSize( 30 )
		self.m_grid2.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.m_grid2.EnableDragRowSize( True )
		self.m_grid2.SetRowLabelSize( 80 )
		self.m_grid2.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.m_grid2.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer8.Add( self.m_grid2, 0, wx.ALL, 5 )
		
		self.btn_new_volunteer = wx.Button( self.pane_volunteers, wx.ID_ANY, u"New", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.btn_new_volunteer, 0, wx.ALL, 5 )
		
		bSizer7.Add( bSizer8, 1, wx.EXPAND, 5 )
		
		self.m_staticline3 = wx.StaticLine( self.pane_volunteers, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer7.Add( self.m_staticline3, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer9 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_grid3 = wx.grid.Grid( self.pane_volunteers, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.m_grid3.CreateGrid( 5, 5 )
		self.m_grid3.EnableEditing( True )
		self.m_grid3.EnableGridLines( True )
		self.m_grid3.EnableDragGridSize( False )
		self.m_grid3.SetMargins( 0, 0 )
		
		# Columns
		self.m_grid3.EnableDragColMove( False )
		self.m_grid3.EnableDragColSize( True )
		self.m_grid3.SetColLabelSize( 30 )
		self.m_grid3.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.m_grid3.EnableDragRowSize( True )
		self.m_grid3.SetRowLabelSize( 80 )
		self.m_grid3.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.m_grid3.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer9.Add( self.m_grid3, 0, wx.ALL, 5 )
		
		self.btn_edit_volunteer = wx.Button( self.pane_volunteers, wx.ID_ANY, u"Edit", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.btn_edit_volunteer, 0, wx.ALL, 5 )
		
		bSizer7.Add( bSizer9, 1, wx.EXPAND, 5 )
		
		self.pane_volunteers.SetSizer( bSizer7 )
		self.pane_volunteers.Layout()
		bSizer7.Fit( self.pane_volunteers )
		self.m_notebook1.AddPage( self.pane_volunteers, u"Volunteers", False )
		self.pane_patients = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer71 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer81 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText51 = wx.StaticText( self.pane_patients, wx.ID_ANY, u"Patients List", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText51.Wrap( -1 )
		bSizer81.Add( self.m_staticText51, 0, wx.ALL, 5 )
		
		m_listBox11Choices = []
		self.m_listBox11 = wx.ListBox( self.pane_patients, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox11Choices, 0 )
		bSizer81.Add( self.m_listBox11, 0, wx.ALL, 5 )
		
		self.m_grid21 = wx.grid.Grid( self.pane_patients, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.m_grid21.CreateGrid( 5, 5 )
		self.m_grid21.EnableEditing( True )
		self.m_grid21.EnableGridLines( True )
		self.m_grid21.EnableDragGridSize( False )
		self.m_grid21.SetMargins( 0, 0 )
		
		# Columns
		self.m_grid21.EnableDragColMove( False )
		self.m_grid21.EnableDragColSize( True )
		self.m_grid21.SetColLabelSize( 30 )
		self.m_grid21.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.m_grid21.EnableDragRowSize( True )
		self.m_grid21.SetRowLabelSize( 80 )
		self.m_grid21.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.m_grid21.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer81.Add( self.m_grid21, 0, wx.ALL, 5 )
		
		self.btn_new_patient = wx.Button( self.pane_patients, wx.ID_ANY, u"New", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer81.Add( self.btn_new_patient, 0, wx.ALL, 5 )
		
		bSizer71.Add( bSizer81, 1, wx.EXPAND, 5 )
		
		self.m_staticline31 = wx.StaticLine( self.pane_patients, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer71.Add( self.m_staticline31, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer91 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_grid31 = wx.grid.Grid( self.pane_patients, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.m_grid31.CreateGrid( 5, 5 )
		self.m_grid31.EnableEditing( True )
		self.m_grid31.EnableGridLines( True )
		self.m_grid31.EnableDragGridSize( False )
		self.m_grid31.SetMargins( 0, 0 )
		
		# Columns
		self.m_grid31.EnableDragColMove( False )
		self.m_grid31.EnableDragColSize( True )
		self.m_grid31.SetColLabelSize( 30 )
		self.m_grid31.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.m_grid31.EnableDragRowSize( True )
		self.m_grid31.SetRowLabelSize( 80 )
		self.m_grid31.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.m_grid31.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer91.Add( self.m_grid31, 0, wx.ALL, 5 )
		
		self.btn_edit_patient = wx.Button( self.pane_patients, wx.ID_ANY, u"Edit", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer91.Add( self.btn_edit_patient, 0, wx.ALL, 5 )
		
		bSizer71.Add( bSizer91, 1, wx.EXPAND, 5 )
		
		self.pane_patients.SetSizer( bSizer71 )
		self.pane_patients.Layout()
		bSizer71.Fit( self.pane_patients )
		self.m_notebook1.AddPage( self.pane_patients, u"Patients", False )
		
		bSizer1.Add( self.m_notebook1, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.SetSizer( bSizer1 )
		self.Layout()
		self.m_menubar1 = wx.MenuBar( 0 )
		self.menu_file = wx.Menu()
		self.menuItem_exit = wx.MenuItem( self.menu_file, wx.ID_EXIT, u"Exit"+ u"\t" + u"x", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_file.Append( self.menuItem_exit )
		
		self.menuItem_about = wx.MenuItem( self.menu_file, wx.ID_ABOUT, u"About", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_file.Append( self.menuItem_about )
		
		self.m_menubar1.Append( self.menu_file, u"File" ) 
		
		self.SetMenuBar( self.m_menubar1 )
		
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	


