// ==============================
// CLEAR BUTTON
// ==============================


function clearMessage() {
    window.location.href = "/";
}

// ==============================
// EXAMPLE MESSAGE
// ==============================

function fillMessage(text) {

    document.getElementById("message").value = text;

}

// ==============================
// CHARACTER COUNTER
// ==============================

window.onload=function(){

const textarea=document.getElementById("message");

if(textarea){

const counter=document.createElement("p");

counter.id="counter";

counter.style.marginTop="10px";

counter.style.color="white";

counter.innerHTML="Characters : 0";

textarea.parentNode.insertBefore(counter,textarea.nextSibling);

textarea.addEventListener("input",function(){

counter.innerHTML="Characters : "+textarea.value.length;

});

}

};

// ==============================
// DETECT BUTTON LOADING
// ==============================

document.addEventListener("DOMContentLoaded",function(){

const form=document.querySelector("form");

const button=document.querySelector(".detect-btn");

if(form){

form.addEventListener("submit",function(){

button.innerHTML="<i class='fa-solid fa-spinner fa-spin'></i> Detecting...";

button.disabled=true;

});

}

});

// ==============================
// CONTAINER FADE EFFECT
// ==============================

window.addEventListener("load",()=>{

document.querySelector(".container").style.opacity="1";

});

// ==============================
// EXAMPLE CHIP ANIMATION
// ==============================

const chips=document.querySelectorAll(".chips span");

chips.forEach(chip=>{

chip.addEventListener("mouseover",()=>{

chip.style.transform="scale(1.08)";

});

chip.addEventListener("mouseleave",()=>{

chip.style.transform="scale(1)";

});

});

// ==============================
// TEXTAREA ANIMATION
// ==============================

const textarea=document.getElementById("message");

if(textarea){

textarea.addEventListener("focus",()=>{

textarea.style.boxShadow="0 0 20px cyan";

});

textarea.addEventListener("blur",()=>{

textarea.style.boxShadow="none";

});

}

// ==============================
// RESULT CARD ANIMATION
// ==============================

const result=document.querySelector(".prediction-card");

if(result){

result.animate(

[

{opacity:0,transform:"scale(.7)"},

{opacity:1,transform:"scale(1)"}

],

{

duration:800,

iterations:1

}

);

}