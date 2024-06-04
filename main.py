from generators.BBS import BBS
from generators.LCG import LCG
from generators.LFSR import LFSR
from build_histogram import BuildHistogram


if __name__ == "__main__":

    lcg = LCG(seed=123, a=1103515245, c=12345, m=2**31)
    bbs = BBS(seed=743, p=383, q=503)
    lfsr = LFSR(seed=0b10101, taps=[0, 2, 3, 4])

    def generate_sequence(generator, length):
        sequence = []
        for _ in range(length):
            value = generator.next()
            bits = bin(value)[2:].zfill(8)
            sequence.append(bits)
        return ''.join(sequence)

    def bits_to_text(bit_string):
        n = 8
        chars = [int(bit_string[i:i+n], 2) for i in range(0, len(bit_string), n)]
        return chars

    lengths = [50, 100, 1000]

    for length in lengths:

        lcg_seq = generate_sequence(lcg, length * 8)
        lcg_text = bits_to_text(lcg_seq)
        BuildHistogram(lcg_text, length, 'LCG')

        bbs_seq = generate_sequence(bbs, length * 8)
        bbs_text = bits_to_text(bbs_seq)
        BuildHistogram(bbs_text, length, 'BBS')

        lfsr_seq = generate_sequence(lfsr, length * 8)
        lfsr_text = bits_to_text(lfsr_seq)
        BuildHistogram(lfsr_text, length, 'LFSR')
