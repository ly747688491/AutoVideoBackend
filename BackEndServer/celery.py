import os

from celery import Celery

# # 设置Django的设置模块为Celery程序的默认设置
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')

app = Celery('BackEndServer')

# 使用字符串，这样worker不需要序列化你的配置对象。
# 命名空间 CELERY 意味着所有与celery有关的配置键都应该有一个`CELERY_`的前缀。
app.config_from_object('django.conf:settings', namespace='CELERY')

# 加载任何在你的Django应用中注册的任务模块
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
