#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Tagged Stream To PDU sandbox 01
# Author: yabool2001
# Copyright: mzemlo.pl@gmail.com
# GNU Radio version: 3.10.12.0

from PyQt5 import Qt
from gnuradio import qtgui
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
from gnuradio import gr, pdu
import Tagged_Stream_To_PDU_sb_01_epy_block_1_0 as epy_block_1_0  # embedded python block
import Tagged_Stream_To_PDU_sb_01_epy_block_1_0_1 as epy_block_1_0_1  # embedded python block
import threading



class Tagged_Stream_To_PDU_sb_01(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Tagged Stream To PDU sandbox 01", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Tagged Stream To PDU sandbox 01")
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

        self.settings = Qt.QSettings("gnuradio/flowgraphs", "Tagged_Stream_To_PDU_sb_01")

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

        self.pdu_tagged_stream_to_pdu_0 = pdu.tagged_stream_to_pdu(gr.types.byte_t, 'packet_len')
        self.pdu_pdu_to_tagged_stream_0 = pdu.pdu_to_tagged_stream(gr.types.byte_t, 'packet_len')
        self.epy_block_1_0_1 = epy_block_1_0_1.byte_logger(samp_rate=samp_rate, filename="01_byte_tx_log.csv")
        self.epy_block_1_0 = epy_block_1_0.byte_logger(samp_rate=samp_rate, filename="02_byte_rx_log.csv")
        self.digital_crc_check_0 = digital.crc_check(32, 0x4C11DB7, 0xFFFFFFFF, 0xFFFFFFFF, True, True, False, True, 0)
        self.digital_crc_append_0 = digital.crc_append(32, 0x4C11DB7, 0xFFFFFFFF, 0xFFFFFFFF, True, True, False, 0)
        self.blocks_unpack_k_bits_bb_0 = blocks.unpack_k_bits_bb(8)
        self.blocks_throttle2_0 = blocks.throttle( gr.sizeof_char*1, samp_rate, True, 0 if "auto" == "auto" else max( int(float(0.1) * samp_rate) if "auto" == "time" else int(0.1), 1) )
        self.blocks_pack_k_bits_bb_0 = blocks.pack_k_bits_bb(8)
        self.blocks_message_strobe_1 = blocks.message_strobe(pmt.cons ( pmt.PMT_NIL , pmt.make_u8vector ( 1 , 0x13 ) ), 1000)
        self.blocks_message_debug_0 = blocks.message_debug(True, gr.log_levels.info)


        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.blocks_message_strobe_1, 'strobe'), (self.digital_crc_append_0, 'in'))
        self.msg_connect((self.digital_crc_append_0, 'out'), (self.pdu_pdu_to_tagged_stream_0, 'pdus'))
        self.msg_connect((self.digital_crc_check_0, 'ok'), (self.blocks_message_debug_0, 'print'))
        self.msg_connect((self.pdu_tagged_stream_to_pdu_0, 'pdus'), (self.digital_crc_check_0, 'in'))
        self.connect((self.blocks_pack_k_bits_bb_0, 0), (self.epy_block_1_0, 0))
        self.connect((self.blocks_pack_k_bits_bb_0, 0), (self.pdu_tagged_stream_to_pdu_0, 0))
        self.connect((self.blocks_throttle2_0, 0), (self.blocks_pack_k_bits_bb_0, 0))
        self.connect((self.blocks_unpack_k_bits_bb_0, 0), (self.blocks_throttle2_0, 0))
        self.connect((self.pdu_pdu_to_tagged_stream_0, 0), (self.blocks_unpack_k_bits_bb_0, 0))
        self.connect((self.pdu_pdu_to_tagged_stream_0, 0), (self.epy_block_1_0_1, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("gnuradio/flowgraphs", "Tagged_Stream_To_PDU_sb_01")
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

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle2_0.set_sample_rate(self.samp_rate)
        self.epy_block_1_0.samp_rate = self.samp_rate
        self.epy_block_1_0_1.samp_rate = self.samp_rate

    def get_nfilts(self):
        return self.nfilts

    def set_nfilts(self, nfilts):
        self.nfilts = nfilts

    def get_header(self):
        return self.header

    def set_header(self, header):
        self.header = header

    def get_const_obj(self):
        return self.const_obj

    def set_const_obj(self, const_obj):
        self.const_obj = const_obj




def main(top_block_cls=Tagged_Stream_To_PDU_sb_01, options=None):

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
