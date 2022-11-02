class TruongThuySon:
    def __init__(self, vukhi, tuoi):
        self.vukhi=vukhi
        self.tuoi=tuoi
    def info(self):
        print("vu khi: ", self.vukhi)
        print("Tuoi: ", self.tuoi)
TTS1=TruongThuySon("kiem",20)
TTS2=TruongThuySon("cung",29)
TTS1.info()
TTS2.info()
class TruongVoKy(TruongThuySon):
    def __init__(self, vukhi, tuoi,level):
        super().__init__(vukhi, tuoi)
        self.level=level
    def infoTVK(self):
        print("vu khi: ", self.vukhi)
        print("tuoi: ", self.tuoi)
        print("level: ",self.level)
TVK1=TruongVoKy("dao","33","lv120")
TVK1.infoTVK()
TVK2=TruongVoKy("kunai",33,"lv300")
TVK2.infoTVK()
if isinstance(TTS2,TruongThuySon)==True:
    print("Đối tượng TTS2 là thực thể của class TruongThuySon")
if isinstance(TTS2,TruongVoKy)==True:
    print("Đối tượng TTS2 là thực thể của class TruongVoKy")
if isinstance(TVK1,TruongThuySon)==True:
    print("Đối tượng TVK1 là thực thể của class TruongThuySon")
if isinstance(TVK1,TruongVoKy)==True:
    print("Đối tượng TVK1 là thực thể của class TruongVoKy")




