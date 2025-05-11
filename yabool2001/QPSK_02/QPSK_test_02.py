#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: QPSK test 02
# Author: yabool2001
# Copyright: mzemlo.pl@gmail.com
# Description: QPSK test 02
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
import QPSK_test_02_epy_block_1_0 as epy_block_1_0  # embedded python block
import QPSK_test_02_epy_block_1_0_0 as epy_block_1_0_0  # embedded python block
import QPSK_test_02_epy_block_1_0_0_0 as epy_block_1_0_0_0  # embedded python block
import QPSK_test_02_epy_block_1_0_0_0_0 as epy_block_1_0_0_0_0  # embedded python block
import sip
import threading



class QPSK_test_02(gr.top_block, Qt.QWidget):

    def __init__(self, hdr_format=digital.header_format_default(digital.packet_utils.default_access_code, 0)):
        gr.top_block.__init__(self, "QPSK test 02", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("QPSK test 02")
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

        self.settings = Qt.QSettings("gnuradio/flowgraphs", "QPSK_test_02")

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
        self.sps = sps = 4
        self.nfilts = nfilts = 32
        self.bdw = bdw = 10000000
        self.samp_rate = samp_rate = int(bdw*2.5)
        self.rrc_taps = rrc_taps = firdes.root_raised_cosine(nfilts, nfilts, 1.0/float(sps), 0.35, 11*sps*nfilts)
        self.pluto_context_uri = pluto_context_uri = "192.168.2.1"
        self.f_o = f_o = 820000000
        self.const_obj = const_obj = digital.constellation_qpsk().base()
        self.const_obj.set_npwr(1)

        ##################################################
        # Blocks
        ##################################################

        self.qtgui_const_sink_x_0_0_0 = qtgui.const_sink_c(
            (sps*8), #size
            "Rx constellation", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_const_sink_x_0_0_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0_0_0.set_y_axis((-2), 2)
        self.qtgui_const_sink_x_0_0_0.set_x_axis((-2), 2)
        self.qtgui_const_sink_x_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0_0_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0_0_0.enable_grid(False)
        self.qtgui_const_sink_x_0_0_0.enable_axis_labels(True)


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
                self.qtgui_const_sink_x_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0_0_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0_0_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0_0_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0_0_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_0_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0_0_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_const_sink_x_0_0_0_win)
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
        self.iio_pluto_source_0 = iio.fmcomms2_source_fc32(pluto_context_uri if pluto_context_uri else iio.get_pluto_uri(), [True, True], 32768)
        self.iio_pluto_source_0.set_len_tag_key('packet_len')
        self.iio_pluto_source_0.set_frequency(f_o)
        self.iio_pluto_source_0.set_samplerate(samp_rate)
        self.iio_pluto_source_0.set_gain_mode(0, 'manual')
        self.iio_pluto_source_0.set_gain(0, 70)
        self.iio_pluto_source_0.set_quadrature(True)
        self.iio_pluto_source_0.set_rfdc(True)
        self.iio_pluto_source_0.set_bbdc(True)
        self.iio_pluto_source_0.set_filter_params('Auto', '', 0, 0)
        self.iio_pluto_sink_0 = iio.fmcomms2_sink_fc32(pluto_context_uri if pluto_context_uri else iio.get_pluto_uri(), [True, True], 32768, False)
        self.iio_pluto_sink_0.set_len_tag_key('packet_len')
        self.iio_pluto_sink_0.set_bandwidth(bdw)
        self.iio_pluto_sink_0.set_frequency(f_o)
        self.iio_pluto_sink_0.set_samplerate(samp_rate)
        self.iio_pluto_sink_0.set_attenuation(0, 1.0)
        self.iio_pluto_sink_0.set_filter_params('Auto', '', 0, 0)
        self.epy_block_1_0_0_0_0 = epy_block_1_0_0_0_0.byte_logger(samp_rate=samp_rate, filename="03_byte_tx_qpsk_mod_log.csv")
        self.epy_block_1_0_0_0 = epy_block_1_0_0_0.byte_logger(samp_rate=samp_rate, filename="01_byte_tx_qpsk_mod_log.csv")
        self.epy_block_1_0_0 = epy_block_1_0_0.byte_logger(samp_rate=samp_rate, filename="02_byte_tx_qpsk_mod_log.csv")
        self.epy_block_1_0 = epy_block_1_0.byte_logger(samp_rate=samp_rate, filename="05_byte_rx_qpsk_mod_log.csv")
        self.digital_protocol_formatter_bb_0 = digital.protocol_formatter_bb(hdr_format, "packet_len")
        self.digital_pfb_clock_sync_xxx_0 = digital.pfb_clock_sync_ccf(sps, 0.0628, rrc_taps, 32, 16, 1.5, 1)
        self.digital_correlate_access_code_xx_ts_1_0 = digital.correlate_access_code_bb_ts(digital.packet_utils.default_access_code,
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
        self.blocks_unpack_k_bits_bb_0 = blocks.unpack_k_bits_bb(2)
        self.blocks_tagged_stream_mux_0 = blocks.tagged_stream_mux(gr.sizeof_char*1, "packet_len", 0)
        self.blocks_pack_k_bits_bb_0 = blocks.pack_k_bits_bb(8)
        self.blocks_message_strobe_1 = blocks.message_strobe(pmt.cons ( pmt.PMT_NIL , pmt.make_u8vector ( 1 , 0x11 ) ), 1000)


        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.blocks_message_strobe_1, 'strobe'), (self.pdu_pdu_to_tagged_stream_0, 'pdus'))
        self.connect((self.blocks_pack_k_bits_bb_0, 0), (self.epy_block_1_0, 0))
        self.connect((self.blocks_tagged_stream_mux_0, 0), (self.digital_constellation_modulator_0, 0))
        self.connect((self.blocks_tagged_stream_mux_0, 0), (self.epy_block_1_0_0_0_0, 0))
        self.connect((self.blocks_unpack_k_bits_bb_0, 0), (self.digital_correlate_access_code_xx_ts_1_0, 0))
        self.connect((self.digital_constellation_decoder_cb_1_0, 0), (self.blocks_unpack_k_bits_bb_0, 0))
        self.connect((self.digital_constellation_modulator_0, 0), (self.iio_pluto_sink_0, 0))
        self.connect((self.digital_constellation_modulator_0, 0), (self.qtgui_const_sink_x_0_0, 0))
        self.connect((self.digital_correlate_access_code_xx_ts_1_0, 0), (self.blocks_pack_k_bits_bb_0, 0))
        self.connect((self.digital_pfb_clock_sync_xxx_0, 0), (self.digital_constellation_decoder_cb_1_0, 0))
        self.connect((self.digital_pfb_clock_sync_xxx_0, 0), (self.qtgui_const_sink_x_0_0_0, 0))
        self.connect((self.digital_protocol_formatter_bb_0, 0), (self.blocks_tagged_stream_mux_0, 0))
        self.connect((self.digital_protocol_formatter_bb_0, 0), (self.epy_block_1_0_0, 0))
        self.connect((self.iio_pluto_source_0, 0), (self.digital_pfb_clock_sync_xxx_0, 0))
        self.connect((self.pdu_pdu_to_tagged_stream_0, 0), (self.blocks_tagged_stream_mux_0, 1))
        self.connect((self.pdu_pdu_to_tagged_stream_0, 0), (self.digital_protocol_formatter_bb_0, 0))
        self.connect((self.pdu_pdu_to_tagged_stream_0, 0), (self.epy_block_1_0_0_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("gnuradio/flowgraphs", "QPSK_test_02")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_hdr_format(self):
        return self.hdr_format

    def set_hdr_format(self, hdr_format):
        self.hdr_format = hdr_format
        self.digital_protocol_formatter_bb_0.set_header_format(self.hdr_format)

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.set_rrc_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0/float(self.sps), 0.35, 11*self.sps*self.nfilts))

    def get_nfilts(self):
        return self.nfilts

    def set_nfilts(self, nfilts):
        self.nfilts = nfilts
        self.set_rrc_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0/float(self.sps), 0.35, 11*self.sps*self.nfilts))

    def get_bdw(self):
        return self.bdw

    def set_bdw(self, bdw):
        self.bdw = bdw
        self.set_samp_rate(int(self.bdw*2.5))
        self.iio_pluto_sink_0.set_bandwidth(self.bdw)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.epy_block_1_0.samp_rate = self.samp_rate
        self.epy_block_1_0_0.samp_rate = self.samp_rate
        self.epy_block_1_0_0_0.samp_rate = self.samp_rate
        self.epy_block_1_0_0_0_0.samp_rate = self.samp_rate
        self.iio_pluto_sink_0.set_samplerate(self.samp_rate)
        self.iio_pluto_source_0.set_samplerate(self.samp_rate)

    def get_rrc_taps(self):
        return self.rrc_taps

    def set_rrc_taps(self, rrc_taps):
        self.rrc_taps = rrc_taps
        self.digital_pfb_clock_sync_xxx_0.update_taps(self.rrc_taps)

    def get_pluto_context_uri(self):
        return self.pluto_context_uri

    def set_pluto_context_uri(self, pluto_context_uri):
        self.pluto_context_uri = pluto_context_uri

    def get_f_o(self):
        return self.f_o

    def set_f_o(self, f_o):
        self.f_o = f_o
        self.iio_pluto_sink_0.set_frequency(self.f_o)
        self.iio_pluto_source_0.set_frequency(self.f_o)

    def get_const_obj(self):
        return self.const_obj

    def set_const_obj(self, const_obj):
        self.const_obj = const_obj
        self.digital_constellation_decoder_cb_1_0.set_constellation(self.const_obj)



def argument_parser():
    description = 'QPSK test 02'
    parser = ArgumentParser(description=description)
    return parser


def main(top_block_cls=QPSK_test_02, options=None):
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
