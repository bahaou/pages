var today = new Date();
var dd = String(today.getDate()).padStart(2, '0');
var mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
var yyyy = today.getFullYear();

today = dd + '-' + mm + '-' + yyyy;


$(document).ready(function(){
	  var arr= [];
	  var today = $("#today").text()
	  var days=["Lundi","Mardi","Mercredi","Jeudi","Vendredi","Samedi"]
        $(".jour").click(function(){
        	$("#jour").show();
        	$("#semaine").hide();
        
        	for (i = 0; i < 6; i++) {
        		 var w = $("."+days[i]).width();
        		 arr.push(w);
			if(days[i] !=today ){  $("."+days[i]).animate({width: 0}); }
}
           
            
     });
     
     
      $(".semaine").click(function(){
      $("#jour").hide();
      $("#semaine").show();
            for (i = 0; i < 6; i++) {
        	if(days[i] !=today ){  $("."+days[i]).animate({width: arr[i]}); }
}
            
     });
     
     
     
     	
    });
    
    document.write(today);
