#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: BPSK test 02 2
# Author: yabool2001
# Copyright: mzemlo.pl@gmail.com
# Description: BPSK test 02 2
# GNU Radio version: 3.10.12.0

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio import blocks
import pmt
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
from gnuradio import gr, pdu
from gnuradio import iio
import sip
import threading



class BPSK_test_02_2(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "BPSK test 02 2", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("BPSK test 02 2")
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

        self.settings = Qt.QSettings("gnuradio/flowgraphs", "BPSK_test_02_2")

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
        self.bw = bw = 20000000
        self.access_key = access_key = '11100001010110101110100010010011'
        self.variable_constellation_1 = variable_constellation_1 = digital.constellation_bpsk().base()
        self.variable_constellation_1.set_npwr(1.0)
        self.usb = usb = "usb:"
        self.sps = sps = 4
        self.samp_rate = samp_rate = int(bw*3)
        self.nfilts = nfilts = 32
        self.ip = ip = "ip:192.168.2.1"
        self.header_format = header_format = digital.header_format_default(access_key, 0)
        self.f_o = f_o = 2900000000

        ##################################################
        # Blocks
        ##################################################

        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
            1024, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            f_o, #fc
            samp_rate, #bw
            "", #name
            1,
            None # parent
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis((-140), 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(True)
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

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_win)
        self.qtgui_const_sink_x_1_0 = qtgui.const_sink_c(
            8, #size
            "", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_const_sink_x_1_0.set_update_time(0.10)
        self.qtgui_const_sink_x_1_0.set_y_axis((-2), 2)
        self.qtgui_const_sink_x_1_0.set_x_axis((-2), 2)
        self.qtgui_const_sink_x_1_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_1_0.enable_autoscale(True)
        self.qtgui_const_sink_x_1_0.enable_grid(False)
        self.qtgui_const_sink_x_1_0.enable_axis_labels(True)


        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        styles = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_1_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_1_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_1_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_1_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_1_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_1_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_1_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_1_0_win = sip.wrapinstance(self.qtgui_const_sink_x_1_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_const_sink_x_1_0_win)
        self.pdu_pdu_to_tagged_stream_0_0 = pdu.pdu_to_tagged_stream(gr.types.byte_t, 'packet_len')
        self.pdu_pdu_to_tagged_stream_0 = pdu.pdu_to_tagged_stream(gr.types.byte_t, 'packet_len')
        self.iio_pluto_sink_0 = iio.fmcomms2_sink_fc32(ip if ip else iio.get_pluto_uri(), [True, True], (int(samp_rate/24)), False)
        self.iio_pluto_sink_0.set_len_tag_key('')
        self.iio_pluto_sink_0.set_bandwidth(bw)
        self.iio_pluto_sink_0.set_frequency(f_o)
        self.iio_pluto_sink_0.set_samplerate(samp_rate)
        self.iio_pluto_sink_0.set_attenuation(0, 10)
        self.iio_pluto_sink_0.set_filter_params('Auto', '', 0, 0)
        self.digital_protocol_formatter_async_0 = digital.protocol_formatter_async(header_format)
        self.digital_constellation_modulator_0_0 = digital.generic_mod(
            constellation=variable_constellation_1,
            differential=False,
            samples_per_symbol=4,
            pre_diff_code=True,
            excess_bw=0.35,
            verbose=True,
            log=True,
            truncate=False)
        self.blocks_tagged_stream_mux_0 = blocks.tagged_stream_mux(gr.sizeof_char*1, "packet_len", 0)
        self.blocks_message_strobe_1 = blocks.message_strobe(pmt.cons ( pmt.PMT_NIL , pmt.init_u8vector ( 1 , 0x01 ) ), 1000)


        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.blocks_message_strobe_1, 'strobe'), (self.digital_protocol_formatter_async_0, 'in'))
        self.msg_connect((self.digital_protocol_formatter_async_0, 'header'), (self.pdu_pdu_to_tagged_stream_0, 'pdus'))
        self.msg_connect((self.digital_protocol_formatter_async_0, 'payload'), (self.pdu_pdu_to_tagged_stream_0_0, 'pdus'))
        self.connect((self.blocks_tagged_stream_mux_0, 0), (self.digital_constellation_modulator_0_0, 0))
        self.connect((self.digital_constellation_modulator_0_0, 0), (self.iio_pluto_sink_0, 0))
        self.connect((self.digital_constellation_modulator_0_0, 0), (self.qtgui_const_sink_x_1_0, 0))
        self.connect((self.digital_constellation_modulator_0_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.pdu_pdu_to_tagged_stream_0, 0), (self.blocks_tagged_stream_mux_0, 0))
        self.connect((self.pdu_pdu_to_tagged_stream_0_0, 0), (self.blocks_tagged_stream_mux_0, 1))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("gnuradio/flowgraphs", "BPSK_test_02_2")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_bw(self):
        return self.bw

    def set_bw(self, bw):
        self.bw = bw
        self.set_samp_rate(int(self.bw*3))
        self.iio_pluto_sink_0.set_bandwidth(self.bw)

    def get_access_key(self):
        return self.access_key

    def set_access_key(self, access_key):
        self.access_key = access_key
        self.set_header_format(digital.header_format_default(self.access_key, 0))

    def get_variable_constellation_1(self):
        return self.variable_constellation_1

    def set_variable_constellation_1(self, variable_constellation_1):
        self.variable_constellation_1 = variable_constellation_1

    def get_usb(self):
        return self.usb

    def set_usb(self, usb):
        self.usb = usb

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.iio_pluto_sink_0.set_samplerate(self.samp_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(self.f_o, self.samp_rate)

    def get_nfilts(self):
        return self.nfilts

    def set_nfilts(self, nfilts):
        self.nfilts = nfilts

    def get_ip(self):
        return self.ip

    def set_ip(self, ip):
        self.ip = ip

    def get_header_format(self):
        return self.header_format

    def set_header_format(self, header_format):
        self.header_format = header_format

    def get_f_o(self):
        return self.f_o

    def set_f_o(self, f_o):
        self.f_o = f_o
        self.iio_pluto_sink_0.set_frequency(self.f_o)
        self.qtgui_freq_sink_x_0.set_frequency_range(self.f_o, self.samp_rate)




def main(top_block_cls=BPSK_test_02_2, options=None):

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
