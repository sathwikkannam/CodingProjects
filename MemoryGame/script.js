const cards = document.querySelectorAll('.card');
const colors = ["pink", "red", "blue", "green", "orange", "yellow", "aqua", "black"];
var randomColors = [];
var randomCards = [];
var counter = 0; 
var testing = new Array();
var e = new Array();



randomizeBoard();

for (var i = 0; i < cards.length;i++){
    cards[i].addEventListener("click", test)
}


function test(){
    counter++;
    this.style.opacity = 1;

}





function randomizeBoard(){
    generateCardIndex();
    generateColorIndex();
    
    for (var i = 0; i < cards.length;i++){
        cards[randomCards[i]].style.backgroundColor = colors[randomColors[i]];
        cards[randomCards[i]].style.opacity = 0;
    }


}

function generateCardIndex(){
    var counter = 0;
    while(counter !== cards.length){
        var num = Math.floor(Math.random()*(cards.length));
        if(!randomCards.includes(num)){
            counter++;
            randomCards.push(num);
        }
    }

}


function generateColorIndex(){
    var counter = 0;

    while(counter !== colors.length){
        var num = Math.floor(Math.random()*(colors.length));
        if(!randomColors.includes(num)){
            randomColors.push(num);
            counter ++;
        }
    }
    const randomColorsCount = randomColors.length;
    for(var i = 0; i < randomColorsCount;i++){
        randomColors.push(randomColors[i]);
    }

}
