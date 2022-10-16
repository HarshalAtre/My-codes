console.log('script running.....')
// document.querySelector('.cross').style.display="none";

document.querySelector('.hamburger').addEventListener('click',()=>{
    document.querySelector('.sidebar').classList.toggle('sidebarGo')
   
})
document.querySelector('.hamburger').addEventListener('click',()=>{
    document.querySelector('.sidebar1').classList.toggle('sidebarGo')
})
document.querySelector('.hamburger').addEventListener('click',()=>
setTimeout(()=>{
    document.querySelector('.cross').classList.toggle('crossgayab')
    document.querySelector('.ham').classList.toggle('hamgayab')   
},0))
