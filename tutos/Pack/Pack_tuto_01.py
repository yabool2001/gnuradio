#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Pack tuto 01
# Author: yabool2001
# Copyright: mzemlo.pl@gmail.com
# Description: Pack tuto 01
# GNU Radio version: 3.10.12.0

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio import blocks
import pmt
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
import Pack_tuto_01_epy_block_1_0_0 as epy_block_1_0_0  # embedded python block
import Pack_tuto_01_epy_block_1_0_0_0 as epy_block_1_0_0_0  # embedded python block
import Pack_tuto_01_epy_block_1_0_0_0_0 as epy_block_1_0_0_0_0  # embedded python block
import Pack_tuto_01_epy_block_1_0_0_0_0_0 as epy_block_1_0_0_0_0_0  # embedded python block
import Pack_tuto_01_epy_block_1_0_0_0_0_1 as epy_block_1_0_0_0_0_1  # embedded python block
import threading



class Pack_tuto_01(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Pack tuto 01", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Pack tuto 01")
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

        self.settings = Qt.QSettings("gnuradio/flowgraphs", "Pack_tuto_01")

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
        self.samp_rate = samp_rate = 32000

        ##################################################
        # Blocks
        ##################################################

        self.pdu_pdu_to_tagged_stream_0 = pdu.pdu_to_tagged_stream(gr.types.byte_t, 'packet_len')
        self.epy_block_1_0_0_0_0_1 = epy_block_1_0_0_0_0_1.byte_logger(samp_rate=samp_rate, filename="05_byte_pack_8_bits_log.csv")
        self.epy_block_1_0_0_0_0_0 = epy_block_1_0_0_0_0_0.byte_logger(samp_rate=samp_rate, filename="04_repack_1_to_8_bytes_log.csv")
        self.epy_block_1_0_0_0_0 = epy_block_1_0_0_0_0.byte_logger(samp_rate=samp_rate, filename="03_byte_pack_8_bits_log.csv")
        self.epy_block_1_0_0_0 = epy_block_1_0_0_0.byte_logger(samp_rate=samp_rate, filename="02_unpack_8_bits_log.csv")
        self.epy_block_1_0_0 = epy_block_1_0_0.byte_logger(samp_rate=samp_rate, filename='01_byte_log.csv')
        self.blocks_unpack_k_bits_bb_0 = blocks.unpack_k_bits_bb(8)
        self.blocks_throttle2_0 = blocks.throttle( gr.sizeof_char*1, samp_rate, True, 0 if "auto" == "auto" else max( int(float(0.1) * samp_rate) if "auto" == "time" else int(0.1), 1) )
        self.blocks_repack_bits_bb_0_0 = blocks.repack_bits_bb(1, 8, "", False, gr.GR_MSB_FIRST)
        self.blocks_repack_bits_bb_0 = blocks.repack_bits_bb(8, 1, "", False, gr.GR_MSB_FIRST)
        self.blocks_pack_k_bits_bb_0 = blocks.pack_k_bits_bb(8)
        self.blocks_message_strobe_1 = blocks.message_strobe(pmt.cons ( pmt.PMT_NIL , pmt.make_u8vector ( 1 , 0xAE ) ), 1000)


        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.blocks_message_strobe_1, 'strobe'), (self.pdu_pdu_to_tagged_stream_0, 'pdus'))
        self.connect((self.blocks_pack_k_bits_bb_0, 0), (self.blocks_repack_bits_bb_0, 0))
        self.connect((self.blocks_pack_k_bits_bb_0, 0), (self.epy_block_1_0_0_0_0, 0))
        self.connect((self.blocks_repack_bits_bb_0, 0), (self.blocks_repack_bits_bb_0_0, 0))
        self.connect((self.blocks_repack_bits_bb_0, 0), (self.epy_block_1_0_0_0_0_0, 0))
        self.connect((self.blocks_repack_bits_bb_0_0, 0), (self.epy_block_1_0_0_0_0_1, 0))
        self.connect((self.blocks_throttle2_0, 0), (self.blocks_pack_k_bits_bb_0, 0))
        self.connect((self.blocks_unpack_k_bits_bb_0, 0), (self.blocks_throttle2_0, 0))
        self.connect((self.blocks_unpack_k_bits_bb_0, 0), (self.epy_block_1_0_0_0, 0))
        self.connect((self.pdu_pdu_to_tagged_stream_0, 0), (self.blocks_unpack_k_bits_bb_0, 0))
        self.connect((self.pdu_pdu_to_tagged_stream_0, 0), (self.epy_block_1_0_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("gnuradio/flowgraphs", "Pack_tuto_01")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle2_0.set_sample_rate(self.samp_rate)
        self.epy_block_1_0_0.samp_rate = self.samp_rate
        self.epy_block_1_0_0_0.samp_rate = self.samp_rate
        self.epy_block_1_0_0_0_0.samp_rate = self.samp_rate
        self.epy_block_1_0_0_0_0_0.samp_rate = self.samp_rate
        self.epy_block_1_0_0_0_0_1.samp_rate = self.samp_rate




def main(top_block_cls=Pack_tuto_01, options=None):

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
