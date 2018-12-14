# Generated by Django 2.0 on 2018-12-10 17:25

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('orgs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(max_length=200, upload_to='course/', verbose_name='课程图片')),
                ('name', models.CharField(max_length=200, verbose_name='课程名称')),
                ('study_time', models.IntegerField(default=0, verbose_name='课程时间')),
                ('study_num', models.IntegerField(default=0, verbose_name='课程人数')),
                ('level', models.CharField(choices=[('easy', '简单'), ('mid', '中等'), ('hard', '高级')], default='easy', max_length=10, verbose_name='课程难度')),
                ('love_num', models.IntegerField(default=0, verbose_name='收藏数量')),
                ('click_num', models.IntegerField(default=0, verbose_name='点击数量')),
                ('desc', models.CharField(max_length=20, verbose_name='课程简介')),
                ('detail', models.TextField(max_length=200, verbose_name='课程详情')),
                ('categaty', models.CharField(choices=[('qd', '前端开发'), ('hd', '后端开发')], max_length=10, verbose_name='课程类别')),
                ('course_notice', models.CharField(max_length=50, verbose_name='课程公告')),
                ('course_need', models.CharField(max_length=100, verbose_name='课程须知')),
                ('teacher_tell', models.CharField(max_length=100, verbose_name='老师名言')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('orginfo', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='orgs.OrgInfo', verbose_name='所属机构')),
                ('teacherinfo', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='orgs.TeacherInfo', verbose_name='所属讲师')),
            ],
            options={
                'verbose_name': '课程信息',
                'verbose_name_plural': '课程信息',
            },
        ),
        migrations.CreateModel(
            name='LessonInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='章节名称')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('courseinfo', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='courses.CourseInfo', verbose_name='所属课程')),
            ],
            options={
                'verbose_name': '章节信息',
                'verbose_name_plural': '章节信息',
            },
        ),
        migrations.CreateModel(
            name='SourceInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='资源名称')),
                ('download', models.FileField(max_length=200, upload_to='source/', verbose_name='下载路径')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('courseinfo', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='courses.LessonInfo', verbose_name='所属课程')),
            ],
            options={
                'verbose_name': '资源信息',
                'verbose_name_plural': '资源信息',
            },
        ),
        migrations.CreateModel(
            name='VideoInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='视频名称')),
                ('study_time', models.IntegerField(default=0, verbose_name='视频时长')),
                ('study_url', models.URLField(default='http://www.baidu.com', verbose_name='视频链接')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('lessinfoinfo', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='courses.LessonInfo', verbose_name='所属章节')),
            ],
            options={
                'verbose_name': '视频信息',
                'verbose_name_plural': '视频信息',
            },
        ),
    ]