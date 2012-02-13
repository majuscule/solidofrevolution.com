$(document).ready(function(){
  $('#submit').click(function(event){
    if ( $('#equation').val() == ''
         || $('#equation').val().indexOf("^") != -1
         || $('#a').val() == ''
         || $('#b').val() == ''
         || $('input[@name=dependent_variable]:checked').length !=2
       ){
         event.preventDefault();
    }
  });
});
