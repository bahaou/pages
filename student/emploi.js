$(document).ready(function(){
     $(".jour").hide();
     $('.btn-dark').prop('disabled', true);
    $(".s").click(function(){
        $(".jour").toggle();
        $(".semaine").toggle();
        $(".s").toggleClass('btn-light btn-dark');
    	$('.s').prop('disabled', false);
    	$(this).prop('disabled', true);	
    });
    
    
    $(".mobile").click(function(){
    	var id = $(this).attr('id');
    	var cours = $("#cours"+id).text();
    	var ins = $("#ins"+id).text();
    	var salle = $("#salle"+id).text();
    	var day = $("#day"+id).text();
    	var time = $("#time"+id).text();
    	var encours = $("#encours"+id).text();
    	$('#exampleModalLongTitle').text(cours+" ");
    	$('#modalins').text("instructeur : "+ins);
    	$('#modalsalle').text(salle);
    	$('#modaltime').text(day+time);
    	$('#modalencours').html('');
    	if( encours=='yes'){
    	$('#modalencours').html("<div class='loader' style = 'vertical-align: top;'><span class='loader__dot' style='color:#fa4e37;font-size: 10px;'><i class='fa fa-circle'></i></span></div>");}
    	
    	
    
    
    });
    
    
    
    
    
});



function is(s){
return ($('.'+s).css("color")=="rgb(255, 255, 255)");
}


var tab = document.getElementById("tab");
var groupe = document.getElementById("groupe");

$(document).on('click','#btn',function(){
	
let pdf = new jsPDF();

let page= function() {
    pdf.save('pagename.pdf');
   
};

pdf.addHTML(tab,page);


})
function switchto(p) {
	var other1 ='pc'; var other2 = 'mobile';
	
	if (p=='pc' && is("j")) { $(".semaine").hide();$(".jour").show(); other1='mobile';other2='mini';}
	if (p=='pc' && is("s")) { $(".semaine").show(); other1='mobile';other2='mini';}
	if (p=='mobile'  && is("j") ){  $(".semaine").hide() ; $(".jour").show(); other1='pc';other2='mini';}
	if (p=='mobile'  && is("s") ){  $(".semaine").show() ; other1='pc';other2='mini';}
	if (p=='mini') {  $(".semaine").hide()   ;  $(".jour").hide() ;  }
  	$("."+other1).hide();
  	$("."+other2).hide();
  	$("."+p).show();
  	$("td").css("width", "5px");
 	}

if( /Android|webOS|iPhone|iPad|Mac|Macintosh|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent) ) {
 	switchto('mobile');
 }else{ switchto('pc');}
const heightOutput = document.querySelector('#height');
const widthOutput = document.querySelector('#width');


function reportWindowSize() {
  var height = window.innerHeight;
  var width = window.innerWidth;
  if (width <500){
  switchto('mini');
  }else if ( width < 750  ){
  switchto('mobile');
  }else {switchto('pc');}
  
  }
reportWindowSize();
window.onresize = reportWindowSize;
 var swiper = new Swiper('.swiper-container', {
      navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
      },
    });
    
    
  mybutton = document.getElementById("myBtn");

// When the user scrolls down 150px from the top of the document, show the button
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 150 || document.documentElement.scrollTop > 150) {
    mybutton.style.display = "block";
  } else {
    mybutton.style.display = "none";
  }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
  document.body.scrollTop = 0; // For Safari
  document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
} 


function generate() {  
    var pdf = new jsPDF('l','pt','a4');
    margins = {  
        top: 150,  
        bottom: 60,  
        left: 40,  
        right: 40,  
        width: 600  
    }; 
   
    pdf.addHTML(document.body,function() {
        pdf.save('web.pdf');
    });
} 
function print() {
            window.open(
              "/student/emploi", "_blank");
        }

        
        

    
