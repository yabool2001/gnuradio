#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Protocol Formatter tutorial 01
# Author: yabool2001
# Copyright: mzemlo.pl@gmail.com
# Description: Protocol Formatter tutorial 01
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
import Protocol_Formatter_tuto_01_epy_block_1_0 as epy_block_1_0  # embedded python block
import Protocol_Formatter_tuto_01_epy_block_1_0_0 as epy_block_1_0_0  # embedded python block
import Protocol_Formatter_tuto_01_epy_block_1_0_0_0 as epy_block_1_0_0_0  # embedded python block
import Protocol_Formatter_tuto_01_epy_block_1_0_1 as epy_block_1_0_1  # embedded python block
import sip
import threading



class Protocol_Formatter_tuto_01(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Protocol Formatter tutorial 01", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Protocol Formatter tutorial 01")
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

        self.settings = Qt.QSettings("gnuradio/flowgraphs", "Protocol_Formatter_tuto_01")

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
        self.access_key = access_key = '11110000111100001010101010101010'
        self.sps = sps = 4
        self.samp_rate = samp_rate = 32000
        self.nfilts = nfilts = 32
        self.header = header = digital.header_format_default(access_key, 0)
        self.const_obj = const_obj = digital.constellation_bpsk().base()
        self.const_obj.set_npwr(1)

        ##################################################
        # Blocks
        ##################################################

        self.qtgui_const_sink_x_0_0 = qtgui.const_sink_c(
            (sps*8), #size
            "Tx constellation", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_const_sink_x_0_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0_0.set_y_axis((-2), 2)
        self.qtgui_const_sink_x_0_0.set_x_axis((-2), 2)
        self.qtgui_const_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0_0.enable_grid(False)
        self.qtgui_const_sink_x_0_0.enable_axis_labels(True)


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
                self.qtgui_const_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_const_sink_x_0_0_win)
        self.pdu_pdu_to_tagged_stream_0 = pdu.pdu_to_tagged_stream(gr.types.byte_t, 'packet_len')
        self.epy_block_1_0_1 = epy_block_1_0_1.byte_logger(samp_rate=samp_rate, filename="03_byte_rx_log.csv")
        self.epy_block_1_0_0_0 = epy_block_1_0_0_0.byte_logger(samp_rate=samp_rate, filename="02_byte_tx_log.csv")
        self.epy_block_1_0_0 = epy_block_1_0_0.byte_logger(samp_rate=samp_rate, filename="01_byte_tx_log.csv")
        self.epy_block_1_0 = epy_block_1_0.byte_logger(samp_rate=samp_rate, filename="04_byte_rx_log.csv")
        self.digital_protocol_formatter_bb_0 = digital.protocol_formatter_bb(header, "packet_len")
        self.digital_pfb_clock_sync_xxx_0 = digital.pfb_clock_sync_ccf(sps, 0.0628, firdes.root_raised_cosine(nfilts, nfilts, 1.0/float(sps), 0.35, 11*sps*nfilts), 32, 16, 1.5, 1)
        self.digital_correlate_access_code_xx_ts_1_0 = digital.correlate_access_code_bb_ts(access_key,
          0, "packet_len")
        self.digital_constellation_modulator_0 = digital.generic_mod(
            constellation=const_obj,
            differential=False,
            samples_per_symbol=sps,
            pre_diff_code=True,
            excess_bw=0.35,
            verbose=True,
            log=True,
            truncate=False)
        self.digital_constellation_decoder_cb_1_0 = digital.constellation_decoder_cb(const_obj)
        self.blocks_throttle2_0 = blocks.throttle( gr.sizeof_gr_complex*1, samp_rate, True, 0 if "auto" == "auto" else max( int(float(0.1) * samp_rate) if "auto" == "time" else int(0.1), 1) )
        self.blocks_tagged_stream_mux_0 = blocks.tagged_stream_mux(gr.sizeof_char*1, "packet_len", 0)
        self.blocks_pack_k_bits_bb_0 = blocks.pack_k_bits_bb(8)
        self.blocks_message_strobe_1 = blocks.message_strobe(pmt.cons ( pmt.PMT_NIL , pmt.make_u8vector ( 1 , 0x13 ) ), 1000)


        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.blocks_message_strobe_1, 'strobe'), (self.pdu_pdu_to_tagged_stream_0, 'pdus'))
        self.connect((self.blocks_pack_k_bits_bb_0, 0), (self.epy_block_1_0, 0))
        self.connect((self.blocks_tagged_stream_mux_0, 0), (self.digital_constellation_modulator_0, 0))
        self.connect((self.blocks_tagged_stream_mux_0, 0), (self.epy_block_1_0_0_0, 0))
        self.connect((self.blocks_throttle2_0, 0), (self.digital_pfb_clock_sync_xxx_0, 0))
        self.connect((self.digital_constellation_decoder_cb_1_0, 0), (self.digital_correlate_access_code_xx_ts_1_0, 0))
        self.connect((self.digital_constellation_modulator_0, 0), (self.blocks_throttle2_0, 0))
        self.connect((self.digital_constellation_modulator_0, 0), (self.qtgui_const_sink_x_0_0, 0))
        self.connect((self.digital_correlate_access_code_xx_ts_1_0, 0), (self.blocks_pack_k_bits_bb_0, 0))
        self.connect((self.digital_correlate_access_code_xx_ts_1_0, 0), (self.epy_block_1_0_1, 0))
        self.connect((self.digital_pfb_clock_sync_xxx_0, 0), (self.digital_constellation_decoder_cb_1_0, 0))
        self.connect((self.digital_protocol_formatter_bb_0, 0), (self.blocks_tagged_stream_mux_0, 0))
        self.connect((self.digital_protocol_formatter_bb_0, 0), (self.epy_block_1_0_0, 0))
        self.connect((self.pdu_pdu_to_tagged_stream_0, 0), (self.blocks_tagged_stream_mux_0, 1))
        self.connect((self.pdu_pdu_to_tagged_stream_0, 0), (self.digital_protocol_formatter_bb_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("gnuradio/flowgraphs", "Protocol_Formatter_tuto_01")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_access_key(self):
        return self.access_key

    def set_access_key(self, access_key):
        self.access_key = access_key
        self.set_header(digital.header_format_default(self.access_key, 0))

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.digital_pfb_clock_sync_xxx_0.update_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0/float(self.sps), 0.35, 11*self.sps*self.nfilts))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle2_0.set_sample_rate(self.samp_rate)
        self.epy_block_1_0.samp_rate = self.samp_rate
        self.epy_block_1_0_0.samp_rate = self.samp_rate
        self.epy_block_1_0_0_0.samp_rate = self.samp_rate
        self.epy_block_1_0_1.samp_rate = self.samp_rate

    def get_nfilts(self):
        return self.nfilts

    def set_nfilts(self, nfilts):
        self.nfilts = nfilts
        self.digital_pfb_clock_sync_xxx_0.update_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0/float(self.sps), 0.35, 11*self.sps*self.nfilts))

    def get_header(self):
        return self.header

    def set_header(self, header):
        self.header = header
        self.digital_protocol_formatter_bb_0.set_header_format(self.header)

    def get_const_obj(self):
        return self.const_obj

    def set_const_obj(self, const_obj):
        self.const_obj = const_obj
        self.digital_constellation_decoder_cb_1_0.set_constellation(self.const_obj)




def main(top_block_cls=Protocol_Formatter_tuto_01, options=None):

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
