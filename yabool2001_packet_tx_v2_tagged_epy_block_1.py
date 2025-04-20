from gnuradio import gr
import numpy as np
import time

class complex_logger(gr.sync_block):
    def __init__(self, filename="yabool2001_packet_tx_v2-tagged_output.txt"):
        gr.sync_block.__init__(self,
            name="COMPLEX LOG",
            in_sig=[np.complex64],
            out_sig=None)
        self.f = open(filename, "a")
        self.start_time = time.time()
        self.sample_index = 0

    def work(self, input_items, output_items):
        current_time = time.time()
        elapsed = current_time - self.start_time
        samp_rate = self.sample_rate()

        for i, c in enumerate(input_items[0]):
            timestamp = elapsed + (i / samp_rate)
            self.f.write(f"{timestamp:.6f},{c.real:.6f},{c.imag:.6f}\n")

        self.f.flush()
        return len(input_items[0])

    def sample_rate(self):
        # Spróbuj odczytać próbkującą częstotliwość z upstream
        try:
            return self.sample_rate_hz
        except AttributeError:
            # Domyślna wartość jeśli nie ustawiona
            return 65105  # <- możesz dopasować do swojego systemu
