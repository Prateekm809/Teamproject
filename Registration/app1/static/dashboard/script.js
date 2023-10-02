document.addEventListener("DOMContentLoaded", function(event) {

    const showNavbar = (toggleId, navId, bodyId, headerId) =>{
        const toggle = document.getElementById(toggleId),
            nav = document.getElementById(navId),
            bodypd = document.getElementById(bodyId),
            headerpd = document.getElementById(headerId)

// Validate that all variables exist
        if(toggle && nav && bodypd && headerpd){
            toggle.addEventListener('click', ()=>{
// show navbar
                nav.classList.toggle('show')
// change icon
                toggle.classList.toggle('bx-x')
// add padding to body
                bodypd.classList.toggle('body-pd')
// add padding to header
                headerpd.classList.toggle('body-pd')
            })
        }
    }

    showNavbar('header-toggle','nav-bar','body-pd','header')

    /*===== LINK ACTIVE =====*/
    const linkColor = document.querySelectorAll('.nav_link')

    function colorLink(){
        if(linkColor){
            linkColor.forEach(l=> l.classList.remove('active'))
            this.classList.add('active')
        }
    }
    linkColor.forEach(l=> l.addEventListener('click', colorLink))

});


            function updateH3Text(text,data) {
   const h3Element = document.querySelector("#details h3");
    const pElement = document.querySelector("#details p");

    // Remove the class to trigger the animation
    h3Element.classList.remove("animate-text");
    pElement.classList.remove("animate-text");

    // Trigger a reflow/repaint to remove the animation class
    void h3Element.offsetWidth;
    void pElement.offsetWidth;

    // Add the class again to trigger the animation
    h3Element.classList.add("animate-text");
    pElement.classList.add("animate-text");

      h3Element.textContent = text;
    pElement.innerHTML = data;
}
 function playVideo(videoSource, videoId) {
  console.log("playVideo function called");
   console.log("playVideo function called with videoSource:", videoSource);
    const video = document.getElementById("exerciseVideo");
    const video_name = videoSource;
    console.log(video_name);
    video.src = videoSource;
    video.load();
    video.play();

           }
    // Get the video element
    const video = document.getElementById("exerciseVideo");

    // Get the custom progress bar element
    const progressBar = document.querySelector(".custom-progress-bar");

    // Update the progress bar width as the video plays
    video.addEventListener("timeupdate", function () {
        const currentTime = video.currentTime;
        const duration = video.duration;
        const progress = (currentTime / duration) * 100;
        progressBar.style.width = progress + "%";
    });

    // Function to toggle the visibility of the "completed" icon

  function markAsActive(linkElement) {
            // Remove the "active-link" class from all links
            const menuItems = document.querySelectorAll(".menu li a");
            menuItems.forEach(item => {
                item.classList.remove("active-link");
            });

            // Add the "active-link" class to the clicked link
            linkElement.classList.add("active-link");
        }
    var age = document.getElementById("age");
        var height = document.getElementById("height");
        var weight = document.getElementById("weight");
        var male = document.getElementById("m");
        var female = document.getElementById("f");
        var form = document.getElementById("form");

        function validateForm() {
            if (
                age.value == "" ||
                height.value == "" ||
                weight.value == "" ||
                (male.checked == false && female.checked == false)
            ) {
                alert("All fields are required!");
                document
                    .getElementById("submit")
                    .removeEventListener("click", countBmi);
            } else {
                countBmi();
            }
        }

        document.getElementById("submit").addEventListener("click", validateForm);

        function countBmi() {
            var p = [age.value, height.value, weight.value];
            if (male.checked) {
                p.push("male");
            } else if (female.checked) {
                p.push("female");
            }
            form.reset();
            var bmi = Number(p[2]) / (((Number(p[1]) / 100) * Number(p[1])) / 100);
            var result = "";
            if (bmi < 18.5) {
                result = "Underweight";
            } else if (18.5 <= bmi && bmi <= 24.9) {
                result = "Healthy";
            } else if (25 <= bmi && bmi <= 29.9) {
                result = "Overweight";
            } else if (30 <= bmi && bmi <= 34.9) {
                result = "Obese";
            } else if (35 <= bmi) {
                result = "Extremely obese";
            }

            // Get references to the existing <h1> and <h2> elements
            var h1 = document.getElementById("bmi");
            var h2 = document.getElementById("bmi1");

            // Update their content
            h1.textContent = result;
            h2.textContent = "BMI: " + parseFloat(bmi).toFixed(2);

            // Remove event listeners if needed
            document.getElementById("submit").removeEventListener("click", countBmi);
            document.getElementById("submit").removeEventListener("click", validateForm);
        }


    $(document).ready(function () {
        function toggleContent(contentId) {
            // Hide all content
            $("#exe, #pro, #upcom, #chats, #calculate, #settings").hide();

            $("#" + contentId).show();
        }

        // Attach click event handlers to each link
        $("#Exercise").click(function () {
            toggleContent("exe");
        });

        $("#Progress").click(function () {
            toggleContent("pro");
        });

        $("#Upcoming").click(function () {
            toggleContent("upcom");
        });

        $("#chat").click(function () {
            toggleContent("chats");
        });

        $("#calc").click(function () {
            toggleContent("calculate");
        });

        $("#set").click(function () {
            toggleContent("settings");
        });

    });





// Function to show the loader
function showLoader() {
    const loader = document.getElementById("loader");
    loader.style.display = "block"; // Show the loader
}

// Function to hide the loader
function hideLoader() {
    const loader = document.getElementById("loader");
    loader.style.display = "none"; // Hide the loader
}

// Event listener for DOMContentLoaded
document.addEventListener("DOMContentLoaded", function() {
    // When the DOM content is loaded, hide the loader
    hideLoader();
});

// Simulate loading (you should replace this with your actual loading logic)
function simulateLoading() {
    showLoader(); // Show the loader
    setTimeout(function() {
        hideLoader(); // Hide the loader after a delay (simulating loading)
    }, 8000); // Adjust the delay as needed
}

// Call simulateLoading when your website is loading
simulateLoading();
