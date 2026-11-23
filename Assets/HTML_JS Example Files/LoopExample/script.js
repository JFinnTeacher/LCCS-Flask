let myList=[5,2,3,1,4]
let display = document.getElementById("display")

for (let i=0; i<myList.length; i++) {
	display.innerHTML += myList[i]+"<br>";
}