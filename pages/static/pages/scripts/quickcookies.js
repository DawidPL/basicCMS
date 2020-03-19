      (function($) {
        $.fn.extend({
            Qkies: function(options) {
                var defaults = {
                    fontSize: '14px',
                    lineHeight: '19px',
                    position: "bottom",
                    cookieText: "Używamy plików cookies, aby ułatwić Ci korzystanie z naszego serwisu oraz do celów statystycznych. Korzystając z naszej strony wyrażasz zgodę na wykorzystywanie przez nas plików cookies. Jeśli nie blokujesz tych plików, to zgadzasz się na ich użycie oraz zapisanie w pamięci urządzenia. Pamiętaj, że możesz samodzielnie zarządzać cookies, zmieniając ustawienia przeglądarki.",
                    background: "#EFEFEF",
                    textColor: "#4d4d4d",
                    textAlign: "center",
                    buttonBackground: "#4F6373",
                    buttonTextColor: "#FFF",
                    buttonFontSize: "15px",
                    buttonTextTop: "12px",
                    buttonTextLeft: "0px",
                    circleBackground: "#BB8C00",
                    hover: {
                        buttonBackground: "#FFF",
                        buttonTextColor: "#4F6373",
                        circleBackground: "#4F6373"
                    },
                    paddingTop: "15px",
                    paddingBot: "15px",
                    expires: 365
                }
                options =  $.extend(defaults, options);
    
                return this.each(function() {
                    if ($("#q-cookie-box").attr("id")) return "";
                    var cookieHTML = "";
                    var cookieStyle = "";
                    var showCookie = true;
                    var buttonCSSPath = "#q-cookie-box #qcb-close-btn";
                    var thisBody = $("body");
    
                    if (document.cookie!="") {
                        var cookies = document.cookie.split("; ");
                        for (i = 0; i < cookies.length; i++) {
                            var cookieName = cookies[i].split("=")[0]; //nazwa ciastka
                            var cookieValue = cookies[i].split("=")[1]; //wartość ciastka
                            if (cookieName === "q_cookie_agree") {
                                if (cookieValue == "1") showCookie = false;
                            }
                        }
                    }
    
                    if (showCookie == true) {
                        cookieStyle = '<style type="text/css">' +
                            '#q-cookie-box { '+
                                'background: '+options.background+';'+
                                'width: 100%;'+
                                'position:fixed;'+
                                'bottom:0px;'+
                                'left: 0;'+
                                'right: 0px;'+
                                'margin: 0px auto;'+
                                'height:auto;'+
                                'padding: '+options.paddingTop+' 0px '+options.paddingBot+' 0px;'+
                                'z-index:65465465656;'+
                                'text-align:center;'+
                                'box-shadow: 0 0 5px #D4D4D4;'+
                                '-webkit-transition: all 0.3s ease;'+
                                '-moz-transition: all 0.3s ease;'+
                                '-o-transition: all 0.3s ease;'+
                                'transition: all 0.3s ease;'+
                            '}' +
                            '#q-cookie-box * { '+
                                '-webkit-box-sizing: initial !important;'+
                                '-moz-box-sizing: initial !important;'+
                                'box-sizing: initial !important;'+
                            '}' +
                            '#q-cookie-box .qcb-text { '+
                                'color: '+options.textColor+';'+
                                'font-size: '+options.fontSize+';'+
                                'line-height: '+options.lineHeight+';'+
                                'text-align: '+options.textAlign+';'+
                                'margin: 0 15px 0 15px;'+
                                'width: auto;'+
                                'padding-right: 60px;'+
                                '-webkit-transition: all 0.3s ease;'+
                                '-moz-transition: all 0.3s ease;'+
                                '-o-transition: all 0.3s ease;'+
                                'transition: all 0.3s ease;'+
                            '}' +
                            '#q-cookie-box .qcb-text a { '+
                                'color: '+options.textColor+';'+
                            '}' +
                            '#q-cookie-box .qcb-text a:hover { '+
                                'color: '+options.textColor+';'+
                            '}' +
                            '#q-cookie-box #qcb-close-btn { '+
                                'position: absolute;'+
                                'right: 10px;'+
                                'top: -25px;'+
                                'cursor: pointer;'+
                            '}' +
                            '#q-cookie-box #qcb-c-1 { '+
                                'background: '+options.buttonBackground+';'+
                                'border: 2px solid white;'+
                                'width: 45px;'+
                                'height: 45px;'+
                                'color: '+options.buttonTextColor+';'+
                                'font-weight: bold;'+
                                'font-size: '+options.buttonFontSize+';'+
                                'text-align: center;'+
                                'padding: 0;'+
                                'margin: 0;'+
                                'border-radius: 35px;'+
                                'position: relative;'+
                                'right: 0;'+
                                'top: 0;'+
                                'box-shadow: 0 0 5px silver;'+
                                'display: block;'+
                                '-webkit-transition: all 0.3s ease;'+
                                '-moz-transition: all 0.3s ease;'+
                                '-o-transition: all 0.3s ease;'+
                                'transition: all 0.3s ease;'+
                            '}' +
                            '#q-cookie-box #qcb-close-btn:hover #qcb-c-1 { '+
                                'background: '+options.hover.buttonBackground+' !important;'+
                                'color: '+options.hover.buttonTextColor+' !important;'+
                                'box-shadow: 0px 0px 5px 5px rgba(214, 214, 214, 0.4) !important;'+
                                '-webkit-transform:rotate(360deg) scale(1.05);'+
                                'transform:rotate(360deg) scale(1.05);'+
                            '}' +
                            '#q-cookie-box #qcb-c-1 strong { '+
                                'position: relative;'+
                                'top: '+options.buttonTextTop+';'+
                                'left: '+options.buttonTextLeft+';'+
                            '}' +
                            '#q-cookie-box #qcb-c-2 { '+
                                'width: 11px;'+
                                'height: 11px;'+
                                'background: '+options.circleBackground+';'+
                                'border: 2px solid white;'+
                                'border-radius: 20px;'+
                                'position: absolute;'+
                                'bottom: -4px;'+
                                'left: -1px;'+
                                '-webkit-transition: all 0.3s ease;'+
                                '-moz-transition: all 0.3s ease;'+
                                '-o-transition: all 0.3s ease;'+
                                'transition: all 0.3s ease;'+
                            '}' +
                            '#q-cookie-box #qcb-close-btn:hover #qcb-c-2 { '+
                                'background: '+options.hover.circleBackground+' !important;'+
                            '}' +
                            '@media (max-width: 767px) { '+
                                '#q-cookie-box .qcb-text {	text-align: justify; }'+
                            '}' +
                            '@media (max-width: 450px) { '+
                                '#q-cookie-box .qcb-text { margin: 25px 15px 0 15px; padding-right: 0px; }'+
                                '#q-cookie-box #qcb-close-btn { '+
                                    'position: absolute;'+
                                    'right: 10px;'+
                                    'top: -25px;'+
                                    'left: 10px;'+
                                    'margin: 0px auto;'+
                                    'width: 52px;'+
                                    'cursor: pointer;'+
                                '}'+
                            '}' +
                        '</style>';
    
                        cookieHTML = '<div id="q-cookie-box">'+
                            '<div class="qcb-text">'+options.cookieText+'</div>'+
                            '<div id="qcb-close-btn">'+
                                '<span id="qcb-c-1">'+
                                    '<strong>OK</strong>'+
                                '</span>'+
                                '<span id="qcb-c-2"></span>'+
                            '</div>'+
                        '</div>' + cookieStyle;
                        $('body').append(cookieHTML);
                    }
    
                    function hideCookies() {
                        var data = new Date();
                        data.setTime(data.getTime()+(options.expires*24*60*60*1000));
                        var expires = "; expires="+data.toGMTString();
                        document.cookie = "q_cookie_agree=1" + expires + "; path=/";
    
                        var cookieBox = $('#q-cookie-box');
    
                        //efekt - schowanie komunikatu w dół
                        var cookieHeight = cookieBox.height() + 80;
                        cookieBox.css("margin-" + options.position, "-" + cookieHeight + "px");
    
                        //efekt - schowanie komunikatu w lewo
                        //var cookieWidth = cookieBox.width() + 30;
                        //cookieBox.css("margin-left", "-"+cookieWidth+"px");
    
                        setTimeout(function() {
                            cookieBox.css('display', 'none');
                        }, 8000);
                    }
    
                    if ($.isFunction(thisBody.on)) thisBody.on('click', buttonCSSPath, function() { hideCookies(); });
                    else if ($.isFunction(thisBody.live)) thisBody.live('click', buttonCSSPath, function() { hideCookies(); });
                    else thisBody.find(buttonCSSPath).click(function() { hideCookies(); });
                });
            }
        });
    })(jQuery);
    jQuery(document).ready(
        function($) {
            $('body').Qkies();
        }
    );
    
    