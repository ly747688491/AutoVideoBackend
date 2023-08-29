"""
数据库连接池配置信息
"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'automated_video',
        'HOST': '43.134.79.6',
        'PORT': 3306,
        'USER': 'automated_video',
        'PASSWORD': 'kTBzG8RSKCeep33D'
    }
}

# redis 服务配置信息，修改端口号密码

REDIS = {
    'host': '127.0.0.1',
    'port': 6379,
    'password': 'Liy_0123',
}