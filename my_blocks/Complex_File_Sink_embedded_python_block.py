from gnuradio import gr
import numpy as np
import time
import os

class complex_logger(gr.sync_block):
    def __init__(self, samp_rate=32000, filename="complex_log.csv"):
        gr.sync_block.__init__(self,
            name="COMPLEX FILE SINK",
            in_sig=[np.complex64],
            out_sig=None)
        self.filename = filename
        self.samp_rate = samp_rate
        self.start_time = time.time()

        file_exists = os.path.isfile(filename)
        self.f = open(filename, "w", encoding="utf-8")

        if not file_exists or os.stat(filename).st_size == 0:
            self.f.write("timestamp;real;imag;samp_rate\n")

    def work(self, input_items, output_items):
        current_time = time.time()
        elapsed = current_time - self.start_time

        for c in input_items[0]:
            timestamp = elapsed
            ts = f"{timestamp:.6f}".replace('.', ',')
            re = f"{c.real:.6f}".replace('.', ',')
            im = f"{c.imag:.6f}".replace('.', ',')
            sr = f"{self.samp_rate:.0f}".replace('.', ',')
            self.f.write(f"{ts};{re};{im};{sr}\n")
            elapsed += 1 / self.samp_rate

        self.f.flush()
        return len(input_items[0])
