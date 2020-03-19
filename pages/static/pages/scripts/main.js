$(document).ready(function(){
    
    // Template sorting 

    jQuery.fn.sortDivs = function sortDivs(tag) {
      $(tag, this[0]).sort(dec_sort).appendTo(this[0]);
      function dec_sort(a, b){ return ($(b).data('sort')) < ($(a).data('sort')) ? 1 : -1; }
  };
      $('.wrapper').sortDivs('> div');
      /*$('.section_one').sortDivs('> img');
      $('.section_two').sortDivs('> .single_box');
      $('.subpage_gallery').sortDivs('> img');*/
}); 
