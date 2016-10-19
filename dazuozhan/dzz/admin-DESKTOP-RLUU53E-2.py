# -*-coding:utf-8 -*-
from django.contrib import admin
from django.conf.urls import url

from django.utils.html import format_html
# Register your models here.
from .models import Jinhuoqudao, Yifu, ChukuLog, RukuLog, Jiagewenjian, Huiyuan, Xiaofeijilu
from django.template.response import TemplateResponse, HttpResponse
import json

from django.urls import reverse
import codecs

admin.site.register(Jinhuoqudao)

from dss.Serializer import serializer


class YiFuAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('name', 'tiaomahao', 'guige', 'yanse', 'qudao')
        }),
        ('其他', {
            'classes': ('collapse',),
            'fields': ('jiage', 'chengben'),
        }),
    )
    #
    # def view_on_site(self, obj):
    #     url = reverse('admin', kwargs={'name': obj.name})
    #     return 'https://example.com' + url
    list_display = ('name', 'tiaomahao', 'guige', 'yanse', 'qudao', 'jiage')
    search_fields = ('name', 'tiaomahao')
    list_filter = ('qudao',)
    save_as = True

    def json_yifu(self, request, iid):
        "提案查询和提交按钮的连接"
        fb = {"data": False}
        try:


            yifuinfo = Yifu.objects.filter(tiaomahao=iid)
            fb['yifu'] = yifuinfo[0]
            fb['kucun'] = len(yifuinfo)
        except Exception as e:
            print e
            fb['data'] = False


        return HttpResponse(json.dumps(serializer(fb)), content_type="application/json")

    def get_urls(self):
        urls = super(YiFuAdmin, self).get_urls()
        my_urls = [
            url(r'^json_yifu/(?P<iid>\w+)/$', self.admin_site.admin_view(self.json_yifu)),
            url(r'^my_view/$', self.admin_site.admin_view(self.my_view)),
        ]
        return my_urls + urls



    def my_view(self, request):
        # ...
        context = dict(
            # Include common variables for rendering the admin template.
            self.admin_site.each_context(request),
            # Anything else you want in the context...
            key='test',
        )
        return TemplateResponse(request, "sometemplate.html", context)


