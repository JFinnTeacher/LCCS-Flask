let students = [];
let results = [];
let nameEle = document.getElementById("studentIn");
let resultsEle = document.getElementById("resultIn");
let outputEle = document.getElementById("output");

function addData(){
	students.push(nameEle.value);   //add the value from the input box to the list
	results.push(resultsEle.value);
	displayData();    //Call the function to display the data
}

function displayData() {
	outputEle.value="";   //clears the output
	for(let i=0; i<students.length;i+=1) {    //loop through the student list
		outputEle.value += students[i]+ "\t\t" + results[i] + "\n";
	}
	
}



