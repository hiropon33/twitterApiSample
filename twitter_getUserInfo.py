#!/usr/bin/env python
# -*- coding: utf-8 -*-

from requests_oauthlib import OAuth1Session
import json

CK = 'ConsumerKey'                             # Consumer Key
CS = 'ConsumerSecret'         # Consumer Secret
AT = 'AccessToken' # Access Token
AS = 'AccessTokenSecret'         # Accesss Token Secert
UI = AT.split("-")[0]                                 # User ID

# ユーザ情報取得用のURL
getUserInfoUrl = "https://api.twitter.com/1.1/users/show.json?user_id=" + UI + "&include_entities=true"

# OAuth認証
twitter = OAuth1Session(CK, CS, AT, AS)
res = twitter.get(getUserInfoUrl)

print(json.loads(res.text))