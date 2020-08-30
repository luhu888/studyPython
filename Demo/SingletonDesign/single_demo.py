class Baby:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self, pants, clothe):
        self.pants = pants
        self.clothe = clothe


baby1 = Baby('牛仔裤', '皮夹克')
baby2 = Baby('运动裤', '卫衣')
print(baby1.clothe, baby1.pants)
print(baby2.clothe, baby2.pants)



