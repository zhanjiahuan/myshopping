import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# 加密要是
SECRET_KEY = '*91@&hle6mpd7lh)0j2s=5cv*o)n482&wdam4#*-tgujpm3s48'

# SECURITY WARNING: don't run with debug turned on in production!
# 开发模式,上线设置为False
DEBUG = True
# 允许访问的ip地址(上线需要配置)
ALLOWED_HOSTS = []

# Application definition
# 注册app
SYS_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
# 第三方模块
EXT_APPS = [
    # 'bootstrap3',
    # 必要组件
    'xadmin',
    'crispy_forms',
    # 非必要,用于修改样式
    'reversion',
    'django_ajax',
]
# 自定义功能模块
MY_APPS = [
    'apps.account',
    'apps.cate',
    'apps.detail',
    'apps.main',
    'apps.search',
    'apps.cart'
]
INSTALLED_APPS = SYS_APPS + EXT_APPS + MY_APPS
# 中间注册
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
# 根路由,一般不需要修改
ROOT_URLCONF = 'myshopping.urls'
# 模版配置
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            # 模版全局变量配置
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
# 启动应用程序,一般不需要修改
WSGI_APPLICATION = 'myshopping.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
# 数据配置
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '91gou',
        'USER': 'root',
        'PASSWORD': '123456',
        'PORT': '3306',
        'HOST': '127.0.0.1',
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators
# 用户密码验证设置,一般不需要修改
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/
# 语言设置,开发中设置成中文
LANGUAGE_CODE = 'zh-hans'
# 时区设置  设置成中国时区
TIME_ZONE = 'Asia/Shanghai'
# 国际化配置,自动转化成多个语言
USE_I18N = True

USE_L10N = True
# 开启django时区,如果不需要设置成False,建议设置成False
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/
# 访问静态文件的路径配置
STATIC_URL = '/static/'
# 配置静态文件整理的跟目录
STATIC_ROOT = 'static_root'
# 静态文件的目录配置
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR, 'apps/main/static')
)
# 配置访问多媒体的路径
MEDIA_URL = '/media/'
# 配置文件上传的路径
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# ========== 缓存的配置=========
# pip install django-redis
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        # 缓存地址
        "LOCATION": "redis://112.74.42.138:6379",
        "OPTIONS": {
            # 'PASSWORD':123
            # 使用线程池管理连接
            "CONNECTION_POOL_KWARGS": {"max_connections": 100}
        }
    },
    'session': {
        'BACKEND': 'django_redis.cache.RedisCache',
        # 缓存地址
        "LOCATION": "redis://112.74.42.138:6379/3",
        "OPTIONS": {
            # 'PASSWORD':123
            # 使用线程池管理连接
            "CONNECTION_POOL_KWARGS": {"max_connections": 100}
        }
    },
}

# ========SESSION 缓存配置======
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "session"

# session失效的时间 7天
SESSION_COOKIE_AGE = 7 * 24 * 60 * 60  # Session的cookie失效日期（2周） 默认1209600秒

# =======邮件配置=======
EMAIL_HOST = 'smtp.163.com'
EMAIL_PORT = 25
EMAIL_HOST_USER = '18614068889@163.com'
EMAIL_HOST_PASSWORD = 'py1805'
EMAIL_USE_TLS = True

# =======日志配置=======
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'DEBUG',
        },
    }
}

AUTH_USER_MODEL = 'main.User'
LOGIN_URL = '/account/login/'

"""
==============支付宝配置=================
"""
# 支付宝注册应用生成的IP
APP_ID = '2016092300580718'

# 沙箱环境支付网关就是沙箱那面那个关口
PAY_URL_DEV = 'https://openapi.alipaydev.com/gateway.do'
# 正式支付的网关
PAY_URL = 'https://openapi.alipay.com/gateway.do'
# 公钥,私钥
APP_PRIVATE_KEY_STR = open(os.path.join(BASE_DIR, 'pay/app_private_key.pem')).read()
APP_PUBLICK_KEY_STR = open(os.path.join(BASE_DIR, 'pay/app_public_key.pem')).read()

"""
==============支付宝配置=================
"""
