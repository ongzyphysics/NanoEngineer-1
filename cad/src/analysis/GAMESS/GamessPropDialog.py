# -*- coding: utf-8 -*-

# Copyright 2005-2007 Nanorex, Inc.  See LICENSE file for details. 
# Form implementation generated from reading ui file 'C:\Atom\qt4\cad\src\GamessPropDialog.ui'
#
# Created: Fri May 04 10:49:03 2007
#      by: PyQt4 UI code generator 4.1.1
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt4 import QtCore, QtGui

class Ui_GamessPropDialog(object):
    def setupUi(self, GamessPropDialog):
        GamessPropDialog.setObjectName("GamessPropDialog")
        GamessPropDialog.resize(QtCore.QSize(QtCore.QRect(0,0,450,512).size()).expandedTo(GamessPropDialog.minimumSizeHint()))

        self.gridlayout = QtGui.QGridLayout(GamessPropDialog)
        self.gridlayout.setMargin(9)
        self.gridlayout.setSpacing(6)
        self.gridlayout.setObjectName("gridlayout")

        self.gridlayout1 = QtGui.QGridLayout()
        self.gridlayout1.setMargin(0)
        self.gridlayout1.setSpacing(6)
        self.gridlayout1.setObjectName("gridlayout1")

        self.runtyp_combox = QtGui.QComboBox(GamessPropDialog)
        self.runtyp_combox.setObjectName("runtyp_combox")
        self.gridlayout1.addWidget(self.runtyp_combox,1,1,1,1)

        spacerItem = QtGui.QSpacerItem(231,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.gridlayout1.addItem(spacerItem,1,2,1,2)

        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setMargin(0)
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setObjectName("hboxlayout")

        self.jig_color_pixmap = QtGui.QLabel(GamessPropDialog)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(5),QtGui.QSizePolicy.Policy(5))
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.jig_color_pixmap.sizePolicy().hasHeightForWidth())
        self.jig_color_pixmap.setSizePolicy(sizePolicy)
        self.jig_color_pixmap.setMinimumSize(QtCore.QSize(40,0))
        self.jig_color_pixmap.setScaledContents(True)
        self.jig_color_pixmap.setObjectName("jig_color_pixmap")
        self.hboxlayout.addWidget(self.jig_color_pixmap)

        self.choose_color_btn = QtGui.QPushButton(GamessPropDialog)
        self.choose_color_btn.setEnabled(True)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(1),QtGui.QSizePolicy.Policy(0))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.choose_color_btn.sizePolicy().hasHeightForWidth())
        self.choose_color_btn.setSizePolicy(sizePolicy)
        self.choose_color_btn.setAutoDefault(False)
        self.choose_color_btn.setObjectName("choose_color_btn")
        self.hboxlayout.addWidget(self.choose_color_btn)
        self.gridlayout1.addLayout(self.hboxlayout,3,1,1,2)

        self.vboxlayout = QtGui.QVBoxLayout()
        self.vboxlayout.setMargin(0)
        self.vboxlayout.setSpacing(6)
        self.vboxlayout.setObjectName("vboxlayout")

        self.psetslbl_2_2 = QtGui.QLabel(GamessPropDialog)
        self.psetslbl_2_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.psetslbl_2_2.setObjectName("psetslbl_2_2")
        self.vboxlayout.addWidget(self.psetslbl_2_2)

        self.textLabel1_2_3 = QtGui.QLabel(GamessPropDialog)
        self.textLabel1_2_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.textLabel1_2_3.setObjectName("textLabel1_2_3")
        self.vboxlayout.addWidget(self.textLabel1_2_3)

        self.textLabel1_3 = QtGui.QLabel(GamessPropDialog)
        self.textLabel1_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.textLabel1_3.setObjectName("textLabel1_3")
        self.vboxlayout.addWidget(self.textLabel1_3)

        self.textLabel1_3_2 = QtGui.QLabel(GamessPropDialog)
        self.textLabel1_3_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.textLabel1_3_2.setObjectName("textLabel1_3_2")
        self.vboxlayout.addWidget(self.textLabel1_3_2)
        self.gridlayout1.addLayout(self.vboxlayout,0,0,4,1)

        self.name_linedit = QtGui.QLineEdit(GamessPropDialog)
        self.name_linedit.setObjectName("name_linedit")
        self.gridlayout1.addWidget(self.name_linedit,0,1,1,3)

        self.comment_linedit = QtGui.QLineEdit(GamessPropDialog)
        self.comment_linedit.setMaxLength(80)
        self.comment_linedit.setObjectName("comment_linedit")
        self.gridlayout1.addWidget(self.comment_linedit,2,1,1,3)

        spacerItem1 = QtGui.QSpacerItem(191,25,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.gridlayout1.addItem(spacerItem1,3,3,1,1)
        self.gridlayout.addLayout(self.gridlayout1,0,0,1,5)

        self.hboxlayout1 = QtGui.QHBoxLayout()
        self.hboxlayout1.setMargin(0)
        self.hboxlayout1.setSpacing(6)
        self.hboxlayout1.setObjectName("hboxlayout1")

        self.scftyp_grpbox = QtGui.QGroupBox(GamessPropDialog)
        self.scftyp_grpbox.setObjectName("scftyp_grpbox")

        self.gridlayout2 = QtGui.QGridLayout(self.scftyp_grpbox)
        self.gridlayout2.setMargin(9)
        self.gridlayout2.setSpacing(6)
        self.gridlayout2.setObjectName("gridlayout2")

        self.hboxlayout2 = QtGui.QHBoxLayout()
        self.hboxlayout2.setMargin(0)
        self.hboxlayout2.setSpacing(6)
        self.hboxlayout2.setObjectName("hboxlayout2")

        self.rhf_radiobtn = QtGui.QRadioButton(self.scftyp_grpbox)
        self.rhf_radiobtn.setChecked(True)
        self.rhf_radiobtn.setObjectName("rhf_radiobtn")
        self.hboxlayout2.addWidget(self.rhf_radiobtn)

        self.uhf_radiobtn = QtGui.QRadioButton(self.scftyp_grpbox)
        self.uhf_radiobtn.setObjectName("uhf_radiobtn")
        self.hboxlayout2.addWidget(self.uhf_radiobtn)

        self.rohf_radiobtn = QtGui.QRadioButton(self.scftyp_grpbox)
        self.rohf_radiobtn.setObjectName("rohf_radiobtn")
        self.hboxlayout2.addWidget(self.rohf_radiobtn)
        self.gridlayout2.addLayout(self.hboxlayout2,0,0,1,1)

        self.hboxlayout3 = QtGui.QHBoxLayout()
        self.hboxlayout3.setMargin(0)
        self.hboxlayout3.setSpacing(6)
        self.hboxlayout3.setObjectName("hboxlayout3")

        self.textLabel1_4 = QtGui.QLabel(self.scftyp_grpbox)
        self.textLabel1_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.textLabel1_4.setObjectName("textLabel1_4")
        self.hboxlayout3.addWidget(self.textLabel1_4)

        self.icharg_spinbox = QtGui.QSpinBox(self.scftyp_grpbox)
        self.icharg_spinbox.setMaximum(1)
        self.icharg_spinbox.setMinimum(-1)
        self.icharg_spinbox.setObjectName("icharg_spinbox")
        self.hboxlayout3.addWidget(self.icharg_spinbox)

        self.textLabel1_2_2 = QtGui.QLabel(self.scftyp_grpbox)
        self.textLabel1_2_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.textLabel1_2_2.setObjectName("textLabel1_2_2")
        self.hboxlayout3.addWidget(self.textLabel1_2_2)

        self.multi_combox = QtGui.QComboBox(self.scftyp_grpbox)
        self.multi_combox.setObjectName("multi_combox")
        self.hboxlayout3.addWidget(self.multi_combox)
        self.gridlayout2.addLayout(self.hboxlayout3,1,0,1,1)
        self.hboxlayout1.addWidget(self.scftyp_grpbox)

        self.groupBox8 = QtGui.QGroupBox(GamessPropDialog)
        self.groupBox8.setObjectName("groupBox8")

        self.gridlayout3 = QtGui.QGridLayout(self.groupBox8)
        self.gridlayout3.setMargin(9)
        self.gridlayout3.setSpacing(6)
        self.gridlayout3.setObjectName("gridlayout3")

        self.hboxlayout4 = QtGui.QHBoxLayout()
        self.hboxlayout4.setMargin(0)
        self.hboxlayout4.setSpacing(6)
        self.hboxlayout4.setObjectName("hboxlayout4")

        self.textLabel2_2 = QtGui.QLabel(self.groupBox8)
        self.textLabel2_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.textLabel2_2.setObjectName("textLabel2_2")
        self.hboxlayout4.addWidget(self.textLabel2_2)

        self.memory_spinbox = QtGui.QSpinBox(self.groupBox8)
        self.memory_spinbox.setMaximum(1024)
        self.memory_spinbox.setMinimum(70)
        self.memory_spinbox.setObjectName("memory_spinbox")
        self.hboxlayout4.addWidget(self.memory_spinbox)

        self.textLabel1 = QtGui.QLabel(self.groupBox8)
        self.textLabel1.setObjectName("textLabel1")
        self.hboxlayout4.addWidget(self.textLabel1)
        self.gridlayout3.addLayout(self.hboxlayout4,0,0,1,1)

        self.dirscf_checkbox = QtGui.QCheckBox(self.groupBox8)
        self.dirscf_checkbox.setChecked(True)
        self.dirscf_checkbox.setObjectName("dirscf_checkbox")
        self.gridlayout3.addWidget(self.dirscf_checkbox,1,0,1,1)
        self.hboxlayout1.addWidget(self.groupBox8)
        self.gridlayout.addLayout(self.hboxlayout1,1,0,1,5)

        self.edit_input_file_cbox = QtGui.QCheckBox(GamessPropDialog)
        self.edit_input_file_cbox.setObjectName("edit_input_file_cbox")
        self.gridlayout.addWidget(self.edit_input_file_cbox,4,0,1,5)

        self.run_job_btn = QtGui.QPushButton(GamessPropDialog)
        self.run_job_btn.setAutoDefault(False)
        self.run_job_btn.setObjectName("run_job_btn")
        self.gridlayout.addWidget(self.run_job_btn,5,2,1,1)

        self.cancel_btn = QtGui.QPushButton(GamessPropDialog)
        self.cancel_btn.setAutoDefault(False)
        self.cancel_btn.setDefault(False)
        self.cancel_btn.setObjectName("cancel_btn")
        self.gridlayout.addWidget(self.cancel_btn,5,4,1,1)

        self.save_btn = QtGui.QPushButton(GamessPropDialog)
        self.save_btn.setAutoDefault(False)
        self.save_btn.setObjectName("save_btn")
        self.gridlayout.addWidget(self.save_btn,5,3,1,1)

        spacerItem2 = QtGui.QSpacerItem(121,27,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.gridlayout.addItem(spacerItem2,5,1,1,1)

        self.whats_this_btn = QtGui.QToolButton(GamessPropDialog)
        self.whats_this_btn.setMinimumSize(QtCore.QSize(30,27))
        self.whats_this_btn.setIcon(QtGui.QIcon("ui/actions/Properties Manager/WhatsThis.png"))
        self.whats_this_btn.setObjectName("whats_this_btn")
        self.gridlayout.addWidget(self.whats_this_btn,5,0,1,1)

        self.groupBox3 = QtGui.QGroupBox(GamessPropDialog)
        self.groupBox3.setObjectName("groupBox3")

        self.gridlayout4 = QtGui.QGridLayout(self.groupBox3)
        self.gridlayout4.setMargin(9)
        self.gridlayout4.setSpacing(6)
        self.gridlayout4.setObjectName("gridlayout4")

        spacerItem3 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.gridlayout4.addItem(spacerItem3,0,3,1,1)

        spacerItem4 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.gridlayout4.addItem(spacerItem4,0,5,1,1)

        self.vboxlayout1 = QtGui.QVBoxLayout()
        self.vboxlayout1.setMargin(0)
        self.vboxlayout1.setSpacing(6)
        self.vboxlayout1.setObjectName("vboxlayout1")

        self.iterations_lbl = QtGui.QLabel(self.groupBox3)
        self.iterations_lbl.setEnabled(False)
        self.iterations_lbl.setObjectName("iterations_lbl")
        self.vboxlayout1.addWidget(self.iterations_lbl)

        self.iterations_spinbox = QtGui.QSpinBox(self.groupBox3)
        self.iterations_spinbox.setEnabled(False)
        self.iterations_spinbox.setProperty("value",QtCore.QVariant(50))
        self.iterations_spinbox.setObjectName("iterations_spinbox")
        self.vboxlayout1.addWidget(self.iterations_spinbox)
        self.gridlayout4.addLayout(self.vboxlayout1,0,4,1,1)

        self.vboxlayout2 = QtGui.QVBoxLayout()
        self.vboxlayout2.setMargin(0)
        self.vboxlayout2.setSpacing(6)
        self.vboxlayout2.setObjectName("vboxlayout2")

        self.rmsd_lbl = QtGui.QLabel(self.groupBox3)
        self.rmsd_lbl.setEnabled(False)
        self.rmsd_lbl.setObjectName("rmsd_lbl")
        self.vboxlayout2.addWidget(self.rmsd_lbl)

        self.rmsd_combox = QtGui.QComboBox(self.groupBox3)
        self.rmsd_combox.setEnabled(False)

        font = QtGui.QFont(self.rmsd_combox.font())
        font.setFamily("Sans Serif")
        font.setPointSize(9)
        font.setWeight(50)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setBold(False)
        self.rmsd_combox.setFont(font)
        self.rmsd_combox.setObjectName("rmsd_combox")
        self.vboxlayout2.addWidget(self.rmsd_combox)
        self.gridlayout4.addLayout(self.vboxlayout2,0,2,1,1)

        spacerItem5 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.gridlayout4.addItem(spacerItem5,0,1,1,1)

        self.vboxlayout3 = QtGui.QVBoxLayout()
        self.vboxlayout3.setMargin(0)
        self.vboxlayout3.setSpacing(6)
        self.vboxlayout3.setObjectName("vboxlayout3")

        self.textLabel3 = QtGui.QLabel(self.groupBox3)
        self.textLabel3.setObjectName("textLabel3")
        self.vboxlayout3.addWidget(self.textLabel3)

        self.density_conv_combox = QtGui.QComboBox(self.groupBox3)
        self.density_conv_combox.setObjectName("density_conv_combox")
        self.vboxlayout3.addWidget(self.density_conv_combox)
        self.gridlayout4.addLayout(self.vboxlayout3,0,0,1,1)
        self.gridlayout.addWidget(self.groupBox3,3,0,1,5)

        self.groupBox2 = QtGui.QGroupBox(GamessPropDialog)
        self.groupBox2.setObjectName("groupBox2")

        self.gridlayout5 = QtGui.QGridLayout(self.groupBox2)
        self.gridlayout5.setMargin(9)
        self.gridlayout5.setSpacing(6)
        self.gridlayout5.setObjectName("gridlayout5")

        self.hboxlayout5 = QtGui.QHBoxLayout()
        self.hboxlayout5.setMargin(0)
        self.hboxlayout5.setSpacing(6)
        self.hboxlayout5.setObjectName("hboxlayout5")

        self.vboxlayout4 = QtGui.QVBoxLayout()
        self.vboxlayout4.setMargin(0)
        self.vboxlayout4.setSpacing(6)
        self.vboxlayout4.setObjectName("vboxlayout4")

        self.checkBox10_3_2 = QtGui.QCheckBox(self.groupBox2)
        self.checkBox10_3_2.setEnabled(False)
        self.checkBox10_3_2.setObjectName("checkBox10_3_2")
        self.vboxlayout4.addWidget(self.checkBox10_3_2)

        self.checkBox10_2_2_2 = QtGui.QCheckBox(self.groupBox2)
        self.checkBox10_2_2_2.setEnabled(False)
        self.checkBox10_2_2_2.setObjectName("checkBox10_2_2_2")
        self.vboxlayout4.addWidget(self.checkBox10_2_2_2)

        self.checkBox35 = QtGui.QCheckBox(self.groupBox2)
        self.checkBox35.setEnabled(False)
        self.checkBox35.setObjectName("checkBox35")
        self.vboxlayout4.addWidget(self.checkBox35)
        self.hboxlayout5.addLayout(self.vboxlayout4)

        self.ecm_grpbox = QtGui.QGroupBox(self.groupBox2)
        self.ecm_grpbox.setObjectName("ecm_grpbox")

        self.vboxlayout5 = QtGui.QVBoxLayout(self.ecm_grpbox)
        self.vboxlayout5.setMargin(11)
        self.vboxlayout5.setSpacing(6)
        self.vboxlayout5.setObjectName("vboxlayout5")

        self.none_radiobtn = QtGui.QRadioButton(self.ecm_grpbox)
        self.none_radiobtn.setChecked(True)
        self.none_radiobtn.setObjectName("none_radiobtn")
        self.vboxlayout5.addWidget(self.none_radiobtn)

        self.dft_radiobtn = QtGui.QRadioButton(self.ecm_grpbox)
        self.dft_radiobtn.setObjectName("dft_radiobtn")
        self.vboxlayout5.addWidget(self.dft_radiobtn)

        self.mp2_radiobtn = QtGui.QRadioButton(self.ecm_grpbox)
        self.mp2_radiobtn.setObjectName("mp2_radiobtn")
        self.vboxlayout5.addWidget(self.mp2_radiobtn)
        self.hboxlayout5.addWidget(self.ecm_grpbox)

        self.vboxlayout6 = QtGui.QVBoxLayout()
        self.vboxlayout6.setMargin(0)
        self.vboxlayout6.setSpacing(6)
        self.vboxlayout6.setObjectName("vboxlayout6")

        self.hboxlayout6 = QtGui.QHBoxLayout()
        self.hboxlayout6.setMargin(0)
        self.hboxlayout6.setSpacing(6)
        self.hboxlayout6.setObjectName("hboxlayout6")

        self.vboxlayout7 = QtGui.QVBoxLayout()
        self.vboxlayout7.setMargin(0)
        self.vboxlayout7.setSpacing(6)
        self.vboxlayout7.setObjectName("vboxlayout7")

        self.dfttyp_label = QtGui.QLabel(self.groupBox2)
        self.dfttyp_label.setEnabled(False)
        self.dfttyp_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.dfttyp_label.setObjectName("dfttyp_label")
        self.vboxlayout7.addWidget(self.dfttyp_label)

        self.gridsize_label = QtGui.QLabel(self.groupBox2)
        self.gridsize_label.setEnabled(False)
        self.gridsize_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.gridsize_label.setObjectName("gridsize_label")
        self.vboxlayout7.addWidget(self.gridsize_label)
        self.hboxlayout6.addLayout(self.vboxlayout7)

        self.vboxlayout8 = QtGui.QVBoxLayout()
        self.vboxlayout8.setMargin(0)
        self.vboxlayout8.setSpacing(6)
        self.vboxlayout8.setObjectName("vboxlayout8")

        self.dfttyp_combox = QtGui.QComboBox(self.groupBox2)
        self.dfttyp_combox.setEnabled(False)
        self.dfttyp_combox.setObjectName("dfttyp_combox")
        self.vboxlayout8.addWidget(self.dfttyp_combox)

        self.gridsize_combox = QtGui.QComboBox(self.groupBox2)
        self.gridsize_combox.setEnabled(False)
        self.gridsize_combox.setObjectName("gridsize_combox")
        self.vboxlayout8.addWidget(self.gridsize_combox)
        self.hboxlayout6.addLayout(self.vboxlayout8)
        self.vboxlayout6.addLayout(self.hboxlayout6)

        self.core_electrons_checkbox = QtGui.QCheckBox(self.groupBox2)
        self.core_electrons_checkbox.setEnabled(False)
        self.core_electrons_checkbox.setObjectName("core_electrons_checkbox")
        self.vboxlayout6.addWidget(self.core_electrons_checkbox)
        self.hboxlayout5.addLayout(self.vboxlayout6)
        self.gridlayout5.addLayout(self.hboxlayout5,1,0,1,1)

        self.hboxlayout7 = QtGui.QHBoxLayout()
        self.hboxlayout7.setMargin(0)
        self.hboxlayout7.setSpacing(6)
        self.hboxlayout7.setObjectName("hboxlayout7")

        self.textLabel6 = QtGui.QLabel(self.groupBox2)
        self.textLabel6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.textLabel6.setObjectName("textLabel6")
        self.hboxlayout7.addWidget(self.textLabel6)

        self.gbasis_combox = QtGui.QComboBox(self.groupBox2)
        self.gbasis_combox.setObjectName("gbasis_combox")
        self.hboxlayout7.addWidget(self.gbasis_combox)

        spacerItem6 = QtGui.QSpacerItem(20,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout7.addItem(spacerItem6)
        self.gridlayout5.addLayout(self.hboxlayout7,0,0,1,1)
        self.gridlayout.addWidget(self.groupBox2,2,0,1,5)

        self.retranslateUi(GamessPropDialog)
        self.runtyp_combox.setCurrentIndex(0)
        self.rmsd_combox.setCurrentIndex(1)
        self.density_conv_combox.setCurrentIndex(1)
        self.gridsize_combox.setCurrentIndex(1)
        self.gbasis_combox.setCurrentIndex(0)
        QtCore.QObject.connect(self.cancel_btn,QtCore.SIGNAL("clicked()"),GamessPropDialog.reject)
        QtCore.QObject.connect(self.save_btn,QtCore.SIGNAL("clicked()"),GamessPropDialog.accept)
        QtCore.QMetaObject.connectSlotsByName(GamessPropDialog)

    def retranslateUi(self, GamessPropDialog):
        
        if sys.platform == "win32":
            gms_str = "PC GAMESS"
        else:
            gms_str = "GAMESS"
        
        GamessPropDialog.setWindowTitle(QtGui.QApplication.translate("GamessPropDialog", gms_str + " Properties", None, QtGui.QApplication.UnicodeUTF8))
        self.runtyp_combox.setToolTip(QtGui.QApplication.translate("GamessPropDialog", "\"Energy\" = Energy Minina, \"Optimization\" = Equilibrium Geometry", None, QtGui.QApplication.UnicodeUTF8))
        self.runtyp_combox.addItem(QtGui.QApplication.translate("GamessPropDialog", "Energy", None, QtGui.QApplication.UnicodeUTF8))
        self.runtyp_combox.addItem(QtGui.QApplication.translate("GamessPropDialog", "Optimization", None, QtGui.QApplication.UnicodeUTF8))
        self.choose_color_btn.setToolTip(QtGui.QApplication.translate("GamessPropDialog", "Change the "+gms_str+" jig color", None, QtGui.QApplication.UnicodeUTF8))
        self.choose_color_btn.setText(QtGui.QApplication.translate("GamessPropDialog", "Choose...", None, QtGui.QApplication.UnicodeUTF8))
        self.psetslbl_2_2.setText(QtGui.QApplication.translate("GamessPropDialog", "Name :", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel1_2_3.setText(QtGui.QApplication.translate("GamessPropDialog", "Calculate :", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel1_3.setText(QtGui.QApplication.translate("GamessPropDialog", "Description :", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel1_3_2.setText(QtGui.QApplication.translate("GamessPropDialog", "Color :", None, QtGui.QApplication.UnicodeUTF8))
        self.name_linedit.setToolTip(QtGui.QApplication.translate("GamessPropDialog", "Name of the "+gms_str+" jig", None, QtGui.QApplication.UnicodeUTF8))
        self.comment_linedit.setToolTip(QtGui.QApplication.translate("GamessPropDialog", "Description, also placed in the $DATA section of the INP file", None, QtGui.QApplication.UnicodeUTF8))
        self.scftyp_grpbox.setTitle(QtGui.QApplication.translate("GamessPropDialog", "Electronic Structure Properties", None, QtGui.QApplication.UnicodeUTF8))
        self.rhf_radiobtn.setToolTip(QtGui.QApplication.translate("GamessPropDialog", "Restricted Hartree-Fock", None, QtGui.QApplication.UnicodeUTF8))
        self.rhf_radiobtn.setText(QtGui.QApplication.translate("GamessPropDialog", "RHF", None, QtGui.QApplication.UnicodeUTF8))
        self.uhf_radiobtn.setToolTip(QtGui.QApplication.translate("GamessPropDialog", "Unrestricted Hartree-Fock", None, QtGui.QApplication.UnicodeUTF8))
        self.uhf_radiobtn.setText(QtGui.QApplication.translate("GamessPropDialog", "UHF", None, QtGui.QApplication.UnicodeUTF8))
        self.rohf_radiobtn.setToolTip(QtGui.QApplication.translate("GamessPropDialog", "Restricted Open-shell Hartree-Fock", None, QtGui.QApplication.UnicodeUTF8))
        self.rohf_radiobtn.setText(QtGui.QApplication.translate("GamessPropDialog", "ROHF", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel1_4.setText(QtGui.QApplication.translate("GamessPropDialog", "Charge:", None, QtGui.QApplication.UnicodeUTF8))
        self.icharg_spinbox.setToolTip(QtGui.QApplication.translate("GamessPropDialog", "The total charge of the structure (IGHARG)", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel1_2_2.setText(QtGui.QApplication.translate("GamessPropDialog", "Multiplicity:", None, QtGui.QApplication.UnicodeUTF8))
        self.multi_combox.setToolTip(QtGui.QApplication.translate("GamessPropDialog", "N + 1, where N is the number of unpaired electrons (MULT)", None, QtGui.QApplication.UnicodeUTF8))
        self.multi_combox.addItem(QtGui.QApplication.translate("GamessPropDialog", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.multi_combox.addItem(QtGui.QApplication.translate("GamessPropDialog", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.multi_combox.addItem(QtGui.QApplication.translate("GamessPropDialog", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.multi_combox.addItem(QtGui.QApplication.translate("GamessPropDialog", "4", None, QtGui.QApplication.UnicodeUTF8))
        self.multi_combox.addItem(QtGui.QApplication.translate("GamessPropDialog", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.multi_combox.addItem(QtGui.QApplication.translate("GamessPropDialog", "6", None, QtGui.QApplication.UnicodeUTF8))
        self.multi_combox.addItem(QtGui.QApplication.translate("GamessPropDialog", "7", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox8.setTitle(QtGui.QApplication.translate("GamessPropDialog", "System Memory and Usage", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel2_2.setText(QtGui.QApplication.translate("GamessPropDialog", "Memory :", None, QtGui.QApplication.UnicodeUTF8))
        self.memory_spinbox.setToolTip(QtGui.QApplication.translate("GamessPropDialog", "System memory reserved for calculation", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel1.setText(QtGui.QApplication.translate("GamessPropDialog", "MB", None, QtGui.QApplication.UnicodeUTF8))
        self.dirscf_checkbox.setToolTip(QtGui.QApplication.translate("GamessPropDialog", "Run the calculation in RAM", None, QtGui.QApplication.UnicodeUTF8))
        self.dirscf_checkbox.setText(QtGui.QApplication.translate("GamessPropDialog", "DirectSCF", None, QtGui.QApplication.UnicodeUTF8))
        self.edit_input_file_cbox.setToolTip(QtGui.QApplication.translate("GamessPropDialog", "Opens INP file in an editor", None, QtGui.QApplication.UnicodeUTF8))
        self.edit_input_file_cbox.setText(QtGui.QApplication.translate("GamessPropDialog", "Open Input File in text editor", None, QtGui.QApplication.UnicodeUTF8))
        self.run_job_btn.setToolTip(QtGui.QApplication.translate("GamessPropDialog", "Save "+gms_str+" parameters and launch job", None, QtGui.QApplication.UnicodeUTF8))
        self.run_job_btn.setText(QtGui.QApplication.translate("GamessPropDialog", "Save and Run", None, QtGui.QApplication.UnicodeUTF8))
        self.cancel_btn.setToolTip(QtGui.QApplication.translate("GamessPropDialog", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.cancel_btn.setText(QtGui.QApplication.translate("GamessPropDialog", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.save_btn.setToolTip(QtGui.QApplication.translate("GamessPropDialog", "Save "+gms_str+" parameters and generates the INP file", None, QtGui.QApplication.UnicodeUTF8))
        self.save_btn.setText(QtGui.QApplication.translate("GamessPropDialog", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.whats_this_btn.setToolTip(QtGui.QApplication.translate("GamessPropDialog", "What\'s This Help Utility", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox3.setTitle(QtGui.QApplication.translate("GamessPropDialog", "Convergence Criteria", None, QtGui.QApplication.UnicodeUTF8))
        self.iterations_lbl.setText(QtGui.QApplication.translate("GamessPropDialog", "Iterations :", None, QtGui.QApplication.UnicodeUTF8))
        self.iterations_spinbox.setToolTip(QtGui.QApplication.translate("GamessPropDialog", "Maximum number of SCF iteration cycles (MAXIT)", None, QtGui.QApplication.UnicodeUTF8))
        self.rmsd_lbl.setText(QtGui.QApplication.translate("GamessPropDialog", "RMSD:", None, QtGui.QApplication.UnicodeUTF8))
        self.rmsd_combox.setToolTip(QtGui.QApplication.translate("GamessPropDialog", "Gradient convergence tolerance (OPTTOL)", None, QtGui.QApplication.UnicodeUTF8))
        self.rmsd_combox.addItem(QtGui.QApplication.translate("GamessPropDialog", "Coarse", None, QtGui.QApplication.UnicodeUTF8))
        self.rmsd_combox.addItem(QtGui.QApplication.translate("GamessPropDialog", "Medium", None, QtGui.QApplication.UnicodeUTF8))
        self.rmsd_combox.addItem(QtGui.QApplication.translate("GamessPropDialog", "Fine", None, QtGui.QApplication.UnicodeUTF8))
        self.rmsd_combox.addItem(QtGui.QApplication.translate("GamessPropDialog", "Very Fine", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel3.setText(QtGui.QApplication.translate("GamessPropDialog", "Energy and Density:", None, QtGui.QApplication.UnicodeUTF8))
        self.density_conv_combox.setToolTip(QtGui.QApplication.translate("GamessPropDialog", "Accuracy of the electron density convergence (CONV)", None, QtGui.QApplication.UnicodeUTF8))
        self.density_conv_combox.addItem(QtGui.QApplication.translate("GamessPropDialog", "Coarse", None, QtGui.QApplication.UnicodeUTF8))
        self.density_conv_combox.addItem(QtGui.QApplication.translate("GamessPropDialog", "Medium", None, QtGui.QApplication.UnicodeUTF8))
        self.density_conv_combox.addItem(QtGui.QApplication.translate("GamessPropDialog", "Fine", None, QtGui.QApplication.UnicodeUTF8))
        self.density_conv_combox.addItem(QtGui.QApplication.translate("GamessPropDialog", "Very Fine", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox2.setTitle(QtGui.QApplication.translate("GamessPropDialog", "Electron Correlation Method", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox10_3_2.setToolTip(QtGui.QApplication.translate("GamessPropDialog", "Read $HESS group from previous output file", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox10_3_2.setText(QtGui.QApplication.translate("GamessPropDialog", "Read $HESS Group", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox10_2_2_2.setToolTip(QtGui.QApplication.translate("GamessPropDialog", "Read $VEC group from previous output file", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox10_2_2_2.setText(QtGui.QApplication.translate("GamessPropDialog", "Read $VEC Group", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox35.setText(QtGui.QApplication.translate("GamessPropDialog", "Frequencies", None, QtGui.QApplication.UnicodeUTF8))
        self.none_radiobtn.setToolTip(QtGui.QApplication.translate("GamessPropDialog", "Neglect electron correlation", None, QtGui.QApplication.UnicodeUTF8))
        self.none_radiobtn.setText(QtGui.QApplication.translate("GamessPropDialog", "None", None, QtGui.QApplication.UnicodeUTF8))
        self.dft_radiobtn.setToolTip(QtGui.QApplication.translate("GamessPropDialog", "Perform a density functional theory calculation", None, QtGui.QApplication.UnicodeUTF8))
        self.dft_radiobtn.setText(QtGui.QApplication.translate("GamessPropDialog", "DFT", None, QtGui.QApplication.UnicodeUTF8))
        self.mp2_radiobtn.setToolTip(QtGui.QApplication.translate("GamessPropDialog", "Perform a Second-Order Moeller Plesset calculation", None, QtGui.QApplication.UnicodeUTF8))
        self.mp2_radiobtn.setText(QtGui.QApplication.translate("GamessPropDialog", "MP2", None, QtGui.QApplication.UnicodeUTF8))
        self.dfttyp_label.setText(QtGui.QApplication.translate("GamessPropDialog", "Functional:", None, QtGui.QApplication.UnicodeUTF8))
        self.gridsize_label.setText(QtGui.QApplication.translate("GamessPropDialog", "Grid Size:", None, QtGui.QApplication.UnicodeUTF8))
        self.dfttyp_combox.setToolTip(QtGui.QApplication.translate("GamessPropDialog", "Density functional", None, QtGui.QApplication.UnicodeUTF8))
        self.dfttyp_combox.addItem(QtGui.QApplication.translate("GamessPropDialog", "SLATER (E)", None, QtGui.QApplication.UnicodeUTF8))
        self.dfttyp_combox.addItem(QtGui.QApplication.translate("GamessPropDialog", "BECKE (E)", None, QtGui.QApplication.UnicodeUTF8))
        self.dfttyp_combox.addItem(QtGui.QApplication.translate("GamessPropDialog", "GILL (E)", None, QtGui.QApplication.UnicodeUTF8))
        self.dfttyp_combox.addItem(QtGui.QApplication.translate("GamessPropDialog", "PBE (E)", None, QtGui.QApplication.UnicodeUTF8))
        self.dfttyp_combox.addItem(QtGui.QApplication.translate("GamessPropDialog", "VWN (C)", None, QtGui.QApplication.UnicodeUTF8))
        self.dfttyp_combox.addItem(QtGui.QApplication.translate("GamessPropDialog", "LYP (C)", None, QtGui.QApplication.UnicodeUTF8))
        self.dfttyp_combox.addItem(QtGui.QApplication.translate("GamessPropDialog", "OP (C)", None, QtGui.QApplication.UnicodeUTF8))
        self.dfttyp_combox.addItem(QtGui.QApplication.translate("GamessPropDialog", "SVWN/LDA (E+C)", None, QtGui.QApplication.UnicodeUTF8))
        self.dfttyp_combox.addItem(QtGui.QApplication.translate("GamessPropDialog", "SLYP (E+C)", None, QtGui.QApplication.UnicodeUTF8))
        self.dfttyp_combox.addItem(QtGui.QApplication.translate("GamessPropDialog", "SOP (E+C)", None, QtGui.QApplication.UnicodeUTF8))
        self.dfttyp_combox.addItem(QtGui.QApplication.translate("GamessPropDialog", "BVWN (E+C)", None, QtGui.QApplication.UnicodeUTF8))
        self.dfttyp_combox.addItem(QtGui.QApplication.translate("GamessPropDialog", "BLYP (E+C)", None, QtGui.QApplication.UnicodeUTF8))
        self.dfttyp_combox.addItem(QtGui.QApplication.translate("GamessPropDialog", "BOP (E+C)", None, QtGui.QApplication.UnicodeUTF8))
        self.dfttyp_combox.addItem(QtGui.QApplication.translate("GamessPropDialog", "GVWN (E+C)", None, QtGui.QApplication.UnicodeUTF8))
        self.dfttyp_combox.addItem(QtGui.QApplication.translate("GamessPropDialog", "GLYP (E+C)", None, QtGui.QApplication.UnicodeUTF8))
        self.dfttyp_combox.addItem(QtGui.QApplication.translate("GamessPropDialog", "GOP (E+C)", None, QtGui.QApplication.UnicodeUTF8))
        self.dfttyp_combox.addItem(QtGui.QApplication.translate("GamessPropDialog", "PBEVWN (E+C)", None, QtGui.QApplication.UnicodeUTF8))
        self.dfttyp_combox.addItem(QtGui.QApplication.translate("GamessPropDialog", "PBELYP (E+C)", None, QtGui.QApplication.UnicodeUTF8))
        self.dfttyp_combox.addItem(QtGui.QApplication.translate("GamessPropDialog", "PBEOP (E+C)", None, QtGui.QApplication.UnicodeUTF8))
        self.dfttyp_combox.addItem(QtGui.QApplication.translate("GamessPropDialog", "BHHLYP (H)", None, QtGui.QApplication.UnicodeUTF8))
        self.dfttyp_combox.addItem(QtGui.QApplication.translate("GamessPropDialog", "B3LYP (H)", None, QtGui.QApplication.UnicodeUTF8))
        self.gridsize_combox.setToolTip(QtGui.QApplication.translate("GamessPropDialog", "Grid spacing for the DFT calculation", None, QtGui.QApplication.UnicodeUTF8))
        self.gridsize_combox.addItem(QtGui.QApplication.translate("GamessPropDialog", "Coarse", None, QtGui.QApplication.UnicodeUTF8))
        self.gridsize_combox.addItem(QtGui.QApplication.translate("GamessPropDialog", "Default", None, QtGui.QApplication.UnicodeUTF8))
        self.gridsize_combox.addItem(QtGui.QApplication.translate("GamessPropDialog", "Fine", None, QtGui.QApplication.UnicodeUTF8))
        self.gridsize_combox.addItem(QtGui.QApplication.translate("GamessPropDialog", "Army Grade", None, QtGui.QApplication.UnicodeUTF8))
        self.core_electrons_checkbox.setToolTip(QtGui.QApplication.translate("GamessPropDialog", "Include both the valence and core electrons in the MP2 calculation", None, QtGui.QApplication.UnicodeUTF8))
        self.core_electrons_checkbox.setText(QtGui.QApplication.translate("GamessPropDialog", "Core electrons?", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel6.setText(QtGui.QApplication.translate("GamessPropDialog", "Basis Set :", None, QtGui.QApplication.UnicodeUTF8))
        self.gbasis_combox.setToolTip(QtGui.QApplication.translate("GamessPropDialog", "Gaussian-type basis sets and semi-empirical parameters", None, QtGui.QApplication.UnicodeUTF8))
        self.gbasis_combox.addItem(QtGui.QApplication.translate("GamessPropDialog", "AM1", None, QtGui.QApplication.UnicodeUTF8))
        self.gbasis_combox.addItem(QtGui.QApplication.translate("GamessPropDialog", "PM3", None, QtGui.QApplication.UnicodeUTF8))
        self.gbasis_combox.addItem(QtGui.QApplication.translate("GamessPropDialog", "STO-3G", None, QtGui.QApplication.UnicodeUTF8))
        self.gbasis_combox.addItem(QtGui.QApplication.translate("GamessPropDialog", "STO-6G", None, QtGui.QApplication.UnicodeUTF8))
        self.gbasis_combox.addItem(QtGui.QApplication.translate("GamessPropDialog", "3-21G", None, QtGui.QApplication.UnicodeUTF8))
        self.gbasis_combox.addItem(QtGui.QApplication.translate("GamessPropDialog", "3-21G*", None, QtGui.QApplication.UnicodeUTF8))
        self.gbasis_combox.addItem(QtGui.QApplication.translate("GamessPropDialog", "6-31G", None, QtGui.QApplication.UnicodeUTF8))
        self.gbasis_combox.addItem(QtGui.QApplication.translate("GamessPropDialog", "6-31G(d)", None, QtGui.QApplication.UnicodeUTF8))
        self.gbasis_combox.addItem(QtGui.QApplication.translate("GamessPropDialog", "6-31G(d,p)", None, QtGui.QApplication.UnicodeUTF8))
        self.gbasis_combox.addItem(QtGui.QApplication.translate("GamessPropDialog", "6-31+G(d)", None, QtGui.QApplication.UnicodeUTF8))
        self.gbasis_combox.addItem(QtGui.QApplication.translate("GamessPropDialog", "6-31+G(d,p)", None, QtGui.QApplication.UnicodeUTF8))
        self.gbasis_combox.addItem(QtGui.QApplication.translate("GamessPropDialog", "6-31++G(d)", None, QtGui.QApplication.UnicodeUTF8))
        self.gbasis_combox.addItem(QtGui.QApplication.translate("GamessPropDialog", "6-31++G(d,p)", None, QtGui.QApplication.UnicodeUTF8))
        self.gbasis_combox.addItem(QtGui.QApplication.translate("GamessPropDialog", "6-311G", None, QtGui.QApplication.UnicodeUTF8))
        self.gbasis_combox.addItem(QtGui.QApplication.translate("GamessPropDialog", "6-311G(d)", None, QtGui.QApplication.UnicodeUTF8))
        self.gbasis_combox.addItem(QtGui.QApplication.translate("GamessPropDialog", "6-311G(d,p)", None, QtGui.QApplication.UnicodeUTF8))
        self.gbasis_combox.addItem(QtGui.QApplication.translate("GamessPropDialog", "6-311+G(d,p)", None, QtGui.QApplication.UnicodeUTF8))
        self.gbasis_combox.addItem(QtGui.QApplication.translate("GamessPropDialog", "6-311++G(d,p)", None, QtGui.QApplication.UnicodeUTF8))
