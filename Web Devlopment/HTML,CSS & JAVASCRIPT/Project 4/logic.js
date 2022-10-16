let Direction = { x: 0, y: 0 }
const foodSound = new Audio('food.mp3')
const gameOverSound = new Audio('gameover.mp3')
const moveSound = new Audio('move.mp3')
const musicSound = new Audio('music.mp3')
let speed = 6;
let lastPaintTime = 0;
let snakeArr = [
    { x: 13, y: 15 }
]
food = { x: 6, y: 8 }
let score=0

//Game Function
function main(ctime) {
    window.requestAnimationFrame(main);
    console.log(ctime)
    if ((ctime - lastPaintTime) / 1000 < 1 / speed) {
        return;
    }
    lastPaintTime = ctime;
    gameEngine();

}

function isCollide(snake) {
    //if you bump into your
    for (let i = 1; i < snakeArr.length; i++) {
        if (snake[i].x === snake[0].x && snake[i].y === snake[0].y) {
            return true;
        
        }

    }
    // if you bump into walls
    if (snake[0].x > 18 || snake[0].x < 0 || snake[0].y > 18 || snake[0].y < 0)
        return true;
}


// Display snake
function gameEngine() {

    // inputDir = { x: 0, y: 0 };
    if (isCollide(snakeArr)) {
        gameOverSound.play()
        inputDir = { x: 0, y: 0 };
        musicSound.pause()
        alert('Game Over ,press any key to Restart')
       
        snakeArr = [{ x: 13, y: 15 }]
        musicSound.play()
        score = 0
    }

    board.innerHTML = "";
    snakeArr.forEach((e, index) => {
        snakeElement = document.createElement('div');
        snakeElement.style.gridRowStart = e.y;
        snakeElement.style.gridColumnStart = e.x;

        if (index === 0) {
            snakeElement.classList.add('head');
        }
        else {
            snakeElement.classList.add('snake')
        }
        board.appendChild(snakeElement);
    })

    // Display Food
    foodElement = document.createElement('div');
    foodElement.style.gridRowStart = food.y;
    foodElement.style.gridColumnStart = food.x;
    foodElement.classList.add('food');
    board.appendChild(foodElement)


    //updating snake and body

   


    //If you have eaten the food-->increase in score and change of food position

    if (snakeArr[0].x === food.x && snakeArr[0].y === food.y) {
        snakeArr.unshift({ x: snakeArr[0].x + inputDir.x, y: snakeArr[0].y + inputDir.y })
        foodSound.play()
        let a = 2
        let b = 16
        food = { x: Math.round(a + (b - a) * Math.random()), y: Math.round(a + (b - a) * Math.random()) }

    }

    for (let i = snakeArr.length - 2; i >= 0; i--) {
        snakeArr[i + 1] = { ...snakeArr[i] };
    }

     snakeArr[0].x += inputDir.x;
     snakeArr[0].y += inputDir.y;
  
    setTimeout(() => {
        
    if (snakeArr[0].x === food.x && snakeArr[0].y === food.y) {
        score++
        sc=document.getElementById('score')
        sc.innerHTML='Your score : ' + score
     }
    }, 1000);

    if(score>hiscore){
       
        hs=document.getElementById('hiscore')
        hs.innerHTML='Hi-Score: '+ score 
        localStorage.setItem('hiscore' , JSON.stringify(score))
    }

}
    
// Main Logic 


window.requestAnimationFrame(main);
window.addEventListener('keydown', e => {


    moveSound.play()
    inputDir = { x: 0, y: 1 };// Starts the game
    sc=document.getElementById('score')
    sc.innerHTML='Your score : ' + score
    switch (e.key) {
        case 'ArrowUp':
            console.log('Up')
            inputDir.x = 0
            inputDir.y = -1
            break;
        case 'ArrowDown':
            console.log('Down')
            inputDir.x = 0
            inputDir.y = 1
            break;

        case 'ArrowRight':
            console.log('Right')
            inputDir.x = 1
            inputDir.y = 0
            break;

        case 'ArrowLeft':
            console.log('Left')
            inputDir.x = -1
            inputDir.y = -0
            break;
            Down
        default:
            break;
    }
})



