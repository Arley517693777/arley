# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "/"
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 20
template = {
    "name": "Galileo",
    "type": "local",
    "path": "../Galileo"
}
enable_jsdelivr = {
    "enabled": True,
    "repo": "Arley517693777/Arley517693777.github.io@master"
}

# 站点设置
site_name = "Arley's Blog"
site_logo = "${static_prefix}arley.png"
site_build_date = "2019-10-18T16:51+08:00"
author = "Arley"
email = "leon517693777@gmail.com"
author_homepage = "https://arley.cn"
description = "<p id="hitokoto">Loading...</p>"
key_words = ['Maverick', 'Arley', 'Galileo', 'arleyblog']
language = 'zh-CN'
background_img = "${static_prefix}bg.jpg"
external_links = [
    {
        "name": "Arley's 书签",
        "url": "https://arley.cn/bookmarks",
        "brief": "我的书签导航"
    },
    {
        "name": "趣味网页",
        "url": "https://arley.cn/Dog/",
        "brief": "滑稽"
    },
    {
        "name": "3D画图",
        "url": "https://arley.cn/pencil_draw/",
        "brief": "画图写字板"
    },
    {
        "name": "屏保自用",
        "url": "https://arley.cn/satscreen/",
        "brief": "科技感屏保，F11开启炫酷视界~"
    },
	
    {
        "name": "变色弹珠跳台阶GAME",
        "url": "https://arley.cn/Color-changing-marbles/",
        "brief": "来挑战一下吧~"
    },
    {
        "name": "2021新年祝福",
        "url": "https://arley.cn/2021/",
        "brief": "新年祝福看云烟花"
    }
]
nav = [
    {
        "name": "首页",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "读书",
        "url": "${site_prefix}read",
        "target": "_self"
    },
    {
        "name": "归档",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "关于",
        "url": "${site_prefix}about/",
        "target": "_self"
    }
]

valine = {
    "enable": True,
    "el": '#vcomments',
    "appId": "djccxqIYE2J9DYtSFY7fg1c1-MdYXbMMI",
    "appKey": "GskHdEqrq48tYUSFSeoJd4Fy",
    "avatar": "wavatar",
    "visitor": True,
    "recordIP": True
}

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
<link rel="shortcut icon" href="${static_prefix}Arley.png">
<script type='text/javascript' src="https://cdn.jsdelivr.net/gh/Arley517693777/Arley517693777.github.io@master/assets/jquery-3.4.1.min.js"></script>
<!-- szgotop -->
<link rel="stylesheet" type="text/css" href="https://cdn.jsdelivr.net/gh/Arley517693777/gotop/css/szgotop.css" />
<!-- FancyBox -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/Arley517693777/Arley517693777.github.io@master/assets/jquery.fancybox.min.css" />
<script type="text/javascript" src="https://cdn.jsdelivr.net/gh/Arley517693777/Arley517693777.github.io@master/assets/jquery.fancybox.min.js"></script>
<script>
$(function() {
   $(".yue figure img").each(function(i) {
      if (!this.parentNode.href) {
         $(this).wrap("<a href='" + this.src + "' data-fancybox='images' data-caption='" + this.alt + "'></a>")
      }
   })
});
</script>
<script type="text/javascript">
$( '[data-fancybox]' ).fancybox({
	protect:true,
	caption : function( instance, item ) {
	return $(this).find('figcaption').html();
	}
});
</script>
'''

footer_addon = r'''
<script>
var _hmt = _hmt || [];
(function() {
  var hm = document.createElement("script");
  hm.src = "https://hm.baidu.com/hm.js?d69b9b23082b2143a5bce14c4c459baa";
  var s = document.getElementsByTagName("script")[0];
  s.parentNode.insertBefore(hm, s);
})();
</script>
'''

body_addon = r'''
<script type="text/javascript" src="https://cdn.jsdelivr.net/gh/Arley517693777/gotop/js/szgotop.js"></script>
<div class="back-to-top cd-top faa-float animated cd-is-visible" style="top: -999px;"></div>
<script src="https://v1.hitokoto.cn/?encode=js&select=%23hitokoto" defer></script>
'''
