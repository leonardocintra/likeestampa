import environ

from likeestampa.settings.base import *

env = environ.Env()

DEBUG = env.bool("DEBUG", False)

SECRET_KEY = env("SECRET_KEY")

ALLOWED_HOSTS = ["likeestampa.com.br", "www.likeestampa.com.br", "likeestampa.herokuapp.com", ]

DATABASES = {
    "default": env.db(),
}


# MERCADO PAGO
MERCADO_PAGO_PRIVATE_KEY = env("MERCADO_PAGO_PRIVATE_KEY")
MERCADO_PAGO_PUBLIC_KEY = env("MERCADO_PAGO_PUBLIC_KEY")

# MELHOR ENVIO
MELHOR_ENVIO_TOKEN = env("MELHOR_ENVIO_TOKEN")
MELHOR_ENVIO_BASE_URL = "https://melhorenvio.com.br"

#LIKE ESTAMPA
MAXIMO_ITENS_CARRINHO = env.int("MAXIMO_ITENS_CARRINHO")


# ANYMAIL
EMAIL_BACKEND = "anymail.backends.mailgun.EmailBackend"
ANYMAIL = {
    "MAILGUN_API_KEY": env("MAILGUN_API_KEY"),
    "MAILGUN_SENDER_DOMAIN": "mg.likeestampa.com.br"
}
DEFAULT_FROM_EMAIL = "no-reply@likeestampa.com.br"
SERVER_EMAIL = DEFAULT_FROM_EMAIL