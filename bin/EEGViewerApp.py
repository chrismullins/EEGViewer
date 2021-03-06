#!/usr/bin/env python

import os
import sys
import pyqtgraph as pg
import mne
#import numpy as np
#import collections

from PyQt4 import QtGui, QtCore
# Since posix symlinks are not supported on windows, let's
# explicitly update sys.path.
try:
    import eegviewer as eegviewer
except ImportError:
    sys.path.append(os.path.join(os.path.dirname(__file__), '../'))
    import eegviewer as eegviewer

#---------------------------------------------------------------------------
class EEGAppController(object):

    def __init__(self):
        self.app = None
        self.MainWindow = None
        self.ui = None

        # Raw file selected by user
        self.selectedRawFile = None
        # MNE Object from selectedRawFile
        self.rawObject = None
        # Events array
        self.events = None
        # Epochs object
        self.epochs = None
        # Evoked object
        self.evoked = None

        self.start_App()

    def start_App(self):
        """Initialize the window """
        self.app = eegviewer.gui.QtGui.QApplication(sys.argv)
        self.MainWindow = eegviewer.gui.QtGui.QMainWindow()
        # Enable antialiasing for prettier plots
        pg.setConfigOptions(antialias=True)
        self.ui = eegviewer.gui.Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.eegplot = self.ui.graphicsView.addPlot(title="EEG Signal")
        self.epochplot = self.ui.graphicsView_2.addPlot(title="Epoch Signals")
        self.evokedplot = self.ui.graphicsView_3.addPlot(title="Evoked Plot")

        self.ui.actionLoad_File.triggered.connect(self.file_load_sequence)        
        self.ui.eeg_channel_combo_box.currentIndexChanged.connect(self.channel_selected_sequence)
        # Epochs stuff
        self.ui.create_epochs_button.pressed.connect(self.compute_epochs_sequence)
        self.ui.epoch_channel_combo_box.currentIndexChanged.connect(self.epoch_update_plot)
        self.ui.epoch_number_spinbox.valueChanged.connect(self.epoch_update_plot)

        # Evoked stuff
        self.ui.create_evoked_button.pressed.connect(self.compute_evoked_sequence)
        self.ui.evoked_channel_combo_box.currentIndexChanged.connect(self.evoked_update_plot)

        #sys.exit(self.app.exec_())
        self.MainWindow.showMaximized()
        self.app.exec_()

    def file_load_sequence(self):
        """ Load a signal from a selected file, and show the plot.
        """
        self.selectedFile = self.show_dialog()
        self.rawObject, self.events = self.read_raw_file(str(self.selectedFile.name))
        self.ui.eeg_channel_combo_box.addItems(self.rawObject.ch_names)
        
    def channel_selected_sequence(self):
        """ Show one of the signals in the graphicsView when a channel
        is selected in the comboBox """
        self.eegplot.clear()
        channelSelectionIndex = self.rawObject.ch_names.index(str(self.ui.eeg_channel_combo_box.currentText()))
        data, times = self.rawObject[channelSelectionIndex, :]
        plotData = self.eegplot.plot(times, data.T[:,0])
        return
        
    def show_dialog(self):
        """ Open the QFileDialog, return the file object """
        fname = QtGui.QFileDialog.getOpenFileName()
        f = open(fname, 'r')
        return f

    def read_raw_file(self, filename):
        """ Read the raw file from filename """
        if filename.endswith('.vhdr'):
            rawObject =  mne.io.read_raw_brainvision(vhdr_fname=filename, preload=True)
            events = rawObject.get_brainvision_events()
            # Use every other since we only care about trigger "on"
            events = events[::2]
            return rawObject, events

    def compute_epochs_sequence(self):
        """ Compute and display epochs when the button is pressed """
        #epochs = mne.Epochs(raw_edf, events_trig_on, event_id, tmin, tmax, proj=True, baseline=baseline, preload=False) 
        event_id = dict(stim_on=1)
        self.epochs = mne.Epochs(raw=self.rawObject, \
                                 events=self.events, \
                                 event_id=event_id,  \
                                 tmin=self.ui.epoch_tmin_spinbox.value(), \
                                 tmax=self.ui.epoch_tmax_spinbox.value(), \
                                 proj=True, \
                                 baseline=(None, 0), \
                                 preload=True)
        self.ui.epoch_channel_combo_box.addItems(self.epochs.ch_names)
        self.ui.epoch_number_spinbox.maximum = self.epochs._data.shape[0]
        

    def epoch_update_plot(self):
        """ Update the epochs plot. """
        self.epochplot.clear()
        channelSelectionIndex = self.epochs.ch_names.index(str(self.ui.epoch_channel_combo_box.currentText()))
        epochSelectionIndex = self.ui.epoch_number_spinbox.value()
        #epochs._data addressed as: [epoch,channel,sample] so its shape is 200x63x3500
        times = self.epochs.times
        data = self.epochs._data[epochSelectionIndex, channelSelectionIndex, :]
        plotData = self.epochplot.plot(times, data)

    def compute_evoked_sequence(self):
        """ Compute the evoked response from the epochs. """
        self.evoked = self.epochs.average()
        self.ui.evoked_channel_combo_box.addItems(self.evoked.ch_names)
        
    def evoked_update_plot(self):
        """ Update the evoked plot. """
        self.evokedplot.clear()
        channelSelectionIndex = self.evoked.ch_names.index(str(self.ui.evoked_channel_combo_box.currentText()))
        times = self.evoked.times
        data = self.evoked.data[channelSelectionIndex]
        plotData = self.evokedplot.plot(times, data)
        


#---------------------------------------------------------------------------
if __name__ == '__main__':
    eeg_controller = EEGAppController()


