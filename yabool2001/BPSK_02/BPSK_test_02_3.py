#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: BPSK test 02.3
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
from gnuradio import iio
from gnuradio import pdu
import BPSK_test_02_3_epy_block_1_0_0_0_0 as epy_block_1_0_0_0_0  # embedded python block
import BPSK_test_02_3_epy_block_1_0_0_0_1 as epy_block_1_0_0_0_1  # embedded python block
import sip
import threading



class BPSK_test_02_3(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "BPSK test 02.3", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("BPSK test 02.3")
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

        self.settings = Qt.QSettings("gnuradio/flowgraphs", "BPSK_test_02_3")

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
        self.sps = sps = 4
        self.nfilts = nfilts = 32
        self.access_key = access_key = '111100001111000011110000101010101010101010101010'
        self.taps = taps = firdes.root_raised_cosine ( nfilts , nfilts , 1.0 / float ( sps ) , 0.35 , 11 * sps * nfilts )
        self.samp_rate = samp_rate = 65105
        self.my_constellation = my_constellation = digital.constellation_bpsk().base()
        self.my_constellation.set_npwr(1.0)
        self.header = header = digital.header_format_default ( access_key , 0 )
        self.f_c = f_c = 2400000000
        self.bw = bw = 20000000

        ##################################################
        # Blocks
        ##################################################

        self.qtgui_sink_x_0 = qtgui.sink_c(
            1024, #fftsize
            window.WIN_BLACKMAN_hARRIS, #wintype
            f_c, #fc
            40000000, #bw
            "Rx", #name
            True, #plotfreq
            True, #plotwaterfall
            True, #plottime
            True, #plotconst
            None # parent
        )
        self.qtgui_sink_x_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_win = sip.wrapinstance(self.qtgui_sink_x_0.qwidget(), Qt.QWidget)

        self.qtgui_sink_x_0.enable_rf_freq(False)

        self.top_layout.addWidget(self._qtgui_sink_x_0_win)
        self.pdu_tagged_stream_to_pdu_0_0 = pdu.tagged_stream_to_pdu(gr.types.byte_t, 'packet_len')
        self.pdu_random_pdu_0 = pdu.random_pdu(2, 2, 0xFF, 1)
        self.pdu_pdu_to_tagged_stream_0_0_0 = pdu.pdu_to_tagged_stream(gr.types.byte_t, 'packet_len')
        self.pdu_pdu_to_tagged_stream_0_0 = pdu.pdu_to_tagged_stream(gr.types.byte_t, 'packet_len')
        self.pdu_pdu_to_tagged_stream_0 = pdu.pdu_to_tagged_stream(gr.types.byte_t, 'packet_len')
        self.iio_pluto_source_0 = iio.fmcomms2_source_fc32('usb:' if 'usb:' else iio.get_pluto_uri(), [True, True], 32768)
        self.iio_pluto_source_0.set_len_tag_key('packet_len')
        self.iio_pluto_source_0.set_frequency(f_c)
        self.iio_pluto_source_0.set_samplerate(samp_rate)
        self.iio_pluto_source_0.set_gain_mode(0, 'fast_attack')
        self.iio_pluto_source_0.set_gain(0, 64)
        self.iio_pluto_source_0.set_quadrature(True)
        self.iio_pluto_source_0.set_rfdc(True)
        self.iio_pluto_source_0.set_bbdc(True)
        self.iio_pluto_source_0.set_filter_params('Auto', '', 0, 0)
        self.iio_pluto_sink_0 = iio.fmcomms2_sink_fc32('usb:' if 'usb:' else iio.get_pluto_uri(), [True, True], 32768, False)
        self.iio_pluto_sink_0.set_len_tag_key('')
        self.iio_pluto_sink_0.set_bandwidth(bw)
        self.iio_pluto_sink_0.set_frequency(f_c)
        self.iio_pluto_sink_0.set_samplerate(samp_rate)
        self.iio_pluto_sink_0.set_attenuation(0, 10)
        self.iio_pluto_sink_0.set_filter_params('Auto', '', 0, 0)
        self.epy_block_1_0_0_0_1 = epy_block_1_0_0_0_1.byte_logger(samp_rate=samp_rate, filename="01_byte_tx_log.csv")
        self.epy_block_1_0_0_0_0 = epy_block_1_0_0_0_0.byte_logger(samp_rate=samp_rate, filename="06_byte_rx_log.csv")
        self.digital_protocol_formatter_bb_0 = digital.protocol_formatter_bb(header, "packet_len")
        self.digital_pfb_clock_sync_xxx_0 = digital.pfb_clock_sync_ccf(sps, 0.0628, taps, 32, 16, 1.5, 1)
        self.digital_crc_check_0 = digital.crc_check(32, 0x4C11DB7, 0xFFFFFFFF, 0xFFFFFFFF, True, True, False, True, 0)
        self.digital_crc_append_0 = digital.crc_append(32, 0x4C11DB7, 0xFFFFFFFF, 0xFFFFFFFF, True, True, False, 0)
        self.digital_correlate_access_code_xx_ts_1_0_0 = digital.correlate_access_code_bb_ts(access_key,
          0, "packet_len")
        self.digital_constellation_modulator_0 = digital.generic_mod(
            constellation=my_constellation,
            differential=False,
            samples_per_symbol=sps,
            pre_diff_code=True,
            excess_bw=0.35,
            verbose=True,
            log=False,
            truncate=False)
        self.digital_constellation_decoder_cb_0 = digital.constellation_decoder_cb(my_constellation)
        self.blocks_tagged_stream_mux_0 = blocks.tagged_stream_mux(gr.sizeof_char*1, "packet_len", 0)
        self.blocks_stream_to_tagged_stream_0_0 = blocks.stream_to_tagged_stream(gr.sizeof_char, 1, 6, "packet_len")
        self.blocks_pack_k_bits_bb_0_0_0 = blocks.pack_k_bits_bb(8)
        self.blocks_message_strobe_1 = blocks.message_strobe(pmt.cons ( pmt.PMT_NIL , pmt.make_u8vector ( 1 , 0x31 ) ), 1000)
        self.blocks_message_debug_0_0 = blocks.message_debug(True, gr.log_levels.info)


        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.blocks_message_strobe_1, 'strobe'), (self.pdu_random_pdu_0, 'generate'))
        self.msg_connect((self.digital_crc_append_0, 'out'), (self.pdu_pdu_to_tagged_stream_0, 'pdus'))
        self.msg_connect((self.digital_crc_check_0, 'ok'), (self.blocks_message_debug_0_0, 'print'))
        self.msg_connect((self.digital_crc_check_0, 'ok'), (self.pdu_pdu_to_tagged_stream_0_0, 'pdus'))
        self.msg_connect((self.pdu_random_pdu_0, 'pdus'), (self.digital_crc_append_0, 'in'))
        self.msg_connect((self.pdu_random_pdu_0, 'pdus'), (self.pdu_pdu_to_tagged_stream_0_0_0, 'pdus'))
        self.msg_connect((self.pdu_tagged_stream_to_pdu_0_0, 'pdus'), (self.digital_crc_check_0, 'in'))
        self.connect((self.blocks_pack_k_bits_bb_0_0_0, 0), (self.pdu_tagged_stream_to_pdu_0_0, 0))
        self.connect((self.blocks_stream_to_tagged_stream_0_0, 0), (self.blocks_pack_k_bits_bb_0_0_0, 0))
        self.connect((self.blocks_tagged_stream_mux_0, 0), (self.digital_constellation_modulator_0, 0))
        self.connect((self.digital_constellation_decoder_cb_0, 0), (self.digital_correlate_access_code_xx_ts_1_0_0, 0))
        self.connect((self.digital_constellation_modulator_0, 0), (self.iio_pluto_sink_0, 0))
        self.connect((self.digital_correlate_access_code_xx_ts_1_0_0, 0), (self.blocks_stream_to_tagged_stream_0_0, 0))
        self.connect((self.digital_pfb_clock_sync_xxx_0, 0), (self.digital_constellation_decoder_cb_0, 0))
        self.connect((self.digital_protocol_formatter_bb_0, 0), (self.blocks_tagged_stream_mux_0, 0))
        self.connect((self.iio_pluto_source_0, 0), (self.digital_pfb_clock_sync_xxx_0, 0))
        self.connect((self.iio_pluto_source_0, 0), (self.qtgui_sink_x_0, 0))
        self.connect((self.pdu_pdu_to_tagged_stream_0, 0), (self.blocks_tagged_stream_mux_0, 1))
        self.connect((self.pdu_pdu_to_tagged_stream_0, 0), (self.digital_protocol_formatter_bb_0, 0))
        self.connect((self.pdu_pdu_to_tagged_stream_0_0, 0), (self.epy_block_1_0_0_0_0, 0))
        self.connect((self.pdu_pdu_to_tagged_stream_0_0_0, 0), (self.epy_block_1_0_0_0_1, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("gnuradio/flowgraphs", "BPSK_test_02_3")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.set_taps(firdes.root_raised_cosine ( self.nfilts , self.nfilts , 1.0 / float ( self.sps ) , 0.35 , 11 * self.sps * self.nfilts ))

    def get_nfilts(self):
        return self.nfilts

    def set_nfilts(self, nfilts):
        self.nfilts = nfilts
        self.set_taps(firdes.root_raised_cosine ( self.nfilts , self.nfilts , 1.0 / float ( self.sps ) , 0.35 , 11 * self.sps * self.nfilts ))

    def get_access_key(self):
        return self.access_key

    def set_access_key(self, access_key):
        self.access_key = access_key
        self.set_header(digital.header_format_default ( self.access_key , 0 ))

    def get_taps(self):
        return self.taps

    def set_taps(self, taps):
        self.taps = taps
        self.digital_pfb_clock_sync_xxx_0.update_taps(self.taps)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.epy_block_1_0_0_0_0.samp_rate = self.samp_rate
        self.epy_block_1_0_0_0_1.samp_rate = self.samp_rate
        self.iio_pluto_sink_0.set_samplerate(self.samp_rate)
        self.iio_pluto_source_0.set_samplerate(self.samp_rate)

    def get_my_constellation(self):
        return self.my_constellation

    def set_my_constellation(self, my_constellation):
        self.my_constellation = my_constellation
        self.digital_constellation_decoder_cb_0.set_constellation(self.my_constellation)

    def get_header(self):
        return self.header

    def set_header(self, header):
        self.header = header
        self.digital_protocol_formatter_bb_0.set_header_format(self.header)

    def get_f_c(self):
        return self.f_c

    def set_f_c(self, f_c):
        self.f_c = f_c
        self.iio_pluto_sink_0.set_frequency(self.f_c)
        self.iio_pluto_source_0.set_frequency(self.f_c)
        self.qtgui_sink_x_0.set_frequency_range(self.f_c, 40000000)

    def get_bw(self):
        return self.bw

    def set_bw(self, bw):
        self.bw = bw
        self.iio_pluto_sink_0.set_bandwidth(self.bw)




def main(top_block_cls=BPSK_test_02_3, options=None):

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
