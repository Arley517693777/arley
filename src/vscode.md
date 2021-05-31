---
layout: post
title: vscode美化
slug: vscode
date: 2021-5-31 10:10
status: publish
author: Arley
categories:
  - 美化
tags:
  - vscode
  - 美化
  - 教程
excerpt: 边看小姐姐边写代码ヾ(≧O≦)〃嗷~
---


### 1.换背景

  在扩展程序中搜索background-cover插件进行安装

  ctrl + shift +p 输入命令

```cpp
 backgroundCover - start
```

  另一种方式直接修vscode的安装文件 *.css*

  由于修改了vscode文件，导致不受支持，可以用插件 Fix VSCode Checksums 隐藏字样

  安装好插件后 ctrl + shift +p 输入命令

```cpp
 Fix Checksums: Apply
```

  添加右下角logo，安装插件 background

  然后进入设置搜索 background 进入json文件配置

  如下我的配置：

```cpp
      //background 的相关配置
    "update.enableWindowsBackgroundUpdates": true,
    "background.customImages": [
      "file:///E:/Pictures/bg.png", //图片地址
    ],
    "background.style": {
        "content":"''",
        "pointer-events":"none",
        "position":"absolute",//开启定位
        "width":"100%",//随窗口宽度
        "height":"100%",//随窗高度
        "z-index":"99999",//最上面
        "background.repeat":"no-repeat",//不进行重复
        "background-size": "20%,20%", //背景大小
        "opacity":0.5 //透明度
    },
    "background.useFront": true,
    "background.useDefault": false,
    "backgroundCover.opacity": 1,
    "backgroundCover.imagePath": "e:\\Pictures\vscodebg.jpg",
    "workbench.colorCustomizations": {
    },

```

### 2.换底部状态栏

  文件->首选项->设置

```cpp
  "workbench.colorCustomizations": {
    "statusBar.background" : "#1A1A1A",
    "statusBar.noFolderBackground" : "#0A0A0D",
    "statusBar.debuggingBackground": "#511f1f"
}
```

### 3.常用插件(转自知乎<https://zhuanlan.zhihu.com/p/112016680>)

1、Bracket Pair Colorizer：给匹配的括号着色

2、Code Spell Checker 拼写检查器

3、Indent-Rainbow 缩进带有颜色

4、Path Intellisense 自动完成文件名

5、Power Mode 光标动画

6、Trailing Spaces 突出显示尾随空格

7、filesize 在状态栏中显示当前文件大小

8、TabNine 代码补全

9、Error Lens 将编辑器诊断出的警告、错误、语法问题（提示的波浪线）等，以用颜色填充行背景的方式突出提示，并将诊断信息显示在尾部

10、Markdown Preview Enhanced  &ensp;Markdown预览插件

### 预览样图

![](./images/vscode.png)
