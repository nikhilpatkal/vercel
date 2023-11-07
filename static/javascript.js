
document.addEventListener("DOMContentLoaded", function() {
    const typewriterElement = document.getElementById("typewriter");
    const textsToType = [
        "FULLSTACK DEVLOPER.",
        "WEB DESIONER.",
        "JAVA DEVLOPER."
    ];
    const typingSpeed = 120; // Adjust typing speed (milliseconds per character)
    
    let textIndex = 0;

    function typeWriter(text, index, onComplete) {
        if (index < text.length) {
            typewriterElement.textContent += text.charAt(index);
            setTimeout(function() {
                typeWriter(text, index + 1, onComplete);
            }, typingSpeed);
        } else {
            setTimeout(onComplete, 1000); // Wait for 1 second before starting the next text
        }
    }

    function typeNextText() {
        const nextText = textsToType[textIndex];
        typewriterElement.textContent = "";
        typeWriter(nextText, 0, function() {
            textIndex = (textIndex + 1) % textsToType.length; // Move to the next text (loop back to the first if at the end)
            typeNextText();
        });
    }

    // Start the typewriter effect when the page loads
    typeNextText();
});


//for dark mode code in js
var count=1;
        function light()
        {
            
        
            if(count%2!=0)
                {
                   
                    document.getElementById("color1").style.backgroundColor = "black";
                    document.getElementById("icon1").style.color = "orange";
                    document.getElementById("icon2").style.color = "orange";
                    document.getElementById("icon3").style.color = "orange";
                    document.getElementById("icon4").style.color = "orange";
                    document.getElementById("nav_item").style.color = "orange";
                    document.getElementById("color3").style.color = "white";
                    
                     document.getElementById("color2").style.backgroundColor = "black";
                    document.getElementById("color3").style.backgroundColor = "black";
            
                    document.getElementById("color4").style.backgroundColor = "black";
                    document.getElementById("skil-header").style.backgroundColor = "black";
                    document.getElementById("my").style.color = "white";
                    document.getElementById("1").style.backgroundColor = "black";
                    document.getElementById("2").style.backgroundColor = "black";
                    document.getElementById("3").style.backgroundColor = "black";
                    document.getElementById("4").style.backgroundColor = "black";
                    document.getElementById("5").style.backgroundColor = "black";
                    document.getElementById("6").style.backgroundColor = "black";
                    document.getElementById("7").style.backgroundImage = "none";
                    count++;

            
                    

         
                }
                else
                {
                    document.getElementById("color1").style.backgroundColor = "gray";
                    document.getElementById("color1").style.backgroundColor = 'white';
                    document.getElementById("color2").style.backgroundColor = ' gray';
                    document.getElementById("color3").style.backgroundColor = '  rgb(246, 240, 240)';
                    document.getElementById("color4").style.backgroundColor = '   rgb(233, 206, 206)'; 
                    document.getElementById("icon1").style.color = "black";
                    document.getElementById("icon2").style.color = "black";
                    document.getElementById("icon3").style.color = "black";
                    document.getElementById("icon4").style.color = "black";
                    document.getElementById("nav_item").style.color = "black";
                    document.getElementById("skil-header").style.backgroundColor = "white";
                    document.getElementById("color3").style.color = "black"; 
                    count++;

                 }    
            }




            //this is code for the the text is move when we open our code
            var s=1500;
            var v=1500;

            var id= ' '
            var id2=' '
            function reverse()
            {
                id=setInterval(fast,40)
                id2=setInterval(sec,40)
            }
            function fast()
            {


                document.getElementById('s1').style.marginLeft=s+'px';
                s=s-100

               
               

                if(s==-100)
                {
                    clearInterval(id);

                }
            }

            function sec()
            {
                document.getElementById('typewriter').style.marginRight=v+'px';
                v=v-100
                if(v==-100)
                {
                    clearInterval(id2);

                }

            }


           
           





            
          






