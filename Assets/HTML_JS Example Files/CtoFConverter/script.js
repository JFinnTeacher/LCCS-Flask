
function cToF(){
	let temp = parseInt(document.getElementById("temp").value);
	ans = (temp * 9/5) + 32;
	document.getElementById("ans").innerHTML = ans;

}

function fToC() {
	let temp = parseInt(document.getElementById("temp").value);
	ans = (temp -32) * 5/9;
	document.getElementById("ans").innerHTML = ans;
}
