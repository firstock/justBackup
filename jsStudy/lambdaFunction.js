// 실행하려면 html 태그 안에서
// <script type= "text/javascirpt">
var calculator= {
	operate: function(method, operand1, operand2){
		// @param 1st: 함수
		if(typeof method== 'function'){
			if(typeof operand1!= 'number' || typeof operand2!= 'number')
				throw new Error('operate():2,3번째 인자_숫자 필요');
			return method(operand1, operand2);
		}else{
			throw new Error('opertate(): 첫인자_함수전달')
		}
	}
};

try{
	// calculator.operate 메소드 첫 매개변수: 익명함수
	// 인자로 lambda그냥 넣듯이
	var result1= calculator.operate(function(x,y){
		return x+y;
	}, 2, 3);
	document.writeln(result1+'<br/>');

	// 2,3번째 매개변수는 꼭 숫자!
	var result2= calculator.operate(function(x,y){
		return x+y;
	}, '2', 3); // error !
	document.writeln(result2);

} catch (e){
	document.writeln(e);
}
document.writeln('<br/>');

// 혹은, 익명함수 정의 후 바로 호출하여 결과 얻기
var result3= (fucntion(x,y){return x+y;})(2,3);

document.writeln(result3);
document.writeln('<br/>');

// </script>