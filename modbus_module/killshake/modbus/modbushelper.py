# import minimalmodbus

PORT = '/dev/cu.usbserial-AC00XX39'
INPUT_REGISTER_100 = 0x100
INPUT_REGISTER_101 = 0x101
INPUT_REGISTER_102 = 0x102
INPUT_REGISTER_103 = 0x103
INPUT_REGISTER_104 = 0x104
INPUT_REGISTER_105 = 0x105
INPUT_REGISTER_106 = 0x106
INPUT_REGISTER_107 = 0x107
INPUT_REGISTER_108 = 0x108
INPUT_REGISTER_120 = 0x120
INPUT_REGISTER_121 = 0x121
INPUT_REGISTER_122 = 0x122
INPUT_REGISTER_123 = 0x123
INPUT_REGISTER_124 = 0x124
INPUT_REGISTER_125 = 0x125
INPUT_REGISTER_126 = 0x126
INPUT_REGISTER_127 = 0x127
INPUT_REGISTER_128 = 0x128
INPUT_REGISTER_129 = 0x129
INPUT_REGISTER_12a = 0x12a
INPUT_REGISTER_12b = 0x12b
INPUT_REGISTER_12c = 0x12c
INPUT_REGISTER_12d = 0x12d
INPUT_REGISTER_12e = 0x12e

# Система термостатирования

INPUT_REGISTER_130 = 0x130
INPUT_REGISTER_131 = 0x131
INPUT_REGISTER_132 = 0x132
INPUT_REGISTER_133 = 0x133
INPUT_REGISTER_134 = 0x134

INPUT_REGISTER_140 = 0x140
INPUT_REGISTER_141 = 0x141
INPUT_REGISTER_142 = 0x142
INPUT_REGISTER_143 = 0x143

INPUT_REGISTER_150 = 0x150
INPUT_REGISTER_151 = 0x151
INPUT_REGISTER_152 = 0x152
INPUT_REGISTER_153 = 0x153

INPUT_REGISTER_160 = 0x160
INPUT_REGISTER_161 = 0x161
INPUT_REGISTER_162 = 0x162
INPUT_REGISTER_163 = 0x163

INPUT_REGISTER_170 = 0x170
INPUT_REGISTER_171 = 0x171
INPUT_REGISTER_172 = 0x172

INPUT_REGISTER_180 = 0x180
INPUT_REGISTER_181 = 0x181
INPUT_REGISTER_182 = 0x182
#
INPUT_REGISTER_190 = 0x190
INPUT_REGISTER_191 = 0x191
INPUT_REGISTER_192 = 0x192
INPUT_REGISTER_193 = 0x193
INPUT_REGISTER_194 = 0x194
INPUT_REGISTER_195 = 0x195
# Система перемешивания         

INPUT_REGISTER_1a0 = 0x1a0
INPUT_REGISTER_1a1 = 0x1a1
INPUT_REGISTER_1a2 = 0x1a2
INPUT_REGISTER_1a3 = 0x1a3
INPUT_REGISTER_1a4 = 0x1a4
INPUT_REGISTER_1a5 = 0x1a5
INPUT_REGISTER_1a6 = 0x1a6
INPUT_REGISTER_1a7 = 0x1a7
INPUT_REGISTER_1a8 = 0x1a8
INPUT_REGISTER_1a9 = 0x1a9

INPUT_REGISTER_1b0 = 0x1b0
INPUT_REGISTER_1b1 = 0x1b1
INPUT_REGISTER_1b2 = 0x1b2
INPUT_REGISTER_1b3 = 0x1b3
INPUT_REGISTER_1b4 = 0x1b4
INPUT_REGISTER_1b5 = 0x1b5
INPUT_REGISTER_1b6 = 0x1b6
INPUT_REGISTER_1b7 = 0x1b7

INPUT_REGISTER_200 = 0x200
INPUT_REGISTER_201 = 0x201

HOLDING_REGISTER_500 = 0x500
REGISTER_501 = 0x501
REGISTER_502 = 0x502
REGISTER_503 = 0x503
REGISTER_504 = 0x504
REGISTER_505 = 0x505

REGISTER_510 = 0x510
REGISTER_511 = 0x511
REGISTER_512 = 0x512
REGISTER_513 = 0x513
REGISTER_514 = 0x514
REGISTER_515 = 0x515
REGISTER_516 = 0x516

REGISTER_520 = 0x520
REGISTER_521 = 0x521
REGISTER_522 = 0x522

REGISTER_530 = 0x530
REGISTER_531 = 0x531
REGISTER_532 = 0x532

REGISTER_540 = 0x540
REGISTER_541 = 0x541
REGISTER_542 = 0x542

REGISTER_560 = 0x560
REGISTER_561 = 0x561
REGISTER_562 = 0x562
REGISTER_563 = 0x563
REGISTER_564 = 0x564
REGISTER_565 = 0x565
REGISTER_566 = 0x566
REGISTER_567 = 0x567

REGISTER_570 = 0x570
REGISTER_571 = 0x571
REGISTER_572 = 0x572
REGISTER_573 = 0x573
REGISTER_574 = 0x574
REGISTER_575 = 0x575
REGISTER_576 = 0x576
REGISTER_577 = 0x577

REGISTER_580 = 0x580
REGISTER_581 = 0x581
REGISTER_582 = 0x582
REGISTER_583 = 0x583
REGISTER_584 = 0x584
REGISTER_585 = 0x585
REGISTER_586 = 0x586
REGISTER_587 = 0x587

REGISTER_590 = 0x590
REGISTER_591 = 0x591
REGISTER_592 = 0x592
REGISTER_593 = 0x593
REGISTER_594 = 0x594
REGISTER_595 = 0x595

