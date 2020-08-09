学习笔记

创建一个类就会创建一个类的名称空间，用来存储类中定义的所有名字，这些名字称为类的属性
而类有两种属性：静态属性和动态属性
静态属性就是直接在类中定义的变量
动态属性就是定义在类中的方法
类的数据属性是共享给所有对象的，而类的动态属性是绑定到所有对象的。
创建一个对象/实例就会创建一个对象/实例的名称空间，存放对象/实例的名字，称为对象/实例的属性

属性的查找顺序
在obj.name会先从obj自己的名称空间里找name，找不到则去类中找，类也找不到就找父类...最后都找不到就抛出异常。
类的三大特性：继承、封装、多态

在python中新建的类可以继承一个或多个父类，父类有称基类或超类，新建的类称为派生类或子类

property本质不是函数，而是特殊类 如果实现了__get__()和__set__数据描述符 如果仅仅定义了__get__(),则称为数据描述符

面向对象编程-继承 object 和 type都属于type类（class 'type'） type 元类 object的父类为空，没有继承任何类 type的父类为object类 单一继承 多重继承 菱形继承 MRO MRO和C3算法 super._getattribute print('object', object.class, object.bases) print('type', type.class, type.bases)
type元类由type自身创建，object类由元类type创建
type类继承了object类
新式类 广式优先 .mro 显示调用顺序 有向无环图DAG (入度为0的节点)

solid设计原则与设计模式&单例模式 单一责任原则
开发封闭原则 里氏替换原则 单例模式 1、对象只存在一个实例 new 静态方法 init 实例方法 __new__先被调用，__init__后被调用 装饰器 1、装饰器 2、new 3、import

工厂模式 静态工厂模式 根据传入的参数不同，创建不同的类 类工厂模式

元类 创建类的类 type,是类的模板 控制如何来创建类， 元类的实例为类 创建元类的两种方法 1、type 2、class

type(类名称，父类的元祖，类的成员) Foo = type('Foo',(),{'say_hi':hi})

metaclass = DelValue 元类 元类必须继承type 必须实现new方法 13 mixin 抽象基类 避免继承错误，使类层次易于理解和维护 无法实现化基类 如果忘记在其中一个子类中实现接口方法，要及早报错 abstractmethod Minxin bases