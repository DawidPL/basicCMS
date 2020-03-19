jQuery(document).ready(function($) {
/*
    var template_1 ="<div><h1>template1</h1></div>"
    var template_2 = "<div><h1>template2</h1></div>"
    var template_3 = "<div><h1>template3</h1></div>"
    var templates_array = [[template_1, template_1, template_1, template_1, template_1],
                            [template_2, template_2, template_2, template_2, template_2],
                            [template_3, template_3, template_3, template_3, template_3],
                            [template_3, template_3, template_3, template_3, template_3],
                            [template_3, template_3, template_3, template_3, template_3],
                            ]
    var child_nums = document.getElementById('id_template');


    document.getElementById('id_template').onchange = function(event) {
        let get_val = event.target.selectedOptions[0].getAttribute("value");
        if (get_val){
            for (let i = 0; i < templates_array.length; i++){
                var iframe = document.getElementsByTagName('iframe')[i].contentWindow.document;
                var iframe_content = iframe.querySelector('body');
                iframe_content.innerHTML = templates_array[get_val-1][i]
                iframe_content.replace('\n', '');
            };
        }else{
            for (let i = 0; i < templates_array.length; i++){
                var iframe = document.getElementsByTagName('iframe')[i].contentWindow.document;
                var iframe_content = iframe.querySelector('body');
                iframe_content.innerHTML = '';
            };
        };
    };
*/
    document.getElementById('id_template').onchange = function(event) {
        var get_val = event.target.selectedOptions[0].getAttribute("value");

        /* template array :
        [2, 1, 4], [1,1,3], [0,1,2] - single templates, 
        [2, 1, 4] : 2 - number of galleries, 1 - number of boxes, 4 - number of sections
        */
        template_array = [[2, 1, 4], [1,1,3], [0,1,2]]

        var min = 200;
        var max = 500;

        $( "li" ).each(function() {
        var $this = $(this);
        var time = $this.data('time');
        
        $this.css('display', (time < min || time > max) ? 'none' : 'block');
        });

        var numForms = $('#homepage_form .module .form-row').length;
        for (let i = 0; i < numForms; i++){
            $('#homepage_form .module .form-row:nth-child('+ (i+1) +')').attr('data-order', i+1);
        }
        for (let i = 0; i < template_array.length; i++){
            for (let template of template_array[i]){
                if(get_val = i){
                    $('#id_template').click(function(){
                        $('#homepage_form .module .form-row:nth-child(n+8)').css('display', 'block');
                    });
                }else{
                    $('#id_template').click(function(){
                        $('#homepage_form .module .form-row:nth-child(n+8):nth-child(-n+16)').css('display', 'block');
                    });
                };  
            };

        };
    };
});

