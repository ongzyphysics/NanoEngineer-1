# Copyright 2004-2007 Nanorex, Inc.  See LICENSE file for details. 
"""
$Id: Ui_BuildStructuresToolBar.py 12416 2008-04-09 05:40:41Z marksims $
"""

from PyQt4 import QtGui
from foundation.wiki_help import QToolBar_WikiHelp
from utilities.debug_prefs import debug_pref, Choice_boolean_True

def setupUi(win, toolbarArea):
    """
    Creates and populates the "Build Structures" toolbar in the main window.

    @param win: NE1's main window object.
    @type  win: U{B{QMainWindow}<http://doc.trolltech.com/4/qmainwindow.html>}
    """
    
    # Create the "Build Structures" toolbar.
    win.buildStructuresToolBar = QToolBar_WikiHelp(win)
    win.buildStructuresToolBar.setEnabled(True)
    win.buildStructuresToolBar.setObjectName("buildStructuresToolBar")
    win.addToolBar(toolbarArea, win.buildStructuresToolBar)
    
    # Populate the "Build Structures" toolbar.
    # Begin with "Builders", then add single shot "Generators".
    win.buildStructuresToolBar.addAction(win.toolsDepositAtomAction)
    win.buildStructuresToolBar.addAction(win.buildDnaAction)
    
    #  New Nanotube Builder or old Nanotube Generator?
    if debug_pref("Use new 'Build > Nanotube' builder? (next session)", 
                  Choice_boolean_True, 
                  prefs_key = "A10 devel/Old Nanotube Generator"):
        # New "Build > CNT", experimental. --Mark 2008-03-10
        win.buildStructuresToolBar.addAction(win.buildNanotubeAction) 
    else:
        # Original "Build > Nanotube"
        win.buildStructuresToolBar.addAction(win.nanotubeGeneratorAction)
        
    win.buildStructuresToolBar.addAction(win.toolsCookieCutAction)
    
    win.buildStructuresToolBar.addSeparator() # Generators after this.
    
    # This adds the Peptide Generator (piotr 080304)
    win.buildStructuresToolBar.addAction(win.insertPeptideAction)
    win.buildStructuresToolBar.addAction(win.insertGrapheneAction)
    
    # This adds the Atom Generator example for developers.
    win.buildStructuresToolBar.addAction(win.insertAtomAction)

def retranslateUi(win):
    """
    Assigns the I{window title} property of the "Build Structures" toolbar.
    
    The window title of the "Build Structures" toolbar will be displayed in the
    popup menu under "View > Toolbars".
    """
    win.buildStructuresToolBar.setWindowTitle(
        QtGui.QApplication.translate(
            "MainWindow", "Build Structures", 
            None, QtGui.QApplication.UnicodeUTF8))
    win.buildStructuresToolBar.setToolTip(
        QtGui.QApplication.translate(
            "MainWindow", "Build Structures Toolbar", 
            None, QtGui.QApplication.UnicodeUTF8))
