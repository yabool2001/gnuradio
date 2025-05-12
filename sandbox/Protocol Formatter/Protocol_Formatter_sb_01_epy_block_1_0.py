from gnuradio import gr
import numpy as np
import time
import os

class byte_logger(gr.sync_block):
    def __init__(self, samp_rate=32000, filename="byte_log.csv"):
        gr.sync_block.__init__(self,
            name="BYTE FILE SINK",
            in_sig=[np.uint8],
            out_sig=None)
        self.filename = filename
        self.samp_rate = samp_rate
        self.start_time = time.time()

        file_exists = os.path.isfile(filename)
        self.f = open(filename, "w", encoding="utf-8")

        if not file_exists or os.stat(filename).st_size == 0:
            self.f.write("timestamp;byte;samp_rate\n")

    def work(self, input_items, output_items):
        current_time = time.time()
        elapsed = current_time - self.start_time

        for i, b in enumerate(input_items[0]):
            timestamp = elapsed + (i / self.samp_rate)
            ts = f"{timestamp:.6f}".replace('.', ',')
            val = str(b)
            sr = f"{self.samp_rate:.0f}".replace('.', ',')
            self.f.write(f"{ts};{val};{sr}\n")

        self.f.flush()
        return len(input_items[0])
