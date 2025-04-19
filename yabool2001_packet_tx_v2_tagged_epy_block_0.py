import numpy as np
from gnuradio import gr
import pmt

class pmt_to_stream(gr.sync_block):
    def __init__(self):
        gr.sync_block.__init__(self,
            name="PMT 2 STREAM",
            in_sig=None,
            out_sig=[np.byte])  # Wyjście jako strumień bajtów
        self.message_port_register_in(pmt.intern("in"))
        self.set_msg_handler(pmt.intern("in"), self.handle_msg)

    def handle_msg(self, msg):
        # Przekształć wiadomość (PMT) na bajty
        self.message = pmt.to_python(msg)
        if pmt.is_u8vector(msg):
            self.message = bytearray(pmt.u8vector_elements(msg))
        if isinstance(self.message, str):
            self.message = bytearray(self.message, 'utf-8')
        elif isinstance(self.message, bytes):
            self.message = bytearray(self.message)
        else:
            self.message = bytearray()

    def work(self, input_items, output_items):
        if hasattr(self, 'message') and self.message:
            # Skopiuj dane do wyjścia
            output_items[0][:len(self.message)] = self.message
            self.message = bytearray()  # Wyczyść wiadomość po wysłaniu
            return len(output_items[0])
        return 0