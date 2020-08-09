# 动物园类
# 动物园类要求有“名字”的属性和“添加动物”的方法，
# “添加动物”方法要实现同一个动物实例不能被重复添加。
class Zoo(object):
    def __init__(self, name):
        self.animal = {}
        self.name = name
    def add_animal(self, obj_animal):
        if obj_animal in self.animal:
            print('该动物已存在')
            return self.animal[obj_animal]
        else:
            self.animal[obj_animal] = obj_animal
            print('添加成功')
            return True

# 动物类
# 定义“体型”（大、中、小）、“类型”（肉、草、杂）、“性格”（凶、顺）、“是否属于凶猛动物”四个属性，
# 是否属于凶猛动物的标准是：
# “体型>=中等”并且是“食肉类型”同时“性格凶猛”；
class Animal(object):
    size_dict = {
        '小型':1,
        '中型':2,
        '大型':3,
    }
    eat_type = {
        '食肉':True,
        '食草':False,
        '杂食':False,
    }
    fierce_flag = {
        '凶猛':True,
        '温顺':False,        
    }
    def __init__(self, eat, size, fierce):
        super().__init__()
        self.size = Animal.size_dict[size]
        self.eat = Animal.eat_type[eat]
        self.fierce = Animal.fierce_flag[fierce]
        if self.size>=2 and self.eat==True and self.fierce==True:
            self.is_fierce_flag = True
        else:
            self.is_fierce_flag = False

# 猫类
# 猫类要求定义“叫声”、“是否合适作为宠物”以及“名字”三个属性，
# 其中“叫声”作为类属性，猫类继承自动物类；
class Cat(Animal):
    cry = '喵喵喵'
    def __init__(self, name, size, eat, fierce, for_pet=False):
        super().__init__(size, eat, fierce)
        self.name = name
        self.for_pet = for_pet

def getattr(cls1,name):
    for key in cls1.animal.keys():
        if name in key:
            print("有%s这个动物" % (name))
            break
        else:
            print("没有%s这个动物" % (name))

if __name__ == '__main__':
    # 实例化动物园
    z = Zoo('时间动物园')
    # 实例化一只猫，属性包括名字、类型、体型、性格
    cat1 = Cat('大花猫1', '食肉', '小型', '温顺')
    # 增加一只猫到动物园
    z.add_animal(cat1)
    # 动物园是否有猫这种动物
    getattr(z, 'Cat')