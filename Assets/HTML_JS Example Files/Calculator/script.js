
function plus(){

	let n1 = parseInt(document.getElementById("num1").value);
	let n2 = parseInt(document.getElementById("num2").value);
	let result = 0;
	result = n1 + n2;
	document.getElementById("ans").innerHTML = result;
}

function minus(){
	let n1 = parseInt(document.getElementById("num1").value);
	let n2 = parseInt(document.getElementById("num2").value);
	let result = 0;
	result = n1 - n2;
	document.getElementById("ans").innerHTML = result;
}

function multiply(){
	let n1 = parseInt(document.getElementById("num1").value);
	let n2 = parseInt(document.getElementById("num2").value);
	let result = 0;
	result = n1 * n2;
	document.getElementById("ans").innerHTML = result;
}

function divide(){
	let n1 = parseInt(document.getElementById("num1").value);
	let n2 = parseInt(document.getElementById("num2").value);
	let result = 0;
	result = n1 / n2;
	document.getElementById("ans").innerHTML = result;
}