class JiagewenjianAdmin(admin.ModelAdmin):
    list_display = ('filename', 'caozuoren', 'time', 'calcnew', 'uploadfile')

    def get_urls(self):
        urls = super(JiagewenjianAdmin, self).get_urls()
        my_urls = [
            url(r'^calc/(?P<iid>\w+)/$', self.admin_site.admin_view(self.my_view)),
        ]
        return my_urls + urls

    def my_view(self, request, iid):
        # ...

        tf = Jiagewenjian.objects.get(pk=iid)

        newprices = []
        with codecs.open('%s' % tf.uploadfile, "r", "utf-8-sig") as f:
            if tf.filename == u'1':
                for line in f:

                    cb = int(line)

                    if cb <= 100:
                        newprice = cb * 2 * 1.25
                    elif cb <= 300:
                        newprice = cb * 1.85 * 1.25
                    else:
                        newprice = cb * 1.8 * 1.25
                    newprices.append(int(newprice))

            else:
                for line in f:
                    ll = line.split(' ')
                    try:
                        if len(ll) < 6:
                            continue
                    except Exception as e:
                        print e
                        continue

                    name = ll[0]
                    tiaomahao = ll[1]
                    guige = ll[2]
                    yanse = ll[3]
                    qudao = ll[4]
                    chengben = ll[5]

                    fqd = Jinhuoqudao.objects.filter(name=qudao)

                    if fqd.count() > 0:
                        fqd = fqd[0]
                    else:
                        fqd = Jinhuoqudao.objects.create(name=fqd)
                    try:
                        if chengben == '-':
                            pass
                        else:
                            chengben = int(chengben)

                            if chengben <= 100:
                                jiage = chengben * 2 * 1.25
                            elif chengben <= 300:
                                jiage = chengben * 1.85 * 1.25
                            else:
                                jiage = chengben * 1.8 * 1.25
                    except Exception as e:
                        print e
                        chengben = '-'
                        jiage = '-'
                    Yifu.objects.create(name=name, tiaomahao=tiaomahao, guige=guige, qudao=fqd, yanse=yanse,
                                        jiage=jiage, chengben=chengben)

        if tf.filename == u'1':
            context = dict(
                # Include common variables for rendering the admin template.
                self.admin_site.each_context(request),
                # Anything else you want in the context...
                newprices=newprices,
            )

            # with open('filename', 'wt') as f:
            #     f.write('hello, world!')
            return TemplateResponse(request, "sometemplate.html", context)

    def calcnew(self, obj):
        return format_html('<a href="/admin/dzz/jiagewenjian/calc/%s">操作</a>' % obj.pk)

    calcnew.short_description = ''

    actions = ['wenjiandaoru']

    def wenjiandaoru(self, request, queryset):
        notcount = 0
        errcount = 0
        okcount = 0
        for one in queryset.all():

            if one.filename == u'0':
                try:
                    with codecs.open('upload/%s' % one.uploadfile, "r", "utf-8-sig") as f:
                        for line in f:
                            ll = line.split('	')
                            try:
                                if len(ll) < 6:
                                    continue
                            except Exception as e:
                                print e
                                continue

                            name = ll[0]
                            if name:
                                tiaomahao = ll[1]
                                guige = ll[2]
                                yanse = ll[3]
                                qudao = ll[5]
                                chengben = ll[4]
                                fqd = Jinhuoqudao.objects.filter(name=qudao)
                                if fqd.count() > 0:
                                    fqd = fqd[0]
                                else:
                                    fqd = Jinhuoqudao.objects.create(name=qudao)
                                try:
                                    if chengben == '-':
                                        pass
                                    else:
                                        chengben = int(chengben)

                                        if chengben <= 100:
                                            jiage = chengben * 2 * 1.25
                                        elif chengben <= 300:
                                            jiage = chengben * 1.85 * 1.25
                                        else:
                                            jiage = chengben * 1.8 * 1.25
                                except Exception as e:
                                    print e
                                    chengben = '-'
                                    jiage = '-'
                                Yifu.objects.create(name=name, tiaomahao=tiaomahao, guige=guige, qudao=fqd, yanse=yanse,
                                                    jiage=jiage, chengben=chengben)
                    okcount += 1
                except Exception as e:
                    print e
                    errcount += 1
            else:
                notcount += 1
                return TemplateResponse(request, "shouyin.html", context)
        self.message_user(request, "导入失败文件数量:%s,成功文件数量:%s,非导入文件勾选数量:%s." % (errcount, okcount, notcount))

    wenjiandaoru.short_description = '执行文件批量导入'


class RukuAdmin(admin.ModelAdmin):
    list_display = ('yifu', 'caozuoren', 'time')
    search_fields = ('yifu', 'caozuoren', 'time')
    actions_on_bottom = True
    actions_on_top = True
    save_on_top = True


class HuiyuanAdmin(admin.ModelAdmin):
    list_display = ('name', 'jifen', 'birthday')
    exclude = ('last_xiaofei', 'zongxiaofeijine', 'zongxiaofeicishu', 'last_xiaofeijine', 'jifen', 'shengrizengpin')


class XiaofeijiluAdmin(admin.ModelAdmin):
    list_display = ('huiyuan', 'jifen', 'xiaofeijine', 'get_products', 'xiaofeishijian')

    def get_products(self, obj):
        return format_html(" ".join(["<a href='/admin/dzz/yifu/%s'>%s</a>" % (p.pk, p.name) for p in obj.yifu.all()]))

    get_products.short_description = '购买的物品'

    def get_urls(self):
        urls = super(XiaofeijiluAdmin, self).get_urls()
        my_urls = [
            url(r'^shouyin/$', self.my_view),
        ]
        return my_urls + urls

    def my_view(self, request):
        # ...
        context = dict(
            # Include common variables for rendering the admin template.
            self.admin_site.each_context(request),
            # Anything else you want in the context...
            yifu=Yifu.objects.all(),
            huiyuan=Huiyuan.objects.all()

        )
        return TemplateResponse(request, "shouyin.html", context)


admin.site.register(Yifu, YiFuAdmin)
admin.site.register(ChukuLog, RukuAdmin)
admin.site.register(RukuLog, RukuAdmin)
admin.site.register(Jiagewenjian, JiagewenjianAdmin)
admin.site.register(Huiyuan, HuiyuanAdmin)
admin.site.register(Xiaofeijilu, XiaofeijiluAdmin)
