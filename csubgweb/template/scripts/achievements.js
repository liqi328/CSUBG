// JavaScript Document
var s=45;
var minheight=45;
var maxheight=270;
function shoppingcat(i){
	var key = document.getElementById("key"+i).innerText;
	var intro =  document.getElementById("intro"+i);
	//alert("intro"+i);
	//alert(intro.style.pixelHeight);
	if(key=="Abstract"){
		intro.style.pixelHeight+=s;
		if(intro.style.pixelHeight<maxheight){
			setTimeout("shoppingcat("+i+");",1);
		}else{
			document.getElementById("key"+i).innerText="close";
		}
	}else{
		intro.style.pixelHeight-=s;
		if(intro.style.pixelHeight>minheight){
			setTimeout("shoppingcat("+i+");",1);
		}else{
			document.getElementById("key"+i).innerText="Abstract";
		}
	}
}