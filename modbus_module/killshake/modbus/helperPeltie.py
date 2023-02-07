import modbushelper

class HelperPeltie(modbushelper):
    REGISTER_190 = 0x190
    REGISTER_191 = 0x191
    REGISTER_192 = 0x192
    REGISTER_193 = 0x193
    REGISTER_194 = 0x194
    REGISTER_195 = 0x195

    REGISTER_550 = 0x550
    REGISTER_551 = 0x551
    REGISTER_552 = 0x552
    REGISTER_553 = 0x553

    def getPeltieState(self):
        return self.getRegisterValue(self.REGISTER_190);

    def getPeltieDir(self):
        return self.getRegisterValue(self.REGISTER_191);

    def getPeltieU(self):
        return self.getRegisterValue(self.REGISTER_192);

    def getPeltieT(self):
        return self.getRegisterValue(self.REGISTER_193);

    def getPeltieOTime(self):
        return self.getRegisterValue(self.REGISTER_194);

    def setPeltieCtrl(self, value):
        return self.setRegisterValue(self.REGISTER_550, value);

    def setPeltieDirSp(self, value):
        return self.setRegisterValue(self.REGISTER_551, value);

    def setPeltieURef(self, value):
        return self.setRegisterValue(self.REGISTER_552, value);
    
    def setPeltieCltOTime(self, value):
        return self.setRegisterValue(self.REGISTER_553, value);