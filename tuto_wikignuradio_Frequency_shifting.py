#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Wiki Tuto GNU Radio Frequency shifting Example
# Author: yabool2001
# Copyright: maciej.zemlo@gmail.pl
# Description: https://wiki.gnuradio.org/index.php?title=Frequency_Shifting
# GNU Radio version: 3.10.10.0

from PyQt5 import Qt
from gnuradio import qtgui
from PyQt5 import QtCore
from gnuradio import analog
from gnuradio import blocks
from gnuradio import filter
from gnuradio.filter import firdes
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
import sip



class tuto_wikignuradio_Frequency_shifting(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Wiki Tuto GNU Radio Frequency shifting Example", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Wiki Tuto GNU Radio Frequency shifting Example")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except BaseException as exc:
            print(f"Qt GUI: Could not set Icon: {str(exc)}", file=sys.stderr)
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "tuto_wikignuradio_Frequency_shifting")

        try:
            geometry = self.settings.value("geometry")
            if geometry:
                self.restoreGeometry(geometry)
        except BaseException as exc:
            print(f"Qt GUI: Could not restore geometry: {str(exc)}", file=sys.stderr)

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 10000000
        self.interpolation_rate = interpolation_rate = 12
        self.trans_width = trans_width = samp_rate/16
        self.samp_rate_interpolated = samp_rate_interpolated = samp_rate*interpolation_rate
        self.f_cutoff = f_cutoff = samp_rate/8
        self.n = n = 1024
        self.low_pass_filter_taps = low_pass_filter_taps = firdes.low_pass(1.0, samp_rate_interpolated, f_cutoff,trans_width, window.WIN_HAMMING, 6.76)
        self.f_c = f_c = 1000000
        self.f = f = 0

        ##################################################
        # Blocks
        ##################################################

        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
            1024, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate_interpolated, #bw
            "", #name
            4,
            None # parent
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis((-140), 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)
        self.qtgui_freq_sink_x_0.set_fft_window_normalized(False)



        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(4):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_win)
        self.low_pass_filter_0 = filter.fir_filter_ccf(
            1,
            firdes.low_pass(
                1,
                samp_rate,
                f_cutoff,
                trans_width,
                window.WIN_HAMMING,
                6.76))
        self._f_range = qtgui.Range(-samp_rate/2, samp_rate/2, 1, 0, 200)
        self._f_win = qtgui.RangeWidget(self._f_range, self.set_f, "frequency", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._f_win)
        self.blocks_throttle2_0 = blocks.throttle( gr.sizeof_gr_complex*1, samp_rate_interpolated, True, 0 if "auto" == "auto" else max( int(float(0.1) * samp_rate_interpolated) if "auto" == "time" else int(0.1), 1) )
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.analog_sig_source_x_0_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, f_c, 1, 0, 0)
        self.analog_fastnoise_source_x_0 = analog.fastnoise_source_c(analog.GR_GAUSSIAN, 1, 0, 8192)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_fastnoise_source_x_0, 0), (self.blocks_throttle2_0, 0))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.qtgui_freq_sink_x_0, 3))
        self.connect((self.blocks_multiply_xx_0, 0), (self.qtgui_freq_sink_x_0, 2))
        self.connect((self.blocks_throttle2_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.blocks_throttle2_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.qtgui_freq_sink_x_0, 1))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "tuto_wikignuradio_Frequency_shifting")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_f_cutoff(self.samp_rate/8)
        self.set_samp_rate_interpolated(self.samp_rate*self.interpolation_rate)
        self.set_trans_width(self.samp_rate/16)
        self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.f_cutoff, self.trans_width, window.WIN_HAMMING, 6.76))

    def get_interpolation_rate(self):
        return self.interpolation_rate

    def set_interpolation_rate(self, interpolation_rate):
        self.interpolation_rate = interpolation_rate
        self.set_samp_rate_interpolated(self.samp_rate*self.interpolation_rate)

    def get_trans_width(self):
        return self.trans_width

    def set_trans_width(self, trans_width):
        self.trans_width = trans_width
        self.set_low_pass_filter_taps(firdes.low_pass(1.0, self.samp_rate_interpolated, self.f_cutoff, self.trans_width, window.WIN_HAMMING, 6.76))
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.f_cutoff, self.trans_width, window.WIN_HAMMING, 6.76))

    def get_samp_rate_interpolated(self):
        return self.samp_rate_interpolated

    def set_samp_rate_interpolated(self, samp_rate_interpolated):
        self.samp_rate_interpolated = samp_rate_interpolated
        self.set_low_pass_filter_taps(firdes.low_pass(1.0, self.samp_rate_interpolated, self.f_cutoff, self.trans_width, window.WIN_HAMMING, 6.76))
        self.blocks_throttle2_0.set_sample_rate(self.samp_rate_interpolated)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate_interpolated)

    def get_f_cutoff(self):
        return self.f_cutoff

    def set_f_cutoff(self, f_cutoff):
        self.f_cutoff = f_cutoff
        self.set_low_pass_filter_taps(firdes.low_pass(1.0, self.samp_rate_interpolated, self.f_cutoff, self.trans_width, window.WIN_HAMMING, 6.76))
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.f_cutoff, self.trans_width, window.WIN_HAMMING, 6.76))

    def get_n(self):
        return self.n

    def set_n(self, n):
        self.n = n

    def get_low_pass_filter_taps(self):
        return self.low_pass_filter_taps

    def set_low_pass_filter_taps(self, low_pass_filter_taps):
        self.low_pass_filter_taps = low_pass_filter_taps

    def get_f_c(self):
        return self.f_c

    def set_f_c(self, f_c):
        self.f_c = f_c
        self.analog_sig_source_x_0_0.set_frequency(self.f_c)

    def get_f(self):
        return self.f

    def set_f(self, f):
        self.f = f




def main(top_block_cls=tuto_wikignuradio_Frequency_shifting, options=None):

    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
