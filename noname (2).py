# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 694,400 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.Size( 600,400 ), wx.Size( 800,500 ) )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Порт:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		bSizer4.Add( self.m_staticText5, 1, wx.ALL, 5 )
		
		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Скорость:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		bSizer4.Add( self.m_staticText6, 1, wx.ALL, 5 )
		
		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Четность:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		bSizer4.Add( self.m_staticText7, 1, wx.ALL, 5 )
		
		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"Кол-во стоп бит:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )
		bSizer4.Add( self.m_staticText8, 1, wx.ALL, 5 )
		
		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )
		bSizer4.Add( self.m_staticText9, 1, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer4, 0, wx.EXPAND, 5 )
		
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		m_comboBox1Choices = []
		self.m_comboBox1 = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, m_comboBox1Choices, 0 )
		self.m_comboBox1.SetSelection( 0 )
		bSizer2.Add( self.m_comboBox1, 1, wx.ALL, 5 )
		
		m_comboBox2Choices = [ u"9600", u"19200", u"38400", u"57600", u"115200" ]
		self.m_comboBox2 = wx.ComboBox( self, wx.ID_ANY, u"9600", wx.DefaultPosition, wx.DefaultSize, m_comboBox2Choices, 0 )
		self.m_comboBox2.SetSelection( 4 )
		self.m_comboBox2.Enable( False )
		
		bSizer2.Add( self.m_comboBox2, 1, wx.ALL, 5 )
		
		m_comboBox3Choices = [ u"NONE", u"EVEN", u"ODD" ]
		self.m_comboBox3 = wx.ComboBox( self, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, m_comboBox3Choices, 0 )
		self.m_comboBox3.SetSelection( 1 )
		self.m_comboBox3.Enable( False )
		
		bSizer2.Add( self.m_comboBox3, 1, wx.ALL, 5 )
		
		m_comboBox4Choices = [ u"1", u"2" ]
		self.m_comboBox4 = wx.ComboBox( self, wx.ID_ANY, u"1 stop bit", wx.DefaultPosition, wx.DefaultSize, m_comboBox4Choices, 0 )
		self.m_comboBox4.SetSelection( 0 )
		self.m_comboBox4.Enable( False )
		
		bSizer2.Add( self.m_comboBox4, 1, wx.ALL, 5 )
		
		self.m_toggleBtn2 = wx.ToggleButton( self, wx.ID_ANY, u"COM-port", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_toggleBtn2, 1, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer2, 0, wx.EXPAND, 5 )
		
		self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer1.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_RICH )
		bSizer1.Add( self.m_textCtrl1, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticline2 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer1.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Файл не выбран", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		bSizer1.Add( self.m_staticText1, 0, wx.ALL, 5 )
		
		self.m_gauge1 = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.m_gauge1.SetValue( 0 ) 
		bSizer1.Add( self.m_gauge1, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticline3 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer1.Add( self.m_staticline3, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button61 = wx.Button( self, wx.ID_ANY, u"Считать CPU", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_button61, 0, wx.ALL, 5 )
		
		self.m_button6 = wx.Button( self, wx.ID_ANY, u"Записать KeyWod", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_button6, 1, wx.EXPAND|wx.ALL, 5 )
		
		self.m_button7 = wx.Button( self, wx.ID_ANY, u"Стереть KeyWod", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_button7, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_button8 = wx.Button( self, wx.ID_ANY, u"RESET", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_button8, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticline4 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL|wx.LI_VERTICAL )
		bSizer3.Add( self.m_staticline4, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_button4 = wx.Button( self, wx.ID_ANY, u"Выбрать файл", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_button4, 1, wx.ALL|wx.RIGHT|wx.EXPAND, 5 )
		
		self.m_button5 = wx.Button( self, wx.ID_ANY, u"Прошить", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_button5, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText71 = wx.StaticText( self, wx.ID_ANY, u"v1.1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText71.Wrap( -1 )
		bSizer3.Add( self.m_staticText71, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer3, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_toggleBtn2.Bind( wx.EVT_TOGGLEBUTTON, self.ConnectToComPort )
		self.m_button61.Bind( wx.EVT_BUTTON, self.ReadCpuName )
		self.m_button6.Bind( wx.EVT_BUTTON, self.SetKeyWord )
		self.m_button7.Bind( wx.EVT_BUTTON, self.ResetKeyWord )
		self.m_button8.Bind( wx.EVT_BUTTON, self.RESET_MCU )
		self.m_button4.Bind( wx.EVT_BUTTON, self.FilDialogOpen )
		self.m_button5.Bind( wx.EVT_BUTTON, self.FlashStart )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def ConnectToComPort( self, event ):
		event.Skip()
	
	def ReadCpuName( self, event ):
		event.Skip()
	
	def SetKeyWord( self, event ):
		event.Skip()
	
	def ResetKeyWord( self, event ):
		event.Skip()
	
	def RESET_MCU( self, event ):
		event.Skip()
	
	def FilDialogOpen( self, event ):
		event.Skip()
	
	def FlashStart( self, event ):
		event.Skip()
	

