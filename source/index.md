#oauth review 结果

##Controller review 结果

###Firstp2pLoginController.java

+ loginLimit 需要声明为final的

javaref cn.ucfgroup.oauth.controller.Firstp2pLoginController.java#line(41)

+ 以下的field已经没有存在的必要，需要重构后删除

javaref{cn.ucfgroup.oauth.controller.Firstp2pLoginController.java#line(41)|声明处} 

compare:focus:: line(261) 统一获取的地方

```java
private String responseRedirectUri = null;
private String responseType = null;
private String responseClientid = null;
private String oauthcode = null;
private OauthClient oc = null;
```

+ 下面的field需要重新命名，并声明为static final的

javaref{cn.ucfgroup.oauth.controller.Firstp2pLoginController.java#line(47)|声明处} 

```java
 private String logoPath = "firstp2p";//默认logo
 private String clientUrl = "www.firstp2p.com";//默认站点URL
 private String clientName = "第一P2P";//默认站点名称
```

+ currentCode操作代码重复的。看能否抽一个方法？

javaref{cn.ucfgroup.oauth.controller.Firstp2pLoginController.java#line(86)|声明处}
```java
	//判断用户是否已登录，优先判断cookie
	Cookie[] cookies = request.getCookies();
	if (cookies != null && cookies.length > 0) {
	    for (Cookie cookie : cookies) {
	        if (cookie.getName().equals("currentCode")) {
	            if (StringUtils.isEmpty(cookie.getValue()))
	                break;
	            Map<String, String> codeMap = new HashMap<String, String>();
	            currentCode = cookie.getValue();
	            codeMap.put("code", currentCode);
	            ocs = oauthCodesService.queryOne(codeMap);
	            if (ocs != null) {
	                user = sysUserService.queryById(ocs.getUserid());
	                break;
	            } else {
	                currentCode = null;
	            }
	        }
	    }
	}
```

