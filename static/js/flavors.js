/* ===========================================================
        HUNKORA FLAVORS SECTION
=========================================================== */

document.addEventListener("DOMContentLoaded", function () {

    const cards = document.querySelectorAll(".flavor-card");

    const observer = new IntersectionObserver(function(entries){

        entries.forEach(function(entry){

            if(entry.isIntersecting){

                entry.target.classList.add("show-card");

            }

        });

    },{

        threshold:.2

    });

    cards.forEach(function(card){

        observer.observe(card);

    });

});


/* ===============================================
        PARALLAX HOVER EFFECT
=============================================== */

const cards=document.querySelectorAll(".flavor-card");

cards.forEach(function(card){

    card.addEventListener("mousemove",function(e){

        const rect=card.getBoundingClientRect();

        const x=e.clientX-rect.left;

        const y=e.clientY-rect.top;

        const rotateY=((x/rect.width)-0.5)*12;

        const rotateX=((rect.height/2-y)/rect.height)*12;

        card.style.transform=

        `
        perspective(1000px)
        rotateX(${rotateX}deg)
        rotateY(${rotateY}deg)
        translateY(-12px)
        scale(1.03)
        `;

    });

    card.addEventListener("mouseleave",function(){

        card.style.transform="";

    });

});


/* ===============================================
        BUTTON RIPPLE EFFECT
=============================================== */

const buttons=document.querySelectorAll(".order-btn a,.flavor-btn");

buttons.forEach(function(btn){

    btn.addEventListener("click",function(e){

        const circle=document.createElement("span");

        circle.classList.add("ripple");

        const rect=btn.getBoundingClientRect();

        circle.style.left=e.clientX-rect.left+"px";

        circle.style.top=e.clientY-rect.top+"px";

        btn.appendChild(circle);

        setTimeout(function(){

            circle.remove();

        },700);

    });

});