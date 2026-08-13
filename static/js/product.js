// ===============================
// PRODUCT GALLERY
// ===============================

const thumbnails = document.querySelectorAll(".thumb");

const mainImage = document.getElementById("mainImage");

thumbnails.forEach((thumb) => {

    thumb.addEventListener("click", () => {

        thumbnails.forEach(item => {
            item.classList.remove("active");
        });

        thumb.classList.add("active");

        mainImage.innerHTML = thumb.dataset.image;

    });

});
const container = document.querySelector(".image-container");
const image = document.getElementById("product-image");

container.addEventListener("mousemove", function(e){

    const rect = container.getBoundingClientRect();

    const x = ((e.clientX - rect.left) / rect.width) * 100;
    const y = ((e.clientY - rect.top) / rect.height) * 100;

    image.style.transformOrigin = `${x}% ${y}%`;
    image.style.transform = "scale(2)";
});

container.addEventListener("mouseleave", function(){

    image.style.transform = "scale(1)";
    image.style.transformOrigin = "center center";

});
function showVideo(){

    document.querySelector(".main-image").style.display="none";

    document.getElementById("productVideo").style.display="block";

}

function changeImage(element){

    document.querySelector(".main-image").style.display="flex";

    const video=document.getElementById("productVideo");

    if(video){
        video.style.display="none";
    }

    document.getElementById("mainImage").src=element.src;

    document.querySelectorAll(".thumb").forEach(function(img){
        img.classList.remove("active");
    });

    element.classList.add("active");

}