function getDateTime() {
    var now     = new Date(); 
    var year    = now.getFullYear();
    var month   = now.getMonth()+1; 
    var day     = now.getDate();
    var hour    = now.getHours();
    var minute  = now.getMinutes();
    var second  = now.getSeconds(); 
    if(month.toString().length == 1) {
         month = '0'+month;
    }
    if(day.toString().length == 1) {
         day = '0'+day;
    }   
    if(hour.toString().length == 1) {
         hour = '0'+hour;
    }
    if(minute.toString().length == 1) {
         minute = '0'+minute;
    }
    if(second.toString().length == 1) {
         second = '0'+second;
    }   
    var dateTime = year+'-'+month+'-'+day+' '+hour+':'+minute+':'+second;   
     return dateTime;
}

function open_close_Nav() {
     nav = document.getElementById("nav");
     if(nav.style.width != "80%"){
          nav.style.width = "80%";
          nav.style.paddingLeft = "25px";
     } else{
          nav.style.width = "0%";          
          nav.style.paddingLeft = "0px";
     }
     document.getElementById("nav_button").classList.toggle("active");
}
   
function closeNav() {
     document.getElementById("nav").style.width = "0%";
     document.getElementById("nav_button").classList.remove("active");
}

$( document ).ready(function() {
    // Что-то сделать    
    
});

