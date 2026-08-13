const faqItems = document.querySelectorAll(".faq-item");

faqItems.forEach(item => {

    const button = item.querySelector(".faq-question");

    button.addEventListener("click", () => {

        faqItems.forEach(i => {

            if(i !== item){

                i.classList.remove("active");

            }

        });

        item.classList.toggle("active");

    });

});
window.addEventListener("scroll", function () {

    const header = document.querySelector(".header");

    if (window.scrollY > 50) {
        header.classList.add("scrolled");
    } else {
        header.classList.remove("scrolled");
    }

});
const counters=document.querySelectorAll(".counter");

counters.forEach(counter=>{

    const update=()=>{

        const target=+counter.getAttribute("data-target");

        const count=+counter.innerText;

        const speed=150;

        const inc=target/speed;

        if(count<target){

            counter.innerText=Math.ceil(count+inc);

            setTimeout(update,15);

        }else{

            counter.innerText=target;

        }

    };

    update();

});