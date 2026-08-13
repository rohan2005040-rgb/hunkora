document.addEventListener("DOMContentLoaded", function () {

    const slides = document.querySelectorAll(".hero-slide");
    const dots = document.querySelectorAll(".hero-dots .dot");

    const nextBtn = document.querySelector(".hero-arrow.next");
    const prevBtn = document.querySelector(".hero-arrow.prev");

    let current = 0;
    let autoSlide;

    // =========================
    // Show Slide
    // =========================

    function showSlide(index){

        slides.forEach((slide)=>{

            slide.classList.remove("active");

        });

        dots.forEach((dot)=>{

            dot.classList.remove("active");

        });

        slides[index].classList.add("active");

        dots[index].classList.add("active");

        current = index;

    }

    // =========================
    // Next Slide
    // =========================

    function nextSlide(){

        let index = current + 1;

        if(index >= slides.length){

            index = 0;

        }

        showSlide(index);

    }

    // =========================
    // Previous Slide
    // =========================

    function prevSlide(){

        let index = current - 1;

        if(index < 0){

            index = slides.length - 1;

        }

        showSlide(index);

    }

    // =========================
    // Auto Slide
    // =========================

    function startAuto(){

        autoSlide = setInterval(function(){

            nextSlide();

        },5000);

    }

    function stopAuto(){

        clearInterval(autoSlide);

    }

    startAuto();

    // =========================
    // Arrow Click
    // =========================

    nextBtn.addEventListener("click",function(){

        stopAuto();

        nextSlide();

        startAuto();

    });

    prevBtn.addEventListener("click",function(){

        stopAuto();

        prevSlide();

        startAuto();

    });

    // =========================
    // Dot Click
    // =========================

    dots.forEach(function(dot,index){

        dot.addEventListener("click",function(){

            stopAuto();

            showSlide(index);

            startAuto();

        });

    });

    // =========================
    // Mobile Swipe
    // =========================

    let touchStartX = 0;
    let touchEndX = 0;

    const hero = document.querySelector(".hero-slider");

    hero.addEventListener("touchstart",function(e){

        touchStartX = e.changedTouches[0].screenX;

    });

    hero.addEventListener("touchend",function(e){

        touchEndX = e.changedTouches[0].screenX;

        if(touchEndX < touchStartX - 50){

            stopAuto();

            nextSlide();

            startAuto();

        }

        if(touchEndX > touchStartX + 50){

            stopAuto();

            prevSlide();

            startAuto();

        }

    });

});