
<!DOCTYPE html>
<html lang="zh-cmn-Hans">
<head>
  <meta charset="UTF-8">
  <link rel="dns-prefetch" href="//s1.tool.lu">
  <link rel="dns-prefetch" href="//s2.tool.lu">
  <link rel="dns-prefetch" href="//s3.tool.lu">
  <link rel="dns-prefetch" href="//s4.tool.lu">
  <link rel="dns-prefetch" href="//qn11.tool.lu">
  <link rel="dns-prefetch" href="//qn12.tool.lu">
  <link rel="dns-prefetch" href="//qn13.tool.lu">
  <link rel="dns-prefetch" href="//qn14.tool.lu">
  <link rel="dns-prefetch" href="//a.tool.lu">
  <title>代码在线运行 - 在线工具</title>
  <link rel="search" type="application/opensearchdescription+xml" title="在线工具"
        href="https://tool.lu/opensearch.xml">
  <!-- <link rel="canonical" href="original url"> -->
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, viewport-fit=contain">
  <meta name="author" content="xiaozi">
  <link rel="publisher" href="https://plus.google.com/113621341737546487026">
  <meta name="keywords" content="在线运行php,c,c++,go,python,nodejs,java,groovy代码,在线测试代码">
  <meta name="description" content="在线运行php,c,c++,go,python,nodejs,java,groovy代码，测试代码">
  <link rel="shortcut icon" href="https://tool.lu/favicon.ico">
  <meta name="apple-mobile-web-app-title" content="在线工具">
  <meta name="format-detection" content="telephone=no">
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="grey">
  <link rel="apple-touch-icon" sizes="57x57" href="//qn11.tool.lu/201711/08/002818pvCvPDnAZK6IioEb_57x57.png">
  <link rel="apple-touch-icon" sizes="72x72" href="//qn11.tool.lu/201711/08/002819Dt982ULrn0pC7AL1_72x72.png">
  <link rel="apple-touch-icon" sizes="114x114" href="//qn11.tool.lu/201711/08/002818ZlzSK5t2HM5icUJN_114x114.png">
  <link rel="apple-touch-icon" sizes="144x144" href="//qn11.tool.lu/201711/08/002819v0Gaydtvy2P4y03G_144x144.png">
  <!--[if lt IE 9]>
  <script src="//s1.tool.lu/js/html5shiv.js"></script>
  <![endif]-->
  <link rel="stylesheet" href="//s2.tool.lu/css/fontawesome/css/all.min.css">
  <link rel="stylesheet" href="//s3.tool.lu/__/8fcb4eae31f317ab8000c71c1f4d5c4d.css">
  <script src="//a.tool.lu/te.js" crossorigin="anonymous"></script>
  <script>
    var _hmt = _hmt || [];
    (function() {
      var hm = document.createElement("script");
      hm.src = "https://hm.baidu.com/hm.js?0fba23df1ee7ec49af558fb29456f532";
      var s = document.getElementsByTagName("script")[0];
      s.parentNode.insertBefore(hm, s);
    })();
  </script>
  <script src="//s4.tool.lu/__/00e92975ed53acdfe1d5c12d7c3a06be.js"></script>
</head>
<body class="app">
<!--[if lt IE 9]>
<div class="notice chromeframe">您的浏览器版本<strong>很旧很旧</strong>，为了正常地访问网站，请升级您的浏览器 <a target="_blank"
                                                                                   href="http://browsehappy.com">立即升级</a>
