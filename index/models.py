from django.db import models


# Create your models here.
# 在MySQL中创建对应的一个表
# class UserInfo(models.Model):
#     # 创建字段
#     name = models.CharField(max_length=32)
#     password = models.CharField(max_length=64)
#     age = models.IntegerField()

# 设置对象结构（对应数据库的结构）
class UserInfo(models.Model):
    id = models.CharField(max_length=50,primary_key=True)  # 字符串类型字段
    name = models.CharField(max_length=50)  # 字符串类型字段
    password = models.CharField(max_length=50)  # 字符串类型字段
    age = models.IntegerField(default=0)  # 整数类型字段
    # date = models.DateField('date registered')  # 时间类型字段，参数为人类可读的字段名

# class Diary(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)  # 外键
#     content = models.TextField()  # 文本类型字段

