# -*-coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Jinhuoqudao(models.Model):
    name = models.CharField(max_length=32, verbose_name="名称")

    class Meta:
        verbose_name = "渠道商"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


wenjianleixing = ((u'1', u'售价计算'), (u'0', u'批量入库'))


class Jiagewenjian(models.Model):
    filename = models.CharField(verbose_name="文件名", max_length=16, choices=wenjianleixing, blank=False, null=False,
                                default=u'1')
    uploadfile = models.FileField(verbose_name="成本价格文件", upload_to='./')
    time = models.DateTimeField(verbose_name="操作时间", auto_created=True, auto_now_add=True)
    caozuoren = models.CharField(max_length=16, verbose_name="执行人")

    class Meta():
        verbose_name = "价格文件"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.filename


#
# class Guige(models.Model):
#
class YifuManager(models.Manager):
    def all(self, keyword):
        return self.order_by("sold")

class Yifu(models.Model):
    name = models.CharField(max_length=32, verbose_name="名称")
    uploadfile = models.FileField(verbose_name="图片", upload_to='./',null=True,blank=True,default="default.png")
    tiaomahao = models.CharField(max_length=32, verbose_name="条码号")
    guige = models.CharField(max_length=32, verbose_name="规格")
    yanse = models.CharField(max_length=32, verbose_name="颜色")
    qudao = models.ForeignKey(Jinhuoqudao, verbose_name="渠道")
    jiage = models.CharField(max_length=8, verbose_name="价格", default='', null=True, blank=True)
    chengben = models.CharField(max_length=8, verbose_name="成本", default='', null=True, blank=True)
    jifen = models.CharField(max_length=8, verbose_name="积分", default='', null=True, blank=True)
    dsq = models.CharField(max_length=8, verbose_name="记一分", default='', null=True, blank=True)
    sold = models.BooleanField(default=False,verbose_name="是否卖掉")

    # jifen = models.CharField(max_length=8,verbose_name="积分",default='',null=True)
  
        

    class Meta():
        verbose_name = "货物信息"
        verbose_name_plural = verbose_name
        ordering = ['-sold']
    def __unicode__(self):
        return self.tiaomahao

    def save(self, *args, **kwargs):
        if self.chengben:
            cb = int(self.chengben)

            if cb <= 100:
                newprice = cb * 2 * 1.25
            elif cb <= 300:
                newprice = cb * 1.85 * 1.25
            else:
                newprice = cb * 1.8 * 1.25
            if not self.jiage:
                self.jiage = str(int(newprice))

        super(Yifu, self).save(*args, **kwargs)


class ChukuLog(models.Model):
    yifu = models.ForeignKey(Yifu, verbose_name="衣服")
    time = models.DateTimeField(verbose_name="操作时间", auto_created=True, auto_now_add=True)
    caozuoren = models.CharField(max_length=16, verbose_name="执行人")

    class Meta():
        verbose_name = "出库日志"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return "%s减少了一件%s" % (self.caozuoren, self.yifu)


class RukuLog(models.Model):
    yifu = models.ForeignKey(Yifu, verbose_name="衣服")
    time = models.DateTimeField(verbose_name="操作时间", auto_created=True, auto_now_add=True)
    caozuoren = models.CharField(max_length=16, verbose_name="执行人")

    class Meta():
        verbose_name = "入库日志"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return "%s添加了一件%s" % (self.caozuoren, self.yifu)


shifou = ((1, u'女'), (0, u'男'))
lingqu = ((1, u'已领取'), (0, u'未领取'))

import datetime

def yestoday():
  return datetime.date.today() - datetime.timedelta(days=1)

class Huiyuan(models.Model):
    name = models.CharField(max_length=8, verbose_name="姓名")
    sex = models.BooleanField(verbose_name="性别", choices=shifou, default=1)
    cellphone = models.CharField(verbose_name="手机号", max_length=11, default='', blank=True, null=True)
    birthday = models.DateField(verbose_name="生日", blank=True, null=True)
    touxiang = models.CharField(verbose_name="头像", max_length=32, blank=True, null=True, default='')
    lianxidizhi = models.CharField(verbose_name="联系地址", blank=True, null=True, max_length=128)
    jifen = models.IntegerField(verbose_name="积分", default=0, blank=True, null=True)
    last_xiaofei = models.DateTimeField(verbose_name="最近一次消费时间", null=True, blank=True,default=yestoday)
    last_xiaofeijine = models.IntegerField(verbose_name="最近一次消费金额", null=True, blank=True, default=0)
    zongxiaofeijine = models.IntegerField(verbose_name="总消费金额", null=True, blank=True, default=0)
    zongxiaofeicishu = models.IntegerField(verbose_name="总消费次数", null=True, blank=True, default=0)
    beizhu = models.TextField(verbose_name="备注", null=True, blank=True)
    shengrizengpin = models.BooleanField(verbose_name="生日奖励已领取", choices=lingqu, default=0)

    class Meta():
        verbose_name = "会员"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class Xiaofeijilu(models.Model):
    huiyuan = models.ForeignKey(Huiyuan, verbose_name="会员")
    jifen = models.IntegerField(verbose_name="积分", default=0, blank=True, null=True)
    xiaofeishijian = models.DateTimeField(verbose_name="消费时间", auto_now_add=True)
    xiaofeijine = models.IntegerField(verbose_name="消费金额", null=True, blank=True, default=0)
    yifu = models.ManyToManyField(Yifu, verbose_name="所购物品", blank=True, related_name="yifu")
    beizhu = models.TextField(verbose_name="备注", null=True, blank=True)
    fapiao = models.BooleanField(verbose_name="发票已领取", choices=lingqu, default=0)

    class Meta:
        verbose_name = "收银"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return '%s%s' % (self.huiyuan, self.xiaofeijine)
