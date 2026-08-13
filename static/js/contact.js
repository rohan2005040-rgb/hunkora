document.querySelectorAll(".faq-question").forEach((item)=>{

    item.addEventListener("click",()=>{

        const answer=item.nextElementSibling;

        const icon=item.querySelector("i");

        if(answer.style.display==="block"){

            answer.style.display="none";

            icon.classList.remove("fa-minus");

            icon.classList.add("fa-plus");

        }

        else{

            document.querySelectorAll(".faq-answer").forEach((ans)=>{

                ans.style.display="none";

            });

            document.querySelectorAll(".faq-question i").forEach((i)=>{

                i.classList.remove("fa-minus");

                i.classList.add("fa-plus");

            });

            answer.style.display="block";

            icon.classList.remove("fa-plus");

            icon.classList.add("fa-minus");

        }

    });

});