result = 0
max = 50
completed = 0

function generateEquation(){
	const operandsT = document.getElementById("operands");
	let operands = [];
	const opCount = (new Date().getTime() % 2) + 2;
	for (i = 0; i < opCount; ++i){
		operands.push(Math.floor(Math.random() * 100));
	}
	operandsT.innerText = operands.join("+") + " = ";
	result = operands.reduce((a,b) => a+b, 0);
}

function showResult(txt){
	let div = document.createElement("P");
	div.innerText = txt;
	document.getElementById("operation").append(div);

	setTimeout(function () {
		div.remove();
	}, 1000);
}

function submit(){
	const entry = document.getElementById("result").value;
	if (entry == "") return;
	document.getElementById("result").value = "";
	if (result == entry){
		showResult("GOOD");
		completed++;
		document.getElementById("progressBar").style.width = completed/max*100 + "%";
		document.getElementById("progressBar").innerText = completed +"/" +max;
		generateEquation();
	}else{
		showResult("KO");
	}
}

function loadGame(){
	generateEquation();
	document.getElementById("result").onkeydown = function(e){
		if(e.keyCode == 13){
			document.getElementById("go").click();
		}
	}
	document.getElementById("progressBar").style.width = completed/max*100 + "%";
	document.getElementById("progressBar").innerText = completed +"/" +max;
}
