/* When the user clicks on the button,
toggle between hiding and showing the dropdown content */

var element = document.getElementById("style-7");
  element.scrollTop = element.scrollHeight;
function myFunction() {
  document.getElementById("myDropdown1").classList.toggle("show");
  

}
var m = 0;

// Close the dropdown menu if the user clicks outside of it
window.onclick = function(event) {
  if (!event.target.matches('.dropbtn1')) {
    var dropdowns = document.getElementsByClassName("dropdown-content");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
      }
    }
  }
}


$(document).ready(function(){
$('.web-footer').hide();
	var s= $('.salle').text();
if ( s.includes('_') ){
var group=s;
var course ='b;'




}
else{
var group=$('#sgroup').text();
var course= s;
}
	frappe.call({
	
				 method: "frappe.general.live", //dotted path to server method
				 args:{ 'group':group,'course':course,'typ':'first'},
				callback: function(r) {
				
				}
			});
    
    
    
    
    $("#textarea").keypress(function (e) {
        var code = (e.keyCode ? e.keyCode : e.which);
        //alert(code);
        if (code == 13) {
            var message = $('#textarea').val();
    var salle = $('.salle').text();
        		frappe.call({
	
				 method: "frappe.general.send", //dotted path to server method
				 args:{'message':message, 'salle':salle},
				callback: function(r) {
				
				}
			});
        }
       
    });
    
    
    
    $("#send").click(function(){
    var message = $('#textarea').val();
    var salle = $('.salle').text();
        		frappe.call({
	
				 method: "frappe.general.send", //dotted path to server method
				 args:{'message':message, 'salle':salle},
				callback: function(r) {
				const w = r.message.split('$');
				
				if ( w[2] =="None") {
				
				w[2]="/files/default.jpg";
				} 
				var toadd = " <div style='margin:10px;padding-bottom:20px;'><div style='display:inline;width:5%;float:left;'> <img src='"+ w[2]+"' alt='poc' width='45' height='45' style='border-radius:50%;'> </div> <div style='background-color:white;width:92%;padding:10px;float:right;border-radius:5px;float:left;'><div style=''> <h3 style='display:inline;'>"+w[1]+"</h3> <span style='display:inline;font-size:14px;color:#adadad'>"+w[0]+"</span> </div><span>"+message+"</span></div></div></br> </br>"
				$(toadd).appendTo( ".scrollbar" );
				$('#textarea').val('');
				var m=parseInt($('#max').text())+1;
				$('#max').text(m);
				var element = document.getElementById("style-7");
   				element.scrollTop = element.scrollHeight;
				}
			});
	
	
	
    
    
   });
    
    
    
    $(".clickgroups").click(function(){
    $('.salle').text($(this).text());
    
    		frappe.call({
	
				 method: "frappe.general.meetingexist", //dotted path to server method
				 args:{ 'salle':$(this).text()},
				callback: function(r) {
				
				
					if (r.message=="1"){
						$('.loader').show();
						$( "#start" ).addClass( "disabledlink" );
						$( "#plan" ).addClass( "disabledlink" );
						$( "#join" ).removeClass( "disabledlink" );
					
					}
					else
					{
					$('.loader').hide();
					$( "#join" ).addClass( "disabledlink" );
					$( "#start" ).removeClass( "disabledlink" );
					$( "#plan" ).removeClass( "disabledlink" );
					
					
					}
				}
			});
		$( ".scrollbar" ).empty();
		frappe.call({
	
				 method: "frappe.general.restart", //dotted path to server method
				 args:{ 'salle':$(this).text()},
				callback: function(r) {
				if (r.message != ""){
				var chat = r.message.split('$');
				var m = chat[chat.length-1];
				$('#max').text(m);
				
				for(var i= 0; i < chat.length-1; i++){
				
				const w = chat[i].split('£');
				
				if ( w[3] =="None") {
				
				w[3]="/files/default.jpg";
				} 
				
					
    					var toadd = " <div style='margin:10px;padding-bottom:20px;'><div style='display:inline;width:5%;float:left;'> <img src='"+ w[3]+"' alt='poc' width='45' height='45' style='border-radius:50%;'> </div> <div style='background-color:white;width:92%;padding:10px;float:right;border-radius:5px;float:left;'><div style=''> <h3 style='display:inline;'>"+w[1]+"</h3> <span style='display:inline;font-size:14px;color:#adadad'>"+w[0]+"</span> </div><span>"+w[2]+"</span></div></div></br></br> "
				$(toadd).appendTo( ".scrollbar" );
				$('#textarea').val('');
    					
    					
    					 var element = document.getElementById("style-7");
   					 element.scrollTop = element.scrollHeight;
					}
				
				
					}
				}
			});
			
			
			
			
			
			
			
			
			
			
			
			
			
			
    });
    });
    
    
    
    
    
const interval = setInterval(function() {
       		frappe.call({
	
				 method: "frappe.general.meetingexist", //dotted path to server method
				 args:{ 'salle':$('.salle').text()},
				callback: function(r) {
				
				
					if (r.message=="1"){
						$('.loader').show();
						$( "#start" ).addClass( "disabledlink" );
						$( "#plan" ).addClass( "disabledlink" );
						$( "#join" ).removeClass( "disabledlink" );
					
					}
					else
					{
					$('.loader').hide();
					$( "#join" ).addClass( "disabledlink" );
					$( "#start" ).removeClass( "disabledlink" );
					$( "#plan" ).removeClass( "disabledlink" );
					
					
					}
				}
			});
			
var s= $('.salle').text();


var m=$('#max').text();
	frappe.call({
	
				 method: "frappe.general.live", //dotted path to server method
				 args:{ 'salle':s,'ma':m},
				callback: function(r) {
				if (r.message != ""){
				var chat = r.message.split('$');
				var m = chat[chat.length-1];
				$('#max').text(m);
				
				for(var i= 0; i < chat.length-1; i++){
				
				const w = chat[i].split('£');
				
				if ( w[3] =="None") {
				
				w[3]="/files/default.jpg";
				} 
				
					
    					var toadd = " <div style='margin:10px;padding-bottom:20px;'><div style='display:inline;width:5%;float:left;'> <img src='"+ w[3]+"' alt='poc' width='45' height='45' style='border-radius:50%;'> </div> <div style='background-color:white;width:92%;padding:10px;float:right;border-radius:5px;float:left;'><div style=''> <h3 style='display:inline;'>"+w[1]+"</h3> <span style='display:inline;font-size:14px;color:#adadad'>"+w[0]+"</span> </div><span>"+w[2]+"</span></div></div></br> </br>"
				$(toadd).appendTo( ".scrollbar" );
				$('#textarea').val('');
				var element = document.getElementById("style-7");
   					 element.scrollTop = element.scrollHeight;
    					
    					
    					
					}
				
				
					}
				
				}
			});		
			
			
			
			
			
			
			
			
			
			
			
			
			
			
 }, 1000);
