#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

import os
import logging
import time

from logging.handlers import RotatingFileHandler

from .translation import Translation

# Change Accordingly While Deploying To A VPS
APP_ID = int(os.environ.get("APP_ID", "21788738"))

API_HASH = os.environ.get("API_HASH", "217f00afea49de7de831ec7cdeb9b81b")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7178851868:AAGsTF039iROJI1N7P57NJ_Z6R7ek2mrv1c")

DB_URI = os.environ.get("DB_URI", "mongodb+srv://akm:akm12109@cluster0.qffly8j.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

USER_SESSION = os.environ.get("USER_SESSION", "BQDtlOIAj6xAL_EMD-Wj1saDtOzEE0LxEZ98RClglPOGH2r7XT7i0_9Y1g09KyUOK7-4Oa992nq4CHJyoefYtt6bUOE_IRtoLvn443xDRWMENjWZXQW4wh0sijIgOuMRIuv1BTP23PI_o9ulnT4kOSVSyOAXMHZJEnhPevKfSs3ss4q3tnY14mUzfLQnSK_xuZtnZg6_jC947SKkgENXWHr7xjT82dt8YkfcB4qOgmcQ6ruy-ToNZkPyWRuohmjx71U-2mvdXxn-6JhsvfVWhkYUOGb0fxtyDNn-Uiv3WIUqQMhmVQ3mcLb85MaVdW5kGsdpmar3ksUMTKXuhFKyW3P1y4w06gAAAAGQp6lRAA")

VERIFY = {}

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            "autofilterbot.txt",
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

start_uptime = time.time()


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
