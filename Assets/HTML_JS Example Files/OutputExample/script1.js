function updateText(){

	let name = document.getElementById("name").value;
	let age = document.getElementById("age").value;
	let valid = "";

	if (age >= 17) {
		document.getElementById("output").value = "Valid";
		document.getElementById("output").style.backgroundColor ="lightgreen";
		validity = "valid";
	}
	else {
		document.getElementById("output").value = "Invalid";
		document.getElementById("output").style.backgroundColor = "red";
		validity = "invalid";
	}

	document.getElementById("outputName").innerHTML = name;
	document.getElementById("outputResult").innerHTML = validity;
}