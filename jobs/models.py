from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Platform(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Job(models.Model):
    job_link = models.CharField(max_length=100)  # 職缺連結
    job_name = models.CharField(max_length=200)  # 工作名稱
    job_addr = models.CharField(max_length=200)  # 工作地址
    company_name = models.CharField(max_length=200)  # 公司名稱
    salary = models.CharField(max_length=50)  # 薪資
    education = models.CharField(max_length=10, default='學歷不拘')  # 學歷
    work_experience = models.CharField(max_length=10, default='經歷不拘')  # 經歷
    web = models.ForeignKey(Platform, on_delete=models.CASCADE)  # 求職平台
    update_time = models.DateTimeField(auto_now=True)  # 更新時間
    users = models.ManyToManyField(User, blank=True)  # 收藏

    def __str__(self) -> str:
        return f'{self.job_name}({self.job_name})'