</div>
<![endif]-->
<div id="wrap">
  <div id="hdr">
    <div class="w">
      <a class="logo" rel="nofollow" href="https://tool.lu/">在线工具</a>
      <h1 class="hidden">代码在线运行</h1>
      <ul class="nav" id="js_login_bar" data-url="https://tool.lu/hello?callback=?">
      </ul>
    </div>
  </div>
  <div id="bdy">
    <div class="w">
      <link rel="stylesheet" href="//s1.tool.lu/__/ec8e320b48f763e940b763b72193a804.css">
      <div class="main">
        <div class="inner">
          <div class="runner-container">
            <div class="runner-toolbar">
              <select name="language" id="language">
                <option value="php" >PHP
                </option>
                <option value="c" >C</option>
                <option value="cpp" >C++
                </option>
                <option value="python" >
                  Python
                </option>
                <option value="python3" >
                  Python3
                </option>
                <option value="golang" >
                  Go
                </option>
                <option value="java" >Java
                </option>
                <option value="js" >NodeJS
                </option>
                <option value="lua" >Lua
                </option>
                <option value="groovy" >
                  Groovy
                </option>
                <option value="bash" >Bash
                </option>
              </select>
              <button id="save" class="runner-save" type="button"><i class="fas fa-save"></i> 保存(<u>S</u>ave)</button>
              <a class="runner-mine" target="_blank" href="//id.tool.lu/sso/login?redirect=https%3A%2F%2Ftool.lu%2Fcoderunner%2F">我的代码</a>
              <button id="embed" class="runner-embed" type="button"><i class="fas fa-pencil-square"></i> 嵌入博客(<u>E</u>mbed)
              </button>
              <button id="run" class="runner-run" type="button"><i class="fas fa-play"></i> 执行(<u>R</u>un)</button>
              <a class="runner-new" target="_blank" href="https://tool.lu/coderunner/"><i
                class="fas fa-plus"></i></a>
            </div>
            <div class="runner-panel">
              <div class="ui-layout-center">
                <textarea id="editor" class="editor"></textarea>
                <div
                  style="position: absolute; top: 0; right: 0; padding: 2px 6px; z-index: 9; background-color: rgba(255, 255, 255, 0.07); border-radius: 0 0 0 5px;">
                  <a class="btn-indent" style="text-decoration: none;" href="javascript:;">缩进</a>
                  <a class="btn-unindent" style="text-decoration: none;" href="javascript:;">减少缩进</a>
                  <a class="btn-toggle-comment" style="text-decoration: none;" href="javascript:;">注释</a>
                  <a class="btn-reindent" style="text-decoration: none;" href="javascript:;">格式化</a>
                </div>
              </div>
              <div class="runner-console">
                <div id="console"><div class="console-line welcome">sandbox&gt; tool.lu connecting<span class="dotting"></span></div></div>
                <a id="console_clear" href="javascript:;">Clear</a>
              </div>
            </div>
          </div>
        </div>
      </div>
      <script>
        window.storeId = 0;
      </script>
      <script src="//s2.tool.lu/__/c450417b39b867905229e46241a9c0c0.js"></script>
    </div>
  </div>
  <div id="ftr">
    <div class="w">
      <p class="declare">
        <a target="_blank" href="mailto:245565986@qq.com">联系我</a> - <a rel="nofollow" href="https://tool.lu/">工具首页</a>
        <br>
        Copyright &copy; 2011-2014 <a href="http://usr.im" target="_blank">iteam</a>. All Rights Reserved. Current
        version is 2.91.2.
        <br>
        <a rel="noopener noreferrer nofollow" target="_blank" href="https://beian.miit.gov.cn/">浙ICP备14020137号-1</a>
      </p>
    </div>
  </div>
</div>
<div id="t_fixed">
  <!--    <a rel="noopener noreferrer" target="_blank" class="btn qq-qun copy-btn js-tip"
     data-clipboard-text="227310278"
     href="http://shang.qq.com/wpa/qunwpa?idkey=556567ae633f9715b4849f7277bbc37d0f657eab2a6366b1b4b528cece2cbe74"
     title="QQ群(二): 227310278"><i class="fab fa-qq"></i></a>-->
  <a rel="noopener noreferrer" target="_blank" class="btn qq-qun copy-btn js-tip"
     data-clipboard-text="174157258"
     href="http://shang.qq.com/wpa/qunwpa?idkey=33602e7bb9a97a3287113dcab6fbd654041db0e115650aac35f56c3fa6dddf7a"
     title="QQ群(一): 174157258"><i class="fab fa-qq"></i></a>
  <a rel="noopener noreferrer" class="btn wechat js-wechat-mp js-tip"
     title="微信公众号: 知鸦"
     href="javascript:;"
     data-image="https://tool.lu/qrcode/basic.html?text=http%3A%2F%2Fweixin.qq.com%2Fr%2FdSkVDQHE5VyarUVu93xn&amp;size=280"><i class="fab fa-weixin"></i></a>
  <a rel="noopener noreferrer" target="_blank" class="btn weibo js-tip" href="http://weibo.com/245565986" title="微博: 小子欠扁"><i class="fab fa-weibo"></i></a>
  <a rel="noopener noreferrer" target="_blank" class="btn github js-tip" href="https://github.com/xiaozi" title="github: xiaozi"><i class="fab fa-github-alt"></i></a>
  <a class="btn gotop js-tip" href="javascript:;" title="返回顶部"><i class="fas fa-arrow-up"></i></a>
</div>
<script>
  (function () {
    var a = document.createElement("script");
    a.async = !0;
    a.src = ("https:" == document.location.protocol ? "https:" : "http:") + "//a.tool.lu/ta.js";
    var b = document.getElementsByTagName("script")[0];
    b.parentNode.insertBefore(a, b)
  })();
</script>
</body>
</html>
