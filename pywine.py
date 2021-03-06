#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.3 on Mon May 23 13:04:29 2011

import wx

# begin wxGlade: extracode
# end wxGlade



class pyWine(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: pyWine.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.wineView = wx.ListCtrl(self, -1, style=wx.LC_REPORT|wx.SUNKEN_BORDER)

        # Here is a list that can be reused later
        cs = ["ワイン", "ワイナリー", "グレープの種類", "製造年"]
        # Add all ot the List Columns to the wineView
        [self.wineView.InsertColumn(cs.index(heading), heading) for heading in cs]

        # Menu Bar
        self.wine_menubar = wx.MenuBar()
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(wx.NewId(), u"ワイン", "", wx.ITEM_NORMAL)
        self.wine_menubar.Append(wxglade_tmp_menu, u"追加")
        self.SetMenuBar(self.wine_menubar)
        # Menu Bar end

        # Tool Bar
        self.wine_toolbar = wx.ToolBar(self, -1)
        self.SetToolBar(self.wine_toolbar)
        self.wine_toolbar.AddLabelTool(wx.NewId(), "Add Wine", wx.Bitmap("/usr/share/icons/gnome/24x24/actions/gtk-add.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, "", "")
        # Tool Bar end
        self.wine_statusbar = self.CreateStatusBar(1, 0)

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_MENU, self.on_AddWine, id=-1)
        self.Bind(wx.EVT_TOOL, self.on_AddWine, id=-1)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: pyWine.__set_properties
        self.SetTitle("PyWine")
        self.SetSize((640, 480))
        self.wine_toolbar.Realize()
        self.wine_statusbar.SetStatusWidths([-1])
        # statusbar fields
        wine_statusbar_fields = ["wine_statusbar"]
        for i in range(len(wine_statusbar_fields)):
            self.wine_statusbar.SetStatusText(wine_statusbar_fields[i], i)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: pyWine.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_1.Add(self.wineView, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        self.Layout()
        # end wxGlade

    def on_AddWine(self, event): # wxGlade: pyWine.<event_handler>
        """Called when the use wants to add a wine"""
        #Create the dialog, show it, and store the results
        wineDlg = wineDialog(None, -1, "")
        result, newWine = wineDlg.ShowModal(), wineDlg.run()

        if result == wx.ID_OK:
            """The user clicked Ok, so let's add this
            wine to the wine list"""
            self.wineView.Append(newWine.getList())

        wineDlg.Destroy()

# end of class pyWine


class wineDialog(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: wineDialog.__init__
        kwds["style"] = wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)
        self.label_1 = wx.StaticText(self, -1, u"ワイン")
        self.enWine = wx.TextCtrl(self, -1, "")
        self.label_2 = wx.StaticText(self, -1, u"ワイナリー")
        self.enWinery = wx.TextCtrl(self, -1, "")
        self.label_3 = wx.StaticText(self, -1, u"グレープの種類")
        self.enGrape = wx.TextCtrl(self, -1, "")
        self.label_4 = wx.StaticText(self, -1, u"製造年")
        self.enYear = wx.TextCtrl(self, -1, "")
        self.Cancel = wx.Button(self, wx.ID_CANCEL, "")
        self.OK = wx.Button(self, wx.ID_OK, "")

        #setup the wine that we will return
        self.wine = Wine()              # ここだけ付け加えた

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: wineDialog.__set_properties
        self.SetTitle("Add Wine")
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: wineDialog.__do_layout
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        grid_sizer_1 = wx.GridSizer(4, 2, 0, 0)
        grid_sizer_1.Add(self.label_1, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_1.Add(self.enWine, 0, wx.ALL|wx.EXPAND, 3)
        grid_sizer_1.Add(self.label_2, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_1.Add(self.enWinery, 0, wx.ALL|wx.EXPAND, 3)
        grid_sizer_1.Add(self.label_3, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_1.Add(self.enGrape, 0, wx.ALL|wx.EXPAND, 3)
        grid_sizer_1.Add(self.label_4, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_1.Add(self.enYear, 0, wx.ALL|wx.EXPAND, 3)
        sizer_2.Add(grid_sizer_1, 4, wx.EXPAND, 0)
        sizer_3.Add((100, 30), 0, 0, 0)
        sizer_3.Add(self.Cancel, 0, 0, 0)
        sizer_3.Add(self.OK, 0, 0, 0)
        sizer_2.Add(sizer_3, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_2)
        sizer_2.Fit(self)
        self.Layout()
        # end wxGlade

    def run(self):
        # get the velue of the entry fields
        self.wine.wine = self.enWine.GetValue().encode('utf_8')
        self.wine.winery = self.enWinery.GetValue().encode('utf_8')
        self.wine.grape = self.enGrape.GetValue().encode('utf_8')
        self.wine.year = self.enYear.GetValue().encode('utf_8')

        return self.wine

# end of class wineDialog

class Wine:
    """This class represents all the wine information"""

    def __init__(self, wine = "", winery = "", grape = "", year = ""):
        self.wine, self.winery, self.grape, self.year = wine, winery, grape, year

    def getList(self):
        """This method returns a list made up of the
        wine information. It is used to add a wine to the
        wineList easily"""
        return [unicode(i, "utf_8") for i in [self.wine, self.winery, self.grape, self.year]]

# end of class Wine 

if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    wine = pyWine(None, -1, "")
    app.SetTopWindow(wine)
    wine.Show()
    app.MainLoop()
