---
layout: post
cid: 25
title: 关于使用Infinity Free服务器开启伪静态的教程
slug: infinity_free
date: 2021/07/14 20:47:00
updated: 2021/07/15 12:19:59
status: publish
author: Arley
categories: 
  - 技术教程
tags: 
  - 伪静态
  - infinity free
  - typecho
  - VOID
banner: 
bannerascover: 1
bannerStyle: 0
excerpt: 
posttype: 0
showfullcontent: 0
showTOC: 0
---


**关于使用Infinity Free服务器开启伪静态的教程**

博客系统：[Typecho][1]
主题：[VOID][2]

----------

在htdocs根目录下创建【.htaccess】文件，复制以下代码
伪静态代码

    <IfModule mod_rewrite.c>
    RewriteEngine On
    RewriteBase /
    RewriteCond %{REQUEST_FILENAME} !-f
    RewriteCond %{REQUEST_FILENAME} !-d
    RewriteRule ^(.*)$ /index.php/$1 [L]
    </IfModule>

Https跳转代码

    <IfModule mod_rewrite.c>
    RewriteEngine On
    RewriteBase /
    RewriteCond %{HTTP:X-Forwarded-Proto} =http
    RewriteRule (.*) https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]
    </IfModule>
保存后去网站后台开启伪静态，如果开启失败勾选强制开启，如下图
![开启伪静态.png][3]

正常情况下，.PHP会消失，伪静态开启成功。

  [1]: http://typecho.org/
  [2]: https://github.com/AlanDecode/Typecho-Theme-VOID/blob/master/README.md
  [3]: https://arley.fun/usr/uploads/2021/07/2740130554.png#vwid=1005&vhei=518