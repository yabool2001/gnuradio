import numpy as np
from gnuradio import gr
import pmt

class pmt_to_stream(gr.sync_block):
    def __init__(self):
        gr.sync_block.__init__(self,
            name="PMT 2 STREAM (z buforem)",
            in_sig=None,
            out_sig=[np.uint8])

        self.message_port_register_in(pmt.intern("in"))
        self.set_msg_handler(pmt.intern("in"), self.handle_msg)
        self.message_queue = []

    def handle_msg(self, msg):
        if pmt.is_u8vector(msg):
            vec = pmt.u8vector_elements(msg)
            self.message_queue.extend(vec)

    def work(self, input_items, output_items):
        out = output_items[0]
        if self.message_queue:
            out[0] = self.message_queue.pop(0)
            return 1
        return 0
