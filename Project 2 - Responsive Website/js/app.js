window.addEventListener("scroll", function(){
    var header = document.querySelector("#navbar");
    header.classList.toggle("bgn", window.scrollY );
})
// var color = window.getComputedStyle(
// 	document.querySelector('#navbar'), ':before'
// ).getPropertyValue('background-color')

// color.opacity.toggle("1", window.scrollY > 0);


// window.onscroll = function() {scrollFunction()};

// function scrollFunction() {
//   if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
//     document.getElementById("#navbar").style.top = "0";
//   } else {
//     document.getElementById("#navbar").style.top = "-50px";
//   }
// } 

const submit = document.querySelector('#submit');

submit.addEventListener('click', (e) => {
    e.preventDefault();
    console.log('click');
})



