var score=0;
var cross=true
audio=new Audio('music.mp3')
audiogo=new Audio('gameover.mp3')
setTimeout(() => {
    audio.play()
}, 1000);
document.onkeydown = function (e) {
    console.log('the key code is;', e.keyCode)

    if (e.keyCode == 38) {
        let mario = document.querySelector('.mario')
        mario.classList.add('animatemario')
        setTimeout(() => {
            mario.classList.remove('animatemario')
        }, 700)
    }
    if (e.keyCode == 39) {
        let mario = document.querySelector('.mario')
        mariox = parseInt(window.getComputedStyle(mario, null).getPropertyValue('left'))
        mario.style.left = mariox + 122 + 'px';
    }

    else if (e.keyCode == 37) {
        let mario = document.querySelector('.mario')
        mariox = parseInt(window.getComputedStyle(mario, null).getPropertyValue('left'))
        mario.style.left = mariox - 122 + 'px';
    }
}

setInterval(() => {
    
    Mario = document.querySelector('.mario');
    Bowser = document.querySelector('.bowser');
    gameOver=document.querySelector('.gameOver');
    dx = parseInt(window.getComputedStyle(Mario, null).getPropertyValue('left'));
    dy = parseInt(window.getComputedStyle(Mario, null).getPropertyValue('top'));

    ox = parseInt(window.getComputedStyle(Bowser, null).getPropertyValue('left'));
    oy = parseInt(window.getComputedStyle(Bowser, null).getPropertyValue('top'));

    offsetX = Math.abs(dx - ox)
    offsetY = Math.abs(dy - oy)
    console.log(offsetX,offsetY)
    if (offsetX<90 && offsetY<150){
        
     gameOver.style.visibility='visible'
     Bowser.classList.remove('bowserAni')
     audiogo.play();
     setTimeout(() => {
        audiogo.pause();
        audio.pause();
     }, 1000);
    }
    else if(offsetX<140 && cross){
        score+=1;
        updateScore(score);
        cross=false
        setTimeout(() => {
            cross=true
        }, 2000);
        setTimeout(() => {
            AniDur=parseFloat(window.getComputedStyle(Bowser, null).getPropertyValue('animation-duration'));
            NewDur=AniDur- 0.1;
            Bowser.style.animationDuration=NewDur+'s'
        }, 700);
        // if(NewDur=2.3){
        //     Bowser.style.animationDuration=2.8+'s'
        // }

    }
    }
, 100);

function updateScore(score){
    scoreCont.innerHTML='Your Score is ' + score
}

