function Player(p) {
    if (!p) {
        p = 0;
    }

    this.point = p;
}

Player.prototype.toString = function() {
    switch(this.point) {
        case 0:
            return "가위";
        case 1:
            return "바위";
        case 2:
            return "보";
    }
};

function playRockScissorsPaper(evt) {

    var source = getEventSource(evt);

    var player = new Player();

    switch(source.id) {
        case 'btnScissors':
            player.point = 0;
            break;
        case 'btnRock':
            player.point = 1;
            break;
        case 'btnPaper':
            player.point = 2;
            break;
        default:
            return;
    }

    var computer = new Player(Math.floor(Math.random() * 3));
    var resultElement = document.getElementById('result');

    if (player.point == computer.point) {
        resultElement.innerHTML = '플레이어: ' + player + ' vs 컴퓨터: ' + computer + ' => 비겼습니다!!!';
    } else {
        if ((player.point + 1) % 3 == computer.point) {
            resultElement.innerHTML = '플레이어: ' + player + ' vs 컴퓨터: ' + computer + ' => 졌습니다!!!';
        } else {
            resultElement.innerHTML = '플레이어: ' + player + ' vs 컴퓨터: ' + computer + ' => 이겼습니다!!!';
        }
    };

}

function init() {

    var gameElement = document.getElementById('game');
    addListener(gameElement, 'click', playRockScissorsPaper);

}

function addListener(el, ev, handler) {

    if (el.addEventListener) {
        el.addEventListener(ev, handler, false);
    } else {
        el.attachEvent('on' + ev, handler);
    }
}

function getEventSource(evt) {
    if (evt.target)
        return evt.target;
    else
        return window.event.srcElement;
}

addListener(window, 'load', init);
