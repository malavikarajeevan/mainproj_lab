$(document).ready(function () {
    $('.derw').slick({
        lazyLoad: 'ondemand',
        slidesToShow: 5,
        slidesToScroll: 4,
        autoplay: true,
        autoplaySpeed: 4000,

        infinite: true,
        arrows: false,
        responsive: [{
            breakpoint: 1280,
            settings: {
                arrows: false,
                slidesToShow: 3,
                slidesToScroll: 2,
            }
        },
        {
            breakpoint: 770,
            settings: {
                arrows: false,
                slidesToShow: 2,
                slidesToScroll: 1,
            }
        },
        {
            breakpoint: 520,
            settings: {
                slidesToShow: 2,
                slidesToScroll: 1,
                centerPadding: '0px',

            }
        }
        ]
    });
});





$(document).ready(function () {
    $('.gmhrw').slick({
        lazyLoad: 'ondemand',
        slidesToShow: 3,
        slidesToScroll: 2,
        autoplay: true,
        autoplaySpeed: 4000,

        infinite: true,
        arrows: false,
        responsive: [{
            breakpoint: 1280,
            settings: {
                arrows: false,
                slidesToShow: 3,
                slidesToScroll: 2,
            }
        },
        {
            breakpoint: 770,
            settings: {
                arrows: false,
                slidesToShow: 2,
                slidesToScroll: 1,
            }
        },
        {
            breakpoint: 520,
            settings: {
                slidesToShow: 2,
                slidesToScroll: 1,
                centerPadding: '0px',

            }
        }
        ]
    });
});







$(document).ready(function () {
    $('.testirw').slick({
        lazyLoad: 'ondemand',
        slidesToShow: 3,
        slidesToScroll: 2,
        autoplay: true,
        autoplaySpeed: 4000,

        infinite: true,
        arrows: false,
        responsive: [{
            breakpoint: 1280,
            settings: {
                arrows: false,
                slidesToShow: 3,
                slidesToScroll: 2,
            }
        },
        {
            breakpoint: 770,
            settings: {
                arrows: false,
                slidesToShow: 2,
                slidesToScroll: 1,
            }
        },
        {
            breakpoint: 520,
            settings: {
                slidesToShow: 2,
                slidesToScroll: 1,
                centerPadding: '0px',

            }
        }
        ]
    });
});


function validateForm() {
    var phoneInput = document.getElementsByName('phone')[0];
    var phoneValue = phoneInput.value;
    // Check if the input contains only numeric characters
    var regex = /^[0-9]*$/;
    if (!regex.test(phoneValue)) {
        alert("Please enter a valid phone number (numeric characters only).");
        return false; // Prevent form submission
    }
    return true; // Allow form submission if validation passes
}

    // window.addEventListener('DOMContentLoaded', function() {
    //     const container = document.querySelector('.packing'); // Select the container element

    //     let isMouseDown = false;
    //     let startX;
    //     let scrollLeft;

    //     container.addEventListener('mousedown', function(e) {
    //         isMouseDown = true;
    //         startX = e.pageX - container.offsetLeft;
    //         scrollLeft = container.scrollLeft;
    //     });

    //     container.addEventListener('mouseup', function() {
    //         isMouseDown = false;
    //     });

    //     container.addEventListener('mouseleave', function() {
    //         isMouseDown = false;
    //     });

    //     container.addEventListener('mousemove', function(e) {
    //         if (!isMouseDown) return;
    //         e.preventDefault();
    //         const x = e.pageX - container.offsetLeft;
    //         const walk = (x - startX) * 3; // Adjust scrolling speed
    //         container.scrollLeft = scrollLeft - walk;
    //     });
    // });
