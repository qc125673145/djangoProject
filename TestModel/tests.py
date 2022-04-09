from django.test import TestCase
from django.http import  HttpResponse
from TestModel.models import  Test
# Create your tests here.
#数据库的操作
def testdb(request):
    #初始化
    response=''
    response1=''
    #通过object 这个模型管理器的all()获取所有数据，相当于sql中slect *from
    list=Test.objects.all()
    #filter相当于sql中where，可以设置过滤条件
    response2=Test.objects.filter(id=1)
    #获取单个对象
    response3=Test.objects.get(id=1)
    #限制返回数据，相当于sqlz中offset 0 limt 2
    Test.objects.order_by('name')[0:2]
    #数据排序
    Test.objects.order_by("id")
    #上面的方法可以连锁使用
    Test.objects.filter(name='runoob').order_by('id')
    #输出所有的数据
    for var in list:
        response1 +=var.name+''
    response=response1
    return HttpResponse("<p>"+response+"<p>")
    #dksljj 