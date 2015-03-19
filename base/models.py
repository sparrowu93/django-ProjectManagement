# -*- coding: utf-8 -*-

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User

# Create your models here.

@python_2_unicode_compatible
class Project(models.Model):
    """项目信息"""
    name = models.CharField(max_length=20, verbose_name=u"项目名")
    description = models.TextField(max_length=100, help_text="项目简介", verbose_name=u"项目详情")

    def __str__(self):
        return u'%s' % self.name

    class Meta:
        verbose_name = "项目信息"
        verbose_name_plural = "项目信息"

    def get_unfinished_tasks(self):
        return self.tasks.filter(status=0)

    def get_finished_tasks(self):
        return self.tasks.filter(status=1)



@python_2_unicode_compatible
class Milestone(models.Model):
    """Milestone for the Project"""
    project = models.ForeignKey(Project, related_name="milestones", help_text=u"所属项目", verbose_name=u'所属项目')
    name = models.CharField(max_length=20, help_text=u"项目的阶段性规划", verbose_name=u"里程碑")
    description = models.TextField(max_length=100, help_text=u"具体规划", verbose_name=u"里程碑详情")


    def __str__(self):
        return u'%s' % self.name

    class Meta:
        verbose_name = "项目里程碑信息"
        verbose_name_plural = "项目里程碑信息"


@python_2_unicode_compatible
class Task(models.Model):
    """specfic issue or tasks"""

    CATEGORY_CHOICES = (
        (0,'无'),
        (1,'Bug'),
        (2,'Feature'),
        (3,'Enhancement'),
    )

    STATUS_CHOICES = (
        (1,'已完成'),
        (0,'未完成'),
    )

    PRIORITY_CHOICES = (
        (0,'无'),
        (1,'低'),
        (2,'中'),
        (3,'高'),
    )

    project = models.ForeignKey(Project, related_name="tasks", help_text="所属项目", verbose_name=u'所属项目')
    milestone = models.ForeignKey(Milestone, blank=True, null=True, related_name="tasks", help_text="所属里程碑", verbose_name=u'所属里程碑')
    category  = models.IntegerField(max_length=2, choices=CATEGORY_CHOICES, default=1, help_text="类型", verbose_name=u"类型")
    status  = models.IntegerField(max_length=2, choices=STATUS_CHOICES, default=0, help_text="状态", verbose_name=u"状态")
    priority  = models.IntegerField(max_length=2, choices=PRIORITY_CHOICES, default=0, help_text="优先级", verbose_name=u"优先级")
    name = models.CharField(max_length=20, help_text="任务名", verbose_name=u"任务名称")
    assign_to = models.ForeignKey(User, help_text="任务跟进人", verbose_name=u"负责人")
    description = models.TextField(max_length=100, help_text="issue 内容", verbose_name=u"详情")
    progress = models.IntegerField(max_length=2, default=0, help_text="%", verbose_name=u"进度")
    plan_date = models.DateTimeField(blank=True, null=True, help_text="任务截止日期", verbose_name=u"截止日期")
    due_date = models.DateTimeField(blank=True, null=True, help_text="完成日期", verbose_name=u"完成日期")
    created_time = models.DateTimeField(auto_now_add=True, help_text="初次上传时间", verbose_name=u"初次上传时间")
    updated_time = models.DateTimeField(auto_now=True, help_text="上次更新时间", verbose_name=u"上次更新时间")

    def progress_with_percent_symbol(self):
        return "%d%s" % (self.progress, "%")
    progress_with_percent_symbol.short_description = '进度'

    def __str__(self):
        return u'%s' % self.name

    class Meta:
        verbose_name = "项目任务信息"
        verbose_name_plural = "项目任务信息"
        ordering = ['-priority', 'status', 'progress']
