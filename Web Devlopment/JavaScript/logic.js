/*firstcontainer=document.getElementsByClassName('container')*/



/*// console.log("Svnit Cse");
// alert("me");
//  document.write("THIS IS ME")
 
var no1=56
 var no2=34
 console.log(no1+no2)
 
 var a=true;
 var b=false;
 console.log(a,b)


 
 var str= 'this is me'
 console.log(str)
 
 var obj={
   ravi:56,
   you:78
 }
 console.log(obj)
 
 //array
 
 var arr=[1,2,'Harry',4,5];
 console.log(arr[2])
 
 //Function
 
function avg(a,b){
 d=(a+b)/2;
 return d;
}
c=avg(4,7 );
console.log(c)

//boolean

//&&-->and
//||-->or
//!-->not

a1=true && false
console.log(a1)
a2=true || false
console.log(a2)
a3=! true
console.log(a3)

//arithmetic operations
o1=a+b
o2=a-b
o3=a*b
o4=a/b

//assignment operator
o1 +=1
o2 *=3

// comparison operation

a>b
a>=b //etc

//else-if ladder
age=22
if (age>22){
 console.log('you are above 22');
}
else if (age>18){
 console.log('you are between 22 and 18');
}
else{
 console.log('you are a kid')
}

// loops

var arr=[1,2,3,4,5,6,7]

//for loop
for (var i=0;i<arr.length;i++){
 console.log(arr[i])
}
//for each
arr.forEach(function(element){
 console.log(element);
})

//while loop
//let j=0;
while(j<arr.length){
 console.log(arr[j]);
 j++;
}

//do while loop
var j=0
do{
 console.log(arr[j]);
} while (j<arr.length);
j++;*/

// constant

//const abc=3//---> this variable can't be modified
//abc+=4 doesn't work

/*for(var i=0;i<arr.length;i++){
    if (i==2){
    //break;
    continue;
    }
 console.log(a[i]);
  
}
//araay method
var arry=['Fan',34,null,true]

//1
arry.pop()
//2
arry.push('harry')
//3
arry.shift(  )
//4
console.log(arry.unshift('harry'))
//5
arry.toString()

//6
arry.sort

//7
arry.length

console.log(arry)

//str meathod
str='harry you are good good'
//1
console.log(str.length)
//2
//console.log   before all
str.indexOf("good")
//3
str.lastIndexOf("good")
//4
str.slice(1,4)
//5
str.replace("harry","rohan")

//date
let mydate=new Date();
console.log(mydate);*/
// .gettime
// .getday
//.get hour
//.getminiute
//google for more methods

click.addEventListener('click', function () {
  console.log('click hua button')

})
//DOM Manipulation

//1.
let elem = document.getElementById('click')
console.log(elem)

//2. change css

con.style.background = 'yellow'

//3. add class 

con.classList.add("color")
// color[0].classList.add('border')

//4. remove class
con.classList.remove('container')

//5. inner text 

console.log(elem.innerText)

//6.with html tag

console.log(document.getElementsByTagName('div'))
//7. add a child element in existing element

let tn = document.getElementsByTagName('h1');

ce1 = document.createElement('p');
ce1.innerText = 'this is para';

tn[0].appendChild(ce1);

//8. replace child element with another

ce2 = document.createElement('b')
ce2.innerText = 'This is bold'

tn[0].replaceChild(ce2, ce1)

//9.query selector

sel = document.querySelector('.container')
console.log(sel)

// or below selects all div elements
sel2 = document.querySelectorAll('.container')

//10. remove child element
const g = document.getElementById('con')

g.removeChild(g.firstElementChild)

// google document method for js 
//ex is document.link,.image,.url,.script,.link,.forms,.domain.etc
//write all in console

//events in js

//1. click

con.addEventListener('click', function () {
  console.log('click hua')
})

//2. mouseover 

con.addEventListener('mouseover', function () {
  console.log('mouse aya')
})

//3. mouse in

con.addEventListener('mousein', function () {
  console.log('mouse container ke ander aya')
})

//4. mouse out
con.addEventListener('mouseout', function () {
  console.log('mouse container ke bhar gaya')
})
//5. mouse down
con.addEventListener('mousedown', function () {
  console.log('mouse clicked')
})

//6. mouse up
con.addEventListener('mouseup', function () {
  console.log('mouse button released')
})

// A sample use of them
// let prevhtml = document.querySelectorAll('.container')[0].innerHTML;

// clicked.addEventListener('mouseup', function () {

//   document.querySelectorAll('.container')[0].innerHTML = prevhtml;

// })
// clicked.addEventListener('mousedown', function () {

//   document.querySelectorAll('.container')[0].innerHTML = '<b>bold</b>';

// })

//  Arrow function
summ = (a,b)=>{
  return a+b;
}
// set timeout
blink=()=>{
  click.style.background="red"//--> execute function after 2000sec as defined
}
blink2=()=>{
  click.style.background="yellow"//--> execute function after 2000sec as defined
}
// setTimeout(blink, 2000)

// set interval
// setInterval(blink,2000)//-->  executes then funtion every 1000ms 
// setInterval(blink2,3000)
 
// clear timeout or clear interval
clr=setInterval(blink2,3000)
// or
clr2=setTimeout(blink, 2000)

//  If we have to stop ther execution we have to write:
// clearTimeout(clr)
// clearTimeout(clr2)
// in console 

//  local storage

// localstorage.setitem('name','harry') ------> in console , to set the items
// localstorage.getitem('name')
// localstorage --> to see whole storage
// localstorage.removeitem('name')
// localstorage.clear

// JSON
// obj={'name':'harry'}
// jso=JSON.stringify(obj)
// console.log(typeof jso)
// par=JSON.parse(`{'name':'harry'}`)
// console.log(par)

// backtick (below esc key)
au=18
console.log(`this is my ${au} birthday`) //--> works like f-string of python

