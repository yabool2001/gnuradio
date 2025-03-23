#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Simple Bpsk Tx V2
# GNU Radio version: 3.10.12.0

from PyQt5 import Qt
from gnuradio import qtgui
from PyQt5 import QtCore
from gnuradio import blocks
import pmt
from gnuradio import blocks, gr
from gnuradio import digital
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio import iio
import simple_bpsk_tx_v2_epy_block_0 as epy_block_0  # embedded python block
import sip
import threading



class simple_bpsk_tx_v2(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Simple Bpsk Tx V2", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Simple Bpsk Tx V2")
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

        self.settings = Qt.QSettings("gnuradio/flowgraphs", "simple_bpsk_tx_v2")

        try:
            geometry = self.settings.value("geometry")
            if geometry:
                self.restoreGeometry(geometry)
        except BaseException as exc:
            print(f"Qt GUI: Could not restore geometry: {str(exc)}", file=sys.stderr)
        self.flowgraph_started = threading.Event()

        ##################################################
        # Variables
        ##################################################
        self.sps = sps = 2
        self.eb = eb = 0.22
        self.tx_rrc_taps = tx_rrc_taps = firdes.root_raised_cosine(sps, sps,1.0, eb, (15*sps))
        self.samp_rate = samp_rate = 200e3
        self.rx_rrc_taps = rx_rrc_taps = firdes.root_raised_cosine(1, sps,1.0, eb, (15*sps))
        self.pkt_len = pkt_len = 1000
        self.my_constellation = my_constellation = digital.constellation_bpsk().base()
        self.my_constellation.set_npwr(1.0)
        self.gain = gain = 56
        self.freq = freq = 483e6-300
        self.amp = amp = 0.7

        ##################################################
        # Blocks
        ##################################################

        self.tab0 = Qt.QTabWidget()
        self.tab0_widget_0 = Qt.QWidget()
        self.tab0_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab0_widget_0)
        self.tab0_grid_layout_0 = Qt.QGridLayout()
        self.tab0_layout_0.addLayout(self.tab0_grid_layout_0)
        self.tab0.addTab(self.tab0_widget_0, 'Time')
        self.tab0_widget_1 = Qt.QWidget()
        self.tab0_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab0_widget_1)
        self.tab0_grid_layout_1 = Qt.QGridLayout()
        self.tab0_layout_1.addLayout(self.tab0_grid_layout_1)
        self.tab0.addTab(self.tab0_widget_1, 'Freq.')
        self.tab0_widget_2 = Qt.QWidget()
        self.tab0_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab0_widget_2)
        self.tab0_grid_layout_2 = Qt.QGridLayout()
        self.tab0_layout_2.addLayout(self.tab0_grid_layout_2)
        self.tab0.addTab(self.tab0_widget_2, 'Const.')
        self.top_grid_layout.addWidget(self.tab0, 2, 0, 1, 2)
        for r in range(2, 3):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._samp_rate_range = qtgui.Range(200e3, 10e6, 200e3, 200e3, 200)
        self._samp_rate_win = qtgui.RangeWidget(self._samp_rate_range, self.set_samp_rate, "Sample Rate", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_grid_layout.addWidget(self._samp_rate_win, 0, 0, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._freq_range = qtgui.Range(50e6, 3e9, 500e3, 483e6-300, 200)
        self._freq_win = qtgui.RangeWidget(self._freq_range, self.set_freq, "Frequency", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_grid_layout.addWidget(self._freq_win, 0, 1, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_1 = qtgui.time_sink_c(
            600, #size
            samp_rate, #samp_rate
            "", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_1.set_update_time(0.10)
        self.qtgui_time_sink_x_1.set_y_axis(-2, 2)

        self.qtgui_time_sink_x_1.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_1.enable_tags(True)
        self.qtgui_time_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, 'packet_len')
        self.qtgui_time_sink_x_1.enable_autoscale(True)
        self.qtgui_time_sink_x_1.enable_grid(False)
        self.qtgui_time_sink_x_1.enable_axis_labels(True)
        self.qtgui_time_sink_x_1.enable_control_panel(False)
        self.qtgui_time_sink_x_1.enable_stem_plot(False)

        self.qtgui_time_sink_x_1.disable_legend()

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(2):
            if len(labels[i]) == 0:
                if (i % 2 == 0):
                    self.qtgui_time_sink_x_1.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_1.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_1_win = sip.wrapinstance(self.qtgui_time_sink_x_1.qwidget(), Qt.QWidget)
        self.tab0_layout_0.addWidget(self._qtgui_time_sink_x_1_win)
        self.iio_pluto_sink_0 = iio.fmcomms2_sink_fc32('ip:192.168.2.1' if 'ip:192.168.2.1' else iio.get_pluto_uri(), [True, True], 32768, False)
        self.iio_pluto_sink_0.set_len_tag_key('')
        self.iio_pluto_sink_0.set_bandwidth(20000000)
        self.iio_pluto_sink_0.set_frequency(int(freq))
        self.iio_pluto_sink_0.set_samplerate(int(samp_rate))
        self.iio_pluto_sink_0.set_attenuation(0, 10.0)
        self.iio_pluto_sink_0.set_filter_params('Auto', '', 0, 0)
        self._gain_range = qtgui.Range(0, 83, 1, 56, 200)
        self._gain_win = qtgui.RangeWidget(self._gain_range, self.set_gain, "Gain", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_grid_layout.addWidget(self._gain_win, 1, 0, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.epy_block_0 = epy_block_0.pmt_to_stream()
        self.digital_constellation_modulator_0 = digital.generic_mod(
            constellation=my_constellation,
            differential=False,
            samples_per_symbol=4,
            pre_diff_code=True,
            excess_bw=0.35,
            verbose=False,
            log=False,
            truncate=False)
        self.blocks_unpack_k_bits_bb_0 = blocks.unpack_k_bits_bb(8)
        self.blocks_message_strobe_0 = blocks.message_strobe(pmt.intern("0101"), 4000)
        self.blocks_message_debug_0 = blocks.message_debug(True, gr.log_levels.info)
        self._amp_range = qtgui.Range(0, 0.9, 0.005, 0.7, 200)
        self._amp_win = qtgui.RangeWidget(self._amp_range, self.set_amp, "Amplitude", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_grid_layout.addWidget(self._amp_win, 1, 1, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)


        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.blocks_message_strobe_0, 'strobe'), (self.blocks_message_debug_0, 'print'))
        self.msg_connect((self.blocks_message_strobe_0, 'strobe'), (self.epy_block_0, 'in'))
        self.connect((self.blocks_unpack_k_bits_bb_0, 0), (self.digital_constellation_modulator_0, 0))
        self.connect((self.digital_constellation_modulator_0, 0), (self.iio_pluto_sink_0, 0))
        self.connect((self.digital_constellation_modulator_0, 0), (self.qtgui_time_sink_x_1, 0))
        self.connect((self.epy_block_0, 0), (self.blocks_unpack_k_bits_bb_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("gnuradio/flowgraphs", "simple_bpsk_tx_v2")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.set_rx_rrc_taps(firdes.root_raised_cosine(1, self.sps, 1.0, self.eb, (15*self.sps)))
        self.set_tx_rrc_taps(firdes.root_raised_cosine(self.sps, self.sps, 1.0, self.eb, (15*self.sps)))

    def get_eb(self):
        return self.eb

    def set_eb(self, eb):
        self.eb = eb
        self.set_rx_rrc_taps(firdes.root_raised_cosine(1, self.sps, 1.0, self.eb, (15*self.sps)))
        self.set_tx_rrc_taps(firdes.root_raised_cosine(self.sps, self.sps, 1.0, self.eb, (15*self.sps)))

    def get_tx_rrc_taps(self):
        return self.tx_rrc_taps

    def set_tx_rrc_taps(self, tx_rrc_taps):
        self.tx_rrc_taps = tx_rrc_taps

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.iio_pluto_sink_0.set_samplerate(int(self.samp_rate))
        self.qtgui_time_sink_x_1.set_samp_rate(self.samp_rate)

    def get_rx_rrc_taps(self):
        return self.rx_rrc_taps

    def set_rx_rrc_taps(self, rx_rrc_taps):
        self.rx_rrc_taps = rx_rrc_taps

    def get_pkt_len(self):
        return self.pkt_len

    def set_pkt_len(self, pkt_len):
        self.pkt_len = pkt_len

    def get_my_constellation(self):
        return self.my_constellation

    def set_my_constellation(self, my_constellation):
        self.my_constellation = my_constellation

    def get_gain(self):
        return self.gain

    def set_gain(self, gain):
        self.gain = gain

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.iio_pluto_sink_0.set_frequency(int(self.freq))

    def get_amp(self):
        return self.amp

    def set_amp(self, amp):
        self.amp = amp




def main(top_block_cls=simple_bpsk_tx_v2, options=None):

    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()
    tb.flowgraph_started.set()

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