REGISTER_600 = 0x600
REGISTER_601 = 0x601
REGISTER_602 = 0x602

REGISTER_610 = 0x610
REGISTER_62F = 0x62f


class ModbusHelper:
    INPUT_REGISTERS = [INPUT_REGISTER_100,
                       INPUT_REGISTER_101,
                       INPUT_REGISTER_102,
                       INPUT_REGISTER_103,
                       INPUT_REGISTER_104,
                       INPUT_REGISTER_105,
                       INPUT_REGISTER_106,
                       INPUT_REGISTER_107,
                       INPUT_REGISTER_108,
                       INPUT_REGISTER_120,
                       INPUT_REGISTER_121,
                       INPUT_REGISTER_122,
                       INPUT_REGISTER_123,
                       INPUT_REGISTER_124,
                       INPUT_REGISTER_125,
                       INPUT_REGISTER_126,
                       INPUT_REGISTER_127,
                       INPUT_REGISTER_128,
                       INPUT_REGISTER_129,
                       INPUT_REGISTER_12a,
                       INPUT_REGISTER_12b,
                       INPUT_REGISTER_12c,
                       INPUT_REGISTER_12d,
                       INPUT_REGISTER_12e,
                       INPUT_REGISTER_130,
                       INPUT_REGISTER_131,
                       INPUT_REGISTER_132,
                       INPUT_REGISTER_133,
                       INPUT_REGISTER_134,

                       INPUT_REGISTER_140,
                       INPUT_REGISTER_141,
                       INPUT_REGISTER_142,
                       INPUT_REGISTER_143,

                       INPUT_REGISTER_150,
                       INPUT_REGISTER_151,
                       INPUT_REGISTER_152,
                       INPUT_REGISTER_153,

                       INPUT_REGISTER_160,
                       INPUT_REGISTER_161,
                       INPUT_REGISTER_162,
                       INPUT_REGISTER_163,

                       INPUT_REGISTER_170,
                       INPUT_REGISTER_171,
                       INPUT_REGISTER_172,

                       INPUT_REGISTER_180,
                       INPUT_REGISTER_181,
                       INPUT_REGISTER_182,

                       INPUT_REGISTER_190,
                       INPUT_REGISTER_191,
                       INPUT_REGISTER_192,
                       INPUT_REGISTER_193,
                       INPUT_REGISTER_194,
                       INPUT_REGISTER_195,
                       INPUT_REGISTER_1a0,
                       INPUT_REGISTER_1a1,
                       INPUT_REGISTER_1a2,
                       INPUT_REGISTER_1a3,
                       INPUT_REGISTER_1a4,
                       INPUT_REGISTER_1a5,
                       INPUT_REGISTER_1a6,
                       INPUT_REGISTER_1a7,
                       INPUT_REGISTER_1a8,
                       INPUT_REGISTER_1a9,

                       INPUT_REGISTER_1b0,
                       INPUT_REGISTER_1b1,
                       INPUT_REGISTER_1b2,
                       INPUT_REGISTER_1b3,
                       INPUT_REGISTER_1b4,
                       INPUT_REGISTER_1b5,
                       INPUT_REGISTER_1b6,
                       INPUT_REGISTER_1b7,

                       INPUT_REGISTER_200,
                       INPUT_REGISTER_201
                       ]
    HOLDING_REGISTERS = [
        HOLDING_REGISTER_500,
        REGISTER_501,
        REGISTER_502,
        REGISTER_503,
        REGISTER_504,
        REGISTER_505,

        REGISTER_510,
        REGISTER_511,
        REGISTER_512,
        REGISTER_513,
        REGISTER_514,
        REGISTER_515,
        REGISTER_516,

        REGISTER_520,
        REGISTER_521,
        REGISTER_522,

        REGISTER_530,
        REGISTER_531,
        REGISTER_532,

        REGISTER_540,
        REGISTER_541,
        REGISTER_542,

        REGISTER_560,
        REGISTER_561,
        REGISTER_562,
        REGISTER_563,
        REGISTER_564,
        REGISTER_565,
        REGISTER_566,
        REGISTER_567,

        REGISTER_570,
        REGISTER_571,
        REGISTER_572,
        REGISTER_573,
        REGISTER_574,
        REGISTER_575,
        REGISTER_576,
        REGISTER_577,

        REGISTER_580,
        REGISTER_581,
        REGISTER_582,
        REGISTER_583,
        REGISTER_584,
        REGISTER_585,
        REGISTER_586,
        REGISTER_587,

        REGISTER_590,
        REGISTER_591,
        REGISTER_592,
        REGISTER_593,
        REGISTER_594,
        REGISTER_595,

        REGISTER_600,
        REGISTER_601,
        REGISTER_602,

        REGISTER_610,
        REGISTER_62F
    ]

    def __init__(self):
        print("Init")

    def getInputRegisterValue(self, register_no):
        if not self.__isInputRegister(register_no):
            raise ValueError('Error input parameter')
        return self.__bit_reverse(register_no)

    def getHoldingRegisterValue(self, register_no):
        if not self.__isHoldingRegister(register_no):
            raise ValueError('Error input parameter')
        return self.__bit_reverse(register_no)

    def setHoldingRegisterValue(self, register_no, value):
        if not self.__isHoldingRegister(register_no):
            raise ValueError('Error input parameter')
        print('value: ' + hex(value))
        print('value: ' + hex(self.__bit_reverse(value)))
        return self.__bit_reverse(value)
     
    def __isInputRegister(self, register_no):
        return register_no in self.INPUT_REGISTERS

    def __isHoldingRegister(self, register_no):
        return register_no in self.HOLDING_REGISTERS

    def __bit_reverse(self, n):
      return int(bin(n)[2:].zfill((n.bit_length()//8+1)*8)[::-1], base=2)