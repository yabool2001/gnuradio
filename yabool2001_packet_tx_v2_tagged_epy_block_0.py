import numpy as np
from gnuradio import gr
import pmt

class pmt_to_stream(gr.sync_block):
    def __init__(self):
        gr.sync_block.__init__(self,
            name="PMT 2 STREAM",
            in_sig=None,
            out_sig=[np.uint8])  # strumień bajtów (uint8)
        self.message_port_register_in(pmt.intern("in"))
        self.set_msg_handler(pmt.intern("in"), self.handle_msg)
        self.message = None  # None = brak danych

    def handle_msg(self, msg):
        if pmt.is_u8vector(msg):
            vec = pmt.u8vector_elements(msg)
            if len(vec) > 0:
                self.message = bytearray(vec)
            else:
                self.message = None
        else:
            self.message = None

    def work(self, input_items, output_items):
        out = output_items[0]
        if self.message:
            # wypuść tylko tyle, ile mamy miejsca
            length = min(len(out), len(self.message))
            out[:length] = np.frombuffer(self.message[:length], dtype=np.uint8)
            self.message = None  # wyczyść bufor po jednym pakiecie
            return length
        return 0
