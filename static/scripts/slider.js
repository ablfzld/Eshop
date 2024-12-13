let slider = document.getElementById('Slider').childElementCount;
let slide = 1;
$("#Slide_1").addClass("slide-show");
setInterval(() => {
    for (let i = 1; i < slider+1; i++) {    
       if (i == slide) {
        $("#Slide_"+i).addClass("slide-show");
       }
       else{
        $("#Slide_"+i).removeClass("slide-show");
       }
    }
    
    if(slide==slider){
        slide  = 1;
    }
    else{
        slide = slide+1;
    }
 }, 10000);

 function MoveSliderRight() {
    if(slide==1){
        slide  = slider;
    }
    else{
        slide = slide-1;
    }
    for (let i = 1; i < slider+1; i++) {    
        if (i == slide) {
         $("#Slide_"+i).addClass("slide-show");
        }
        else{
         $("#Slide_"+i).removeClass("slide-show");
        }
     }
 }

 function MoveSliderLeft() {
    for (let i = 1; i < slider+1; i++) {    
        if (i == slide) {
         $("#Slide_"+i).addClass("slide-show");
        }
        else{
         $("#Slide_"+i).removeClass("slide-show");
        }
     }
     
     if(slide==slider){
         slide  = 1;
     }
     else{
         slide = slide+1;
     }  
 }

 function ChangeSlide(aslide) {
    for (let i = 1; i < slider+1; i++) {    
        if (i == aslide) {
         $("#Slide_"+i).addClass("slide-show");
        }
        else{
         $("#Slide_"+i).removeClass("slide-show");
        }
     }
 }