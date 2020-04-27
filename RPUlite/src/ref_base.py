#!/usr/bin/python
# -*- coding: utf-8 -*-
ref = {'233.7.70.222':':0:1:457:2:64:2590000:0:0:0', '233.7.70.239':':0:1:61:1:2:0:0:0:0', '233.7.70.244':':0:1:61:1:2:0:0:0:0', \
'233.7.70.225':':0:1:3718:E:70:1680000:0:0:0', '233.7.70.253':':0:1:458:1:64:2580000:0:0:0', '233.7.70.195':':0:1:45D:1:64:2580000:0:0:0', \
'233.7.70.132':':0:1:3308:190:13e:820000:0:0:0', '233.7.70.162':':0:1:4:8:1:3842D95:0:0:0', '233.7.70.127':':0:1:29:1:2:0:0:0:0', \
'233.7.70.158':':0:1:28:1:2:0:0:0:0', '233.7.70.157':':0:19:6e:1f40:6b2:5a0000:0:0:0', '233.7.70.230':':0:1:70:1:2:FFFF0000:0:0:0', \
'233.7.70.125':':0:1:3717:E:70:1680000:0:0:0', '233.7.70.161':':0:1:25A:1:2:0:0:0:0', '233.7.70.160':':0:1:672:170C:9E:5A0000:0:0:0', \
'233.7.70.133':':0:1:3715:E:70:1680000:0:0:0', '233.7.70.159':':0:19:28:20D0:6B2:5A000:0:0:0', '233.7.70.164':':0:1:1F:578:13E:82ACCE:0:0:0', \
'233.7.70.163':':0:1:1F7:B:1:3542F58:0:0:0', '233.7.70.114':':0:1:1D6:191:3A:2EF0000:0:0:0', '233.7.70.216':':0:1:7D1:22C4:13E:820000:0:0:0', \
'233.7.70.217':':0:1:7D2:22C4:13E:820000:0:0:0', '233.7.70.126':':0:1:25A:C:1:3542F80:0:0:0', '233.7.70.211':':0:19:6595:9:70:1680000:0:0:0', \
'233.7.70.156':':0:1:426B:D9:FFFF:1682F01:0:0:0', '233.7.70.130':':0:19:107C:1A:44:300000:0:0:0', '233.7.70.179':':0:19:107C:1A:44:300000:0:0:0', \
'233.7.70.128':':0:19:1072:1A:44:300000:0:0:0', '233.7.70.178':':0:19:1072:1A:44:300000:0:0:0', '233.7.70.129':':0:19:1068:1A:44:300000:0:0:0', \
'233.7.70.193':':0:19:1068:1A:44:300000:0:0:0', '233.7.70.134':':0:19:7b2:1d:56:320000:0:0:0', '233.7.70.180':':0:19:7b2:1d:56:320000:0:0:0', \
'233.7.70.177':':0:1:24:1:2:0:0:0:0', '233.7.70.218':':0:1:24:1:2:0:0:0:0', '233.7.70.116':':0:1:89B2:22:1:168AF89:0:0:0', \
'233.7.70.194':':0:1:89B2:22:1:168AF89:0:0:0', '233.7.70.200':':0:1:25C:1:2:0:0:0:0', '233.7.70.201':':0:1:25D:1:2:0:0:0:0', \
'233.7.70.131':':0:1:25B:1:2:0:0:0:0', '233.7.70.181':':0:1:37:1:2:0:0:0:0', '233.7.70.89':':0:1:64:68:3A:2EE0000:0:0:0', \
'233.7.70.124':':0:1:479:2:64:2580000:0:0:0', '233.7.70.43':':0:1:3:15:90E:3850000:0:0:0', '233.7.70.182':':0:1:986C:27:FFFF:23030A8:0:0:0', \
'233.7.70.60':':0:1:69:32:64:3C50000:0:0:0', '233.7.70.215':':0:1:1004:2:64:3850000:0:0:0', '233.7.70.52':':0:1:514:65:3A:2EE0000:0:0:0', \
'233.7.70.183':':0:1:1C5:26AC:13F:820000:0:0:0', '233.7.70.21':':0:1:3330:D:70:1680000:0:0:0', '233.7.70.214':':0:1:1E16:7:1111:E072EC8:0:0:0', \
'233.7.70.212':':0:1:40E:3:1111:E08B0A7:0:0:0', '233.7.70.30':':0:1:19:1:2:0:0:0:0', '233.7.70.111':':0:1:29DB:3CF0:13E:820000:0:0:0', \
'233.7.70.188':':0:1:439d:2cec:13e:820000:0:0:0', '233.7.70.186':':0:1:50E8:7:70:1680000:0:0:0', '233.7.70.121':':0:1:485:2:64:2580000:0:0:0', \
'233.7.70.187':':0:1:4687:12:FFFF:168AF16:0:0:0', '233.7.70.110':':0:1:46BB:12:70:1680000:0:0:0', '233.7.70.102':':0:1:26C:66:3A:2EE0000:0:0:0', \
'233.7.70.232':':0:1:501F:5:70:1680000:0:0:0', '233.7.70.231':':0:1:508B:6:70:1680000:0:0:0', '233.7.70.63':':0:1:1964:64:56:2EE0000:0:0:0', \
'233.7.70.191':':0:1:5A00:17:FFFF:1682F75:0:0:0', '233.7.70.26':':0:1:458:1:64:2580000:0:0:0', '233.7.70.27':':0:1:45D:1:64:2580000:0:0:0', \
'233.7.70.28':':0:1:45C:1:64:2580000:0:0:0', '233.7.70.9':':0:1:0:0:0:0:0:0:0', '233.7.70.91':':0:1:9:14:90E:3840000:0:0:0', \
'233.7.70.72':':0:1:50DD:7:70:1680000:0:0:0', '233.7.70.96':':0:1:1CD4:13:55:300000:0:0:0', '233.7.70.42':':0:1:C:D:1:DE82A07:0:0:0', \
'233.7.70.196':':0:1:57:1:2:0:0:0:0', '233.7.70.45':':0:1:16:1:2:0:0:0:0', '233.7.70.81':':0:1:35f5:c8:13e:820000:0:0:0', \
'233.7.70.197':':0:1:7D6:C8:356E:DE80000:0:0:0', '233.7.70.147':':0:1:508d:6:70:1680000:0:0:0', '233.7.70.47':':0:1:43a3:2cec:13e:820000:0:0:0', \
'233.7.70.154':':0:1:29:1:2:0:0:0:0', '233.7.70.85':':0:1:28:1:2:0:0:0:0', '233.7.70.149':':0:1:50EB:7:70:1680000:0:0:0', \
'233.7.70.171':':0:1:84E1:22:1:168AF89:0:0:0', '233.7.70.185':':0:1:70:1:2:FFFF0000:0:0:0', '233.7.70.192':':0:1:5B:1:2:FFFF0000:0:0:0', \
'233.7.70.39':':0:1:A3A:1:FFFF:1682DCF:0:0:0', '233.7.70.148':':0:1:4F:1:2:0:0:0:0', '233.7.70.76':':0:1:22:12C:2324:D840000:0:0:0', \
'233.7.70.109':':0:1:508c:6:70:1680000:0:0:0', '233.7.70.204':':0:1:501C:5:70:1680000:0:0:0', '233.7.70.205':':0:1:636:2:64:2580000:0:0:0', \
'233.7.70.206':':0:1:120:1:1:302F4F:0:0:0', '233.7.70.207':':0:1:508a:6:70:1680000:0:0:0', '233.7.70.208':':0:1:3AFE:F:70:1680000:0:0:0', \
'233.7.70.209':':0:1:2A3C:8:70:168AFFB:0:0:0', '233.7.70.202':':0:1:5016:5:70:1680000:0:0:0', '233.7.70.53':':0:1:2986:3d54:13e:820000:0:0:0', \
'233.7.70.223':':0:1:5D:1:2:0:0:0:0', '233.7.70.32':':0:1:1D:1:2:0:0:0:0', '233.7.70.84':':0:1:0:0:0:0:0:0:0', \
'233.7.70.224':':0:1:5277:15:70:1680000:0:0:0', '233.7.70.169':':0:1:1E:578:13E:82ACCE:0:0:0', '233.7.70.97':':0:1:1F:1:2:0:0:0:0', \
'233.7.70.236':':0:1:391:9:FFFF:1682E68:0:0:0', '233.7.70.95':':0:1:13F:5:FFFF:1682E1C:0:0:0', '233.7.70.226':':0:1:1F7:B:1:3542F58:0:0:0', \
'233.7.70.113':':0:1:1D6:191:3A:2EF0000:0:0:0', '233.7.70.227':':0:1:6FE:6A:3A:2EE0000:0:0:0', '233.7.70.115':':0:1:3338:D:70:1680000:0:0:0', \
'233.7.70.83':':0:1:2485:23f0:13f:820000:0:0:0', '233.7.70.228':':0:1:46B:2:64:2580000:0:0:0', '233.7.70.82':':0:1:44dd:258:13e:820000:0:0:0', \
'233.7.70.139':':0:1:3E8:68:3A:2EE0000:0:0:0', '233.7.70.54':':0:1:D4B:15:FFFF:1682F4F:0:0:0', '233.7.70.70':':0:1:640:69:3A:2EE0000:0:0:0', \
'233.7.70.135':':0:1:D4A:15:FFFF:1682F4F:0:0:0', '233.7.70.184':':0:1:BC8:12C:356E:DE80000:0:0:0', '233.7.70.166':':0:1:276:66:3A:2EE0000:0:0:0', \
'233.7.70.140':':0:1:D53:15:FFFF:1682F4F:0:0:0', '233.7.70.50':':0:1:454:2:64:2580000:0:0:0', '233.7.70.101':':0:1:84E2:22:1:168AF89:0:0:0', \
'233.7.70.29':':0:1:5019:5:70:1680000:0:0:0', '233.7.70.56':':0:1:387:9:FFFF:1682E69:0:0:0', '233.7.70.119':':0:1:5A0A:17:FFFF:1682F75:0:0:0', \
'233.7.70.36':':0:1:780:1d:56:320000:0:0:0', '233.7.70.59':':0:1:79e:1d:56:300000:0:0:0', '233.7.70.67':':0:1:776:1d:56:300000:0:0:0', \
'233.7.70.151':':0:1:50E7:7:70:1680000:0:0:0', '233.7.70.152':':0:1:6FF0:42a:1:c00000:0:0:0', '233.7.70.229':':0:1:6ff1:42a:1:c00000:0:0:0', \
'233.7.70.33':':0:1:67:1:2:0:0:0:0', '233.7.70.88':':0:1:195A:64:56:2EE0000:0:0:0', '233.7.70.103':':0:1:195a:14:56:320000:0:0:0', \
'233.7.70.138':':0:1:1A90:64:56:2EE0000:0:0:0', '233.7.70.35':':0:1:D:1:2:0:0:0:0', '233.7.70.122':':0:1:484:2:64:2580000:0:0:0', \
'233.7.70.104':':0:1:6152:7:FFFF:1682E42:0:0:0', '233.7.70.90':':0:1:1F4:68:3A:2EE0000:0:0:0', '233.7.70.79':':0:1:472:2:64:2580000:0:0:0', \
'233.7.70.57':':0:1:140:5:FFFF:1682E1C:0:0:0', '233.7.70.78':':0:1:3C:1:2:0:0:0:0', '233.7.70.233':':0:1:23:1:2:0:0:0:0', \
'233.7.70.77':':0:1:5A8C:17:FFFF:1682F75:0:0:0', '233.7.70.174':':0:1:0:0:0:0:0:0:0', '233.7.70.99':':0:1:1E:1:2:0:0:0:0', \
'233.7.70.234':':0:1:39d3:1fa4:13e:820000:0:0:0', '233.7.70.18':':0:1:FB:8:1:352B138:0:0:0', '233.7.70.31':':0:1:2:65:3A:2EE0000:0:0:0', \
'233.7.70.235':':0:1:514:68:3A:2EE0000:0:0:0', '233.7.70.105':':0:1:3B0B:F:70:1680000:0:0:0', '233.7.70.69':':0:1:E74:9:64:3840000:0:0:0', \
'233.7.70.49':':0:1:4:65:3A:2EE0000:0:0:0', '233.7.70.62':':0:1:190:68:3A:2EE0000:0:0:0', '233.7.70.173':':0:1:481:2:64:2590000:0:0:0', \
'233.7.70.37':':0:1:483:2:64:2580000:0:0:0', '233.7.70.150':':0:1:483:2:64:2580000:0:0:0', '233.7.70.40':':0:1:9:1:2:0:0:0:0', \
'233.7.70.170':':0:1:9:1:2:0:0:0:0', '233.7.70.167':':0:1:0:0:0:0:0:0:0', '233.7.70.80':':0:1:44F:1:64:2580000:0:0:0', \
'233.7.70.240':':0:1:A33:1:FFFF:1682DCF:0:0:0', '233.7.70.55':':0:1:0:0:0:0:0:0:0', '233.7.70.241':':0:1:277C:1:70:1680000:0:0:0', \
'233.7.70.94':':0:1:144:5:FFFF:1682E1C:0:0:0', '233.7.70.108':':0:1:143:5:FFFF:1682E1C:0:0:0', '233.7.70.41':':0:1:12F:5:FFFF:1682E1C:0:0:0', \
'233.7.70.58':':0:1:71C:6B:3A:2EE0000:0:0:0', '233.7.70.120':':0:1:23A:67:3A:2EE0000:0:0:0', '233.7.70.71':':0:1:212:67:3A:2EE0000:0:0:0', \
'233.7.70.137':':0:1:47D:2:64:2580000:0:0:0', '233.7.70.242':':0:1:2BC:67:3A:2EE0000:0:0:0', '233.7.70.74':':0:1:14A:5:FFFF:1682E1C:0:0:0', \
'233.7.70.64':':0:1:C8D:140:70:2300000:0:0:0', '233.7.70.246':':0:1:21:1:2:0:0:0:0', '233.7.70.247':':0:1:474:2:64:2590000:0:0:0', \
'233.7.70.248':':0:1:284A:3:70:1680000:0:0:0', '233.7.70.249':':0:1:40:1:2:0:0:0:0', '233.7.70.250':':0:1:3F:1:2:0:0:0:0', \
'233.7.70.251':':0:1:20:1:2:0:0:0:0', '233.7.70.243':':0:1:1F9:B:1:3532F58:0:0:0', '233.7.70.245':':0:1:28aa:4:70:1680000:0:0:0', \
'233.7.70.141':':0:1:4CE:7:2283:DA20000:0:0:0', '233.7.70.252':':0:1:532:65:3A:2EE0000:0:0:0', '233.7.70.48':':0:1:3:65:3A:2EE0000:0:0:0', \
'233.7.70.142':':0:1:62:1:2:0:0:0:0', '233.7.70.23':':0:1:1:B0:64:3530000:0:0:0', '233.7.70.66':':0:1:323:e:1:3522e40:0:0:0', \
'233.7.70.165':':0:1:323:e:1:3522e40:0:0:0', '233.7.70.168':':0:1:135:5:FFFF:1682E1C:0:0:0', '233.7.70.175':':0:1:230:67:3A:2EE0000:0:0:0', \
'233.7.70.237':':0:1:0:0:0:0:0:0:0', '233.7.70.198':':0:1:B4:78:3A:3200000:0:0:0', '233.7.70.22':':0:1:258:67:3A:2EE0000:0:0:0', \
'233.7.70.100':':0:1:14C:5:FFFF:1682E1C:0:0:0', '233.7.70.145':':0:1:10:7:1:3840e3d:0:0:0', '233.7.70.44':':0:1:1:65:3A:2EE0000:0:0:0', \
'233.7.70.172':':0:1:6:2:1113:2EF0000:0:0:0', '233.7.70.68':':0:1:7:2:1113:2EF0000:0:0:0', '233.7.70.61':':0:1:0:0:0:0:0:0:0', \
'233.7.70.112':':0:1:38B:9:FFFF:1682E69:0:0:0', '233.7.70.176':':0:1:2D:190:2324:D840000:0:0:0', '233.7.70.155':':0:1:12C:68:3A:2EE0000:0:0:0', \
'233.7.70.153':':0:1:47F:2:64:2580000:0:0:0', '233.7.70.24':':0:1:43a1:2cec:13e:822faf:0:0:0', '233.7.70.38':':0:1:1F:12C:2324:D840000:0:0:0', \
'233.7.70.254':':0:1:2F:1:2:0:0:0:0', '233.7.70.75':':0:1:15:1:2:0:0:0:0', '233.7.70.213':':0:1:FA0:2:64:3840000:0:0:0', \
'233.7.70.220':':0:1:0:0:0:0:0:0:0', '233.7.70.221':':0:1:7:2:2:3840E5B:0:0:0', '233.7.70.203':':0:1:0:0:0:0:0:0:0', \
'233.7.70.219':':0:1:0:0:0:0:0:0:0', '233.7.70.143':':0:1:147:5:ffff:1682e1c:0:0:0', '233.7.70.51':':0:1:5:65:3A:2EE0000:0:0:0', \
'233.7.70.34':':0:1:5272:15:70:1680000:0:0:0', '233.7.70.86':':0:1:708:69:3A:2EE0000:0:0:0', '233.7.70.210':':0:1:0:0:0:0:0:0:0', \
'233.7.70.107':':0:1:D49:15:FFFF:1682F4F:0:0:0', '233.7.70.92':':0:1:2C:1:2:0:0:0:0', '233.7.70.46':':0:1:D4C:15:FFFF:1682F4F:0:0:0'}
