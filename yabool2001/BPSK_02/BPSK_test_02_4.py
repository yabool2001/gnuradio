#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: BPSK test 02 4
# Author: yabool2001
# Copyright: mzemlo.pl@gmail.com
# Description: BPSK test 02 4
# GNU Radio version: 3.10.12.0

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio import analog
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
import threading



class BPSK_test_02_4(gr.top_block, Qt.QWidget):

    def __init__(self, hdr_format=digital.header_format_default(digital.packet_utils.default_access_code, 0)):
        gr.top_block.__init__(self, "BPSK test 02 4", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("BPSK test 02 4")
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

        self.settings = Qt.QSettings("gnuradio/flowgraphs", "BPSK_test_02_4")

        try:
            geometry = self.settings.value("geometry")
            if geometry:
                self.restoreGeometry(geometry)
        except BaseException as exc:
            print(f"Qt GUI: Could not restore geometry: {str(exc)}", file=sys.stderr)
        self.flowgraph_started = threading.Event()

        ##################################################
        # Parameters
        ##################################################
        self.hdr_format = hdr_format

        ##################################################
        # Variables
        ##################################################
        self.bw = bw = 20000000
        self.variable_constellation_1 = variable_constellation_1 = digital.constellation_bpsk().base()
        self.variable_constellation_1.set_npwr(1.0)
        self.sps = sps = 4
        self.samp_rate = samp_rate = int(bw*3)
        self.pluto_context = pluto_context = "usb:"
        self.nfilts = nfilts = 32
        self.f_c = f_c = 2400000000

        ##################################################
        # Blocks
        ##################################################

        self.pdu_pdu_to_tagged_stream_0 = pdu.pdu_to_tagged_stream(gr.types.byte_t, 'packet_len')
        self.digital_protocol_formatter_bb_0 = digital.protocol_formatter_bb(hdr_format, "packet_len")
        self.digital_pfb_clock_sync_xxx_0 = digital.pfb_clock_sync_ccf(4, 0.0628, firdes.root_raised_cosine(nfilts, nfilts, 1.0/float(sps), 0.35, 11*sps*nfilts), 32, 16, 1.5, 1)
        self.digital_correlate_access_code_xx_ts_1 = digital.correlate_access_code_bb_ts(digital.packet_utils.default_access_code,
          0, "packet_len")
        self.digital_constellation_modulator_0_0 = digital.generic_mod(
            constellation=variable_constellation_1,
            differential=False,
            samples_per_symbol=4,
            pre_diff_code=True,
            excess_bw=0.35,
            verbose=True,
            log=True,
            truncate=False)
        self.digital_constellation_decoder_cb_1_0 = digital.constellation_decoder_cb(variable_constellation_1)
        self.blocks_tagged_stream_mux_0 = blocks.tagged_stream_mux(gr.sizeof_char*1, "packet_len", 0)
        self.blocks_selector_0 = blocks.selector(gr.sizeof_gr_complex*1,0,0)
        self.blocks_selector_0.set_enabled(True)
        self.blocks_repack_bits_bb_0_0_0 = blocks.repack_bits_bb(1, 8, "packet_len", False, gr.GR_MSB_FIRST)
        self.blocks_message_strobe_1 = blocks.message_strobe(pmt.cons(pmt.PMT_NIL, pmt.init_u8vector(1, 0x31)), 500)
        self.blocks_file_sink_0_0_0 = blocks.file_sink(gr.sizeof_char*1, 'output_text.txt', False)
        self.blocks_file_sink_0_0_0.set_unbuffered(False)
        self.analog_pwr_squelch_xx_0 = analog.pwr_squelch_cc((-40), (1e-4), 0, True)


        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.blocks_message_strobe_1, 'strobe'), (self.pdu_pdu_to_tagged_stream_0, 'pdus'))
        self.connect((self.analog_pwr_squelch_xx_0, 0), (self.blocks_selector_0, 1))
        self.connect((self.blocks_repack_bits_bb_0_0_0, 0), (self.blocks_file_sink_0_0_0, 0))
        self.connect((self.blocks_selector_0, 0), (self.digital_pfb_clock_sync_xxx_0, 0))
        self.connect((self.blocks_tagged_stream_mux_0, 0), (self.digital_constellation_modulator_0_0, 0))
        self.connect((self.digital_constellation_decoder_cb_1_0, 0), (self.digital_correlate_access_code_xx_ts_1, 0))
        self.connect((self.digital_constellation_modulator_0_0, 0), (self.analog_pwr_squelch_xx_0, 0))
        self.connect((self.digital_constellation_modulator_0_0, 0), (self.blocks_selector_0, 0))
        self.connect((self.digital_correlate_access_code_xx_ts_1, 0), (self.blocks_repack_bits_bb_0_0_0, 0))
        self.connect((self.digital_pfb_clock_sync_xxx_0, 0), (self.digital_constellation_decoder_cb_1_0, 0))
        self.connect((self.digital_protocol_formatter_bb_0, 0), (self.blocks_tagged_stream_mux_0, 0))
        self.connect((self.pdu_pdu_to_tagged_stream_0, 0), (self.blocks_tagged_stream_mux_0, 1))
        self.connect((self.pdu_pdu_to_tagged_stream_0, 0), (self.digital_protocol_formatter_bb_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("gnuradio/flowgraphs", "BPSK_test_02_4")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_hdr_format(self):
        return self.hdr_format

    def set_hdr_format(self, hdr_format):
        self.hdr_format = hdr_format
        self.digital_protocol_formatter_bb_0.set_header_format(self.hdr_format)

    def get_bw(self):
        return self.bw

    def set_bw(self, bw):
        self.bw = bw
        self.set_samp_rate(int(self.bw*3))

    def get_variable_constellation_1(self):
        return self.variable_constellation_1

    def set_variable_constellation_1(self, variable_constellation_1):
        self.variable_constellation_1 = variable_constellation_1
        self.digital_constellation_decoder_cb_1_0.set_constellation(self.variable_constellation_1)

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.digital_pfb_clock_sync_xxx_0.update_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0/float(self.sps), 0.35, 11*self.sps*self.nfilts))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate

    def get_pluto_context(self):
        return self.pluto_context

    def set_pluto_context(self, pluto_context):
        self.pluto_context = pluto_context

    def get_nfilts(self):
        return self.nfilts

    def set_nfilts(self, nfilts):
        self.nfilts = nfilts
        self.digital_pfb_clock_sync_xxx_0.update_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0/float(self.sps), 0.35, 11*self.sps*self.nfilts))

    def get_f_c(self):
        return self.f_c

    def set_f_c(self, f_c):
        self.f_c = f_c



def argument_parser():
    description = 'BPSK test 02 4'
    parser = ArgumentParser(description=description)
    return parser


def main(top_block_cls=BPSK_test_02_4, options=None):
    if options is None:
        options = argument_parser().parse_args()

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
