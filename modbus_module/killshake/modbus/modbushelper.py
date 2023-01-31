#import minimalmodbus

PORT='/dev/cu.usbserial-AC00XX39'
REGISTER_100 = 0x100
REGISTER_101 = 0x101
REGISTER_102 = 0x102
REGISTER_103 = 0x103
REGISTER_104 = 0x104
REGISTER_105 = 0x105
REGISTER_106 = 0x106
REGISTER_107 = 0x107
REGISTER_108 = 0x108
REGISTER_120 = 0x120
REGISTER_121 = 0x121
REGISTER_122 = 0x122
REGISTER_123 = 0x123
REGISTER_124 = 0x124
REGISTER_125 = 0x125
REGISTER_126 = 0x126
REGISTER_127 = 0x127
REGISTER_128 = 0x128
REGISTER_129 = 0x129
REGISTER_12a = 0x12a
REGISTER_12b = 0x12b
REGISTER_12c = 0x12c
REGISTER_12d = 0x12d
REGISTER_12e = 0x12e


# Система термостатирования

REGISTER_130 = 0x130
REGISTER_131 = 0x131
REGISTER_132 = 0x132
REGISTER_133 = 0x133
REGISTER_134 = 0x134

REGISTER_140 = 0x140
REGISTER_141 = 0x141
REGISTER_142 = 0x142
REGISTER_143 = 0x143

REGISTER_150 = 0x150
REGISTER_151 = 0x151
REGISTER_152 = 0x152
REGISTER_153 = 0x153

REGISTER_160 = 0x160
REGISTER_161 = 0x161
REGISTER_162 = 0x162
REGISTER_163 = 0x163

REGISTER_170 = 0x170
REGISTER_171 = 0x171
REGISTER_172 = 0x172

REGISTER_180 = 0x180
REGISTER_181 = 0x181
REGISTER_182 = 0x182

REGISTER_190 = 0x190
REGISTER_191 = 0x191
REGISTER_192 = 0x192
REGISTER_193 = 0x193
REGISTER_194 = 0x194
REGISTER_195 = 0x195

# Система перемешивания         

REGISTER_1a0 = 0x1a0
REGISTER_1a1 = 0x1a1
REGISTER_1a2 = 0x1a2
REGISTER_1a3 = 0x1a3
REGISTER_1a4 = 0x1a4
REGISTER_1a5 = 0x1a5
REGISTER_1a6 = 0x1a6
REGISTER_1a7 = 0x1a7
REGISTER_1a8 = 0x1a8
REGISTER_1a9 = 0x1a9

REGISTER_1b0 = 0x1b0
REGISTER_1b1 = 0x1b1
REGISTER_1b2 = 0x1b2
REGISTER_1b3 = 0x1b3
REGISTER_1b4 = 0x1b4
REGISTER_1b5 = 0x1b5
REGISTER_1b6 = 0x1b6
REGISTER_1b7 = 0x1b7

REGISTER_200 = 0x200
REGISTER_201 = 0x201

REGISTER_500 = 0x500
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

REGISTER_550 = 0x550
REGISTER_551 = 0x551
REGISTER_552 = 0x552
REGISTER_553 = 0x553

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
  def __init(self):
    print("Init")

  def getRegisterValue(self, register_no):
    return register_no

  def setRegisterValue(self, register_no, value):
    return value*register_no
