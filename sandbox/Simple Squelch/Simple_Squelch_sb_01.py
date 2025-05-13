#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Simple Squelch sand box 01
# Author: yabool2001
# Copyright: mzemlo.pl@gmail.com
# GNU Radio version: 3.10.12.0

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio import analog
from gnuradio import blocks
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
import Simple_Squelch_sb_01_epy_block_1_0_0_0_0 as epy_block_1_0_0_0_0  # embedded python block
import threading



class Simple_Squelch_sb_01(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Simple Squelch sand box 01", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Simple Squelch sand box 01")
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

        self.settings = Qt.QSettings("gnuradio/flowgraphs", "Simple_Squelch_sb_01")

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
        self.access_key = access_key = '11110000111100001010101010101010'
        self.variable_constellation_1 = variable_constellation_1 = digital.constellation_bpsk().base()
        self.variable_constellation_1.set_npwr(1.0)
        self.sps = sps = 4
        self.samp_rate = samp_rate = int(bw*3)
        self.pluto_context = pluto_context = "usb:"
        self.nfilts = nfilts = 32
        self.header = header = digital.header_format_default(access_key, 0)
        self.f_o = f_o = 820000000
        self.f_c = f_c = 2400000000

        ##################################################
        # Blocks
        ##################################################

        self.iio_pluto_source_0 = iio.fmcomms2_source_fc32(pluto_context if pluto_context else iio.get_pluto_uri(), [True, True], 32768)
        self.iio_pluto_source_0.set_len_tag_key('packet_len')
        self.iio_pluto_source_0.set_frequency(f_o)
        self.iio_pluto_source_0.set_samplerate(samp_rate)
        self.iio_pluto_source_0.set_gain_mode(0, 'slow_attack')
        self.iio_pluto_source_0.set_gain(0, 64)
        self.iio_pluto_source_0.set_quadrature(True)
        self.iio_pluto_source_0.set_rfdc(True)
        self.iio_pluto_source_0.set_bbdc(True)
        self.iio_pluto_source_0.set_filter_params('Auto', '', 0, 0)
        self.iio_pluto_sink_1 = iio.fmcomms2_sink_fc32('usb:' if 'usb:' else iio.get_pluto_uri(), [True, True], 32768, False)
        self.iio_pluto_sink_1.set_len_tag_key('packet_len')
        self.iio_pluto_sink_1.set_bandwidth(20000000)
        self.iio_pluto_sink_1.set_frequency(f_o)
        self.iio_pluto_sink_1.set_samplerate(samp_rate)
        self.iio_pluto_sink_1.set_attenuation(0, 1)
        self.iio_pluto_sink_1.set_filter_params('Auto', '', 0, 0)
        self.epy_block_1_0_0_0_0 = epy_block_1_0_0_0_0.byte_logger(samp_rate=samp_rate, filename="06_byte_rx_log.csv")
        self.digital_protocol_formatter_bb_0 = digital.protocol_formatter_bb(header, "packet_len")
        self.digital_pfb_clock_sync_xxx_0 = digital.pfb_clock_sync_ccf(4, 0.0628, firdes.root_raised_cosine(nfilts, nfilts, 1.0/float(sps), 0.35, 11*sps*nfilts), 32, 16, 1.5, 1)
        self.digital_correlate_access_code_xx_ts_1 = digital.correlate_access_code_bb_ts(access_key,
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
        self.blocks_stream_to_tagged_stream_0_0 = blocks.stream_to_tagged_stream(gr.sizeof_char, 1, 1, "packet_len")
        self.blocks_repack_bits_bb_0_0_0 = blocks.repack_bits_bb(1, 8, "packet_len", False, gr.GR_MSB_FIRST)
        self.blocks_file_sink_0_0_0 = blocks.file_sink(gr.sizeof_char*1, 'output_text.txt', False)
        self.blocks_file_sink_0_0_0.set_unbuffered(False)
        self.analog_simple_squelch_cc_0 = analog.simple_squelch_cc((-100), (1e-4))
        self.analog_const_source_x_0 = analog.sig_source_b(0, analog.GR_CONST_WAVE, 0, 0, 0x31)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_const_source_x_0, 0), (self.blocks_stream_to_tagged_stream_0_0, 0))
        self.connect((self.analog_simple_squelch_cc_0, 0), (self.digital_pfb_clock_sync_xxx_0, 0))
        self.connect((self.blocks_repack_bits_bb_0_0_0, 0), (self.blocks_file_sink_0_0_0, 0))
        self.connect((self.blocks_repack_bits_bb_0_0_0, 0), (self.epy_block_1_0_0_0_0, 0))
        self.connect((self.blocks_stream_to_tagged_stream_0_0, 0), (self.blocks_tagged_stream_mux_0, 1))
        self.connect((self.blocks_stream_to_tagged_stream_0_0, 0), (self.digital_protocol_formatter_bb_0, 0))
        self.connect((self.blocks_tagged_stream_mux_0, 0), (self.digital_constellation_modulator_0_0, 0))
        self.connect((self.digital_constellation_decoder_cb_1_0, 0), (self.digital_correlate_access_code_xx_ts_1, 0))
        self.connect((self.digital_constellation_modulator_0_0, 0), (self.iio_pluto_sink_1, 0))
        self.connect((self.digital_correlate_access_code_xx_ts_1, 0), (self.blocks_repack_bits_bb_0_0_0, 0))
        self.connect((self.digital_pfb_clock_sync_xxx_0, 0), (self.digital_constellation_decoder_cb_1_0, 0))
        self.connect((self.digital_protocol_formatter_bb_0, 0), (self.blocks_tagged_stream_mux_0, 0))
        self.connect((self.iio_pluto_source_0, 0), (self.analog_simple_squelch_cc_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("gnuradio/flowgraphs", "Simple_Squelch_sb_01")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_bw(self):
        return self.bw

    def set_bw(self, bw):
        self.bw = bw
        self.set_samp_rate(int(self.bw*3))

    def get_access_key(self):
        return self.access_key

    def set_access_key(self, access_key):
        self.access_key = access_key
        self.set_header(digital.header_format_default(self.access_key, 0))

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
        self.epy_block_1_0_0_0_0.samp_rate = self.samp_rate
        self.iio_pluto_sink_1.set_samplerate(self.samp_rate)
        self.iio_pluto_source_0.set_samplerate(self.samp_rate)

    def get_pluto_context(self):
        return self.pluto_context

    def set_pluto_context(self, pluto_context):
        self.pluto_context = pluto_context

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

    def get_f_o(self):
        return self.f_o

    def set_f_o(self, f_o):
        self.f_o = f_o
        self.iio_pluto_sink_1.set_frequency(self.f_o)
        self.iio_pluto_source_0.set_frequency(self.f_o)

    def get_f_c(self):
        return self.f_c

    def set_f_c(self, f_c):
        self.f_c = f_c




def main(top_block_cls=Simple_Squelch_sb_01, options=None):

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
